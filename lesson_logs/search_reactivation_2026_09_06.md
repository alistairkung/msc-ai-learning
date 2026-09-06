# Search reactivation — BFS, DFS, UCS and A* theory

**Date:** 2026-09-06  
**Status:** Substantive retrieval + new theory session  
**MSc context:** AIMS5701 Fundamentals begins this week; first class is Wednesday. Search is the Week-2 topic and had been deliberately parked after Lessons 24–26.

## Session objective

Cold-retrieve the conceptual structure of BFS, DFS and A* without rereading the old implementations, then extend the existing search foundation with UCS and course-level vocabulary around heuristic quality and search guarantees.

No implementation was written in this session. The next session should test whether the algorithms can be reconstructed from cold recall.

---

## What survived cold retrieval

### BFS

The learner correctly recovered level-by-level traversal and explained why BFS returns a shortest path in an unweighted/equal-edge-cost graph: nodes are explored in increasing path depth, so a shorter undiscovered route cannot remain behind a deeper one.

Frontier mechanics initially needed one prompt: the learner first answered `set` when asked for the frontier data structure, then immediately recognised that the set belongs to visited-state tracking and that BFS uses a `deque` as a FIFO queue.

Durable distinction:

```text
BFS → lowest depth / fewest edges from the start
frontier → FIFO queue
```

### DFS

The learner correctly traced DFS through a branching graph, including backtracking after a dead end, and recovered the LIFO behaviour after a small wording correction.

Durable distinction:

```text
DFS → pursue most recently discovered branch deeply
frontier → LIFO stack behaviour
```

The learner also correctly reasoned that DFS is not guaranteed to return the shortest path and can fail completeness in an infinite-depth search space by following one infinite branch forever.

### A*

The learner retained the main A* structure with a small initial mix-up between `f` and the heuristic itself. After separating the terms, recall was solid:

```text
g(n) = accumulated real cost from start to n
h(n) = estimated remaining cost from n to goal
f(n) = g(n) + h(n)
```

Given frontier values, the learner correctly calculated `f` scores and selected the lowest-priority node.

---

## New material — Uniform Cost Search

UCS was introduced from the weighted-graph failure mode of BFS.

The learner correctly reasoned that BFS can prefer a two-edge path of cost 11 over a three-edge path of cost 6 because BFS sees depth, not edge weights.

UCS was then derived as:

> expand the frontier node with the lowest accumulated path cost `g(n)`.

The learner correctly traced a weighted example through successive frontier states and understood why the cheaper longer path is selected.

Important relationship established:

```text
BFS → lowest depth
UCS → lowest g(n)
A*  → lowest f(n) = g(n) + h(n)
```

If all edge costs are equal, BFS and UCS effectively prioritise the same depths.

If `h(n)=0` everywhere, A* reduces to UCS.

---

## New material — admissible heuristics

Admissibility was introduced as:

> An admissible heuristic never overestimates the true remaining cost to the goal.

The learner initially reversed the condition once, treating underestimation as the problem. After correction, the distinction landed quickly and was applied correctly across several changed examples.

Useful mental model:

```text
admissible = globally optimistic
```

Underestimation is allowed; exact estimates are allowed; overestimation is not.

The learner also correctly explained the danger of overestimation: inflating `h(n)` inflates `f(n)`, which can make an actually better route appear less promising and be overlooked/deprioritised.

---

## New material — consistency

Consistency was built from neighbouring heuristic estimates rather than presented as an isolated formula.

For an edge `A -> B`:

```text
h(A) <= cost(A,B) + h(B)
```

Intuition established:

> The estimate at A must be locally coherent with taking one real step to B and then using B's estimate.

Equivalent useful wording:

> `h` should not fall by more than the cost of the edge just traversed.

The learner needed several examples before this became stable. The main semantic slip was briefly interpreting `h(B)` as the cost of getting **from A to B**, rather than the estimated remaining cost **from B to the goal**. The learner then self-corrected this distinction in the final example.

Useful pair:

```text
admissibility → compare h(n) with TRUE remaining cost
consistency   → compare h(A) with edge cost + h(B)
```

