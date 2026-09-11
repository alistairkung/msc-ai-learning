# AIMS5702 — Tensor operations cold review

_Date: 2026-09-11_  
_Status: 45-minute maintenance/retrieval session; no lecture today_

## Purpose

Short cold refresh of basic tensor operations already encountered in NumPy/PyTorch preparation, with emphasis on writing/reasoning through slicing, broadcasting, transpose/permute, reshape and reductions. This was deliberately a maintenance session rather than new frontier work.

## Evidence boundary

Most of this session was **retrieval/reactivation of prior material**, not first teaching. `keepdim=True` was the clear exception: the learner explicitly said they had not encountered it, so it was introduced as new material and must not be recorded as a retrieval miss.

No durable implementation file/test was created; evidence comes from interactive changed examples and code snippets.

## Slicing — rusty syntax and axis placement, then rapid recovery

The learner initially remembered ordinary start/stop slicing but had forgotten the three-part form:

```text
start : stop : step
```

The review recovered:

```text
::2       -> start at beginning, every second item
1::2      -> start at index 1, every second item
2:9:3     -> indices 2,5,8
-1        -> last item
-2        -> second-last item
-2:       -> last two items
:-1       -> everything except the last item
```

A changed example `x[1:, ::2, 2:9:3]` on shape `(4,7,10)` was eventually answered correctly as shape `(3,4,3)`.

Important fragility: **mapping the slice to the intended tensor axis**. Given `(batch,tokens,features) = (64,20,16)`, the learner first placed `-5:` on the feature axis when asked for the last five tokens, then corrected to:

```python
x[:, -5:, :]
```

Another useful correction: `-5:` and `-5::` are equivalent when stop and step are omitted/defaulted; the issue was axis placement, not the extra colon.

Do not over-interpret early value-tracing errors on `x[::2,1::2]`: after the row-index distinction (`::2 -> 0,2`; `1::2 -> 1,3`) was repaired, the slicing model returned.

## Broadcasting — concept largely intact

The learner correctly reasoned that for:

```text
x      (64,10,8)
bias          (8,)
```

the eight feature-specific values are applied to every token in every sample, yielding `(64,10,8)`.

They also correctly handled:

```text
(32,10,8)
    (10,1)
```

by right-aligning dimensions: `10` matches and `1` expands to `8`, with the missing leading dimension broadcasting across the batch.

They correctly rejected `(32,10,8) + (10,)` because the rightmost comparison is `8` vs `10`, with neither dimension equal to `1`.

Durable rule retrieved:

> Broadcasting compares shapes from the right; aligned dimensions must be equal or one must be `1`.

## Feature centring — reasoning intact, minor API rust

For `x.shape == (100,8)`, the learner correctly chose the sample dimension for feature means and correctly relied on `(8,)` broadcasting back across `(100,8)`.

They wrote `x.means(axis=0)`, which exposed a small API/spelling slip rather than a conceptual gap. Correct PyTorch form used in review:

```python
m = x.mean(dim=0)
centered = x - m
```

Treat this as Python/PyTorch API rust, not loss of reduction/broadcasting understanding.

## Transpose vs permute

For `(batch,tokens,features) -> (batch,features,tokens)`, the learner first supplied the desired full axis order `(0,2,1)`. This was used to recover the distinction:

```text
transpose(a,b) -> swap exactly two dimensions
permute(...)   -> specify the complete new dimension order
```

They then correctly produced `permute(0,3,1,2)` to transform shape `(2,3,4,5)` into `(2,5,3,4)`.

The learner also correctly predicted:

```text
x: (8,12,5)
y = x.transpose(1,2) -> (8,5,12)
y is non-contiguous
z = y.reshape(8,-1)  -> (8,60)
```

This is useful supporting retrieval for yesterday's newer view/contiguity material, but stride arithmetic itself was not re-tested today.

## Reshape

When asked to flatten `(16,20,32)` into `(320,32)`, the learner initially called the operation “transpose” while giving the intended target shape. The operation distinction was repaired:

```python
x.reshape(-1, 32)
```

They immediately predicted `(8,12,5).reshape(-1,5) -> (96,5)` correctly.

Treat this as an operation-name distinction worth occasional changed-example retrieval, not a failure of element/shape reasoning.

## Reductions

Reduction semantics were strong:

- `sum(dim=2)` on `(32,10,8)` -> `(32,10)`, correctly explained as summing the eight features for each token;
- `mean(dim=1)` on `(64,5,16)` -> `(64,16)`, correctly identified as averaging across tokens;
- after learning multi-axis reduction, the learner correctly wrote `x.mean(dim=(0,2))` for shape `(16,7,4,20)`, leaving `(7,20)`.

The learner initially proposed separate token/batch means for a requested mean over both dimensions. This prompted introduction of tuple dimensions:

```python
x.mean(dim=(0,1))
```

The final multi-axis example was then answered correctly.

## New material — `keepdim=True`

The learner explicitly reported no prior encounter with `keepdim`, so it was taught rather than cold-tested.

New model:

```text
normal reduction:
(32,10,8) --mean dim=1--> (32,8)

keepdim=True:
(32,10,8) --mean dim=1--> (32,1,8)
```

The purpose became concrete in the centring exercise. For `last_five.shape == (64,5,16)`, the learner independently recognised that `(64,16)` would not broadcast correctly back across `(64,5,16)` and said **“we need to keep dim”**. Thus, immediately after introduction, they successfully applied:

```python
means = last_five.mean(dim=1, keepdim=True)  # (64,1,16)
centered = last_five - means                 # (64,5,16)
```

Record `keepdim` as **newly taught + successfully applied with immediate context**, not durable independent mastery yet.

## Current assessment

### Retrieved well

- semantic shape reasoning;
- right-aligned broadcasting rules;
- reductions and which dimensions disappear;
- feature-wise centring logic;
- transpose producing non-contiguous views;
- `permute` full-axis ordering once the distinction was surfaced.

### Rusty but recovered

- `start:stop:step` slicing syntax;
- negative/stepped slice details;
- attaching a slice to the correct semantic axis;
- `transpose` vs `permute` vs `reshape` operation names;
- occasional PyTorch API spelling/convention.

### Newly introduced

- `keepdim=True`;
- reducing over multiple dimensions with a tuple such as `dim=(0,1)`.

## Future retrieval

Do not replay the whole tensor block. A later 5–10 minute changed-example check can sample:

1. one stepped/negative slice on a `(batch,tokens,features)` tensor;
2. one valid and one invalid broadcasting pair;
3. one `transpose` vs `permute` choice;
4. one reshape that combines dimensions;
5. one reduction where `keepdim=True` is needed for a subsequent broadcast;
6. one multi-axis reduction.

Continue to use **shapes as the learner's primary reasoning anchor**. When an answer fails, distinguish syntax/axis placement from an underlying tensor-concept gap.
