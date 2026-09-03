# Lesson 20 — NumPy + Pandas Refresher

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 20 was a mixed refresher spanning the two practical data layers learned so far:

```text
NumPy / manual ML
+
pandas data wrangling
```

The purpose was retrieval and integration before moving into sklearn/classical ML lessons.

Source: `foundations/pandas/lesson20_np_pandas_refresher.py` + `foundations/pandas/test_lesson20_np_pandas_refresher.py`.

## What was retrieved

### NumPy / ML
- feature-wise standardisation;
- multiclass linear scores + `argmax(axis=1)`;
- linear-regression prediction + MSE loss.

### pandas
- threshold filtering;
- derived columns on a copied DataFrame;
- filling missing grades with the mean;
- grouped mean/max summary + renamed columns.

## Core concepts reinforced

### Numerical pipeline continuity

The NumPy section keeps the same mental model established earlier:

```text
(samples, features)
-> feature-wise statistics
-> matrix multiplication
-> score/prediction arrays
-> scalar evaluation metric
```

### Pandas as table-level transformation

The pandas half focuses on row filtering, column derivation, missing-data handling and grouped summaries. The contrast is useful:

- NumPy is being used for dense numerical array mechanics;
- pandas is being used for labelled tabular manipulation.

The source lesson does not claim one library replaces the other; it practises switching between them.

### Copy-before-transform contract

`add_weighted_score` and `fill_missing_grades` copy their inputs before mutation, and the tests verify the original DataFrame remains unchanged.

### Groupby with NaN

The test confirms that for NLP, where Bob's grade is NaN and Dan's is 64:

```text
mean_grade = 64
highest_grade = 64
```

because the default pandas aggregations here ignore the NaN.

## Chat-history context

The durable roadmap explicitly records Lessons 18–20 as pandas selection/filtering, missing data, sorting, `groupby`/aggregation, merges and refresher work, while Lessons 10–17 were the NumPy/shape/linear-model block. Lesson 20 is therefore a genuine transition checkpoint between those blocks and the sklearn lessons that follow.

Future cold retrieval should preserve that mixed style rather than reviewing NumPy and pandas in completely separate sessions every time.

## Cold-retrieval question bank

### NumPy / ML
1. Standardise a `(n,d)` feature matrix: which axis supplies feature means/stds?
2. What post-standardisation statistics should each feature have in this standalone exercise?
3. If `X=(25,4)` and `W=(4,3)`, trace score and prediction shapes.
4. Which axis does `argmax` use to produce one class per sample?
5. Derive MSE from `X @ w + b` predictions.

### pandas
6. Filter only students whose attendance is at least 0.9.
7. Add `weighted_score = grade * attendance` without modifying the input DataFrame.
8. Fill NaN grades using the grade-column mean.
9. Why does the missing grade not contribute to pandas mean in this source exercise?
10. Build grouped mean/max grade statistics and rename the columns.

### Integration
11. When would you naturally choose pandas over NumPy for a task?
12. When would you naturally drop down to NumPy-style array operations?
13. Explain how a DataFrame feature table might eventually become the numerical matrix used by a model.

## Retrieval blueprint

For 12–15 minutes, alternate libraries:
1. NumPy standardisation;
2. pandas filter;
3. matrix/classification shape;
4. pandas missing-value transform;
5. MSE;
6. groupby summary;
7. ask the learner why each library fits each task.

## Mastery signal

The learner can switch comfortably between labelled tabular operations and dense numerical-array reasoning, while retaining standardisation, matrix-shape, classification and MSE concepts from the earlier NumPy block.

## Dependency forward

This checkpoint leads naturally into the next curriculum block:

```text
NumPy + pandas foundations
-> sklearn train/test workflows
-> logistic regression / metrics
-> linear regression / metrics
-> later PyTorch real-data pipelines
```
