# AIMS5701 search guarantees reactivation — 23 Sep 2026

**Session:** 1-hour morning search block before the later AIMS5701 search session/lecture  
**Evidence type:** delayed cold retrieval plus same-session teaching/changed-example transfer  
**Scope:** BFS/DFS/UCS/A* mechanics, UCS optimality condition, A* admissibility and consistency

## Cold retrieval

### BFS

The learner reconstructed the core BFS state and control flow from memory:

- a deque frontier;
- a parents mapping that records both discovery and predecessor;
- FIFO removal with `popleft()`;
- goal check on the current node;
- enqueue only neighbours not already present in `parents`;
- reconstruct the path through parent links.

They explained the causal link:

```text
FIFO -> all shallower depths are processed before deeper ones
     -> first reached path is shortest by number of edges
```

This was strong delayed retrieval. No implementation rewrite was needed.

### DFS

The learner immediately identified the frontier change from BFS:

```text
popleft() -> pop()
FIFO      -> LIFO
```

They correctly explained that newest descendants remain highest priority, so DFS follows a branch deeply and does not guarantee the shortest path.

### UCS

Initial retrieval mixed UCS with A*: the learner first said the frontier needed both heuristic and cost-so-far. After one correction, they correctly recovered:

```text
g(n) = accumulated cost from start
UCS expands the frontier node with lowest g(n)
```

They also retrieved the cheaper-route update rule: if a newly found route to an already discovered node has lower total cost, update its cost and parent.

A substantive gap appeared around termination. The learner initially thought UCS could safely return when the goal was first discovered. A counterexample established the correct rule:

```text
goal discovered != optimality guaranteed
goal popped as minimum-g frontier item -> optimality guaranteed
```

The learner then immediately retrieved this distinction in a recap.

## A* reactivation and new guarantee work

The learner correctly retrieved:

```text
g(n) = actual cost so far
h(n) = estimated remaining cost to a goal
f(n) = g(n) + h(n)
A* expands lowest f(n)
h(n) = 0 for every node -> UCS
```

They explained the role of the heuristic as directing search toward routes that appear promising overall rather than ranking only by cost already spent.

### Admissibility

The learner initially inverted the safe direction, choosing exact/overestimating heuristics rather than exact/underestimating ones. After correction and reasoning through why overestimation can make an optimal route look artificially unattractive, they transferred correctly to changed examples.

Current same-session model:

```text
admissible:
h(n) <= h*(n)

heuristic may underestimate or be exact
heuristic must not overestimate true cheapest remaining cost
```

Useful intuition: an admissible heuristic may be optimistic or even uninformative (`h=0`), but must not be overconfident about remaining cost.

### Consistency

Consistency was the most fragile/new part of the session and required several examples.

The formal condition taught was:

```text
h(A) <= c(A,B) + h(B)
```

or equivalently:

```text
h(A) - h(B) <= c(A,B)
```

The learner initially inverted consistency examples twice. The conceptual breakthrough came from distinguishing:

```text
h(B)        = estimated cost still remaining after reaching B
h(A)-h(B)   = estimated progress toward the goal
c(A,B)      = actual cost paid to make that move
```

The resulting intuition:

> A consistent heuristic cannot claim that one edge produced more estimated progress toward the goal than the cost paid for that edge.

After this distinction was explicit, the learner correctly classified multiple changed examples, including equality at the boundary.

They also connected consistency to monotonic `f` values. Since a consistent heuristic's drop cannot exceed the increase in `g`, `f=g+h` cannot decrease along an edge. An example where `f` fell from 14 to 13 was correctly diagnosed as inconsistent.

### Admissible vs consistent

On a changed example where true remaining costs were supplied, the learner correctly separated the tests:

- admissibility compares each `h(n)` with the true cheapest remaining cost;
- consistency compares the change in heuristic across an edge with that edge's cost.

They correctly identified an example that was admissible at both nodes but inconsistent across the edge.

A Google Maps analogy was used to clarify the distinction:

- an optimistic remaining-time estimate can still be admissible;
- consistency concerns whether successive remaining-time estimates change coherently with the travel cost between positions.

## Evidence boundary

Do **not** promote search guarantees to independent mastery from this session.

Strong delayed evidence:
- BFS mechanics, seen-state/parents role, FIFO and shortest-by-edges reasoning;
- DFS LIFO/depth-first behaviour and lack of shortest-path guarantee;
- A* core `g/h/f` definitions after the UCS/A* contamination was corrected.

Reactivated with a substantive correction:
- UCS uses `g`, not a heuristic;
- UCS optimality is safe when the goal is popped as minimum cost, not merely discovered.

Same-session/new and still fragile:
- admissibility initially inverted, then transferred correctly;
- consistency required repeated teaching and changed examples before the progress-vs-remaining-cost distinction landed;
- consistency -> nondecreasing `f` was derived in-session;
- the formal relationship that consistency is stronger than admissibility has not yet been developed;
- general completeness/time/space complexity remains open.

## Next block

Start the afternoon search block with a short cold check of:

1. UCS: why goal-popped matters;
2. admissibility: which direction the inequality goes;
3. consistency: `h(A)-h(B) <= c(A,B)` and the estimated-progress intuition.

Then continue with A* optimality/assumptions and completeness/time/memory complexity. Do not spend the block rewriting BFS/DFS.
