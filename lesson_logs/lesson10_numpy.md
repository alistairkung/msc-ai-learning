# Lesson 10 — NumPy Foundations

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This was the transition from general Python/DSA into the numerical array model used throughout ML. The original prep plan aimed to get to NumPy early because array shapes, vectorised operations and axes would become the working language for later linear models, tensors and neural networks.

The repo shows that the actual sequence first built a firmer Python/DSA base, then started NumPy here.

## What was implemented

Source: `foundations/numpy/lesson10_numpy.py` + `foundations/numpy/test_lesson10_numpy.py`.

### Array metadata
- `.shape`
- `.ndim`
- `.size`

### Indexing and slicing
- first row: `array[0]`;
- first/last column: `array[:, 0]`, `array[:, -1]`;
- scalar element: `array[row, column]`;
- first rows/columns;
- 2D top-left slice.

### Vectorised arithmetic
- scalar + array;
- scalar * array;
- elementwise square;
- elementwise addition/multiplication of arrays;
- prediction errors and squared errors.

### Boolean masks
- passing/failing grades;
- range masks using `(a >= min) & (a < max)`;
- counting selected values;
- copying before masked replacement.

### Reductions and axes
- total sum;
- column sums / row sums;
- column means / row means;
- column maximums / row minimums;
- feature means across samples.

## Core concepts

### Shape is semantic

For a 2D ML-style array:

```text
(samples, features)
```

Example `(4, 3)` can mean 4 samples, each with 3 features.

`.shape`, `.ndim`, and `.size` answer different questions:
- shape = length of each axis;
- ndim = number of axes;
- size = total number of scalar elements.

### `:` means “all values along this axis”

```python
array[:, 0]
```

means all rows, column 0.

### Vectorisation

NumPy operations usually act elementwise across entire arrays, replacing explicit Python loops:

```python
predictions - actual
(predictions - actual) ** 2
```

This is a crucial bridge into loss functions and later tensor operations.

### Boolean masking

A comparison such as:

```python
grades >= 50
```

produces a boolean array. Indexing with that boolean array selects the matching values.

Multiple elementwise conditions use `&` / `|` with parentheses rather than Python's scalar `and` / `or`.

### Axis reasoning

For shape `(rows, columns)`:

```text
axis=0 -> collapse rows -> one result per column
axis=1 -> collapse columns -> one result per row
```

In ML semantics `(samples, features)`:

```python
features.mean(axis=0)
```

returns one mean per **feature**, calculated across samples.

## Chat-history context

The initial study plan explicitly included arrays, shapes, indexing, slicing, vectorisation and broadcasting as a major first-stage goal. Later learning records confirm NumPy became a strong practical foundation but that **shape/axis recall stayed somewhat fragile**, which is why later sessions repeatedly cold-retrieved shapes rather than treating this lesson as permanently mastered.

The user’s preferred style was semantic: not just “axis 0 is columns,” but “what does each dimension represent?” That should remain the retrieval style.

## Cold-retrieval question bank

### Shape / metadata
1. Given `X.shape == (200, 12)`, interpret both numbers in an ML dataset.
2. What are `.ndim` and `.size` for shape `(3, 4)`?
3. If `array[0]` is taken from a 2D array, what happens to the number of dimensions?

### Indexing / slicing
4. For a 3x4 matrix, write the expression for all rows of the second column.
5. What does `array[:2, :2]` return conceptually?
6. Contrast `array[0]` with `array[:, 0]`.

### Vectorisation
7. Given predictions and actual arrays, write elementwise errors and squared errors without a loop.
8. What is the difference between NumPy `first * second` and matrix multiplication?
9. Why is vectorised code important for later ML code?

### Boolean masks
10. What does `grades >= 50` return before it is used as an index?
11. Filter values between 20 inclusive and 50 exclusive.
12. Why are parentheses important around NumPy comparison conditions joined by `&`?
13. Why might `replace_failing_with_zero` copy the input before assigning through a mask?

### Axes
14. Given shape `(100, 8)`, what shape does `X.mean(axis=0)` return and what do the 8 values mean?
15. What does `X.sum(axis=1)` produce semantically?
16. If you want one average per feature, which axis should be reduced?
17. Explain `axis=0` by saying what disappears, not by memorising “column axis.”

## Retrieval blueprint

For 10–15 minutes:
1. semantic shape question;
2. row vs column indexing;
3. vectorised arithmetic;
4. boolean mask with two conditions;
5. axis=0 vs axis=1 on an ML-style matrix;
6. ask for output shapes of reductions.

If an axis question is missed, switch to a concrete small matrix and manually identify which values are combined before returning to notation.

## Known fragile point

The durable learning state later records **shape/axis reasoning as something worth periodic retrieval**. Do not interpret a correct implementation here as permanent automatic recall.

## Mastery signal

Lesson 10 is retained when the learner can interpret shapes semantically, slice rows/columns confidently, use vectorised arithmetic and masks, and reason about reductions by asking **which axis is being collapsed and what remains**.

## Longer-term dependency

This lesson unlocks nearly everything that follows in the practical ML track:

```text
NumPy shapes / vectorisation / axes
    -> broadcasting + standardisation
    -> manual linear models
    -> sklearn pipelines
    -> PyTorch tensors
    -> batch/feature shape reasoning
    -> neural networks
```
