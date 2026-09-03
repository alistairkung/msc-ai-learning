# Lesson 02 — Python Dictionaries

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

This lesson moved from ordered sequences to key/value lookup, mutation, aggregation and small data transformations. That was important both for idiomatic Python and for later DSA work, where hash-map lookup becomes a core performance pattern.

## What was implemented

Source: `foundations/python/lesson02_dictionaries.py` + `foundations/python/test_lesson02_dictionaries.py`.

Exercises covered:
- constructing dictionaries;
- adding/replacing keys;
- `.get()` for optional lookup;
- nested dictionaries and `.values()`;
- `.pop(key, None)` for safe removal;
- word-frequency counting with `.get(word, 0) + 1`;
- inventory accumulation;
- averages over `.values()`;
- `max(..., key=...)` over `.items()`;
- dictionary merge with `defaults | overrides`;
- dictionary inversion;
- grouping records with `setdefault(course, []).append(name)`.

## Core concepts

- Dictionaries map unique keys to values and are mutable.
- `d[key]` assumes the key exists; `d.get(key)` can safely return `None`/a default.
- `.items()` yields `(key, value)` pairs; `.values()` yields values.
- Frequency counting is a bridge from basic Python into hash-map algorithms.
- `setdefault` is one way to initialise grouped collections lazily.
- `defaults | overrides` creates a new merged dict, with right-hand values winning on duplicate keys.
- Mutation vs non-mutation should be explicit in tests.

## Chat-history context

Recoverable history specifically records `count_words` via `.get`, grouping with `setdefault`, dictionary inversion, and merge via `|` as part of the early Python sequence. The teaching preference was to learn the Pythonic idiom while still discussing clarity trade-offs rather than treating shorter syntax as automatically better.

## Current repo anomaly

The current `invert_dictionary` implementation does **not** match its tests: the tests require successful inversion and a `ValueError` for duplicate values, while the checked-in implementation iterates incorrectly and does not implement the duplicate-value guard. Treat this as a source-state anomaly to fix separately, not as evidence that the original lesson necessarily ended in that state.

## Cold-retrieval question bank

1. What is the difference between `student["grade"]` and `student.get("grade")` when the key is missing?
2. Count word frequencies in one pass without `Counter`.
3. Why does `counts.get(word, 0) + 1` work for both new and existing words?
4. Given a dict of grades, return `(student, grade)` for the highest value using `max(..., key=...)`.
5. What does `{**a, **b}` or `a | b` do when the same key occurs in both? Which wins?
6. Group a list of students by course using `setdefault`.
7. What is the difference between `.keys()`, `.values()`, and `.items()`?
8. Why might inverting a dictionary be unsafe when original values are duplicated?
9. What contract does `.pop(key, None)` give you for missing keys?
10. Which operations here mutate the original dict and which return new dictionaries?

## Retrieval blueprint

For a 10-minute review:
1. safe lookup with `.get`;
2. one-pass frequency counter;
3. `items()` + `key=` retrieval;
4. merge semantics;
5. grouping with `setdefault`;
6. discuss duplicate-value problem when inverting.

## Mastery signal

The learner can choose direct indexing vs `.get`, use dicts naturally for counting/grouping/lookup, explain mutation semantics, and recognise dictionaries as the basis for constant-time average-case lookup patterns used later in DSA.
