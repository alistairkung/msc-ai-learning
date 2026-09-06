# Search reactivation — BFS, DFS, UCS and A* theory + implementation continuation

**Date:** 2026-09-06  
**Status:** Theory reactivation complete; implementation reconstruction in progress  
**MSc context:** AIMS5701 Fundamentals begins this week; first class is Wednesday. Search is the Week-2 topic and had been deliberately parked after Lessons 24–26.

## Session 1 — theory reactivation

Cold-retrieved the conceptual structure of BFS, DFS and A* without rereading the old implementations, then extended the existing search foundation with UCS and course-level vocabulary around heuristic quality and search guarantees.

### BFS
- Correctly recovered level-by-level traversal and shortest-path reasoning for unweighted/equal-edge-cost graphs.
- Frontier mechanics initially needed one prompt: a set was first suggested, then correctly separated as visited-state tracking from the FIFO `deque` frontier.

```text
BFS → lowest depth / fewest edges from the start
frontier → FIFO queue
```

### DFS
- Correctly traced depth-first traversal and backtracking.
- Recovered LIFO behaviour after a small wording correction.
- Correctly reasoned that DFS is not shortest-path optimal and can fail completeness in infinite-depth search spaces.

```text
DFS → pursue most recently discovered branch deeply
frontier → LIFO stack behaviour
```

### A*
Recovered the main structure after a small initial `f`/heuristic terminology mix-up:

```text
g(n) = accumulated real cost from start to n
h(n) = estimated remaining cost from n to goal
f(n) = g(n) + h(n)
```

### UCS — new material
UCS was introduced from the weighted-graph failure mode of BFS. The learner correctly reasoned that BFS can prefer a lower-depth but higher-cost path because it sees depth rather than edge weights.

```text
BFS → lowest depth
UCS → lowest g(n)
A*  → lowest f(n) = g(n) + h(n)
```

If all edge costs are equal, BFS and UCS effectively prioritise the same depths. If `h(n)=0` everywhere, A* reduces to UCS.

### Admissibility — new material

```text
admissible = globally optimistic
```

An admissible heuristic never overestimates true remaining cost. Underestimation/equality are allowed. The condition was initially reversed once, then applied correctly across examples.

### Consistency — new material
For edge `A -> B`:

```text
h(A) <= cost(A,B) + h(B)
```

Useful intuition: `h` should not fall by more than the cost of the edge just traversed. Several examples were needed before the semantics stabilised, especially that `h(B)` is estimated remaining cost from B to the goal.

```text
admissibility → compare h(n) with TRUE remaining cost
consistency   → compare h(A) with edge cost + h(B)
```

### Completeness and optimality — new vocabulary

```text
BFS → complete; optimal for equal-cost/unweighted edges
DFS → not complete with possible infinite-depth branches; not optimal
UCS → complete + optimal under the positive-cost assumptions used in the lesson
A*  → complete/optimal under appropriate search + heuristic assumptions
```

Do not over-generalise guarantees beyond the assumptions taught here.

---

## Session 2 — implementation continuation after ~90-minute break

This was explicitly treated as a continuation of the same day's work, not a new cold-retrieval session. The goal was to move from conceptual understanding into code without repeatedly testing the same theory.

### BFS guided reconstruction

The learner reconstructed BFS incrementally without opening the old Lesson 24 implementation.

Recovered state:

```python
parents = {start: None}
frontier = deque([start])
```

The learner correctly identified that the parent dictionary can both record predecessor links and serve as discovered-state tracking. Exact `deque([start])` syntax was recalled tentatively and confirmed.

Recovered FIFO mechanics:

```python
current = frontier.popleft()
```

Recovered neighbour traversal and discovery:

```python
for node in graph[current]:
    if node not in parents:
        parents[node] = current
        frontier.append(node)
```

The learner correctly explained that a newly discovered node must be recorded with `current` as its parent and appended to the frontier.

### Goal and path reconstruction

The learner correctly chose to detect the goal when it is popped as `current` and then reconstruct the path from parent pointers.

Initial reconstruction attempt followed the right backwards-parent idea but looked up the parent before appending, which would omit the goal and append `None`. After tracing this concrete failure, the learner immediately identified the fix: append the current node first.

Stable pattern reached:

