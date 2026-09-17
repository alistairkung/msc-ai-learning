# AIMS5702 Assignment 1 — tensor vectorisation preparation plan

**Date reviewed:** 2026-09-17  
**Source:** learner-provided `AIMS_5702_2026_27_Assignment_1.ipynb`  
**Status:** assignment reviewed; preparation/scaffolding required; assignment implementation not yet evidenced

## Assignment boundary

The assignment is due **2026-09-24** and asks for both notebook and PDF submission. The supplied notebook prohibits `torch.matmul`, `torch.mm`, and `@` unless a question explicitly permits them.

The implementation work falls into two conceptual groups.

### Q1 — pairwise row dot products

Given tensors with conceptual shapes:

```text
x: (m, k)
y: (n, k)
```

produce:

```text
z: (m, n)
```

where each output entry is the dot product between one row of `x` and one row of `y`.

The same operation must be expressed in three ways:

1. exactly two Python loops;
2. broadcasting + reduction with no Python loop;
3. `einsum`.

This should be treated as one mathematical operation represented three different ways, not three unrelated coding tricks.

### Q2 — vectorised bilinear interpolation

The notebook provides a loop-based reference implementation and asks for the equivalent calculation without Python loops.

Conceptual flow:

```text
normalised query coordinates
    ↓
convert to grid coordinates
    ↓
identify four neighbouring grid values
    ↓
compute relative x/y distances
    ↓
weighted combination of four neighbours
    ↓
interpolated values
```

The main learning challenge is to replace per-point scalar/loop reasoning with batched tensor reasoning while preserving the same calculation.

## Current readiness / evidence boundary

Relevant existing evidence:

- tensor shape reasoning is a current strength;
- broadcasting and reductions have been practised recently;
- tuple-dimension reductions and `keepdim=True` were introduced/retrieved recently;
- slicing/indexing syntax can still be rusty even when the intended shape transformation is understood;
- basic `einsum` remains guided/pre-read rather than independently established;
- vectorised advanced indexing for interpolation has not yet been established.

Do **not** treat completion of generated examples or scaffolding as evidence that the assignment functions can be implemented independently.

## Preparation roadmap

The assignment should be approached through changed examples before filling the notebook blanks.

### Block A — pairwise operations + broadcasting (~60–90 min)

Goal: independently derive a pairwise row-dot-product operation without relying on matrix multiplication shortcuts.

Progression:

```text
single vector dot product
    ↓
pairwise row dot products with explicit loops
    ↓
reason about target shape (m, n, k)
    ↓
insert/broadcast dimensions deliberately
    ↓
elementwise multiply
    ↓
reduce the feature dimension k
    ↓
recover (m, n)
```

Retrieval targets:

- distinguish sample/row axes from feature axis;
- explain why a new pairwise axis is required;
- predict every intermediate shape before running code;
- identify the reduction dimension from semantics rather than guessing API syntax.

### Block B — `einsum` as index notation (~30–45 min, can sit inside Block A)

Do not teach `einsum` as a magic string to memorise.

Progression:

```text
write scalar indexed operation
    ↓
identify retained indices
    ↓
identify summed/repeated index
    ↓
translate to einsum notation
```

Target understanding: the `einsum` form should describe the same pairwise dot-product operation already understood through loops and broadcasting.

### Block C — vectorised indexing (~45–60 min)

Prepare for interpolation without using the assignment's exact implementation.

Changed-example targets:

- `floor` / integer conversion for coordinate-to-index mapping;
- clamping/boundary reasoning where required by the supplied reference;
- use vectors/tensors of row and column indices to gather many grid values at once;
- predict the shape of gathered results;
- distinguish indexing dimensions from value dimensions.

### Block D — interpolation reasoning (~60–90 min)

Progression:

```text
1D linear interpolation by hand
    ↓
one 2D bilinear interpolation point by hand
    ↓
identify the four neighbour values and weights
    ↓
trace the lecturer's loop implementation
    ↓
replace scalar-per-point variables with length-n tensors
```

Key vectorisation question:

> If loop index `i` represented all query points simultaneously, what shape would each variable have and which operations would become elementwise?

Do not jump directly from the loop reference to a copied vectorised answer.

## Assignment attempt boundary

After Blocks A–D, attempt the actual notebook independently.

Assistant role during the assignment attempt:

- ask for predicted shapes before suggesting syntax;
- explain unfamiliar PyTorch APIs;
- diagnose errors from learner attempts;
- provide progressively stronger hints rather than immediately supplying the final function;
- use changed examples when a concept needs reteaching;
- preserve learner ownership of the four requested implementations.

## Suggested schedule before 24 Sep

This assignment is nearer than the FTEC5660 receipts homework (29 Sep), so AIMS5702 needs a temporary delivery bump without erasing the other active lanes.

Suggested minimum:

```text
Session 1: 60–90 min  pairwise operations + einsum
Session 2: 90 min     vectorised indexing + interpolation
Session 3:             independent assignment attempt + targeted debugging
Final pass:            execute all cells, verify restrictions, export PDF
```

## Success criteria

By submission, distinguish **delivery success** from **learning evidence**.

Delivery success:

- notebook runs correctly;
- required restrictions are respected;
- notebook and PDF are ready for submission.

Stronger learning evidence would require the learner to be able to explain/reconstruct, on a changed example:

- why pairwise dot products create `(m, n, k)` before reducing to `(m, n)`;
- how broadcasting dimensions are inserted and aligned;
- how the einsum indices encode retained vs reduced dimensions;
- how many grid values are gathered simultaneously using tensor indices;
- how scalar bilinear interpolation becomes batched elementwise tensor arithmetic.
