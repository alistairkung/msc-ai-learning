# Lesson 22 — sklearn Classification Pipeline + Thresholds

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

Lesson 22 consolidated the sklearn classification workflow into a reusable end-to-end pipeline and then exposed an important idea hidden by `.predict()`: binary classification decisions depend on a probability threshold.

## What was implemented

Source: `exercises/lesson22_classification_pipeline.py` + `tests/test_lesson22_classification_pipeline.py`.

The pipeline:

```text
DataFrame
 -> choose X/y
 -> stratified 80/20 split
 -> fit LogisticRegression
 -> predict test classes
 -> accuracy / precision / recall / confusion matrix
 -> return model + predictions + actual labels + metrics
```

The lesson also implemented:

```python
probabilities = model.predict_proba(X_test)
class_1_prob = probabilities[:, 1]
predictions = (class_1_prob >= threshold).astype(int)
```

Tests verified that lowering the threshold from 0.5 to 0.3 produced more positive predictions for the same probabilities.

## Core concepts

### Probabilities vs class predictions

`predict_proba` returns per-class probabilities. In binary sklearn classification, column 1 corresponds to the probability of class 1.

A class prediction can be constructed from a chosen threshold:

```text
P(class 1) >= threshold -> predict 1
otherwise               -> predict 0
```

### Threshold trade-offs

Lowering the threshold generally predicts class 1 more often:
- recall may increase;
- false positives may also increase;
- precision may change.

Raising the threshold makes positive predictions more conservative.

This is a decision-policy question layered on top of the fitted model—not retraining the model itself.

### Pipeline decomposition

The exercise separated `train_model`, `predict_model`, `evaluate_model`, and the orchestration function. This mirrors software-engineering decomposition: fit, inference and evaluation have distinct responsibilities.

## Chat-history context

Thresholding from model probabilities later became an important bridge into neural-network classification: Lesson 30/31 repeats the conceptual sequence as logit -> sigmoid -> probability -> threshold -> class. Lesson 22 is therefore the earlier sklearn version of the same decision boundary idea.

## Cold-retrieval question bank

1. What shape might `predict_proba` return for 10 binary examples?
2. Which column do we use for class-1 probability in this lesson?
3. Convert probabilities `[0.1, 0.49, 0.5, 0.8]` to predictions at threshold 0.5.
4. What changes if the threshold becomes 0.3?
5. Does changing the prediction threshold retrain logistic regression?
6. Why might a fraud detector choose a lower threshold than another application?
7. What is the likely precision/recall trade-off when lowering the threshold?
8. Reconstruct the full classification pipeline in order.
9. Why is returning `actual` alongside `predictions` useful for later analysis?

## Retrieval blueprint

1. pipeline order;
2. `predict_proba` shape/meaning;
3. threshold several concrete probabilities;
4. reason about precision/recall direction;
5. connect threshold choice to asymmetric costs.

## Mastery signal

The learner can distinguish fitted model probabilities from final class decisions, explain threshold trade-offs, and reconstruct a clean train/predict/evaluate sklearn pipeline.
