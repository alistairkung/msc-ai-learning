# Lesson 31 — Real-Data Classification Workflow

_Date: 2026-09-03; completed 2026-09-04_
_Status: **Complete — end-to-end workflow implemented and tested**

## Why this lesson exists

Lesson 30 built a binary PyTorch classifier on synthetic data, but evaluated it on the same data used for training. Lesson 31 moves from isolated neural-network mechanics to a more realistic ML engineering workflow:

```text
real data
  -> inspect
  -> train / validation / test split
  -> fit preprocessing on training data only
  -> transform all splits
  -> NumPy -> PyTorch tensors
  -> TensorDataset / DataLoader
  -> MLP classifier
  -> train across epochs
  -> track train + validation loss
  -> final evaluation
```

This advances the existing practical-ML/PyTorch track and prepares directly for AI in Practice real-data work. The follow-up session fixed the classifier-test import, connected the complete preparation/training/evaluation workflow, and verified it with tests.

---

## Retrieval at the start of the session

A short cold-retrieval block revisited Lesson 30 before introducing new material.

### Retrieved successfully
- `nn.Linear` changes the representation dimension while preserving the batch dimension.
- Binary classifier output is one **raw logit** per sample.
- `BCEWithLogitsLoss` consumes logits directly.
- Sigmoid converts logits to probabilities; thresholding converts probabilities to classes.
- Evaluating on training data does not demonstrate generalisation.
- Training data learns parameters; validation data guides development decisions; test data is the final untouched evaluation.
- Falling train loss with rising validation loss is a classic overfitting signal.
- `optimizer.zero_grad()` is required because PyTorch gradients accumulate.
- Early stopping should retain/restore the best validation checkpoint, not simply the epoch where patience expires.

### Retrieval slips worth re-testing later
- PyTorch stored linear weight orientation `(out_features, in_features)` needed a prompt on first retrieval.
- One quick output-shape answer substituted the wrong batch size.
- These looked like retrieval/attention slips rather than missing conceptual understanding.

---

# 1. Loading and inspecting a real dataset

Used sklearn's built-in breast-cancer dataset to avoid a network/download dependency:

```python
from sklearn.datasets import load_breast_cancer


def load_data():
    X, y = load_breast_cancer(return_X_y=True)
    return X, y
```

The dataset was **inspected rather than memorised**:

```python
X, y = load_data()
print(X.shape)
print(y.shape)
```

Observed:

```text
X: (569, 30)
y: (569,)
```

Semantic interpretation:
- 569 samples;
- 30 input features per sample;
- one binary target per sample.

Testing lesson: it is reasonable to turn an inspected, stable dataset contract into assertions, but the learner should not be expected to magically know a library dataset's dimensions beforehand.

---

# 2. Train / validation / test splitting

Target split:

```text
60% training
20% validation
20% test
```

Implemented by splitting twice:

1. Full dataset -> 60% train / 40% remainder.
2. Remainder -> 50% validation / 50% test.

```python
from sklearn.model_selection import train_test_split


def split_data(X, y):
    X_train, X_remainder, y_train, y_remainder = train_test_split(
        X,
        y,
        test_size=0.4,
        stratify=y,
        random_state=42,
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_remainder,
        y_remainder,
        test_size=0.5,
        stratify=y_remainder,
        random_state=42,
    )

    return X_train, X_val, X_test, y_train, y_val, y_test
```

Observed/expected shapes:

```text
X_train: (341, 30)    y_train: (341,)
X_val:   (114, 30)    y_val:   (114,)
X_test:  (114, 30)    y_test:  (114,)
```

### Stratification

`stratify=y` asks sklearn to preserve roughly the same class proportions in the resulting splits.

Important retrieval point from this lesson: on the **second split**, the samples being split are `X_remainder` / `y_remainder`, so the corresponding stratification labels must be:

```python
stratify=y_remainder
```

not the original full `y`.

---

# 3. Feature scaling and data leakage

## Why scale?

Real features may live on very different numerical scales. A feature around tens of thousands can create much larger numerical contributions/gradients than a feature around fractions, even if it is not inherently more predictive. Standardisation improves the numerical conditioning of gradient-based optimisation.

