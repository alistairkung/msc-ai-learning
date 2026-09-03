# Lesson 06 — `key=` Functions and Lambdas

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

This lesson made Python's `key=` pattern explicit so sorting/min/max over structured data could become idiomatic rather than manual. It also introduced small lambdas as throwaway selectors, not as a goal in themselves.

## What was implemented

Source: `foundations/python/lesson06_key_functions.py` + `foundations/python/test_lesson06_key_functions.py`.

Exercises included:
- `max(words, key=len)` / `min(words, key=len)`;
- `sorted(words, key=len)`;
- sorting by last character with `lambda w: w[-1]`;
- max/min over `grades.items()` using the value part of each tuple;
- sorting lists of dictionaries by a field;
- choosing the record with the longest name;
- choosing the oldest person;
- sorting people by age.

## Core concepts

`key=` does **not** transform the returned object. It tells Python what value to use when comparing objects.

Example:

```python
max(grades.items(), key=lambda item: item[1])
```

Python compares each pair by `item[1]` but returns the original `(key, value)` tuple.

Use a named function or built-in like `len` when possible; use a short lambda when the comparison rule is local and simple.

## Chat-history context

Recoverable history explicitly mentions sorting with `key` lambdas and `longest_name` as part of the Python preparation. This was one of the idioms intended to reduce verbose boilerplate compared with manually tracking maxima/sort keys.

## Cold-retrieval question bank

1. What does `key=len` mean in `max(words, key=len)`?
2. Does `sorted(students, key=lambda s: s["age"])` return ages or student records?
3. Given `{name: grade}`, why do we use `.items()` if we want both the winning name and grade?
4. Write a key function that sorts strings by their last character.
5. Return the dictionary record with the longest `"name"` field.
6. When could `key=len` replace a lambda?
7. Explain the difference between the object being compared and the key used to compare it.
8. What happens if multiple items have the same maximum key value? What should you expect about which item is returned?

## Retrieval blueprint

1. built-in `key=len`;
2. tuple `.items()` + lambda;
3. dictionary-record selector;
4. sort by nested field;
5. explain what `key=` actually changes.

## Mastery signal

The learner can reach for `min`, `max`, and `sorted` with `key=` rather than writing unnecessary tracking loops, and can explain why the original object—not the key—is returned.
