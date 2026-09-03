# Lesson 14 — Manual Multiclass Classification Pipeline

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 12 introduced linear scores and `argmax`; Lesson 14 turned those pieces into a small **multiclass classification pipeline**: compute class scores, choose the best class, compare with labels, calculate accuracy.

Source: `machine_learning/fundamentals/lesson14_classification_pipeline.py` + `machine_learning/fundamentals/test_lesson14_classification_pipeline.py`.

## What was implemented

```python
def class_scores(features, weights, biases):
    return features @ weights + biases


def predict_classes(features, weights, biases):
    scores = class_scores(features, weights, biases)
    return np.argmax(scores, axis=1)


def classification_accuracy(features, weights, biases, actual):
    predictions = predict_classes(features, weights, biases)
    return (predictions == actual).mean()
```

The tests use 4 samples, 2 features and 3 classes:

```text
features: (4,2)
weights:  (2,3)
biases:   (3,)
scores:   (4,3)
predicted class indices: (4,)
```

## Core concepts

### Scores are not yet probabilities

The linear model here produces one raw **score** for each class. The highest score wins. The source files do not introduce softmax/probabilities in this lesson, so future retrieval should preserve that framing rather than silently upgrading it.

### Row-wise class selection

Each row belongs to one sample; each column is one class score:

```text
sample 0: [score class0, score class1, score class2]
```

`argmax(axis=1)` therefore chooses one class index per row/sample.

### Accuracy via boolean mean

```python
predictions == actual
```

produces a boolean vector. NumPy treats `True`/`False` numerically in `.mean()`, giving the fraction correct.

Example from the test: 3 correct out of 4 -> `0.75`.

## Chat-history context

This manual pipeline later became a conceptual bridge to sklearn classification and then neural-network logits. The long-term record says classification-score matrices and `argmax` were repeatedly retrieved across Lessons 10–17, suggesting the goal was shape/semantic fluency rather than memorising one implementation.

## Cold-retrieval question bank

1. If `X=(64,5)` and `W=(5,4)`, what is the score matrix shape?
2. What does each row and each column of `(64,4)` mean?
3. Which axis should `argmax` use to get one class per sample? Why?
4. What shape should the class-prediction array have?
5. Are these class scores probabilities? What does the source actually establish?
6. Given scores `[[1,8,3],[7,2,4]]`, what classes are predicted?
7. Given predictions `[2,0,1,1]` and actual `[2,1,1,1]`, calculate accuracy.
8. Why does `(predictions == actual).mean()` work?
9. Trace the whole pipeline: features -> scores -> predicted classes -> accuracy.

## Retrieval blueprint

1. one matrix-shape calculation;
2. interpret score matrix semantically;
3. `argmax` axis question;
4. manual accuracy example;
5. reconstruct three pipeline functions from intent.

## Mastery signal

The learner can trace a multiclass linear classifier from `(samples, features)` to `(samples, classes)` scores, choose classes row-wise and calculate accuracy without confusing scores, class indices and correctness.
