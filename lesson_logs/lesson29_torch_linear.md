# Lesson 29 — Standard PyTorch Linear Training Loop

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

Lesson 29 replaced Lesson 28's manually managed `W`, `b`, updates and gradient clearing with the standard PyTorch abstractions used in real models. The underlying mathematics stayed the same; the framework began managing repetitive mechanics.

## What was implemented

Source: `deep_learning/pytorch_fundamentals/lesson29_torch_linear.py` + `deep_learning/pytorch_fundamentals/test_lesson29_torch_linear.py`.

Model/loss/optimiser:

```python
model = nn.Linear(in_features=2, out_features=1)
loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
```

Training loop:

```python
for _ in range(steps):
    optimizer.zero_grad()
    y_hat = model(X)
    loss = loss_fn(y_hat, y)
    loss.backward()
    optimizer.step()
```

The test trains on a small linear mapping and verifies final MSE is below `0.01`.

## Core concepts

### `nn.Linear`

Represents the affine map:

```text
y = XWᵀ + b
```

Conceptually it is still weights + bias, but PyTorch creates, stores and exposes those trainable parameters for us.

Important orientation distinction:

```text
nn.Linear(in_features, out_features).weight.shape
    == (out_features, in_features)
```

This differs from the earlier manual NumPy convention where we often wrote `X @ W` with `W.shape=(in_features,out_features)`.

### `nn.MSELoss`

Packages the same mean-squared-error idea already built manually in earlier lessons.

### `torch.optim.SGD`

Owns the parameter-update step. Instead of manually writing:

```python
with torch.no_grad():
    W -= lr * W.grad
```

we call:

```python
optimizer.step()
```

### Standard training-loop order

```text
zero gradients
 -> forward pass
 -> compute loss
 -> backward pass
 -> optimiser step
```

Each line has a distinct job.

## Bridge from Lesson 28

Lesson 28 manual form:

```text
explicit W/b
manual forward equation
manual MSE
backward
manual no-grad update
manual grad.zero_()
```

Lesson 29 framework form:

```text
nn.Linear
model(X)
n.MSELoss
backward
optimizer.step
optimizer.zero_grad
```

The abstraction is useful only if the learner can still explain what is happening underneath.

## Chat-history context

This standard loop became the template immediately reused in Lesson 30 binary classification. Later cold retrieval showed the learner understood that `zero_grad()` prevents gradient accumulation and that evaluation should omit gradient/update steps.

A durable fragile point is PyTorch's stored linear-weight orientation `(out,in)`, which should remain in short shape retrieval.

## Cold-retrieval question bank

1. What does `nn.Linear(5,3)` do to an input batch of shape `(32,5)`?
2. What is the shape of that layer's stored `.weight` tensor?
3. Why is the weight orientation different from a manual `X @ W` matrix you might write as `(5,3)`?
4. Put `zero_grad`, forward, loss, backward, step in order.
5. What does `loss.backward()` do that `optimizer.step()` does not?
6. What does `optimizer.step()` do that `loss.backward()` does not?
7. Why is `optimizer.zero_grad()` still needed even though the optimiser manages the parameters?
8. Which parts of Lesson 28 have been abstracted by `nn.Linear`, `MSELoss`, and SGD?
9. If training loss does not decrease, name several different categories of things you would inspect before assuming the optimiser API is broken.

## Retrieval blueprint

1. trace `nn.Linear` input/output and stored weight shape;
2. reconstruct five-line training loop;
3. map each line to its mathematical meaning;
4. compare manual Lesson 28 update with `optimizer.step()`;
5. explain gradient accumulation.

## Mastery signal

The learner can write the canonical PyTorch training loop from memory, explain each line underneath the abstraction, and trace the shapes of model input, output, weights and gradients.

## Bridge onward

Lesson 30 keeps this exact optimisation skeleton and changes the task from linear regression to a nonlinear binary classifier:

```text
nn.Linear + ReLU + nn.Linear
MSELoss -> BCEWithLogitsLoss
continuous predictions -> logits/probabilities/classes
```
