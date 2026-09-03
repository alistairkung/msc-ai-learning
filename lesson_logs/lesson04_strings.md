# Lesson 04 — Python Strings

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

Strings were used to practise Python slicing, built-in methods, normalisation, and small transformations. Several exercises deliberately combined earlier ideas—loops, collections, `max(..., key=...)`, and frequency counting—into text-processing tasks.

## What was implemented

Source: `foundations/python/lesson04_strings.py` + `foundations/python/test_lesson04_strings.py`.

Exercises included:
- first/last character indexing;
- reverse slicing `[::-1]`;
- `split`, `join`, `title`, `replace`, `startswith`;
- f-strings;
- whitespace normalisation using `" ".join(text.split())`;
- reversing word order;
- palindrome normalisation across case/spaces;
- word count robust to extra whitespace;
- longest word with `max(..., key=...)`;
- acronym generation;
- email-domain extraction;
- prefix removal;
- case-insensitive word frequencies using `defaultdict(int)`.

## Core concepts

- Strings are sequences, so indexing/slicing transfer from lists.
- `split()` with no explicit separator handles arbitrary whitespace differently from `split(" ")`.
- Normalisation before comparison is a recurring data-processing pattern.
- String methods generally return new strings rather than mutating the original.
- `join` is the idiomatic way to assemble strings from components.
- Text tasks often combine sequence processing with dictionaries/defaultdicts.

## Chat-history context

Recoverable learning history specifically mentions palindrome, acronym and `defaultdict(list/int)`-style work during the early Python phase. The aim was practical Python fluency, not exhaustive knowledge of every string method.

## Cold-retrieval question bank

1. What does `text[::-1]` do?
2. Why does `text.split()` handle repeated spaces better than `text.split(" ")` for word counting?
3. Normalise `"  hello   world "` to `"hello world"` using `split` + `join`.
4. How would you make palindrome checking ignore case and spaces?
5. Explain the difference between reversing characters and reversing word order.
6. Build an acronym from a phrase with arbitrary extra whitespace.
7. Given an email address, extract everything after the first `@`.
8. Count words case-insensitively using a dictionary/defaultdict.
9. What does `max(words, key=len)` ask Python to maximise?
10. Do methods such as `.replace()` mutate the original string?

## Retrieval blueprint

1. slicing/indexing;
2. split/join and whitespace normalisation;
3. palindrome/acronym transformation;
4. one `key=` exercise;
5. one frequency-counting exercise.

## Mastery signal

The learner can manipulate text without falling back to verbose character-by-character code, recognises normalisation as a preprocessing step, and can combine strings with earlier collection patterns.
