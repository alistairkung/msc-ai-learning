# Lesson 15 — NumPy Challenge: Combining Preprocessing, Classification and Array Operations

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 15 was a consolidation/challenge lesson. Rather than introducing one new concept, it combined the NumPy/ML ideas from Lessons 10–14 and added a few practical array operations: feature concatenation, clipping and confidence-margin calculation.

Source: `exercises/lesson15_numpy_challenge.py` + `tests/test_lesson15_numpy_challenge.py`.

## What was implemented

- column-wise centering;
- standardisation;
- horizontal feature concatenation with `np.concatenate(..., axis=1)`;
- linear class-score prediction;
- best class with `argmax(axis=1)`;
- counting correct predictions;
- accuracy;
- simple score rescaling + clipping to `[0,1]`;
- confidence margin = largest class score minus second-largest score.

## Core concepts

### Combining feature sets

If two matrices contain the same samples but different features:

```text
first:  (n, a)
second: (n, b)
```

concatenating on `axis=1` gives:

```text
(n, a+b)
```

Rows/samples remain aligned; columns/features are appended.

### Count correct vs accuracy

```python
(predictions == actual).sum()
```

counts correct predictions.

```python
(predictions == actual).mean()
```

returns the fraction correct.

Keep those two outputs distinct.

### Clipping

The exercise's `normalise_scores` is specifically:

```python
scores / 100
np.clip(..., 0, 1)
```

This is a simple numeric transformation from the source exercise, **not** a principled probability calibration method. Future tutors should not describe these values as softmax probabilities.

### Confidence margin

For each sample:
1. sort the class scores;
2. select highest and second-highest;
3. subtract them.

A larger margin means the winning raw score is further ahead of the runner-up. The source exercise does not claim this is calibrated confidence.

## Chat-history context

The durable history records repeated practice with shapes, classification score matrices, `argmax`, standardisation and NumPy vectorisation through Lessons 10–17. Lesson 15 is useful evidence that these ideas were deliberately recombined rather than taught once and abandoned.

## Cold-retrieval question bank

1. If feature matrices are `(100,3)` and `(100,5)`, what shape results from `axis=1` concatenation?
2. What would `axis=0` mean instead, and when would that be invalid?
3. Distinguish `count_correct` from `accuracy`.
4. Given five predictions with three correct, what do those two functions return?
5. Why should `argmax(axis=1)` be used on `(samples, classes)` scores?
6. Given raw scores `[-20,50,120]`, apply the exercise's divide-by-100 then clip transformation.
7. Why should those clipped values not automatically be called probabilities?
8. Given class scores `[2,8,5]`, calculate the winning class and confidence margin.
9. How can the largest and second-largest score be found vectorially for every row?
10. Reconstruct the pipeline from standardised features through accuracy.

## Retrieval blueprint

For 10–12 minutes:
1. concatenate two feature matrices and predict shape;
2. standardisation recall;
3. score -> argmax -> accuracy;
4. one clipping example;
5. one confidence-margin calculation.

## Mastery signal

The learner can combine NumPy operations into a small pipeline, reason about concatenation axes and shapes, and keep raw scores, predicted classes, count-correct, accuracy and heuristic score margin conceptually separate.
