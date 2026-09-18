# AIMS5702 — Representation checkpoint and interpolation bridge

**Date:** 2026-09-18  
**Status:** Substantive guided study session; interpolation concept established, assignment implementation not yet attempted

## Session goal

Use the post-lecture calibration from 17 Sep to deepen low-level tensor representation first, then work toward the bilinear-interpolation portion of Assignment 1 without copying an assignment solution.

## Dtype / storage checkpoint

### Storage-size calculation

On a changed `float32` tensor the learner initially converted 32 bits to “4 KB per item” rather than 4 bytes, then corrected the unit chain. A changed `float16` example was then calculated correctly:

```text
16 bits / 8 = 2 bytes per element
500,000 elements -> 1,000,000 bytes -> about 1 MB
```

Current evidence: the element-count × bytes-per-element method is understood, but bits/bytes/KB/MB unit discipline should be sampled again later.

### Signed int8 / two's complement

The learner explicitly reported having no concept of how signed `int8` represented negatives, so this was taught from first principles rather than treated as recall.

Built model:

```text
n bits -> 2^n bit patterns
signed n-bit integer range -> -2^(n-1) to 2^(n-1)-1
int8 -> -128 to 127
```

Two's-complement intuition was introduced using signed place values. For int8 the high bit has weight -128 and remaining weights are 64,32,16,8,4,2,1. After teaching, the learner successfully decoded a changed pattern as `-125`.

Evidence boundary: newly taught + successful immediate transfer, not cold-independent knowledge.

### Floating-point representation

Scientific notation was used as the bridge. The learner correctly identified exponent vs significand after terminology correction.

Current conceptual model:

```text
sign        -> positive / negative
exponent    -> scale / representable range
significand -> precision
```

The learner initially reversed exponent-range vs significand-precision, then correctly transferred the distinction to a changed hypothetical format.

Evidence boundary: conceptual foothold with immediate corrected transfer; IEEE-754 bit-level mechanics were intentionally not over-drilled.

## Strides, storage, views and contiguity

This was the deepest drill of the session.

The learner now has the useful intuition:

> A tensor is contiguous when its current logical layout corresponds to a compact traversal of the underlying storage.

They correctly recovered contiguous 2D strides such as `(4,1)`, then worked through transpose and stepped-slice views. Early in the drill they incorrectly expected transpose and stepped slicing to remain contiguous because the underlying storage itself remained ordered; after concrete storage walks, they explained why the logical traversal no longer matches compact storage order.

Durable connection:

```text
storage
  <-> strides
  <-> logical tensor layout
  <-> contiguity
```

### Lecturer slicing formulas recovered

The learner supplied the exact formulas remembered from lecture:

```text
Storage indexing equation:
s[stride0 * i0 + stride1 * i1 + offset]

Base offset:
i0’ * stride0 + i1’ * stride1
```

These were then applied to changed examples.

Important distinction exposed:

```text
slice START -> affects base offset
slice STEP  -> affects new stride
```

The learner briefly used the new stepped stride while calculating an offset, then corrected on explanation and later calculated changed offsets correctly.

For ordinary positive-step slicing, the learner successfully transferred:

```text
new_stride[d] = old_stride[d] * slice_step[d]
```

A later changed example correctly produced `(40,3)` from old stride `(20,1)` with slice steps 2 and 3.

### Slice syntax

`start:stop:step` was not initially retrievable when all three fields appeared. It was re-taught as start inclusive, stop exclusive, step jump. Immediate changed examples were then enumerated correctly.

Keep slice-length/index enumeration as a small future retrieval target.

## Singleton-axis insertion

The learner clarified that the lecture used `newaxis`. `np.newaxis` / `None` indexing was connected to the previously introduced PyTorch `unsqueeze` operation:

```text
x[:, np.newaxis, :]
x[:, None, :]
x.unsqueeze(1)

-> insert singleton axis at position 1
```

Changed shape examples were answered correctly for singleton insertion at the front, middle and end. The learner asked whether `unsqueeze` is more idiomatic; for PyTorch it was framed as the more explicit dimension-manipulation API while both representations should be readable for the course.

