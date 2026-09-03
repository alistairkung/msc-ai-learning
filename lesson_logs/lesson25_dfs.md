# Lesson 25 — Depth-First Search (DFS)

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

Lesson 25 intentionally kept most of the BFS machinery the same so the effect of the **frontier discipline** became obvious. The main algorithmic change was FIFO -> LIFO.

## What was implemented

Source: `exercises/lesson25_dfs.py` + `tests/test_lesson25_dfs.py`.

The implementation retains:
- adjacency-list graph;
- `seen` set;
- parent map;
- path reconstruction;
- unreachable/start-is-goal handling.

The key difference is:

```python
current_state = queue.pop()
```

instead of BFS's:

```python
current_state = queue.popleft()
```

So the deque is used as a stack: most recently added state is explored next.

## Core concepts

### LIFO produces depth-first behaviour

DFS follows one branch deeper before returning to alternatives. With an explicit stack, the exact path explored also depends on neighbour insertion order.

### DFS does not promise the shortest path

Unlike BFS on unit-cost graphs, the first goal reached by DFS may be on a longer route even if a shallower route exists elsewhere.

### Same graph-search scaffolding, different search strategy

This lesson is useful because it separates reusable search machinery from the algorithm-specific frontier policy:

```text
same: seen + parent + neighbours + goal check
change: which frontier item is selected next
```

## Chat-history context

DFS was learned as part of the BFS/DFS/A* search block and then deliberately parked. Current planning calls for **comparison-level retrieval** rather than rewriting DFS in isolation: the important upcoming skill is explaining when BFS and DFS behave differently and what guarantees each does or does not have.

## Important theory still pending

Future search reactivation should make explicit:
- DFS completeness assumptions (finite vs infinite/deep state spaces);
- non-optimality;
- time and memory trade-offs;
- depth limits / iterative deepening if the course introduces them.

## Cold-retrieval question bank

1. What one-line frontier change converts this BFS-style loop into DFS?
2. Why does LIFO make the search go deeper?
3. Does DFS always return the fewest-edge path? Give a counterexample verbally.
4. How can neighbour ordering affect the path DFS finds?
5. Why is a `seen` set still useful in DFS on a graph?
6. What does the parent map do independently of DFS/BFS choice?
7. Compare likely memory use of BFS vs DFS on a wide tree.
8. What risk does DFS face in an unbounded-depth search space?
9. If the goal is very shallow but the first branch is extremely deep, which algorithm may behave better and why?

## Retrieval blueprint

1. derive DFS by modifying BFS;
2. trace stack order;
3. compare returned path with BFS on the same graph;
4. ask shortest-path/optimality question;
5. discuss memory and depth qualitatively;
6. later add formal course notation.

## Mastery signal

The learner can reconstruct DFS, explain LIFO behaviour, distinguish graph traversal machinery from frontier policy, and clearly state that DFS does not generally guarantee a shortest/lowest-cost solution.
