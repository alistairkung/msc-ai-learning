# Lesson 18 — Pandas Fundamentals

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

After a long NumPy/ML block, Lesson 18 introduced pandas as the table-oriented layer for real datasets. The lesson was broad: selection, filtering, `.loc`/`.iloc`, derived columns, missing data, sorting, groupby/aggregation and joins.

Source: `foundations/pandas/lesson18_pandas_basics.py` + `foundations/pandas/test_lesson18_pandas_basics.py`.

## What was implemented

### DataFrame creation and selection
- construct a DataFrame from a dictionary of columns;
- select one column -> `Series`;
- select multiple columns -> `DataFrame`.

### Filtering
- numeric threshold masks;
- equality masks;
- combine conditions with `&` and `|`;
- `.loc[mask, columns]` for row + column selection.

### Positional indexing
- `.iloc[0:2]`;
- `.iloc[0:2, 0:2]`.

### Derived columns
- copy DataFrame first;
- add boolean `passed` column;
- add numeric `weighted_score = grade * attendance`.

### Sorting
- one column descending;
- multiple columns with separate ascending directions.

### Missing values
- `dropna(subset=[...])`;
- compute mean while ignoring NaN;
- `fillna(mean)`;
- preserve the original DataFrame by copying.

### Groupby / aggregation
- mean/max by course;
- `.agg(["mean", "max", "min"])`;
- `.reset_index()` to return grouping key to a normal column.

### Merging
- default inner merge on `course`;
- left merge to keep all student rows even when no matching teacher exists.

## Core concepts

### Series vs DataFrame

```python
students["grade"]
```

returns a `Series`.

```python
students[["name", "grade"]]
```

returns a `DataFrame`.

The doubled brackets are not cosmetic: they pass a list of columns.

### Boolean filtering mirrors NumPy

Pandas masks reuse the same vectorised mental model developed in NumPy:

```python
(students["grade"] >= 70) & (students["attendance"] >= 0.85)
```

### `.loc` vs `.iloc`

- `.loc` is label/condition-oriented;
- `.iloc` is integer-position-oriented.

### Copy vs mutation

Several helpers intentionally call `students.copy()` before adding/filling columns. The tests explicitly verify the original DataFrame remains unchanged.

### Groupby changes the question

Instead of asking for one overall statistic, `groupby("course")` partitions rows by course and applies an aggregation within each group.

### Merge semantics

Default `merge(..., on="course")` is an inner join: unmatched rows disappear. `how="left"` keeps every left-side student and fills missing teacher information with NaN when no match exists.

## Chat-history context

The durable learning record confirms pandas selection/filtering, `loc`/`iloc`, derived columns, missing data, sorting, `groupby`/aggregation and merges were all part of Lessons 18–20. This was intended as practical data-tool fluency rather than deep pandas specialisation.

Given the user's SQL/backend background, future retrieval can use relational analogies for groupby/join when helpful, but the source lesson itself is pandas code and should remain the factual anchor.

## Cold-retrieval question bank

### Selection / filtering
1. What is the return-type difference between `df["grade"]` and `df[["grade"]]`?
2. Filter rows where grade >= 80.
3. Filter grade >= 70 **and** attendance >= 0.9. Which operator combines masks?
4. Use `.loc` to return only `name` and `grade` for matching rows.
5. Contrast `.loc` and `.iloc`.

### Derived columns / mutation
6. Add a `passed` boolean column without mutating the original DataFrame.
7. Why might copying be preferable in these small pure helper functions?
8. Add a vectorised `weighted_score` from two existing columns.

### Missing data
9. What does pandas `mean()` normally do with NaN values?
10. Drop only rows whose `grade` is missing.
11. Fill missing grades with the column mean while preserving the input.

### Groupby / merge
12. Calculate mean grade by course.
13. What shape/type difference does `.reset_index()` create after a groupby aggregation?
14. Explain inner merge vs left merge using the Robotics student example.
15. If a left-side row has no match, what value appears in the new right-side columns?

## Retrieval blueprint

For 12–15 minutes:
1. Series vs DataFrame selection;
2. combined mask;
3. `.loc` vs `.iloc`;
4. derived column with no input mutation;
5. missing-value fill;
6. groupby aggregate;
7. inner vs left merge.

## Mastery signal

The learner can inspect/filter/transform a small DataFrame, reason about return types, handle missing values without accidental mutation, summarise groups, and choose inner vs left merge based on which rows must survive.