## Bilinear interpolation — conceptual bridge

Interpolation was built from scalar intuition rather than presenting the final formula.

### 1D interpolation

The learner understood:

```text
value = start + fraction * (end - start)
```

After one initial mistake that treated coordinate distance as direct value change, changed interpolation examples were calculated correctly.

For a fractional coordinate such as 3.7:

```text
lower index = floor(3.7) = 3
upper index = 4
fraction = 3.7 - 3 = 0.7
```

### 2D / bilinear interpolation

For a query point, the learner independently identified lower/upper row and column indices and then the four surrounding grid values after one early neighbour-selection correction.

Durable model:

```text
fractional (row, col)
    ↓
lower / upper row + col
    ↓
four surrounding grid values A B C D
    ↓
column fraction + row fraction
    ↓
interpolate A -> B horizontally
interpolate C -> D horizontally
    ↓
interpolate top -> bottom vertically
    ↓
final value
```

On a changed numerical example the learner correctly calculated top interpolation, bottom interpolation and final bilinear value `84`.

### Vectorisation bridge

Advanced paired indexing was introduced:

```python
grid[rows, cols]
```

with the model that same-shaped row/column index tensors pair element-by-element. The pairing concept was understood, though reading values from the toy grid produced a couple of lookup slips.

The learner recognised that interpolation arithmetic can operate elementwise over tensors. The vectorised arithmetic was reconstructed with one final-direction correction:

```python
top = A + col_fraction * (B - A)
bottom = C + col_fraction * (D - C)
result = top + row_fraction * (bottom - top)
```

Do not treat this as an independent implementation of the assignment; the expressions were developed interactively.

## Assignment test harness — understood

The supplied Test 1 was read as a test/oracle rather than implementation.

The learner now understands:

- `v` is the random `(h,w)` value grid;
- `x` and `y` enumerate its integer coordinate axes;
- SciPy `RegularGridInterpolator` is the trusted reference implementation;
- `x_ref` and `y_ref` are `(vlen,)` random normalised coordinates in `[0,1)`;
- multiplying by `w-1` / `h-1` converts normalised coordinates to grid coordinates;
- stacking gives `(vlen,2)` query coordinate pairs in `(y,x)` order;
- SciPy produces one reference interpolated value per query;
- the loop and no-loop student functions must match those reference values within tolerance.

The learner correctly identified that their implementation will first need to convert normalised coordinates into grid coordinates before selecting neighbours.

## Evidence boundary

### Meaningfully improved today

- signed-int range and two's-complement place-value intuition: newly taught, immediate changed-example transfer;
- float sign/exponent/significand roles: newly clarified, immediate corrected transfer;
- strides/storage/contiguity: substantially deeper conceptual model with multiple changed examples;
- lecturer storage-index/base-offset formulas: recovered and applied;
- `start:stop:step`: reactivated after initial failure;
- `np.newaxis` / singleton insertion: immediate changed-example transfer;
- 1D and bilinear interpolation: conceptual algorithm now understood and manually executed;
- advanced paired indexing: concept introduced and understood at a guided level;
- assignment Test 1: purpose and data flow understood.

### Still not established

- delayed cold retrieval of today's dtype/stride/slicing material;
- automatic slice-size counting;
- independent advanced-indexing implementation;
- boundary handling for interpolation;
- independent `interp2d_forloop` implementation;
- independent `interp2d_nofor` implementation;
- passing Assignment 1 interpolation tests.

## Next session

Do **not** restart interpolation from first principles.

Estimated remaining focused implementation runway: roughly 2–3 hours, depending on PyTorch indexing/API debugging.

Resume with:

1. short changed-example retrieval of lower/upper indices, fractions, stride/offset distinction and paired indexing;
2. read the supplied `interp2d_forloop` reference/target context and map each scalar variable to the model above;
3. learner implements/reconstructs the loop version with hints/debugging;
4. translate scalar-per-point variables into `(N,)` tensors;
5. learner implements the no-loop version using advanced indexing + elementwise interpolation;
6. run the supplied tests and localise failures, including edge/boundary cases.

Do not provide the complete assignment solution before the learner has attempted each implementation.