```python
path = []
node = current

while node is not None:
    path.append(node)
    node = parents[node]

path.reverse()
return path
```

The learner also correctly supplied `return None` for exhausted frontier / unreachable goal.

### BFS → DFS derivation

Rather than cold-reconstructing DFS separately, the BFS implementation was transformed. The learner immediately identified the fundamental change:

```python
# BFS
current = frontier.popleft()

# DFS
current = frontier.pop()
```

They correctly understood this as changing FIFO to LIFO while retaining parent tracking, duplicate detection, goal handling and path reconstruction. It was also established that a normal Python list is sufficient for DFS with end `append()`/`pop()`.

Given neighbours `['B', 'C']`, the learner correctly predicted that appending B then C means C is explored first under LIFO. This reinforced that DFS traversal order depends on neighbour insertion order.

---

## Independent BFS practice result

The learner then used the skipped `test_practice_bfs_reconstruction.py` exercise and independently reached a correct complete BFS implementation. The solution itself is intentionally **not committed**: the skipped test is being retained as a reusable periodic reconstruction exercise.

### Fragilities exposed by the independent attempt

1. **Fixed search variable vs moving reconstruction cursor.** During path reconstruction the learner initially used `path.append(current)` and `node = parents[current]`. Because `current` remains the goal node and never changes inside the reconstruction loop, this caused an infinite loop. The corrected mental model is:

```text
current = fixed node that ended the search / goal
node    = moving cursor walking goal → parent → parent → ... → start
```

Correct invariant:

```python
while node is not None:
    path.append(node)
    node = parents[node]
```

2. **Graph membership vs discovered-state membership.** The neighbour loop was briefly inverted into logic resembling:

```python
if current not in graph:
    for node in graph[current]:
        ...
```

This confused two separate responsibilities:

```text
graph[current]      → which neighbours are reachable from current?
node not in parents → has this neighbour already been discovered?
```

The correct expansion shape was recovered:

```python
for node in graph[current]:
    if node not in parents:
        parents[node] = current
        frontier.append(node)
```

### Interpretation

These errors are implementation/state-role confusions rather than failures of the BFS conceptual model. The independent final implementation correctly contained FIFO frontier behaviour, parent/discovered tracking, goal detection, neighbour expansion, duplicate prevention, path reversal and unreachable-goal handling. No further full BFS reconstruction is required immediately; future BFS practice should use the retained skipped test periodically rather than turning BFS into repeated cold-retrieval sessions.

---

## Current demonstrated strengths

- BFS level/depth reasoning and unweighted shortest-path intuition.
- Independent successful BFS implementation after debugging two state-role errors.
- FIFO queue semantics and `popleft()`.
- Parent map serving both predecessor reconstruction and discovered-state tracking.
- BFS neighbour expansion and duplicate prevention.
- Parent-chain path reconstruction with the fixed-`current` vs moving-`node` distinction now explicitly identified.
- DFS as the same graph-search skeleton with LIFO frontier policy.
- DFS neighbour-order implications.
- Weighted-vs-unweighted distinction.
- UCS `g(n)` concept and A* `g+h` relationship.
- Introductory admissibility, consistency, completeness and optimality vocabulary.

## Still fragile / evidence needed

1. Keep variable roles explicit during path reconstruction: fixed `current` vs moving `node`.
2. Keep graph adjacency (`graph[current]`) separate from discovered-state membership (`node in parents`).
3. UCS implementation: weighted neighbours, priority queue, accumulated `g`, cheaper-path updates.
4. A* implementation as UCS + `h`.
5. Consistency semantics and guarantee assumptions after implementation work.

---

## Practice asset

`classical_ai/search/test_practice_bfs_reconstruction.py` remains module-skipped so it cannot block CI. It should remain **solution-free** and can be revisited periodically as a lightweight reconstruction check. Do not turn it into a frequent compulsory retrieval loop.

## Next continuation

Continue directly into UCS implementation:
- weighted neighbour representation;
- `heapq` priority frontier;
- accumulated `g` cost;
- `cost_so_far` / cheaper-path updates.

Then derive A* by changing priority to `g+h`. Finish with a brief guarantees/heuristics check and complexity only if useful.

Do **not** restart with broad cold retrieval of BFS/DFS/A* theory.
