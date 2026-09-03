# Lesson 16 — Manual ML Evaluation Pipeline

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 16 composed earlier NumPy/ML functions into a single evaluation pipeline:

```text
raw features
-> standardise
-> linear class scores
-> predicted classes
-> accuracy
```

This is an important stepping stone toward later sklearn and PyTorch workflows because it turns isolated operations into an end-to-end flow.

Source: `exercises/lesson16_ml_pipeline.py` + `tests/test_lesson16_ml_pipeline.py`.

## What was implemented

```python
def prepare_features(features):
    ... standardise columns ...


def run_model(features, weights, biases):
    return features @ weights + biases


def predict_classes(scores):
    return np.argmax(scores, axis=1)


def classification_accuracy(predictions, actual):
    return (predictions == actual).mean()


def evaluate_model(features, weights, biases, actual):
    prepared = prepare_features(features)
    scores = run_model(prepared, weights, biases)
    predicted = predict_classes(scores)
    return classification_accuracy(predicted, actual)
```

## Core concepts

### Pipelines are composition

Each function has one clear responsibility, and `evaluate_model` composes them. This mirrors later ML engineering structure even though everything is still manual NumPy.

### Shape flow

For `features=(n,d)` and `weights=(d,c)`:

```text
prepare_features -> (n,d)
run_model        -> (n,c)
predict_classes  -> (n,)
accuracy         -> scalar
```

The preprocessing changes values, not shape.

### Testability of stages

The tests verify each stage separately **and** verify that `evaluate_model` produces the same result as manually composing the helper functions. This supports the study preference for pytest as a concrete scaffold: a pipeline is easier to reason about when each transformation has an explicit contract.

## Important limitation

`prepare_features` calculates mean/std from the same features it receives. At this stage, the source does **not** implement train/validation/test splitting or train-only fitted preprocessing. Lesson 31 later adds that generalisation discipline. Do not claim this lesson solved leakage.

## Chat-history context

The long-term roadmap records Lessons 10–17 as repeated NumPy shape/vectorisation/standardisation/linear-layer retrieval. This lesson appears to be where those pieces were consciously treated as a pipeline rather than isolated numerical exercises.

## Cold-retrieval question bank

1. Put these in order: `argmax`, standardisation, accuracy, linear scores.
2. If raw features are `(80,6)` and there are 4 classes, trace every intermediate shape.
3. Which pipeline stages change shape, and which only change values?
4. Why might keeping `prepare_features`, `run_model`, and `predict_classes` separate be useful for tests/debugging?
5. Reconstruct `evaluate_model` from the helper-function names without seeing its body.
6. What does `classification_accuracy` expect as its inputs here: raw scores or class indices?
7. What important real-data issue is **not** addressed by standardising all features together in this exercise?
8. If one helper function is wrong, how do stage-specific tests make diagnosis easier?

## Retrieval blueprint

1. verbal pipeline ordering;
2. shape trace from raw features to scalar accuracy;
3. reconstruct one stage;
4. reconstruct `evaluate_model` composition;
5. ask what the pipeline still lacks compared with a real train/validation/test workflow.

## Mastery signal

The learner can explain the end-to-end data flow, trace every intermediate shape and reconstruct the composed pipeline from intent rather than memorised syntax.