Manual standardisation idea:

```text
scaled = (x - mean) / std
```

For each feature, training data after standardisation should have approximately:

```text
mean = 0
std  = 1
```

Example retrieval:
- training mean 100, std 20, value 140 -> `(140 - 100) / 20 = 2`;
- interpretation: two training-set standard deviations above the training mean.

## Critical rule: fit preprocessing on training data only

Correct workflow:

```text
raw data
  -> split
  -> learn scaler statistics from TRAIN
  -> transform train / validation / test using those frozen statistics
```

Incorrect workflow:

```text
raw data
  -> standardise using all samples
  -> split
```

The incorrect version leaks information from validation/test into the fitted preprocessing pipeline.

Also do **not** fit a separate scaler on validation or test. Even though that would not update neural-network weights, it would recalibrate the fitted pipeline using unseen data. Validation/test should be processed exactly as future unseen samples would be: using preprocessing parameters learned during training.

Therefore validation/test data do **not** need to have mean 0 and std 1 after transformation. Their transformed distributions may legitimately differ from training.

## sklearn implementation

```python
from sklearn.preprocessing import StandardScaler


def scale_data(X_train, X_val, X_test):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_val_scaled, X_test_scaled
```

Conceptual distinction:

```text
fit       = learn preprocessing parameters
transform = apply already-learned parameters
fit_transform = fit, then transform the same data
```

Useful rule:

> Anything learned/calculated from the dataset as part of the fitted pipeline should generally be learned from training data only.

---

# 4. Testing standardisation and floating-point tolerance

For `X_train_scaled.shape == (341, 30)`:

```python
X_train_scaled.mean(axis=0)
```

has shape `(30,)`, not `(1, 30)`, because NumPy removes the reduced axis by default.

Expected values:

```text
mean(axis=0) -> 30 values approximately 0
std(axis=0)  -> 30 values approximately 1
```

Test:

```python
assert np.allclose(X_train_scaled.mean(axis=0), 0, atol=1e-7)
assert np.allclose(X_train_scaled.std(axis=0), 1, atol=1e-7)
```

### `atol`

`atol` = absolute tolerance. Floating-point arithmetic may produce a tiny value such as `0.0000000000000032` where mathematically we expect zero.

```text
1e-7 = 1 x 10^-7 = 0.0000001
```

So the test means approximately:

> Assert that every training feature mean is effectively zero, allowing tiny floating-point error.

---

# 5. Crossing from sklearn / NumPy to PyTorch

The split/scaling work happens as NumPy arrays. `TensorDataset` needs PyTorch tensors.

```python
import torch


def to_tensors(X, y):
    X = torch.tensor(X, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32).reshape(-1, 1)
    return X, y
```

For the training split:

```text
NumPy X: (341, 30) -> float32 tensor (341, 30)
NumPy y: (341,)    -> float32 tensor (341, 1)
```

Why reshape `y`?

The classifier produces one logit per sample:

```text
logits: (batch, 1)
targets: (batch, 1)
```

This makes the target shape line up with `BCEWithLogitsLoss` input shape.

---

# 6. TensorDataset and DataLoader

Retrieved from Lesson 30:

```python
from torch.utils.data import DataLoader, TensorDataset


def make_dataloader(X, y, batch_size):
    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    return loader
```

Roles:

```text
TensorDataset -> pairs each X sample with its corresponding y
DataLoader    -> serves those pairs as shuffled mini-batches
```

For 341 samples and `batch_size=32`:

```text
10 full batches of 32
1 final partial batch of 21
len(loader) = 11
```

Shapes:

```text
normal batch: X (32, 30), y (32, 1)
final batch:  X (21, 30), y (21, 1)
```

Important distinction to retrieve:

```text
train_loader.batch_size = samples per normal batch (32)
len(train_loader)       = batches in the epoch (11)
```

---

# 7. Real-data MLP architecture

Designed architecture:

```python
from torch import nn


def make_classifier():
    return nn.Sequential(
        nn.Linear(30, 16),
        nn.ReLU(),
        nn.Linear(16, 1),
    )
```

