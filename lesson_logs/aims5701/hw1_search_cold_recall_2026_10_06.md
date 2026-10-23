# AIMS5701 — HW1-targeted Search cold recall — 2026-10-06

## Session purpose

Run a bounded generic Search diagnostic before an independent AIMS5701 HW1 attempt. The HW1 problem sheet was deliberately **not** loaded into this tutoring context. Practice used fresh examples only; assignment-specific scaffolding is reserved for a separate transcript-recorded context if needed.

## State-space cardinality

The first example exposed a small counting slip: two independent binary switches were initially counted as two states rather than four joint configurations. The learner immediately repaired this to `2^2` and then independently solved a changed example with four binary switches and a second multi-factor state-counting problem.

Evidence boundary: treat this as repaired same-session evidence. The underlying multiplicative counting model appears intact; retain the reminder that **number of binary variables != number of joint configurations**.

## UCS / A* manual bookkeeping

UCS goal handling remained conceptually available. The learner correctly stated that discovering a goal is not sufficient because a cheaper route may still exist; safe termination occurs when the goal is popped from the frontier as the current minimum-cost item under the usual assumptions.

A* bookkeeping revealed two different issues that should not be conflated:

1. one genuine conceptual/bookkeeping slip used the parent's `f` as though it were accumulated `g`;
2. later errors were substantially contaminated by text-only graph presentation and the need to hold the remaining frontier in working memory.

After repair, the relevant invariant was understood:

```text
g(child) = g(parent) + edge cost
f(child) = g(child) + h(child)
```

For written questions, externalise the graph and frontier on paper. A search-tree sketch may help visual reasoning, but graph-search correctness still requires tracking best-known state cost / closed status so duplicate states and cheaper rediscoveries are handled correctly.

Do not promote manual A* execution to effortless independent fluency from this session.

## Admissibility vs consistency

The first changed example mixed the two tests. After correction, the distinction repaired cleanly:

```text
admissibility: h(n) <= h*(n)
consistency:   h(A) <= c(A,B) + h(B)
```

A later fresh example was classified independently as both admissible and consistent, including separate edge-by-edge consistency checks. This is useful same-session transfer evidence.

## Admissible but inconsistent A*

The learner's initial explanation incorrectly said inconsistency could make `g(n)` fall. This was corrected: actual path cost `g` still accumulates; the quantity that may decrease along an edge is `f=g+h` when the heuristic falls by more than the edge cost.

The practical graph-search consequence became clear: with an admissible but inconsistent heuristic, a node that was previously closed can later be reached with a cheaper `g`, so A* may need to reopen it rather than treating closed states as permanently final.

The derivation

```text
consistency
h(A) <= c(A,B) + h(B)

=> g(A)+h(A) <= g(A)+c(A,B)+h(B)
=> f(A) <= f(B)
```

was understood when shown. However, the learner explicitly reported that this proof had been studied extensively the previous week but was still unlikely to be cold-retrievable.

## Retrieval boundary

Strong enough to move on today:
- joint state-space counting after one repaired slip;
- UCS goal-discovered vs goal-popped distinction;
- admissibility vs consistency on changed data;
- conceptual consequence of admissible-but-inconsistent A* graph search.

Still fragile:
- manual A* bookkeeping when `g`, `h`, `f` and the frontier must all be tracked;
- cold reconstruction of consistency => nondecreasing `f`;
- therefore the exact proof-level justification for why inconsistency can require reopening.

## Next

1. Attempt HW1 independently.
2. If a real homework question exposes a block, use a separate transcript-recorded context with the HW1 uploaded and practise on structurally equivalent but concretely different examples rather than solving the assignment question directly.
3. On 7 Oct, spend only **5–10 minutes** cold-reconstructing consistency => nondecreasing `f` and the reopening consequence. Stop if it returns cleanly.
4. Preserve the remainder of the protected 7 Oct AIMS5701 blocks for HMM / particle-filtering JIT rather than turning Search into comprehensive revision.


## HW1-calibrated survey continuation

A second Search block on 6 Oct explicitly loaded the HW1 sheet only to calibrate concept coverage, reasoning pattern and difficulty. All tutoring exercises remained freshly generated analogues; no homework solution, intermediate homework step or disguised copy was produced. Because this block was directly assignment-related, the full user-visible transcript is preserved under `lesson_logs/aims5701/assignments/hw1_search/ai_transcripts/`.

### State formulation and cardinality

The strongest newly exposed gap was minimal-state formulation. The learner initially mixed dynamic state with fixed environment/problem data, and on changed examples occasionally omitted a dynamic Boolean flag that changed future legal transitions. After repeated fresh examples, the distinction became operational:

```text
candidate state variable
  -> can it change during one search run?
  -> if yes, can it change legal future actions / goal-relevant outcomes?
  -> if yes, include it in the state
fixed map / goal / problem data stay outside the state
path-cost bookkeeping is not automatically world state
```

By the final changed factory example, the learner independently selected all future-relevant dynamic variables, excluded fixed corridor/tool-station/goal information and counted the product correctly. A follow-up symbolic-range question also correctly used `Rmax + 1` values for an inclusive `0..Rmax` integer range. Treat this as repaired same-session evidence rather than delayed mastery.

