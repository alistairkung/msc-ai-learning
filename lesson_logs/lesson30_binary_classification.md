# Lesson 30 — Binary Classification with PyTorch

_Date logged: 2026-09-03_
_Source exercise: `deep_learning/mlp/lesson30_binary_classification.py`_
_Source tests: `deep_learning/mlp/test_lesson30_binary_classification.py`_

## Purpose of this log

This is a **retrieval blueprint**, not just a summary. If the learner asks to "cold retrieve lesson 30", use this file to recreate the lesson's interactive questioning style without simply showing the answers first.

Rules for retrieval:
- Ask **one small question at a time**.
- Start with cold recall; do not lecture first.
- Prefer concrete tensor shapes, short code snippets, predictions, and "why?" questions.
- Give immediate feedback after each answer, then continue.
- If an answer is wrong, distinguish a notation/arithmetic slip from a conceptual misunderstanding.
- Re-test a missed concept shortly afterwards with changed numbers/context.
- Do not require memorisation of unfamiliar API syntax; test what each component means and why it is there.
- A normal review should be timeboxed to roughly **10–15 minutes** unless deeper review is explicitly requested.

---

## What was implemented

The lesson built a small binary neural-network classifier with:

```python
nn.Sequential(
    nn.Linear(10, 6),
    nn.ReLU(),
    nn.Linear(6, 1),
)
```

Training used:

```python
loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
```

and a mini-batch training loop:

```python
for epoch in range(epochs):
    for X_batch, y_batch in loader:
        optimizer.zero_grad()
        logits = model(X_batch)
        loss = loss_fn(logits, y_batch)
        loss.backward()
        optimizer.step()
```

The dataset was synthetic:

```python
X = torch.randn(1000, 10)
y = ((X[:, 0] + X[:, 1]) > 0).float().reshape(-1, 1)
```

Evaluation converted logits to probabilities and then classes:

```python
logits = model(X)
probabilities = torch.sigmoid(logits)
predictions = (probabilities >= 0.5).float()
accuracy = (predictions == y).float().mean()
```

A `TensorDataset` and shuffled `DataLoader` were used for mini-batches of paired `X` and `y` values.

---

## Core concepts learned

### 1. Binary classifier architecture

For input `X.shape == (batch, 10)`:

```text
(batch, 10)
    ↓ Linear(10, 6)
(batch, 6)
    ↓ ReLU
(batch, 6)
    ↓ Linear(6, 1)
(batch, 1)
```

The batch dimension is preserved; the feature/representation dimension changes.

PyTorch stores `nn.Linear(in_features, out_features).weight` as:

```text
(out_features, in_features)
```

So `nn.Linear(10, 6).weight.shape == (6, 10)`.

### 2. Why the hidden layer needs a nonlinearity

Stacked linear layers without an activation still collapse into a single affine transformation. ReLU introduces nonlinearity so the network can represent more complex relationships.

ReLU:

```text
ReLU(x) = max(0, x)
```

It changes values but does not change tensor shape.

### 3. Logits, sigmoid, probabilities, classes

The final `Linear(..., 1)` emits **one raw logit per sample**.

Conceptual inference pipeline:

```text
logit → sigmoid → probability of class 1 → threshold → predicted class
```

A positive logit gives a sigmoid probability above `0.5`; a negative logit gives one below `0.5`; zero gives `0.5`.

`p` means the model's predicted probability of **class 1**, regardless of the true label.

### 4. Binary cross entropy

Conceptual BCE:

```text
-[y log(p) + (1-y) log(1-p)]
```

If `y = 1`, the relevant term becomes `-log(p)`.
If `y = 0`, it becomes `-log(1-p)`.

Confident correct predictions receive low loss; confident wrong predictions receive high loss.

### 5. BCEWithLogitsLoss

`nn.BCEWithLogitsLoss()` expects **raw logits**. Do not add a `Sigmoid()` to the model output during training.

It combines the sigmoid/BCE calculation in a numerically stable way.

Explicit sigmoid is useful during evaluation/inference when a probability is wanted.

### 6. Mini-batches, epochs and updates

- **Batch**: subset of training examples used for one update.
- **Epoch**: one pass through the complete training dataset.
- With 1000 examples and batch size 32, there are 32 batches if the final smaller batch is retained: 31 full batches plus 8 examples.
- The optimizer normally updates parameters once per batch.

`TensorDataset(X, y)` keeps corresponding samples and labels paired. `DataLoader(..., shuffle=True)` creates shuffled mini-batches.

### 7. Gradient loop

The key loop semantics are:

```text
zero_grad → forward pass → loss → backward → optimizer step
```

`loss.backward()` calculates gradients through the computation graph.
`optimizer.step()` uses those gradients to update parameters.
`optimizer.zero_grad()` is required because PyTorch gradients accumulate by default.

### 8. Parameters and capacity

For:

```python
nn.Linear(10, 6)
nn.Linear(6, 1)
```

parameter count is:

```text
first layer:  10×6 weights + 6 biases = 66
second layer: 6×1 weights + 1 bias   = 7
total:                                   73
```

Weights and biases are learned **parameters**. Learning rate, batch size, epoch count and architecture choices are **hyperparameters**.