Shape flow:

```text
(batch, 30)
    -> Linear(30, 16)
(batch, 16)
    -> ReLU
(batch, 16)
    -> Linear(16, 1)
(batch, 1) raw logits
```

Contract test intended during session:

```python
def test_make_classifier():
    model = make_classifier()
    X = torch.randn(32, 30)

    logits = model(X)

    assert logits.shape == (32, 1)
```

### Current unresolved blocker

At the stopping point this test was reported as failing locally, despite the pasted test and pasted architecture being shape-compatible. The exact pytest traceback was not captured.

**Next-session rule: do not guess or rewrite the architecture first. Get the exact traceback and inspect the actual local files/imports/state.**

---

# 8. Training with validation across epochs

Binary loss and optimiser:

```python
loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
```

Training-batch update was retrieved successfully apart from the small API typo `backwards()` -> `backward()`:

```python
optimizer.zero_grad()
logits = model(X_batch)
loss = loss_fn(logits, y_batch)
loss.backward()
optimizer.step()
```

## Epoch structure

An early attempt accidentally performed only one pass through the loader because there was no outer epoch loop. Correct conceptual nesting:

```python
train_losses = []
val_losses = []

for epoch in range(epochs):
    total_train_loss = 0

    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        logits = model(X_batch)
        loss = loss_fn(logits, y_batch)
        total_train_loss += loss.item()
        loss.backward()
        optimizer.step()

    average_train_loss = total_train_loss / len(train_loader)
    train_losses.append(average_train_loss)

    with torch.no_grad():
        val_logits = model(X_val)
        val_loss = loss_fn(val_logits, y_val)
        val_losses.append(val_loss.item())
```

For `epochs=10`:

```text
len(train_losses) = 10
len(val_losses)   = 10
```

### Loss bookkeeping

`loss_fn` gives one average loss for each batch. In the simple implementation above we sum those batch-average losses and divide by the **number of batches**:

```python
total_train_loss / len(train_loader)
```

Do not divide that sum by `train_loader.batch_size`; `batch_size` is samples per normal batch, not the number of loss values accumulated.

There is a later subtlety: because the final batch is smaller, an unweighted average of batch averages does not weight every sample equally. That refinement was deliberately deferred; the simple average is sufficient for this lesson.

---

# 9. Validation is measurement, not learning

Validation happens after all training batches in each epoch, but still **inside the epoch loop**.

```python
with torch.no_grad():
    val_logits = model(X_val)
    val_loss = loss_fn(val_logits, y_val)
```

No:

```text
backward
optimizer.step
```

on validation data.

Reason:

> Validation asks how the current fitted model performs on data it did not train on. It must not update the model.

Tracking both training and validation loss makes overfitting visible.

Example:

```text
epoch    train loss    val loss
20       0.12          0.15
21       0.10          0.16
22       0.08          0.19
23       0.06          0.23
```

Interpretation: training fit continues to improve while validation performance worsens -> overfitting.

If histories are:

```text
train: 0.60, 0.45, 0.30, 0.20, 0.12
val:   0.58, 0.43, 0.32, 0.35, 0.41
```

best validation performance is around epoch 3.

---

# 10. Classification accuracy

Evaluation pipeline:

```text
X
 -> model
 -> raw logits
 -> sigmoid
 -> probabilities
 -> threshold (normally 0.5)
 -> class predictions
 -> compare with true y
 -> mean correctness
```

Implementation developed conceptually:

```python
def classification_accuracy(model, X, y, threshold=0.5):
    with torch.no_grad():
        probabilities = torch.sigmoid(model(X))
        predictions = (probabilities >= threshold).float()
        accuracy = (predictions == y).float().mean()

    return accuracy
```

Important correction from the session:

```python
predictions.mean()
```

does **not** calculate accuracy. It calculates the proportion of samples predicted as class 1.

Accuracy requires:

```python
(predictions == y).float().mean()
```

Example:

```text
predictions = [1, 0, 1, 0]
y           = [1, 1, 1, 0]
```

Three of four are correct -> 75% accuracy.

---