The learner also correctly recognised that knowing only `h(A)` and the true remaining cost can establish admissibility at A but cannot establish consistency without neighbouring-edge information.

---

## New material — completeness and optimality

These terms were largely new formal vocabulary even though some of the underlying reasoning was already present.

### Complete

> If a solution exists, is the algorithm guaranteed eventually to find one under the stated search assumptions?

The learner initially interpreted complete as accounting for the whole population/search space. After the definition was introduced, it was applied correctly.

### Optimal

> Is the returned solution guaranteed to be the best/lowest-cost solution under the stated assumptions?

Working comparison established during the session:

```text
BFS → complete; optimal for equal-cost/unweighted edges
DFS → not complete with possible infinite-depth branches; not optimal
UCS → complete + optimal under the positive-cost assumptions used in the lesson
A*  → complete/optimal under the appropriate search + heuristic assumptions; admissibility is central to the optimality intuition
```

Do not over-generalise these guarantees beyond the assumptions taught in this session. Tree-search vs graph-search subtleties and consistency/re-expansion guarantees remain future course-level extensions if needed.

---

## What the learner demonstrated confidently

- BFS traversal order and level-by-level reasoning.
- DFS traversal/backtracking intuition.
- Why BFS shortest-path reasoning depends on increasing depth/equal edge costs.
- Why BFS is unsuitable for minimising arbitrary weighted path cost.
- UCS priority by accumulated `g(n)`.
- `g`, `h`, `f=g+h` after one initial terminology correction.
- A* frontier comparisons from numerical `g/h` values.
- Admissibility after one initial reversal.
- Why overestimating can threaten optimal-path reasoning.
- Consistency calculations after examples and the local-coherence intuition.
- Completeness vs optimality once the vocabulary was introduced.
- UCS as the natural weighted no-heuristic choice; A* with `h=0` as equivalent behaviour.

---

## Fragile points to re-test

1. **Frontier vs visited structure** — a set tracks visited states; it does not define BFS/DFS frontier order.
2. **FIFO/LIFO wording** — BFS queue = first in, first out; DFS stack = last in, first out.
3. **BFS terminology** — say lowest depth/fewest edges, not “shortest edge distance”, which can sound like weighted cost.
4. **`h(n)` semantics** — estimated remaining cost from node `n` to the goal, not cost of reaching `n`.
5. **Admissibility direction** — underestimation/equality allowed; overestimation forbidden.
6. **Consistency** — requires neighbour/edge information; absence of conflicting information is not evidence of consistency.
7. **Completeness** — means guaranteed to find an existing solution under assumptions, not exhaustive exploration.
8. **Guarantee assumptions** — keep equal-cost/positive-cost/heuristic conditions attached to claims about optimality/completeness.

---

## Next session — implementation reconstruction

Do **not** show the existing Lessons 24–26 implementations first.

The next session should reconstruct search code incrementally from cold recall using the normal tutoring ladder:

```text
BFS from cold
→ DFS by changing frontier behaviour
→ UCS as new weighted implementation using g(n)
→ A* reconstruction as UCS + h(n)
→ small tests / compare returned paths and costs
```

The learner should write the important code. Ask for one implementation decision at a time and provide hints before syntax/full solutions.

Specific implementation concepts to test:

- frontier initialization;
- visited/seen handling for BFS/DFS;
- parent/path reconstruction;
- weighted neighbour representation;
- priority queue / `heapq` for UCS/A*;
- accumulated `g` cost;
- cheaper-path updates / `cost_so_far`;
- A* priority `g+h`;
- relationship `UCS == A* with h=0`.

After implementation reconstruction, re-test a short guarantees table and then decide whether time/memory complexity and any graph-search-specific A* subtleties need further work before/after the Wednesday Fundamentals lecture.

## Mastery signal for closing search reactivation

Search reactivation can move from pending to course-ready when the learner can:

- reconstruct BFS/DFS mechanics without rereading old code;
- implement/trace UCS correctly on weighted graphs;
- reconstruct A* as `g+h` search with cheaper-path handling;
- distinguish frontier ordering across BFS/DFS/UCS/A*;
- explain completeness vs optimality with the relevant assumptions;
- explain admissibility and consistency semantically and apply both to small examples.
