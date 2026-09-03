# Lesson 09 — Sliding Window

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This lesson extended DSA pattern recognition beyond hash lookup/two pointers into **sliding windows**: maintain a contiguous region and update it incrementally instead of recomputing every candidate range from scratch.

It introduced both:
- **fixed-size windows**, where the width stays constant;
- **variable-size windows**, where the left edge moves to restore a constraint.

## What was implemented

Source: `foundations/dsa/lesson09_sliding_window.py` + `foundations/dsa/test_lesson09_sliding_window.py`.

### Fixed-size window

`max_sum_of_k(numbers, k)`:
1. compute the first window sum once;
2. move right one position at a time;
3. subtract the value leaving the window;
4. add the new value entering the window;
5. track the maximum.

Core update:

```python
window_sum = window_sum - numbers[index - k] + numbers[index]
```

`max_average_of_k` uses the same window-sum logic and divides the best sum by `k` at the end.

### Variable-size window

`longest_unique_substring(text)`:
- maintain a `seen` set for the current window;
- expand `right`;
- while the new character violates uniqueness, move `left` and remove outgoing characters;
- update the longest valid window length.

`longest_sum_at_most(numbers, limit)`:
- add each new right-side number to `window_sum`;
- while the sum is too large, subtract from the left and advance `left`;
- track the largest valid window length.

## Core concepts

### Fixed window invariant

At every iteration, the window contains exactly `k` contiguous items. Rather than summing those `k` items again, update from the previous answer in O(1).

### Variable window invariant

The window represents a **currently valid contiguous region**. Expand right; if the constraint breaks, shrink from the left until valid again.

### The key recognition question

> Is this asking about a contiguous subarray/substring, and can the answer for the next range be updated from the current range?

If yes, sliding window may be relevant.

## Chat-history context

The learning record confirms both fixed and variable sliding windows were completed, but explicitly marks this as “established once; not yet broad DSA fluency.” That means future review should focus on **recognising when to use the pattern**, not simply retyping these four functions.

No detailed transcript-level record of specific mistakes was recoverable, so none are asserted here.

## Cold-retrieval question bank

### Fixed window
1. Given `[2,1,5,1,3,2]` and `k=3`, what is the first window sum?
2. When the window moves one position right, which value leaves and which enters?
3. Why is `index - k` the outgoing element in the implementation?
4. Why can maximum average of a fixed-size window be solved by tracking maximum sum?
5. Compare recomputing every `k`-item sum with maintaining `window_sum`.

### Variable window
6. In longest-unique-substring, what condition makes the left pointer move?
7. Why is a `while` needed rather than a single `if` when restoring uniqueness?
8. For `"pwwkew"`, trace `left`, `right`, and the valid window after the second `w` arrives.
9. For a positive-number array with a sum limit, why can shrinking from the left restore validity?
10. What invariant should hold immediately before measuring `right - left + 1`?

### Pattern recognition
11. Is “maximum sum of any 5 consecutive days” a fixed or variable window?
12. Is “longest substring with no repeated characters” fixed or variable?
13. Is two-sum on an unsorted array naturally a sliding-window problem? Why not?
14. What word in a problem statement often hints that sliding window may apply? (`contiguous`, substring, subarray, consecutive, etc.)

## Retrieval blueprint

For 10–15 minutes:
1. derive fixed-window update from first principles;
2. trace one move by hand;
3. explain fixed vs variable window;
4. trace a duplicate-character shrink loop;
5. solve one new recognition question without code;
6. state rough time complexity.

## Complexity intuition

For the implemented forms, each element is generally added/visited and removed at most a small constant number of times, giving O(n)-style traversal rather than recomputing overlapping windows repeatedly.

## Mastery signal

The learner can identify contiguous-window structure, maintain the window invariant, explain why left/right move, and derive the update rule instead of memorising a template.

## Longer-term status

This should stay in periodic DSA retrieval. The lesson established the pattern once, but it was never intended to imply broad mastery of arbitrary sliding-window interview problems.
