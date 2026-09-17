# AIMS5702 Assignment 1 — pairwise vectorisation practice

**Date:** 2026-09-17  
**Status:** Pairwise dot-product representations implemented in changed-example practice; delayed cold retrieval still due

## Session purpose

Prepare for Assignment 1 without filling the assignment notebook directly. The session used a red-test → learner implementation loop on changed examples.

The focus was the Q1 prerequisite family:

```text
single dot product
    -> pairwise row dot products with two loops
    -> pairwise row dot products with broadcasting/reduction
    -> the same operation in einsum
```

The assignment's interpolation/vectorised-indexing section was deliberately left for a later block.

## Pre-implementation retrieval

### Reductions / semantic axes

For a tensor shaped `(samples, time, features)`, output shapes after reductions were retrieved correctly. The first semantic description briefly confused which axis had been reduced, then corrected once the axis roles were made explicit.

### Integer indexing vs slicing

The learner initially predicted that integer indexing such as `x[:, 1]` would retain a singleton dimension. The distinction was then recovered:

```text
integer index  -> select one value and remove that axis
one-item slice -> preserve that axis with size 1
```

The learner immediately transferred this to changed examples such as `1:2` slices.

### Broadcasting

Broadcasting output shapes were generally strong. Attaching concrete numbers and semantic labels to axes made the reuse pattern clear:

```text
size 1 on an axis -> reuse/broadcast along that axis
```

For `(samples, time, features)`, the learner correctly reasoned about per-time, per-feature and per-sample scaling after short concrete examples.

### `unsqueeze`

The learner first proposed `reshape` when asked how to insert a singleton axis. `reshape` was accepted as valid, and `unsqueeze` was introduced as the more expressive operation for inserting one size-1 dimension. Axis placement transferred immediately on changed shapes.

## Pairwise dot-product concept

The operation was built from first principles.

For:

```text
x: (m, k)
y: (n, k)
```

we want every x row paired with every y row:

```text
result: (m, n)
```

with:

```text
result[m,n] = sum_k x[m,k] * y[n,k]
```

The learner correctly understood that `k` is the feature dimension consumed by the dot-product reduction, while `m` and `n` survive as output axes.

Equivalent linear-algebra description introduced after implementation: `X Y^T`.

## Learner implementations

### Single dot product

After isolating the test contract, the learner implemented:

```python
return (x * y).sum()
```

This was the first primitive used by the two-loop version.

### Two Python loops

The learner independently proposed the core structure:

```text
for each row m in x:
    for each row n in y:
        result[m,n] = dot_product(x[m], y[n])
```

Targeted Python/API help was needed for:

- `range(len(x))` rather than iterating over the integer `len(x)`;
- allocating the output tensor with `torch.zeros((len(x), len(y)))` rather than the initially recalled `arange` idea.

The important conceptual point remained intact: the two loops iterate over the two output pairing axes; the feature computation is performed by tensor operations inside `dot_product`.

### Broadcasting + reduction

The learner derived the pairwise shape construction interactively:

```text
x: (m, k) -> (m, 1, k)
y: (n, k) -> (1, n, k)

multiply -> (m, n, k)
sum k   -> (m, n)
```

One correction was needed for the singleton placement on `y`. During the first code expression, reminders were also needed that `unsqueeze` returns a new tensor and that `.sum()` without a dimension would collapse all axes.

After those corrections, the learner wrote and later implemented the full expression directly:

```python
(x.unsqueeze(1) * y.unsqueeze(0)).sum(axis=2)
```

Changed-dimension transfer succeeded before implementation.

### `einsum`

`einsum` was taught from index semantics rather than as a memorised string.

The learner correctly inferred:

```text
indices on the output survive
indices omitted from the output are reduced
```

and successfully interpreted:

```text
ij->i
ij->j
ij->ji
```

before transferring pairwise dot products to changed semantic labels.

The learner independently produced an equivalent pattern such as:

```text
ik,jk->ij
```

and then implemented:

```python
return torch.einsum("mk,nk -> mn", x, y)
```

## Representation equivalence

The durable synthesis from the session is that these are not three different mathematical problems:

```text
TWO LOOPS
result[m,n] = (x[m] * y[n]).sum()

BROADCASTING
(m,1,k) * (1,n,k)
    -> (m,n,k)
    -> sum k
    -> (m,n)

EINSUM
mk,nk -> mn
```

They are three representations/execution strategies for the same pairwise dot-product matrix.

## Evidence boundary

Strong same-session evidence:

- output `(m,n)` and reduction of `k` are understood;
- dot product is understood as elementwise multiply + sum;
- pairwise looping structure was independently proposed;
- broadcasting shapes transferred to changed dimensions after one initial correction;
- final broadcasting implementation was recalled after the scaffold;
- einsum index semantics transferred to changed examples before implementation;
- learner implemented all four changed-example practice functions.

Still fragile / not yet delayed cold evidence:

- integer-index vs slice rank behaviour was rusty initially;
- `unsqueeze` API name was newly introduced;
- output-buffer allocation / `range(len(...))` needed Python support;
- first vectorised expression needed reminders about using returned `unsqueeze` tensors and specifying the reduction axis;
- einsum is newly learned in this session;
- advanced tensor indexing and bilinear interpolation have not yet been taught/practised;
- no claim is made about independent completion of the actual Assignment 1 notebook.

## Next step

Do not immediately repeat the same pairwise exercise.

Next assignment-prep block:

1. one short changed pairwise cold check;
2. vectorised row/column indexing and gathering many grid values simultaneously;
3. 1D interpolation;
4. one bilinear-interpolation point by hand;
5. trace the supplied loop implementation;
6. vectorise the loop variables across all query points;
7. attempt the assignment notebook independently with progressive hints/debugging only.
