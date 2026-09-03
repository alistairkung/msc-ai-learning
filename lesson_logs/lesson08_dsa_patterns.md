# Lesson 08 — DSA Patterns: Hash Lookup and Two Pointers

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This lesson marked the shift from “learn Python syntax” to “use Python to express algorithmic patterns.” It reused sets/dictionaries from Lessons 02–03 and introduced two-pointer reasoning. This was the beginning of the DSA track that later connected naturally into graph search.

## What was implemented

Source: `foundations/dsa/lesson08_dsa_patterns.py` + `foundations/dsa/test_lesson08_dsa_patterns.py`.

### Hash/set lookup patterns

`contains_duplicate(numbers)`:
- maintain `seen = set()`;
- return when a repeated value is encountered.

`first_duplicate(numbers)`:
- same pattern, but return the first value whose second occurrence is reached.

`two_sum(numbers, target)`:
- store previously seen number -> index;
- for each number calculate `lookup = target - number`;
- if complement already exists, return its index and current index.

`are_anagrams(first, second)`:
- count characters with dictionaries/defaultdicts;
- compare frequency maps.

### Two-pointer patterns

`is_palindrome(text)`:
- normalise input;
- compare left/right characters while moving inward.

`two_sum_sorted(numbers, target)`:
- sorted input lets us move `left` or `right` based on whether the current sum is too small/large.

`reverse_list(items)`:
- swap outside elements and move pointers inward.

## Core concepts

### Trading memory for time

A set/dictionary lets us remember what we have already seen so we avoid repeated full-list scans. The important insight is not “memorise two-sum”; it is:

> When a problem repeatedly asks “have I seen X?” or “where did I see X?”, consider a hash-based structure.

### Complement reasoning

For two-sum:

```text
current + complement = target
complement = target - current
```

Store past values so the complement can be checked immediately.

### Two pointers

When useful structure exists—especially sorted data or symmetric comparisons—two indices can often replace nested loops.

## Chat-history context

The recoverable history explicitly records `contains duplicate`, `first duplicate`, two-sum O(n), `enumerate`, two-pointer palindrome and anagrams via `defaultdict`. It also records a preference for hints rather than complete solutions. This lesson is therefore suitable for retrieval by asking “what pattern do you see?” before asking for code.

No reliable transcript was recovered for specific mistakes made during this lesson, so personal weak points are not invented.

## Cold-retrieval question bank

### Pattern recognition
1. You need to know whether any value appears twice. What structure would you reach for and why?
2. Why is repeatedly doing `x in some_list` inside a loop potentially worse than a `seen` set?
3. For two-sum, if the current number is 7 and target is 12, what value are you looking for?
4. Why do we check for the complement **before** storing the current number in the standard two-sum loop? Consider `[3,3]`, target 6.
5. What extra information must the hash map store if the answer requires indices rather than just True/False?

### Two pointers
6. Why does the left/right pointer approach work particularly well for sorted two-sum?
7. If the current sorted-pair sum is greater than target, which pointer should move and why?
8. Trace palindrome pointers for `"racecar"`.
9. Reverse `[1,2,3,4,5]` in place using two pointers. Which element never needs swapping?
10. What is the common structural idea linking palindrome checking, sorted two-sum and in-place reversal?

### Complexity
11. Compare a nested-loop two-sum with the hash-map solution at a high level.
12. What additional space does the `seen` approach use?
13. When can sorted two-sum use O(1) auxiliary space?

## Retrieval blueprint

For 10–15 minutes:
1. contains-duplicate from scratch;
2. two-sum complement reasoning;
3. ask for time/space trade-off;
4. sorted two-sum pointer movement;
5. palindrome or reverse-list trace;
6. ask learner to name the patterns rather than just solve examples.

## Mastery signal

Lesson 08 is retained when the learner can recognise “seen/complement” and two-pointer problem shapes from an unfamiliar prompt, derive the movement/lookup logic, and give the rough complexity reason for preferring the pattern over a nested scan.

## Longer-term dependency

This lesson should remain in periodic retrieval rather than being treated as a completed one-off. The set/dictionary “seen” idea later reappears in BFS/DFS, while structured frontier movement becomes part of broader algorithmic reasoning.
