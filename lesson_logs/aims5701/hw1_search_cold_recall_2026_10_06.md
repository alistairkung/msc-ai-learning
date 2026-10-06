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
