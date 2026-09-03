# Lesson 03 — Python Sets

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Sets introduced uniqueness and fast membership checks, then connected naturally to later DSA patterns such as duplicate detection and “seen” collections.

## What was implemented

Source: `foundations/python/lesson03_sets.py` + `foundations/python/test_lesson03_sets.py`.

Exercises covered:
- set creation and `.add()`;
- duplicate insertion having no effect;
- membership with `in`;
- converting a list to a set to deduplicate;
- intersection with `&`;
- set difference with `-`;
- duplicate detection by comparing `len(set(items))` with `len(items)`;
- `.discard()` for safe removal;
- union with `|`;
- counting unique values;
- subset checks;
- set comprehension / turning membership into a lookup dictionary.

## Core concepts

- Sets contain unique values and do not represent sequence order as a list does.
- Membership is a primary use case and becomes algorithmically important later.
- Set algebra directly expresses overlap and difference between collections.
- `.discard(x)` differs from `.remove(x)` because it does not fail if `x` is absent.
- Converting to a set is often the simplest way to ask a uniqueness question.

## Chat-history context

The early Python progression explicitly included set operations and then reused sets in DSA. This is an important curriculum dependency: Lesson 08’s `contains_duplicate` and `first_duplicate` are not isolated tricks; they build directly on the membership/uniqueness ideas established here.

## Cold-retrieval question bank

1. Why does adding the same value to a set twice not increase its size?
2. Given two sets, what do `a & b`, `a | b`, and `a - b` mean?
3. How could you detect whether a list contains duplicates using a set in one line?
4. Why might `.discard()` be preferable to `.remove()` in a “remove if present” helper?
5. If `first.issubset(second)` is true, what relationship holds between the values?
6. Given a list with repeated city names, return only unique names.
7. Which data structure would you prefer for repeated membership checks: list or set, and why at an algorithmic level?
8. How does this lesson prepare you for a `seen` set in graph traversal or duplicate detection?

## Retrieval blueprint

For a short review:
1. union/intersection/difference;
2. membership and uniqueness;
3. duplicate detection;
4. safe removal;
5. explain why sets become useful in DSA.

## Mastery signal

The learner can recognise when uniqueness/membership is the problem, choose a set naturally, and understand that this choice later changes algorithmic complexity compared with repeatedly scanning a list.
