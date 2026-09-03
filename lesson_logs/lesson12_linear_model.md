# Lesson 12 — Manual Linear Models, Loss and Linear Layers

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

This lesson connected NumPy matrix operations to ML mechanics. Instead of treating `@` as abstract matrix multiplication, it was used to build predictions, losses, multi-output linear layers and class selection.

Source: `machine_learning/fundamentals/lesson12_linear_model.py` + `machine_learning/fundamentals/test_lesson12_linear_model.py`.

## What was implemented

- linear prediction: `features @ weights + bias`;
- prediction errors;
- squared errors;
- mean squared error;
- model loss as prediction + MSE;
- multi-output linear layer: `inputs @ weights + biases`;
- class prediction from a score matrix using `argmax(axis=1)`.

## Core concepts

### Linear prediction

For:

```text
features: (samples, input_features)
weights:  (input_features,)
```

`features @ weights` produces one scalar prediction per sample:

```text
(samples, input_features) @ (input_features,) -> (samples,)
```

A scalar bias is then added to every sample via broadcasting.

### Error and MSE

```text
error = prediction - actual
squared error = error²
MSE = mean(squared errors)
```

Squaring makes positive/negative errors contribute positively and penalises larger misses more strongly.

### Multi-output linear layer

For:

```text
inputs:  (batch, in_features)
weights: (in_features, out_features)
biases:  (out_features,)
```

```text
inputs @ weights + biases -> (batch, out_features)
```

This is the manual NumPy convention used here. Later PyTorch `nn.Linear(in, out)` stores its weight tensor as `(out, in)`, which became a known retrieval trap. Keep those two views distinct.

### Classification scores

A score matrix `(samples, classes)` can be turned into class indices with:

```python
scores.argmax(axis=1)
```

That means: for each sample/row, return the column index with the highest score.

## Chat-history context

The broader learning history shows this manual linear-model work became an important foundation for later PyTorch shape reasoning, MSE, `nn.Linear`, logits and classification. The preferred teaching style was to understand the shape calculation before relying on framework APIs.

## Cold-retrieval question bank

1. If `X.shape == (50, 4)` and `w.shape == (4,)`, what is `(X @ w).shape`?
2. What does each number in `(50,4)` represent in an ML dataset?
3. Why can a scalar bias be added to a `(50,)` predictions vector?
4. Given predictions `[8, 12]` and actual `[10, 9]`, compute errors, squared errors and MSE.
5. Why square the errors instead of just averaging raw signed errors?
6. If `inputs=(32,6)` and `weights=(6,10)`, what is the output shape?
7. What shape should a bias vector have for that 10-output layer?
8. Given scores `(100,3)`, what does `argmax(axis=1)` return and what shape is it?
9. Contrast the manual NumPy weight orientation here with PyTorch's stored `nn.Linear` weight orientation.

## Retrieval blueprint

1. one vector prediction shape;
2. manually compute one prediction;
3. derive MSE from errors;
4. one multi-output matrix shape;
5. one `argmax(axis=1)` classification question.

## Mastery signal

The learner can trace `X @ W + b` semantically, derive MSE, distinguish scalar/vector/matrix outputs, and explain how a score matrix becomes class predictions.
