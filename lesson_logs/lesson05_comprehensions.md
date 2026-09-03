# Lesson 05 — Comprehensions

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

This lesson shifted from explicit loops toward concise Python collection transformations. The goal was to recognise when a loop is simply mapping/filtering into a new list, dict or set, while keeping readability as the priority.

## What was implemented

Source: `foundations/python/lesson05_comprehensions.py` + `foundations/python/test_lesson05_comprehensions.py`.

Exercises covered:
- list mapping: square each number;
- list filtering: evens and words above a length threshold;
- dict comprehension: word -> length;
- set comprehension: lowercase + deduplicate;
- extracting fields from lists of dictionaries;
- filtering records by grade;
- building lookup dicts from records;
- producing formatted summaries;
- grouping by course, where a normal loop + `defaultdict(list)` was kept because it was clearer than forcing a comprehension.

## Core concepts

Canonical shapes:

```python
[transform(x) for x in items]
[x for x in items if condition(x)]
{key(x): value(x) for x in items}
{transform(x) for x in items}
```

- A comprehension is best when the transformation is conceptually simple.
- Not every loop should become a comprehension.
- Dict/set comprehensions are especially useful for creating indexes and normalised unique collections.
- Filtering and mapping can be combined in one readable expression.

## Chat-history context

The broader early-learning record explicitly says you valued Pythonic idioms but accepted clarity trade-offs. That matters here: the lesson was not “make everything one line.” The checked-in `names_by_course` still uses an ordinary loop with `defaultdict(list)`, which is a good example of keeping the clearer structure.

## Cold-retrieval question bank

1. Convert a loop that squares numbers into a list comprehension.
2. Filter only passing grades with a comprehension.
3. Build `{name: grade}` from a list of student dicts.
4. Build a set of lowercase unique words from mixed-case input.
5. Explain the order of `expression`, `for`, and `if` in a comprehension.
6. When is a normal loop preferable to a comprehension?
7. Given student records, return formatted strings such as `"Alice studies AI"`.
8. Why is grouping multiple values under one key often clearer with `defaultdict(list)` than a comprehension?

## Retrieval blueprint

1. one mapping list comprehension;
2. one filtering comprehension;
3. one dict comprehension;
4. one set comprehension;
5. choose between comprehension and explicit loop for a grouping task.

## Mastery signal

The learner can read/write list/dict/set comprehensions without mentally translating every line into a long loop, while still choosing an explicit loop when stateful grouping or readability makes it better.
