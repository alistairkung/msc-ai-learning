# AIMS5702 Lecture 1/2 — pre-lecture bridge

_Date: 2026-09-10_
_Status: pre-lecture preparation; source decks supplied by learner_

## Why this note exists

The first two AIMS5702 decks overlap substantially with the existing NumPy/PyTorch preparation, but introduce a lower-level systems view of tensors that had not previously been studied. This note records the boundary between retrieved prior knowledge and newly taught material so later review does not mistake today's guided introduction for historical mastery.

## Existing preparation retrieved successfully

The session cold-recalled several concepts before introducing new material:

- tabular shape `(samples, features)`;
- reduction semantics: the selected axis disappears;
- `(n,d) - (d,)` broadcasting across samples;
- matrix multiplication shape `(batch,in) @ (in,out) -> (batch,out)`;
- tensor reductions after transformations.

This aligns with Lessons 10, 11 and 27. Shape/axis reasoning remains worth occasional retrieval: an initial image-layout question was deliberately discarded because image/channel conventions had not been part of prior preparation.

## New material introduced from AIMS5702

### Dtypes and memory estimation

Core model:

```text
8 bits = 1 byte
float32 = 4 bytes/value
float16 = 2 bytes/value
int8 = 1 byte/value

number of elements = product(shape)
memory bytes = number of elements * bytes per element
```

Successful changed examples included:
- `(100,8)` float32 -> 800 elements -> 3200 bytes;
- 1B float32 parameters -> roughly 4 GB decimal storage;
- 3B float16 parameters -> roughly 6 GB decimal storage;
- `(64,512)` float16 -> 32768 elements -> 65536 bytes.

The learner initially carried the correct `4 billion bytes` arithmetic into the wrong output unit (`4 billion GB`), then corrected the bytes-to-GB conversion and subsequent examples were correct.

### Floating-point intuition

Introduced only at the level required by the supplied deck:

```text
more exponent bits -> wider magnitude/range
more mantissa/significand bits -> greater precision
```

The learner correctly inferred the range-vs-precision trade-off. Exact IEEE encoding was intentionally not taught as a pre-lecture requirement.

### Flat storage, shape, stride and offset

New mental model:

```text
tensor view = logical shape + strides + offset over underlying flat storage
```

For a normal contiguous `(2,3)` tensor:

```text
stride = (3,1)
```

because moving one row advances 3 storage positions and moving one column advances 1.

For a normal contiguous `(2,3,4)` tensor:

```text
stride = (12,4,1)
```

The learner understood the physical jump interpretation after worked examples.

Important new fragile point: the learner initially recomputed strides from a sliced view's new shape, e.g. predicting `(8,4,1)` for a `(2,2,4)` view. The correction was that basic slicing does not repack storage; a view may keep `(12,4,1)`. Durable rule:

> Shape alone does not determine the stride of a view. For a view, reason about how it walks the underlying storage.

### Views, copies and contiguity

Experimentally inspected in PyTorch:

- `x.T` changed `(2,3)/(3,1)/contiguous=True` to `(3,2)/(1,3)/contiguous=False`;
- mutation through the transpose view changed the original tensor, confirming shared storage;
- basic slicing such as `x[:,1:]` shares storage;
- explicit index-list selection such as `x[:,[0,2]]` produced independent storage in the exercised case, so mutation did not affect `x`;
- step slicing `x[:,::2]` was reasoned as representable by changed strides;
- shared storage and contiguity were distinguished as separate properties.

Fresh fragilities:
- initially assumed a basic slice's stride could be recomputed as though the slice were freshly contiguous;
- initially predicted an indexed selection would share storage until tested;
- stride prediction after transpose needed support, although the learner quickly understood that transposing axes swaps their associated shape/stride entries.

### Einstein summation

Introduced at the deck's basic level.

Durable reading rule:

```text
indices on the output survive
contracted/omitted indices are summed over
```

Examples discussed:

```text
ij->i      row sums
ij->j      column sums
ij,j->i    matrix-vector product
ik,kj->ij  matrix multiplication as an einsum expression
```

A small numerical example expanded `ij,j->i` into elementwise products followed by a sum over `j`. The learner correctly identified surviving/summed indices and output shapes after the explanation.

## Coding evidence

This was interactive scratch/REPL work rather than a committed numbered exercise. PyTorch was used to inspect:

- `.shape`;
- `.stride()`;
- `.is_contiguous()`;
- transpose behaviour;
- mutation through shared views;
- mutation after explicit index-list selection.

Do not infer independent mastery from this session. The systems concepts were introduced immediately before the first AIMS5702 lecture.

## Cold-recall targets for a later AIMS5702 review

Use changed examples and ask one at a time:

1. Estimate tensor/model storage from shape/parameter count and dtype.
2. Convert bits to bytes and explain why float16 halves parameter storage relative to float32.
3. Explain range vs precision using exponent vs mantissa/significand intuition.
4. Derive contiguous strides for a small 2D/3D tensor by physical storage jumps.
5. Given a basic slice, explain why its new shape may not imply fresh contiguous strides.
6. Predict whether transpose/basic slicing/index-list selection shares storage in examples like those used here.
7. Distinguish shared storage from contiguity.
8. Read a simple einsum by identifying which indices survive and which are summed away.

## Next course-facing step

Attend Lecture 1/2 with special attention to:
- lecturer terminology for dtype/float representation;
- stride/offset/view/contiguity examples;
- the exact scope expected for `einsum`;
- CPU/GPU memory and device movement, which was only lightly previewed here.

After the lecture, record what was actually emphasized before expanding this course note further.