### Admissibility from problem mechanics

A changed momentum-style example exposed an inequality-direction slip, but the learner correctly identified the central modelling issue: a heuristic measured in geometric distance is not automatically a lower bound when the objective is action count and one action may traverse multiple spatial units. After feedback, the learner restated that if `h(s)` can exceed the true remaining action cost `h*(s)`, the heuristic is not necessarily admissible.

This is conceptually sound after repair. Keep a light reminder to check both the admissibility inequality direction and whether heuristic units align with the cost model.

### BFS path reconstruction

The learner initially conflated expansion order with the returned solution path. Parent tracing repaired this immediately. On a second fresh BFS graph, FIFO order, duplicate suppression and the reconstructed path were conceptually correct; remaining mistakes were small table/notation slips. Keep the practical rule that expansion/frontier order and parent-chain reconstruction are separate bookkeeping tracks.

### A* trace

A fresh A* trace produced one arithmetic error in the initial `f=g+h` calculation, which changed the expansion order. Once corrected, the cheaper-path update and parent-chain logic were understood. This reinforces the earlier conclusion: A* mechanics are conceptually available, but manual `g/h/f` arithmetic and frontier bookkeeping are vulnerable under fatigue. Externalise the table on paper.

### Admissibility vs consistency

This area strengthened relative to the earlier generic recall. The learner cold-restated that consistency implies admissibility via the local edge condition / nondecreasing-`f` intuition, then independently gave the canonical distinction that an admissible heuristic can still violate `h(A) <= c(A,B)+h(B)` on an edge.

The formal repeated-edge proof of consistency => admissibility is not a major conceptual gap, but remains worth a brief cold reconstruction.

## Revised next retrieval targets

Treat 7 Oct as a short confirmation pass rather than another long Search lesson:

1. one cold UCS trace;
2. one clean A* trace with careful `g/h/f` arithmetic and parent updates;
3. one heuristic-design/admissibility question where cost units must be reasoned about;
4. one small admissible-but-inconsistent graph with closed-set tracing;
5. a brief cold reconstruction of consistency => admissibility / nondecreasing `f`.

Do not overdrill state formulation tomorrow unless it fails a changed delayed example. The learner's energy was visibly dropping late in this session, so today's final status should be treated as a survey of likely failure modes rather than a mastery exam.


## 7 Oct delayed confirmation — exam-ready A* proof scripts

The bounded Search confirmation ran longer than intended because the learner chose to make two proof arguments conceptually retrievable rather than merely memorised. This produced useful delayed evidence and is now a stop condition for Search today.

### Consistency => nondecreasing f

Exam-ready structure with conceptual narration:

```text
Consistency on edge A -> B:
h(A) <= c(A,B) + h(B)

Meaning: estimated remaining cost at A cannot exceed the real one-step cost to B
plus the estimated remaining cost from B.

Add g(A) to both sides:
g(A) + h(A) <= g(A) + c(A,B) + h(B)

Meaning: add the cost already accumulated from the start to A. This converts a
remaining-cost comparison into an estimated total-solution-cost comparison.

Since g(B) = g(A) + c(A,B):
f(A) <= f(B)

Therefore f is nondecreasing along every edge/path.
```

The learner initially reused the goal-node fact `h(goal)=0`, then after visual/scaffolded repair independently reconstructed the full derivation without looking. The conceptual anchor that landed was: **`g` = cost already paid, `h` = estimated cost still to pay, `f=g+h` = estimated total solution cost through the current node.**

A small inconsistent-heuristic graph also made the reopening mechanism concrete: if `f` is allowed to drop along an edge, a later route can reveal a cheaper `g` for a node that was already closed; consistency forbids this decreasing-`f` surprise.

### A* blocking a suboptimal goal

Exam-ready structure with the same conceptual narration:

```text
Let C* be the optimal solution cost and let n be a frontier node on an optimal path.

Admissibility:
h(n) <= h*(n)

Add g(n):
g(n) + h(n) <= g(n) + h*(n) = C*
so f(n) <= C*.

Meaning: a frontier node on an optimal path advertises an estimated TOTAL solution
cost no greater than the true optimal solution cost.

For a suboptimal goal G:
h(G) = 0, so f(G) = g(G) > C*.

Meaning: at a goal there is no remaining estimate, so f is the actual complete path
cost. A suboptimal goal therefore advertises a cost greater than C*.

Thus:
f(n) <= C* < f(G)

Since A* pops minimum f, n must be popped before the suboptimal goal G.
```

Useful memory contrast: both proofs use adding `g` to convert a statement about remaining cost into one about estimated total solution cost. Consistency uses this to obtain `f(A) <= f(B)`; admissibility on an optimal-path node uses it to obtain `f(n) <= C*`.

### Evidence boundary / next

This is meaningful delayed strengthening, but the first consistency attempt needed repair before the final cold reconstruction. Do not spend more of today's HMM/particle-filtering JIT block on Search. Move now to the historically weak-evidence Markov-chain diagnostic.
