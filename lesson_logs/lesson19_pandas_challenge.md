# Lesson 19 — Pandas Challenge: Cleaning, Filtering and Aggregation

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Lesson 19 consolidated Lesson 18 into three slightly larger data-manipulation tasks. Instead of one pandas operation per helper, each function combines several steps into a small workflow.

Source: `exercises/lesson19_pandas_challenge.py` + `tests/test_lesson19_pandas_challenge.py`.

## What was implemented

### `clean_students`
- copy the DataFrame;
- calculate mean grade;
- fill missing grades;
- add `weighted_score = grade * attendance`;
- return cleaned copy without mutating original.

### `top_students`
- create a grade mask;
- create an attendance mask;
- combine with `&`;
- filter;
- sort selected rows by grade descending.

### `course_performance`
- group by course;
- aggregate mean and max grade;
- reset index;
- rename output columns to domain-friendly names.

## Core concepts

### Composing pandas operations

A realistic data-cleaning function is often a chain of simple vectorised steps rather than a single clever expression. The lesson rewards readable staging:

```text
copy
-> fill missing
-> derive feature
-> return
```

### Missing-value semantics matter

The test for `course_performance` deliberately leaves one NLP grade as NaN and confirms pandas mean ignores it. That means:

```text
NLP mean = (64 + 88) / 2
```

not division by all three NLP rows.

### Filtering then sorting

`top_students` demonstrates a common pattern:

```text
build masks
-> combine masks
-> filter rows
-> sort result
```

The constraints and ranking step are separate concerns.

### Rename after aggregation

Raw aggregation names such as `mean` and `max` are technically correct but less expressive. Renaming to `mean_grade` / `highest_grade` makes the resulting table self-describing.

## Chat-history context

The learning history describes Lessons 18–20 as pandas selection/filtering, missing data, sorting, groupby/aggregation, merges and challenge/refresher work. Lesson 19 is the challenge layer: future retrieval should therefore ask for small multi-step transformations rather than isolated syntax trivia.

## Cold-retrieval question bank

1. Why does `clean_students` copy before filling/adding columns?
2. If one grade is NaN, how does pandas mean treat it by default in this source lesson?
3. Design the steps for “fill missing grades, then add grade × attendance.”
4. Build two boolean masks and combine them to find grade >= 80 and attendance >= 0.9.
5. Why filter before sorting in `top_students`?
6. What does `.sort_values("grade", ascending=False)` mean?
7. Build a course summary with mean and maximum grade.
8. Why call `.reset_index()` after the groupby aggregation here?
9. Rename `mean` and `max` columns to clearer domain names.
10. Given the source data, explain why Bob's missing grade affects cleaning and course-summary workflows differently.

## Retrieval blueprint

For a 10–12 minute review:
1. reconstruct cleaning pipeline from intent;
2. combined mask + sort;
3. groupby + agg + reset_index + rename;
4. ask one question about NaN aggregation semantics;
5. explain input-mutation contract.

## Mastery signal

The learner can combine pandas primitives into readable small workflows, reason correctly about missing-value behaviour, and preserve source DataFrames when a helper is intended to return a transformed copy.
