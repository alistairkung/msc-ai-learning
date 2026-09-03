# Lesson 11 — NumPy Broadcasting and Standardisation

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 10 introduced shapes, axes, masks and vectorised operations. Lesson 11 used those ideas to perform one of the first genuinely ML-relevant preprocessing operations: **centering and standardising features without Python loops**.

Source: `exercises/lesson11_broadcasting_numpy.py` + `tests/test_lesson11_broadcasting_numpy.py`.

## What was implemented

```python
def center_features(features):
    feature_mean = features.mean(axis=0)
    return features - feature_mean


def standardise_features(features):
    centered = center_features(features)
    stds = centered.std(axis=0)
    return centered / stds
```

Tests verify:
- feature-wise centering;
- centered feature means are approximately zero;
- standardisation preserves the original matrix shape;
- each standardised feature has mean ≈ 0 and std ≈ 1.

## Core concepts

### Feature-wise statistics

For `features.shape == (samples, features)`, `features.mean(axis=0)` collapses the sample axis and returns **one mean per feature**.

### Broadcasting

If `features` has shape `(4, 3)` and `feature_mean` has shape `(3,)`, NumPy can subtract the three means from every row automatically:

```text
(4, 3)
-  (3,)
-------
(4, 3)
```

No explicit loop over rows is needed.

### Centering vs standardisation

Centering:

```text
x_centered = x - mean
```

moves each feature's mean to zero.

Standardisation:

```text
z = (x - mean) / std
```

also scales the feature so its standard deviation becomes approximately one.

## Chat-history context

Later conversation history shows standardisation repeatedly returned as a retrieval target, especially axis reasoning and the interpretation **mean ≈ 0, std ≈ 1**. Lesson 31 eventually revisited the same mathematics in a real train/validation/test workflow, adding the important rule that preprocessing statistics must be fitted on training data only.

At Lesson 11 stage, the repo supports standardising one matrix; it does **not** yet establish train-only preprocessing discipline. Do not retroactively attribute that later concept to this lesson.

## Cold-retrieval question bank

1. Given `X.shape == (100, 5)`, what is `X.mean(axis=0).shape` and what do the five values mean?
2. If `X` is `(4,3)` and `means` is `(3,)`, why can `X - means` work?
3. What property should `center_features(X).mean(axis=0)` have?
4. What two operations make up standardisation?
5. What should the standardised feature means and stds approximately be?
6. Why does standardisation preserve the input shape?
7. Explain broadcasting semantically rather than saying “NumPy just knows.”
8. If you accidentally used `axis=1`, what would you be centering instead?

## Retrieval blueprint

For 8–10 minutes:
1. one axis-shape question;
2. derive centering;
3. explain broadcasting of `(n,d) - (d,)`;
4. derive standardisation;
5. predict mean/std after transformation.

## Known fragile point

Axis and shape reasoning remained worth periodic retrieval later. Ask what each dimension **represents**, not just which axis number to type.

## Mastery signal

The learner can derive feature-wise centering/standardisation from first principles, explain why broadcasting works, and predict the output shape/statistics without running code.
