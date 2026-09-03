# Lesson 13 — Cold Retrieval: DSA + NumPy + Broadcasting + Linear Models

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 13 was explicitly a **cold-retrieval lesson**, not a new-topic lesson. That matters for future tutors: the point was to see whether earlier patterns could be reconstructed without simply following the previous exercise file.

Source: `foundations/retrieval/lesson13_cold_retrieval.py` + `foundations/retrieval/test_lesson13_cold_retrieval.py`.

## What was retrieved

### Python / DSA
- first duplicate with a `seen` set;
- O(n)-style two-sum with complement lookup;
- two-pointer palindrome.

### NumPy fundamentals
- boolean-mask filtering;
- `mean(axis=0)`;
- feature standardisation.

### Broadcasting
- add a different offset to each **row** by reshaping a 1D vector:

```python
reshaped_offsets = offsets.reshape(-1, 1)
return matrix + reshaped_offsets
```

### Manual ML
- linear prediction `X @ w + b`;
- multi-output linear layer `X @ W + b`;
- model loss with MSE.

## Core concepts reinforced

### Retrieval across topic boundaries

This lesson deliberately mixed DSA and numerical ML rather than reviewing one isolated chapter. The useful skill was switching mental models:

```text
hash/set lookup
-> two pointers
-> NumPy masks/axes
-> broadcasting
-> matrix multiplication
-> loss
```

### Broadcasting by reshaping

A row-offset example made shape compatibility explicit. For:

```text
matrix:  (4, 3)
offsets: (4,)
```

`(4,)` naturally aligns with the **last** axis, so it cannot represent one offset per row of a 3-column matrix. Reshaping to:

```text
(4, 1)
```

lets each row's scalar offset broadcast across its three columns:

```text
(4,3) + (4,1) -> (4,3)
```

This is an important precursor to later reshape/transpose/batch-shape work.

## Chat-history context

The long-term learning history confirms repeated cold retrieval became a deliberate part of the study method, especially for DSA patterns and NumPy shape reasoning. This repo file is unusually valuable because it records what “cold retrieval” meant **at that stage** rather than requiring a future model to infer it.

No reliable transcript-level list of individual mistakes from Lesson 13 was recovered, so the log does not invent them.

## Cold-retrieval question bank

This lesson is already a retrieval checkpoint, so future review should **change the examples**.

1. Reconstruct first-duplicate with a set. What invariant does `seen` represent?
2. Reconstruct two-sum and explain complement lookup before writing code.
3. Check a palindrome with two pointers rather than slicing.
4. Given a NumPy array, filter values above a threshold with a mask.
5. For shape `(20,4)`, what does `mean(axis=0)` return?
6. Derive standardisation and expected post-transform statistics.
7. A matrix is `(5,3)` and you have five row offsets. What shape should the offsets have for broadcasting?
8. Why does `.reshape(-1,1)` solve that problem?
9. Trace `X @ W + b` for `X=(7,2)`, `W=(2,4)`, `b=(4,)`.
10. Explain MSE from predictions to final scalar loss.

## Retrieval blueprint

For 12–15 minutes, mix domains rather than grouping them:
1. DSA pattern;
2. NumPy axis question;
3. DSA pattern;
4. broadcasting shape question;
5. linear-layer shape;
6. MSE reasoning.

The purpose is to test **context switching and durable recall**.

## Mastery signal

The checkpoint is successful when the learner can reconstruct the underlying patterns with changed numbers/data and explain *why* the code works, rather than reproducing remembered syntax from Lessons 8–12.
