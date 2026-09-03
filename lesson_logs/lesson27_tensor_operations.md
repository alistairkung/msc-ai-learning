# Lesson 27 — Tensor/Shape Operations

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This lesson refreshed and extended multidimensional NumPy shape reasoning immediately before the move into PyTorch/autograd. Despite the lesson name saying “tensor operations”, the implementation uses NumPy arrays; the conceptual target was dimension semantics that transfer directly to tensors.

## What was implemented

Source: `deep_learning/tensor_operations/lesson27_tensor_operations.py` + `deep_learning/tensor_operations/test_lesson27_tensor_operations.py`.

Exercises covered:
- batch mean via `X.mean(axis=0)`;
- feature centring via broadcasting;
- flattening every sample while preserving the batch dimension;
- swapping the last two axes of a 3D array;
- linear layer `X @ W + b`.

Examples from tests:

```text
(3, 2, 2) --mean axis 0--> (2, 2)
(2, 3, 4) --flatten samples--> (2, 12)
(3, 2, 4) --flatten samples--> (3, 8)
(2, 3, 4) --transpose(0,2,1)--> (2, 4, 3)
(2, 3) @ (3, 2) + (2,) -> (2, 2)
```

## Core concepts

### Preserve batch semantics

For ML arrays/tensors, the first dimension commonly represents independent samples. Flattening should often preserve that dimension:

```python
X.reshape(X.shape[0], -1)
```

The `-1` asks NumPy to infer the product of all remaining dimensions.

### Reduction changes shape

`mean(axis=0)` collapses the batch axis. For `X.shape = (batch, h, w)`, the result is `(h, w)`—the average value at each within-sample position across the batch.

### Transpose is axis reordering

`transpose(0, 2, 1)` preserves axis 0 and swaps axes 1/2. This should be reasoned about by axis meaning, not memorised as magic syntax.

### Linear-layer shape rule

```text
(batch, in_features) @ (in_features, out_features)
    -> (batch, out_features)
```

Bias `(out_features,)` then broadcasts across the batch.

## Chat-history context

Later learning-state notes repeatedly identify shape reasoning as a **retrieval-sensitive** skill: occasional slips included losing the batch dimension or mixing manual NumPy weight orientation with PyTorch's stored `nn.Linear.weight` orientation. This lesson is therefore a useful cold-retrieval anchor rather than old material to ignore.

## Cold-retrieval question bank

1. If `X.shape=(32, 3, 28, 28)`, what should a “flatten each sample” output shape be?
2. Why is `reshape(X.shape[0], -1)` safer conceptually than flattening the whole array?
3. Given `(5,4,3)`, what shape results from `.mean(axis=0)`? What was averaged?
4. Given `(8,10,20)`, what shape results from `transpose(0,2,1)`?
5. For `X=(32,30)` and `W=(30,16)`, what is `X @ W`?
6. What shape must a bias have to add one value per output feature?
7. Explain centring by broadcasting a `(features,)` mean vector across `(samples, features)`.
8. How does NumPy `W.shape=(in,out)` differ from PyTorch `nn.Linear(in,out).weight.shape` later?

## Retrieval blueprint

1. one reduction-shape question;
2. one flatten-preserving-batch question;
3. one transpose trace;
4. one linear-layer multiplication;
5. explicitly contrast conceptual linear map with PyTorch stored weight orientation.

## Mastery signal

The learner can predict output shapes before running code, preserve batch dimensions deliberately, explain which axis is reduced/reordered, and trace `X @ W + b` semantically rather than by rote.
