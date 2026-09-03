# Lesson 26 — A* Search

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

Lesson 26 moved from uninformed graph traversal into cost-aware informed search. It introduced a priority queue, accumulated path cost `g`, heuristic estimate `h`, and the A* priority `f = g + h`.

## What was implemented

Source: `classical_ai/search/lesson26_astar.py` + `classical_ai/search/test_lesson26_astar.py`.

Implementation components:
- weighted graph: neighbours stored as `(state, edge_cost)`;
- priority frontier via `heapq`;
- initial priority uses the start heuristic;
- `cost_so_far[state]` stores best known `g` cost;
- a neighbour is updated if unseen **or** reached through a cheaper path;
- `parent` is updated alongside cheaper cost;
- frontier priority is:

```python
priority = new_cost + heuristic[neighbour]
```

- reaching the goal reconstructs the path through parents;
- unreachable goal returns `None`.

The test graph verifies the returned path is `A -> B -> D -> G`, whose path cost is lower than the tempting alternatives.

## Core concepts

### `g(n)`

Actual cost already paid from start to node `n`.

### `h(n)`

Estimated remaining cost from `n` to goal.

### `f(n) = g(n) + h(n)`

A* prioritises nodes using both known cost and estimated remaining cost.

### Why `cost_so_far` differs from a simple `seen` set

In weighted search, discovering a state once does not necessarily mean the first path to it is cheapest. If a later route produces a lower `g`, this implementation updates its cost and parent and pushes a new frontier entry.

That is a major conceptual step beyond BFS/DFS.

## Chat-history context

A* was implemented with BFS/DFS and then deliberately parked. Current learning state says reactivation should add **UCS and heuristic theory**, not restart A* from zero. The code-level `g+h` mechanism exists; course-level guarantees are the unfinished piece.

## Important theory still pending

Do not overclaim from this implementation alone. A* optimality depends on assumptions about the heuristic/search formulation. Future work should explicitly cover:
- uniform-cost search as A* with `h=0`;
- admissible heuristic: does not overestimate true remaining cost;
- consistency/monotonicity at course-appropriate depth;
- why these properties matter for optimality/re-expansion behaviour;
- comparison with BFS/UCS/greedy best-first if taught;
- time/memory limitations.

## Cold-retrieval question bank

1. In A*, what do `g`, `h`, and `f` each mean?
2. If a node has `g=7`, `h=3`, what frontier priority does A* use?
3. Why is a priority queue needed rather than FIFO/LIFO?
4. Why can a plain `seen` set be insufficient on a weighted graph?
5. If node X was reached at cost 10 and later at cost 6, what should happen?
6. What does A* become when every heuristic value is zero?
7. What makes a heuristic “admissible”?
8. Why could an overestimating heuristic threaten an optimality guarantee?
9. Compare BFS and A* when every edge cost is 1 but useful heuristic information exists.
10. Reconstruct the path using a parent map after the goal is popped.

## Retrieval blueprint

For search reactivation:
1. retrieve BFS/DFS distinction;
2. introduce weighted graph and `g`;
3. reconstruct heap frontier and `g+h`;
4. explain cheaper-path updates;
5. derive UCS from `h=0`;
6. add admissibility/consistency theory;
7. compare guarantees across BFS/DFS/UCS/A*.

## Mastery signal

Implementation mastery: explain and reconstruct `heapq`, `cost_so_far`, parent updates and `g+h` priority.

Course-ready mastery additionally requires heuristic properties and algorithm-comparison theory, which remain intentionally pending.
