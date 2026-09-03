# Lesson 28 — PyTorch Autograd and Manual Gradient Descent

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This was a major bridge lesson: calculus and manual backprop stopped being separate maths exercises and became executable PyTorch training mechanics. It connected derivatives/gradients to `.backward()`, parameter `.grad`, gradient-descent updates, and eventually a complete manually parameterised linear model.

## What was implemented

Source: `deep_learning/autograd/lesson28_autograd.py` + `deep_learning/autograd/test_lesson28_autograd.py`.

### Scalar autograd

```python
x = torch.tensor(x_value, requires_grad=True)
loss = x**2
loss.backward()
return x.grad
```

At `x=3`, the test expects gradient `6`, matching `d(x²)/dx = 2x`.

### Two-variable gradients

Loss:

```text
L = x³ + 4xy + 2y²
```

Autograd retrieves both partial derivatives. At `(x,y)=(2,3)` the tests expect:

```text
dL/dx = 24
dL/dy = 20
```

### Manual gradient-descent step

```text
new_parameter = old_parameter - learning_rate * gradient
```

The exercise applies this independently to x and y.

### Training one weight

Model:

```text
y_hat = x * w
loss = (y - y_hat)²
```

Repeated loop:
1. forward calculation;
2. loss;
3. `loss.backward()`;
4. update `w` inside `torch.no_grad()`;
5. `w.grad.zero_()`.

The learned weight approaches 2 for `x=3`, `y=6`.

### Manual linear model

Parameters are explicit tensors:

```python
W = torch.zeros((2, 1), requires_grad=True)
b = torch.zeros((1,), requires_grad=True)
```

Forward/loss:

```python
y_hat = X @ W + b
loss = ((y_hat - y) ** 2).mean()
```

Autograd computes `W.grad` and `b.grad`; manual updates reduce loss below the test threshold.

## Core concepts

### `requires_grad=True`

Tells PyTorch to track operations involving that tensor so gradients can later be computed with respect to it.

### `.backward()`

Runs reverse-mode automatic differentiation from a scalar loss through the recorded computation graph and **accumulates** gradients into leaf tensors' `.grad` fields.

### Gradient shape

A parameter's gradient has the **same shape as the parameter** because there is one partial derivative of the scalar loss for every parameter element.

### Why `torch.no_grad()` around updates?

The parameter update itself should not become part of the differentiable computation graph. We want gradients of the model/loss computation, not gradients through the optimiser's bookkeeping update.

### Why zero gradients?

PyTorch accumulates gradients by default. If old gradients are not cleared, the next backward pass adds to them rather than replacing them.

This later becomes `optimizer.zero_grad()` when an optimiser object manages the parameters.

## Chat-history context

This lesson followed an interactive calculus sequence covering slope, derivatives, product rule, partial derivatives, gradients, chain rule and manual backprop. The learner explicitly reached the point of genuinely understanding gradient descent rather than only recognising the vocabulary. The learning plan therefore treats this as a strong conceptual milestone, with notation/algebra kept alive through short retrieval rather than restarting calculus.

Durable fragile points recorded later:
- derivative direction notation (`df/du` vs `du/df`);
- constant factors/powers during hand derivations;
- `.grad` shape;
- distinguishing a conceptual gradient mistake from algebra arithmetic.

## Cold-retrieval question bank

### Autograd
1. For `loss=x²` at `x=5`, what should `x.grad` become after backward?
2. What does `requires_grad=True` change?
3. Why must the final loss normally be scalar for a plain `.backward()` call in these exercises?
4. If `W.shape=(3,2)`, what shape should `W.grad` have?

### Gradient descent
5. If `w=4`, gradient=3 and learning rate=0.1, what is the next `w`?
6. Why do we subtract the gradient rather than add it when minimising loss?
7. What qualitative problem can a learning rate that is much too large cause?

### Training loop
8. Put these in order: backward, forward, zero gradient, parameter update, loss.
9. Why is the manual parameter update inside `torch.no_grad()`?
10. What happens if `w.grad.zero_()` is omitted across several training steps?
11. Trace the shapes in `X(10,2) @ W(2,1) + b(1,)`.
12. Explain why `W.grad` represents many partial derivatives at once.

### Link to calculus
13. For `L=(y-y_hat)²`, what chain of dependencies connects `w` to `L` when `y_hat=xw`?
14. What job does autograd automate that we previously did by hand with the chain rule?

## Retrieval blueprint

For 10–15 minutes:
1. manually derive one scalar gradient;
2. predict what autograd should return;
3. one GD update arithmetic question;
4. reconstruct the manual training loop;
5. explain gradient accumulation/no-grad;
6. trace W/b gradient shapes;
7. connect backward to chain-rule propagation.

## Mastery signal

The learner can explain—not just type—the path from scalar loss -> backward -> parameter gradients -> no-grad update -> zero gradients, and can connect every step to the calculus/gradient-descent model underneath.

This is a core prerequisite for Lessons 29–31 and later backprop/optimisation theory.
