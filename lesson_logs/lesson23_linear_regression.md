# Lesson 23 — sklearn Linear Regression

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This lesson transferred the standard sklearn workflow from classification to regression. It connected earlier hand-built linear prediction/MSE work to `LinearRegression`, then introduced the common regression metrics MAE, MSE and R².

## What was implemented

Source: `machine_learning/regression/lesson23_linear_regression.py` + `machine_learning/regression/test_lesson23_linear_regression.py`.

Synthetic housing data used:
- features: `size`, `bedrooms`, `age`;
- target: `price`.

Pipeline:

```text
DataFrame
 -> X/y
 -> 80/20 train/test split
 -> LinearRegression.fit
 -> model.predict
 -> MAE / MSE / R²
```

The function returned the fitted model, predictions, actual values and all three metrics. Tests checked prediction/test lengths, valid metric ranges and the presence of learned `coef_` / `intercept_`.

## Core concepts

### Regression vs classification

Regression predicts a continuous value rather than a discrete class. The model interface can look similar (`fit`, `predict`), but the target type and evaluation metrics differ.

### MAE

Mean absolute error averages `|prediction - actual|`.

It is directly interpretable in the target's units and treats each unit of error linearly.

### MSE

Mean squared error averages squared residuals.

Large errors contribute disproportionately because of squaring. This links directly back to the manual MSE work in Lesson 12 and later PyTorch `MSELoss`.

### R²

R² compares the model's squared-error performance to a baseline that predicts the target mean. Rough intuition:
- 1 = perfect fit;
- 0 = no better than mean prediction under the usual definition;
- negative values are possible if the model performs worse than that baseline.

So the repo test correctly checks `r2 <= 1`, not `0 <= r2 <= 1`.

## Chat-history context

The durable curriculum records Lesson 23 as the practical sklearn linear-regression introduction and treats linear regression as already encountered before the MSc. Later housing-price preparation is meant to deepen this into neural-network regression rather than restart from zero.

## Cold-retrieval question bank

1. What makes a problem regression rather than classification?
2. Given residuals `[2, -4, 1]`, calculate MAE and MSE.
3. Why does MSE penalise a very large error more heavily than MAE?
4. Can R² be negative? What would that mean intuitively?
5. What do `coef_` and `intercept_` represent in a fitted linear model?
6. Reconstruct the split -> fit -> predict -> evaluate workflow.
7. Which metric would you choose if you want errors reported in the same units as house price?
8. How does this lesson connect to the hand-built `X @ W + b` model from Lesson 12?

## Retrieval blueprint

1. classify task as regression;
2. manually calculate MAE/MSE;
3. explain R² at an introductory level;
4. map sklearn model back to weights + bias;
5. rebuild the pipeline order.

## Mastery signal

The learner can distinguish regression evaluation from classification evaluation, calculate/interpret MAE and MSE, give a sensible explanation of R², and connect sklearn `LinearRegression` to the earlier linear-model equation.