More model capacity can fit more complex functions but can also increase overfitting risk.

---

## Important limitation discovered

The lesson's test trains and evaluates on the **same 1000 synthetic examples**. Therefore high measured training accuracy (observed around 99%+) does **not** demonstrate generalisation to unseen data.

This limitation is the bridge into the next lesson: real-data train/validation/test workflow.

---

## Retrieval question bank

Do **not** ask all of these at once. Select/adapt them dynamically and ask one at a time.

### Tensor shapes

```python
layer = nn.Linear(12, 5)
X = torch.randn(64, 12)
```

Ask:
- What is `X.shape`?
- What is `layer.weight.shape`?
- What is `layer(X).shape`?
- What does each dimension mean?

Variation after a mistake:

```python
layer = nn.Linear(8, 3)
X = torch.randn(40, 8)
```

Ask for the stored weight and output shapes.

### Network shape trace

```python
model = nn.Sequential(
    nn.Linear(30, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
)
X = torch.randn(32, 30)
```

Ask one layer at a time:
- Shape after first Linear?
- Shape after ReLU?
- Shape after final Linear?
- What does the final `1` mean?

### Nonlinearity

Ask:
- If we remove ReLU and stack two Linear layers, what important capability do we lose?
- Does ReLU change shape or values?
- What happens to a negative activation under ReLU?

### Logits and probabilities

Ask:
- Should the model contain `Sigmoid()` when training with `BCEWithLogitsLoss()`? Why?
- What does a positive logit imply after sigmoid?
- What probability does logit `0` map to?
- If sigmoid gives `0.82`, what does `0.82` mean?
- With threshold `0.5`, which class is predicted?

### BCE intuition

Ask:
- In BCE, what does `p` represent?
- If the true class is 1, should loss be lower for `p=0.9` or `p=0.1`? Why?
- If the true class is 0, should loss be lower for `p=0.1` or `p=0.9`?
- Why is a confidently wrong prediction punished strongly?

### Training loop

Show:

```python
optimizer.zero_grad()
logits = model(X_batch)
loss = loss_fn(logits, y_batch)
loss.backward()
optimizer.step()
```

Ask:
- What does each line do?
- Why `zero_grad()`?
- Which line calculates gradients?
- Which line actually changes the weights?

### Batching

Ask:
- What is the difference between a batch and an epoch?
- 1000 examples, batch size 32: how many batches/updates per epoch if the final partial batch is retained?
- Why use `TensorDataset`?
- What does `shuffle=True` change?

### Parameters vs hyperparameters

Given the lesson's model/training call, ask the learner to classify examples such as:
- weights
- biases
- learning rate
- batch size
- number of epochs
- hidden-layer width

### Parameter counting

For a changed network such as:

```python
nn.Linear(4, 3)
nn.ReLU()
nn.Linear(3, 1)
```

ask for the total number of trainable parameters. Use changed dimensions rather than simply recalling `73`.

### Generalisation bridge

Ask:
- Why is 99% accuracy on the same data used for training insufficient evidence that the model learned something useful?
- What would unseen data tell us that training accuracy cannot?

---

## Known fragile points to probe

These are not necessarily conceptual failures; use retrieval to see whether they persist.

1. **PyTorch stored weight orientation** — learner may initially answer `(in, out)` from manual matrix multiplication instead of PyTorch's `(out, in)`.
2. **Preserving batch dimension** — occasional quick slip where an earlier batch size is substituted, despite correct conceptual understanding that the batch dimension remains fixed through Linear/ReLU layers.
3. **Logit vs probability** — reinforce that the final Linear output is a logit; sigmoid converts it to probability.
4. **Meaning of `p` in BCE** — always probability assigned to class 1, not probability assigned to whichever class is correct.
5. **Batch arithmetic** — distinguish full batches from the final partial batch and `drop_last` behavior.

When one of these is missed, ask a nearby variation shortly afterwards rather than repeatedly explaining the same example.

---

## Suggested cold-retrieval sequence (10–15 minutes)

Use this as a template, not a script:

1. One `nn.Linear` weight/output shape question.
2. Trace shapes through a small classifier.
3. Explain why ReLU is present.
4. Logit → sigmoid → probability → class question.
5. Explain why `BCEWithLogitsLoss` should receive logits.
6. One BCE intuition question with `y=0` or `y=1`.
7. Explain `zero_grad`, `backward`, and `step` from a short loop.
8. Batch/epoch/update-count question.
9. Parameter-vs-hyperparameter or parameter-count question.
10. Generalisation question connecting lesson 30 to lesson 31.

Stop once retention is clear; do not force every question into every review.

## Mastery signal

Lesson 30 is cold-retrieved successfully when the learner can, without running code:
- trace the shapes through a small binary MLP;
- distinguish PyTorch's stored Linear weight shape from conceptual matrix orientation;
- explain why ReLU is needed;
- distinguish logits, sigmoid probabilities and thresholded classes;
- explain why `BCEWithLogitsLoss` takes logits;
- reason qualitatively about BCE for class 0 and class 1;
- explain the mini-batch training loop and gradient accumulation;
- distinguish parameters from hyperparameters;
- reason about batch/epoch/update counts; and
- explain why training-set accuracy alone does not establish generalisation.
