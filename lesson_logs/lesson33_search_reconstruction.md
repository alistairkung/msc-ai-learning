# Lesson 33 — Search reconstruction: BFS / DFS / UCS / A*

**Date:** 2026-09-10  
**Status:** Integrated practice suite passes; BFS/DFS recall refreshed; UCS and A* derived with guidance; search guarantees/complexity still due

## Curriculum role

This session reactivated the classical-search track after Lesson 32 and moved forward rather than restarting it. It began with a short BFS/DFS cold recall, repeated the DFS implementation exercise, then introduced UCS and derived A* directly from UCS.

Source practice suite: `classical_ai/search/test_lesson33_search_reconstruction_practice.py` (path/name inferred from the learner's rename intent and latest commit content; use the commit as implementation evidence if the exact path later changes).

Latest learner commit reviewed: `89e16b1c3a99e62968597155da47f6a5dfe340e8` — `lesson_33: derives ucs and A*`.

## What was demonstrated

### BFS / DFS cold recall

The learner correctly recalled:

- BFS uses `popleft()` / FIFO;
- DFS uses `pop()` / LIFO;
- FIFO explores a depth level before moving deeper;
- LIFO tends to continue down the most recently discovered branch;
- BFS guarantees a fewest-edge path on an unweighted graph, while DFS can return a deeper first-found goal;
- the parent map can serve both discovered-state tracking and path reconstruction.

A useful precision point was reinforced: the parent map records the route; BFS's frontier ordering is what gives the fewest-edge guarantee.

### BFS reconstruction fragility repeated

During BFS reconstruction, the previously logged path-reconstruction fragility recurred. A moving cursor (`next` / `next_node`) was created, but the fixed `current` variable was initially used inside the reconstruction loop. The learner recognised and fixed this after a prompt.

This is now repeated evidence rather than a one-off typo:

```text
search current/goal = fixed node that triggered reconstruction
reconstruction cursor = node that must move parent-by-parent toward start
```

A smaller Python slip also appeared around calling `path.reverse()` rather than referring to `path.reverse`.

### DFS reconstruction

The learner reconstructed DFS from the BFS skeleton with the correct LIFO frontier and correct moving reconstruction cursor. The main issue was indentation: `return None` was initially inside the search loop, which would stop after the first expansion. After correction, the DFS practice tests passed.

This is stronger current evidence than the prior guided BFS→DFS derivation, but it was still performed immediately after BFS recall and with targeted debugging support. Treat DFS as refreshed/implemented evidence, not a pristine unaided cold reconstruction.

## UCS — new implementation in this session

UCS was taught as the transition from unweighted frontier order to weighted accumulated-cost order.

Core representation learned:

```text
frontier entry = (g, node)
g = accumulated cost from start to node
cost_so_far[node] = cheapest known g for that node
```

The learner correctly articulated the key update rule:

> update when a node has not been discovered before, or when the newly found accumulated cost is lower than the recorded cost.

The implementation used `heapq` and passed tests covering:

- lowest-cost path;
- start equals goal;
- unreachable goal;
- replacing a previously discovered route when a cheaper path is found;
- preferring lower total cost even when it uses more edges.

### UCS support / fragilities

Several targeted corrections were needed during construction:

- frontier heap is a list of tuples rather than a `heapq(...)` object;
- tuple unpacking from `heapq.heappop`;
- weighted neighbour tuple order `(node, edge_cost)`;
- distinguishing `current_cost` (accumulated g) from `edge_cost`;
- update logic initially checked `current` instead of the neighbour;
- the unseen/cheaper condition was initially inverted;
- short-circuit logic was reinforced: `node not in cost_so_far or new_cost < cost_so_far[node]` avoids indexing a missing key;
- `heapq.heappush(frontier, (new_cost, node))` syntax required support.

A trace question exposed one remaining conceptual arithmetic slip: after `A→C=2` and `C→B=3`, the learner initially said B's new cost was 3 rather than accumulated 5 and prematurely advanced to G. This was corrected. Retest accumulated-cost tracing later.

Therefore UCS is **implemented with guided derivation**, not independent yet.

## A* — derived from UCS

A* was intentionally taught as a small extension rather than a separate algorithm skeleton:

```text
UCS priority = g(n)
A* priority  = f(n) = g(n) + h(n)
```

The learner correctly recalled that `f = g + h`, answered a numeric `5 + 3 = 8` priority check, and understood that the frontier needs to preserve both priority and true path cost.

The implementation used flattened heap entries:

```text
(f, g, node)
```

and computed neighbour priority as:

```text
new_g + heuristic[neighbour]
```

The practice tests passed for:

- lowest-cost path;
- start equals goal;
- unreachable goal;
- cheaper-path replacement;
- heuristic-based frontier prioritisation;
- zero heuristic reducing A* to UCS.

### A* support / fragilities

Targeted support was still required for:

- initial heap shape: a list containing one tuple rather than three separate list items;
- unpacking `(f, g, node)`;
- using `heuristic[neighbour]` rather than the heuristic of the expanded node;
- avoiding accidental use of `cost_so_far[neighbour]` in the priority formula.

The implementation therefore demonstrates successful **guided derivation from UCS**, not yet cold independent A* reconstruction.

## Integrated conceptual map

Keep this compact comparison cold-retrievable:

```text
BFS  frontier priority: discovery order / FIFO
DFS  frontier priority: most recent / LIFO
UCS  frontier priority: g
A*   frontier priority: g + h
```

And:

```text
g(n) = real accumulated cost from start to n
h(n) = estimated remaining cost from n to goal
f(n) = g(n) + h(n)
```

With `h(n)=0` everywhere, A* behaves like UCS.

## Evidence boundary

The final integrated test suite passing is strong implementation evidence, but it should not erase the tutoring support required during construction.

- **BFS:** remains the strongest search implementation evidence; current recall was good, with repeated reconstruction-cursor fragility.
- **DFS:** successfully reconstructed and tested today after brief recall, with one indentation correction; stronger than the previous guided-only record but not labelled fully independent from this session alone.
- **UCS:** concept understood and implementation completed; guided.
- **A*:** successfully derived from UCS and tested; guided/currently implemented, not cold independent.

Do not infer guarantees or complexity mastery from implementation success.

## Next search work

Do **not** immediately rewrite all four algorithms again.

Next useful block:

1. consolidate completeness and optimality across BFS / DFS / UCS / A*;
2. state assumptions behind UCS optimality (especially non-negative edge costs);
3. retrieve admissibility and consistency for A* and distinguish them;
4. add qualitative then formal time/memory complexity as required by AIMS5701;
5. confirm the course meaning of “searching with other agents” before teaching it;
6. later use one short changed-graph reconstruction to test whether UCS/A* have become independently retrievable.

## Future cold-recall targets

- Why stop UCS/A* when the goal is **popped**, not merely discovered?
- What does `cost_so_far` add beyond costs already present in heap entries?
- Why can the same node appear more than once in a heap?
- Given a cheaper route, which three pieces of state change?
- Distinguish edge cost from accumulated `g`.
- Recompute a short UCS trace where an initially expensive node is improved later.
- Explain why A* with `h=0` is UCS.
- Given `g` and `h`, compute `f` and identify which node A* expands next.
- Probe the repeated path-reconstruction cursor fragility.
