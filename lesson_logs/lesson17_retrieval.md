# Lesson 17 — Mixed Retrieval: DSA + NumPy + ML Mechanics

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 17 was another explicit retrieval checkpoint. Compared with Lesson 13, it focused on a tighter set of recurring high-value patterns:

- two-sum;
- fixed sliding window;
- feature standardisation;
- multiclass linear prediction;
- linear-regression MSE loss.

Source: `foundations/retrieval/lesson17_retrieval.py` + `foundations/retrieval/test_lesson17_retrieval.py`.

## What was retrieved

### DSA
- complement-map two-sum;
- fixed-window maximum sum.

### NumPy / ML
- standardise columns to mean ≈ 0 / std ≈ 1;
- `features @ weights + biases` then `argmax(axis=1)`;
- regression predictions and MSE.

The MSE implementation uses `actual - predictions` rather than `predictions - actual`, but squaring makes the final MSE identical. That is a useful conceptual check: the sign of the error disappears after squaring.

## Core concepts reinforced

### Pattern durability

This was not about learning another API. It tested whether the learner could still derive:

```text
hash complement lookup
fixed sliding-window update
feature-wise axis statistics
matrix score shapes
scalar loss
```

### Sign and squared error

For MSE:

```text
(actual - prediction)^2 == (prediction - actual)^2
```

The direction matters for signed error interpretation and later derivatives, but not for the squared value itself.

### Shape continuity

For `features=(n,d)`, `weights=(d,c)`, `biases=(c,)`:

```text
scores=(n,c) -> argmax(axis=1) -> predictions=(n,)
```

## Chat-history context

The user's later reaction that earlier two-sum/sliding-window work had been forgotten is exactly why logs like this matter. The repo shows these patterns were not just early one-off exercises: they were explicitly retrieved again before moving into pandas and later ML work.

That makes Lesson 17 a good cold-retrieval source whenever DSA/NumPy foundations feel stale.

## Cold-retrieval question bank

1. Reconstruct two-sum using a complement dictionary; explain what is stored.
2. For a fixed window of size `k`, derive the O(1) update when moving one step right.
3. Given `(6,3)` features, what statistics are computed by `mean(axis=0)`?
4. What should standardised training-matrix feature means/stds be in this standalone exercise?
5. If `X=(20,4)` and `W=(4,3)`, what shape are class scores and predictions?
6. Given scores for three samples, choose classes manually with row-wise argmax.
7. Derive MSE for a perfect model and explain why it becomes zero.
8. Does swapping `actual - prediction` for `prediction - actual` change MSE? Why?
9. Which of the five functions here are DSA patterns and which are numerical-ML operations?

## Retrieval blueprint

For a 10–15 minute mixed review:
1. two-sum from intent;
2. fixed-window trace;
3. standardisation axis/output-statistics question;
4. classification shape trace;
5. MSE derivation.

Avoid grouping by subject; alternate DSA and ML to test switching.

## Mastery signal

The learner can reconstruct these recurring foundations without opening the earlier lesson files and can explain the invariant/shape/mathematics behind each implementation.
