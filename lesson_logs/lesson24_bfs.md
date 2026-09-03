# Lesson 24 — Breadth-First Search (BFS)

_Status: reconstructed retrospectively from repo + recoverable learning history_

## Curriculum role

This began the classical-search block for Fundamentals in AI. It reused earlier DSA ideas—sets for `seen`, dictionary state, queue behaviour—inside an actual graph-search algorithm and added parent-based path reconstruction.

## What was implemented

Source: `exercises/lesson24_bfs.py` + `tests/test_lesson24_bfs.py`.

Implementation components:
- graph represented as adjacency lists;
- FIFO frontier with `collections.deque`;
- start state inserted into frontier and `seen` immediately;
- `popleft()` chooses the oldest frontier state;
- unseen neighbours are marked seen, assigned a parent and enqueued;
- reaching goal triggers path reconstruction by following `parent` pointers backward;
- unreachable goal returns `None`;
- `start == goal` returns `[start]`.

Core structure:

```text
frontier: FIFO queue
seen: avoid re-exploration
parent: reconstruct solution path
```

## Core concepts

### Why FIFO matters

BFS expands states in increasing number of edges from the start: depth 0, then depth 1, then depth 2, etc.

That gives BFS its key unweighted-graph property: the first discovered goal path has the minimum number of edges, assuming ordinary unit-cost edges.

### Seen set

Without `seen`, a cyclic graph can repeatedly enqueue the same states. Marking a state seen when it is first enqueued avoids duplicate frontier entries in this implementation.

### Parent map

Search and path reconstruction are separate problems. The frontier tells us what to explore next; `parent[child] = current` remembers the tree of discoveries so the final route can be reconstructed after reaching the goal.

## Chat-history context

BFS was implemented successfully and then **deliberately parked** with DFS/A* so the learning plan could move forward. The durable state explicitly says the next return should be cold reconstruction + comparison/theory rather than relearning from zero. That reactivation remains time-sensitive for Fundamentals Week 2.

## Important theory still pending

The implementation lesson did **not** finish the whole search-theory syllabus. Future reactivation should add:
- completeness;
- optimality assumptions;
- time/memory intuition in branching-factor/depth terms;
- comparison with DFS/UCS/A*;
- state/action/goal/path-cost vocabulary.

## Cold-retrieval question bank

1. Why is a queue/FIFO structure essential to BFS behaviour?
2. What changes if `popleft()` becomes `pop()`?
3. Why put `start` in `seen` before the loop?
4. What bug can occur on cyclic graphs without a `seen` set?
5. Why is `parent` needed if we only care whether a goal exists? When is it not needed?
6. Reconstruct the path from `parent = {A:None, B:A, D:B, G:D}`.
7. Under what edge-cost assumption does BFS give a lowest-cost path?
8. Does BFS necessarily use little memory? Why can its frontier become large?
9. Trace frontier order on a small branching graph.
10. Explain why the start-is-goal case naturally works in the loop.

## Retrieval blueprint

For the planned search reactivation:
1. rebuild BFS from blank pseudocode;
2. trace queue + seen on a graph;
3. reconstruct path from parents;
4. explain shortest-path condition;
5. compare frontier behaviour with DFS;
6. then add formal completeness/time/memory theory.

## Mastery signal

Implementation mastery: reconstruct FIFO frontier + seen + parent map and explain each data structure.

Course-ready mastery requires the later theory layer too; this lesson alone should therefore remain **Amber/Green**, not “done forever”.