# 11. Train / validation / test discipline

Roles consolidated in this lesson:

```text
training   -> learn model parameters
validation -> development/model/hyperparameter decisions
             + monitor generalisation/overfitting
test       -> final untouched evaluation
```

The test set should be evaluated after model/training decisions are finished. Repeatedly checking test results and changing the model in response turns the test set into another validation set.

This is the main conceptual improvement over Lesson 30's synthetic same-data evaluation.

---

# Known fragile points from Lesson 31

Re-test these rather than re-teaching the whole lesson:

1. **Standardisation target values**
   - training feature mean ≈ 0;
   - training feature std ≈ 1.

2. **Reduced-axis NumPy shape**
   - `(341,30).mean(axis=0)` -> `(30,)`, not `(1,30)`.

3. **Train-only fitted preprocessing**
   - fit scaler on training only;
   - transform validation/test with training statistics;
   - validation/test need not themselves become mean 0/std 1.

4. **Epoch vs batch bookkeeping**
   - outer loop = epochs;
   - inner loop = batches;
   - `len(loader)` = batches;
   - `.batch_size` = samples per normal batch.

5. **Epoch loss history**
   - store one train loss and one validation loss per epoch, not one train loss per batch and one validation loss at the very end.

6. **Accuracy**
   - thresholding creates predictions;
   - compare predictions to targets before taking mean.

7. **Best-validation checkpoint (optional extension)**
   - if early stopping/model selection is added, retain and restore the parameters from the best validation epoch;
   - the current lesson correctly tracks validation loss but intentionally returns the final trained model.

---

# Suggested cold-retrieval sequence (10–15 minutes)

Ask **one question at a time** and change numbers/context so this is retrieval rather than memorisation.

1. Given `X.shape=(800,12)`, `y.shape=(800,)`, describe samples/features/targets.
2. Design a 60/20/20 split using two calls; what is the first split and the second split?
3. Why use stratification for binary classification?
4. Should the scaler be fitted on train, validation, all data, or separately on each? Why?
5. Training mean=50, std=10; validation value=80. What scaled value does validation receive?
6. After fitting `StandardScaler`, what should training feature means/stds approximately be?
7. For `X.shape=(500,30)`, what is `X.mean(axis=0).shape`?
8. Why reshape binary labels from `(n,)` to `(n,1)` for this model?
9. 341 samples, batch size 32: how many batches and what is the final batch shape?
10. Reconstruct `30 -> 16 -> ReLU -> 1` and trace a `(32,30)` batch through it.
11. Reconstruct the five training-update lines.
12. Where does validation sit relative to epoch and batch loops, and why no backward pass?
13. What should `len(train_losses)` be after 25 epochs?
14. Explain why `predictions.mean()` is not accuracy.
15. Explain why the test set should remain untouched until final evaluation.

For any miss, give immediate feedback and re-test the same concept shortly with different numbers.

---

# Mastery signal

Lesson 31 is ready to mark complete when the learner can:

- build the real-data pipeline without leaking validation/test information;
- explain the role and shape of every representation from raw NumPy arrays through PyTorch batches;
- write the nested epoch/batch training loop and validation pass with minimal prompting;
- track train/validation loss and identify overfitting;
- compute binary accuracy correctly from logits;
- explain why test evaluation is deferred;
- run the complete pipeline successfully on the real dataset.

All bullets are satisfied by the completed `prepare_data()` and `run_experiment()` integration and the passing Lesson 31 tests.

---

# Completion evidence and next step

- `prepare_data()` composes loading, stratified splitting, train-only scaling, tensor conversion and shuffled training batches.
- `run_experiment()` trains the classifier, returns one train and validation loss per epoch, and evaluates held-out test accuracy once.
- The classifier import now resolves to Lesson 31's 30-input model.
- Verified on 2026-09-04: Lesson 31 and dashboard tests pass (`9 passed`).

Primary next session: reactivate BFS/DFS/A*, compare their guarantees and resource trade-offs, then add UCS and heuristic admissibility/consistency. Best-validation-checkpoint restoration is optional Lesson 31 continuation work, not the primary next target.
