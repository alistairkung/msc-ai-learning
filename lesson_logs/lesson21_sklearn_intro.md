# Lesson 21 — sklearn Classification Intro

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This lesson was the first move from hand-built NumPy classification mechanics into a standard ML library workflow. The point was not to hide the model behind sklearn, but to connect familiar concepts—features, labels, train/test separation, predictions and accuracy—to a real estimator API.

## What was implemented

Source: `machine_learning/classification/logistic_regression/lesson21_sklearn_intro.py` + `machine_learning/classification/logistic_regression/test_lesson21_sklearn_intro.py`.

The lesson used `LogisticRegression` and practised:
- selecting feature columns and a binary target from a DataFrame;
- `train_test_split` with `stratify=y`;
- `.fit(X_train, y_train)`;
- `.predict(X_test)`;
- manual accuracy via `(predictions == y_test).mean()`;
- sklearn `accuracy_score`;
- confusion matrix;
- precision and recall.

The synthetic dataset had 3 features (`age`, `income`, `attendance`) and a binary `passed` target.

## Core concepts

### Fit vs predict

```text
fit     -> learn parameters from training examples
predict -> apply the learned model to new X values
```

A fitted sklearn model exposes learned attributes such as coefficients/intercepts, but the lesson focused primarily on using the training/evaluation API correctly.

### Train/test split

The test set is separated before fitting so evaluation uses examples not supplied to `.fit()`.

`stratify=y` helps maintain class proportions in the split, especially useful for classification.

### Confusion matrix

For binary classification, the matrix organises correct and incorrect predictions by actual/predicted class. Exact position semantics should be recalled deliberately rather than inferred vaguely from the 2x2 shape.

### Accuracy, precision, recall

- accuracy: fraction of all predictions correct;
- precision: among predicted positives, fraction actually positive;
- recall: among actual positives, fraction successfully identified.

These metrics answer different questions and can diverge sharply on imbalanced or asymmetric-error problems.

## Chat-history context

The durable learning record identifies Lessons 21–22 as the sklearn logistic-regression/classification introduction and specifically records train/test splitting, stratification, thresholding, confusion matrix, accuracy, precision and recall as practised. The later MSc-prep plan therefore treats logistic regression as a consolidation topic rather than first exposure.

## Cold-retrieval question bank

1. What does `.fit()` do that `.predict()` does not?
2. Why should test examples not be supplied to model fitting?
3. Why might `stratify=y` matter in a classification split?
4. Given TP=30, FP=10, FN=5, TN=55, calculate accuracy, precision and recall.
5. If false negatives are especially costly, which of precision/recall would you watch closely?
6. Explain the four cells of a binary confusion matrix.
7. Why can accuracy be misleading when one class is rare?
8. What are `X` and `y` semantically in the student example?

## Retrieval blueprint

For a 10-minute review:
1. reconstruct split -> fit -> predict -> evaluate;
2. explain stratification;
3. manually compute one confusion-matrix metric set;
4. ask which metric matters under different business costs;
5. distinguish model training from evaluation.

## Mastery signal

The learner can build a basic sklearn classification workflow, explain why the split precedes fitting, interpret a confusion matrix, and choose between accuracy/precision/recall based on the error being measured.
