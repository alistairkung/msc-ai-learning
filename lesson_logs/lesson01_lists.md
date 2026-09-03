# Lesson 01 — Python Lists

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

This was part of the initial Python conversion phase: the goal was not to teach programming from scratch, but to make Python syntax and idioms low-friction for an experienced Ruby/Java engineer before NumPy/ML. The early workflow deliberately used small functions + pytest contracts so there was always a concrete definition of “working”.

## What was implemented

Source: `foundations/python/lesson01_lists.py` + `foundations/python/test_lesson01_lists.py`.

Functions practised:
- create a list of cities;
- mutate a list with `append`;
- retrieve the final element with negative indexing;
- membership with `in`;
- length with `len`;
- loop over values, build a transformed list, and sort it.

Representative ideas:

```python
cities.append(city)
cities[-1]
city in cities
len(cities)
sorted(cities)
```

The final exercise uppercased city names in a loop and then sorted the transformed values.

## Core concepts

- Python lists are ordered, mutable sequences.
- `append` mutates the existing list and returns `None`.
- Negative indexes count from the end (`-1` = final element).
- Membership is expressed directly with `in`.
- Iterating over values is often clearer than index-based loops.
- A function can either mutate an input or return a new value; tests should make that contract explicit.

## Chat-history context

The original prep plan was a tailored “conversion course” rather than generic beginner Python: explanations were intended to connect back to Ruby/Java, use TDD, and move quickly toward NumPy/AI work. No reliable transcript-level record of specific mistakes from this lesson was recovered, so none are invented here.

## Cold-retrieval question bank

Ask one at a time and change the data rather than reusing the exact tests.

1. What is the difference between `items.append(x)` and `items + [x]` in terms of mutation?
2. Given `cities = ["Tokyo", "Seoul", "Taipei"]`, how do you retrieve the last element?
3. What does `"Seoul" in cities` return?
4. If a function calls `cities.append("Osaka")` and has no `return`, what does the function return?
5. Write a function that returns the number of cities in a list.
6. Given mixed-case city names, return a new list of uppercase names sorted alphabetically.
7. Does `sorted(cities)` mutate `cities`? Contrast it with `cities.sort()`.
8. Why might a pytest check both the mutated list and a function’s return value?

## Retrieval blueprint

For a 5–8 minute review:
1. negative indexing;
2. mutation vs return value;
3. membership + length;
4. small transform-and-sort function;
5. explain the resulting test contract.

## Mastery signal

Lesson 01 is retained if the learner can use list indexing/membership/mutation without syntax hesitation and can explain whether a small function mutates its input, returns a new object, or both.
