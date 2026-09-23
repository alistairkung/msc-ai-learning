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


---

## Afternoon continuation — guarantees, complexity and adversarial search

**Session:** ~2-hour afternoon block before the AIMS5701 lecture  
**Evidence type:** delayed cold check + same-session teaching/changed-example transfer  
**Scope:** A* optimality intuition, completeness/optimality comparison, BFS/DFS complexity, minimax and introductory alpha-beta pruning

### Fragile-point cold check

The learner immediately retrieved the UCS termination distinction from the morning session:

```text
goal discovered != safe to return
goal popped as lowest-g frontier item -> safe under the usual cost assumptions
```

Admissibility also returned correctly on the first changed check: with true remaining cost 7, heuristic values 4 and 7 were classified admissible while 9 was rejected because an admissible heuristic must not overestimate.

Consistency was still fragile. The learner reasoned through the local route comparison but initially attached the wrong consistent/inconsistent label on a changed example. After correction, the useful learner-generated intuition became:

> going via a known edge should not reveal an estimated shortcut that contradicts the estimate from where we are.

The session then linked consistency to monotonic `f=g+h`. One arithmetic slip temporarily treated `g(B)` as the edge cost rather than accumulated start-to-B cost; after correction the learner correctly computed changed examples where `f` stayed equal or increased.

### A* optimality connection

The learner reasoned through:

```text
consistent h
-> f cannot decrease along a path
-> A* pops the smallest frontier f
-> at the goal, h(goal)=0
-> f(goal)=g(goal)
-> a frontier path with larger f cannot later descend to a cheaper goal
```

This is same-session conceptual evidence, not delayed independent proof mastery. The distinction between "smallest f" and "already the optimal goal path" needed one refinement before the goal-state argument was clear.

### Completeness and optimality

The learner defined completeness approximately as a guaranteed answer, then refined it to:

> if a solution exists, the algorithm is guaranteed to eventually find one.

They reasoned correctly that:

- BFS is complete under the usual finite-branching/repeated-state assumptions because it exhausts increasing depths;
- DFS is not generally complete in infinite-depth spaces because it can disappear forever down one branch;
- UCS completeness depends on a positive lower bound on step costs; the learner initially worried correctly about infinite distraction by cheap paths, then understood why `c >= epsilon > 0` prevents an infinite-depth path remaining permanently cheaper than a finite-cost goal;
- A* remains complete under the usual finite-branching/positive-cost and suitable-heuristic assumptions;
- BFS is optimal for equal step costs but not arbitrary unequal costs;
- DFS is not generally optimal;
- UCS is optimal under its usual non-negative/positive-cost assumptions when the goal is popped;
- A* optimality was explained through admissibility, consistency and the goal's `h=0` condition.

Do not treat the exact theorem assumptions as cold memorised yet; the learner can currently reason about them with the model in view.

### Search complexity

Branching-factor growth was newly/reactivated. The learner initially treated `b=3` as additive growth (`3,6,9,12`) before correcting to multiplicative/exponential level sizes:

```text
depth d -> approximately b^d nodes at that level
```

BFS time/space was then connected to the size of the shallowest-goal level:

```text
time  O(b^d)
space O(b^d)
```

DFS was distinguished as:

```text
time  O(b^m)
space O(bm)
```

where `d` is shallowest solution depth and `m` maximum depth. The learner correctly explained why DFS can perform exponential total work while storing only the current path plus unexplored siblings. On immediate recap, DFS complexity was retrieved correctly but BFS was temporarily given `O(b^m)`; keep the `d` vs `m` notation distinction fragile rather than established.

### Adversarial / multi-agent search introduction

The learner asked for the second hour to introduce adversarial search.

The key conceptual bridge was eventually made explicit:

```text
MAX = one decision-making agent
MIN = the opposing decision-making agent
node label = whose turn it is to choose among that node's children
terminal utility = represented from MAX's perspective
```

This framing was important. Initial examples showed repeated confusion between action labels, terminal scores and which player controlled a child choice. After stepping back and replacing algorithmic "MAX/MIN node" language with "your agent's turn / opponent agent's turn", the learner correctly tracked alternating levels:

```text
MAX -> MIN -> MAX
you -> opponent -> you
```

### Minimax

After the turn-taking reset, the learner successfully propagated several changed game trees bottom-up:

- MAX chooses the highest child utility;
- MIN chooses the lowest child utility;
- values propagate upward because each value represents the outcome expected under optimal play from that state;
- the root agent chooses based on the opponent's optimal response, not the branch's best-case terminal leaf.

A three-level changed tree was solved correctly after the reset, including correctly identifying a MIN-root example.

Current conceptual model:

> minimax models two agents with opposed objectives; MAX chooses to maximise utility, MIN chooses to minimise the same MAX-perspective utility, and the tree is evaluated backward under optimal play.

### Alpha-beta pruning

Alpha-beta was initially introduced too early and deliberately reset until turn ownership was stable.

After rebuilding from player choices, the learner understood the pruning intuition:

- if MAX already has an alternative worth 5 and a newly explored MIN branch has already found a response worth 4, that MIN branch can never improve above 4 for MAX, so its remaining children cannot affect MAX's decision;
- conversely, if MIN already has an alternative worth 6 and a MAX branch has already reached at least 8, MIN will never choose that branch, so its remaining children can be ignored.

Terminology then attached to the established intuition:

```text
alpha = best lower bound / option MAX can already guarantee
beta  = best upper bound / option MIN can already guarantee
alpha >= beta -> remaining work under the current branch cannot affect the rational ancestor decision
```

The learner correctly retrieved `alpha=max(3,7,5)=7` and `beta=min(8,6,9)=6`, and correctly identified a no-prune case with alpha 6 / beta 7.

On a full left-to-right tree, the learner correctly found the first MAX-side cutoff under a MIN parent. A later whole-subtree cutoff initially failed because the learner forgot that MIN, not MAX, controls the B1/B2 choice. After correction the learner articulated the key insight:

> even if B2 were 1000, MIN would still return B1's lower value, so the branch cannot beat MAX's existing alternative.

This is good immediate conceptual transfer, but turn ownership and pruning direction remain **same-session fragile**, not established mastery.

### Big-picture synthesis

The learner explicitly asked why minimax belongs in AI fundamentals. The session connected the classical-AI progression:

```text
BFS/DFS -> find reachable goal states
UCS/A*  -> choose good paths efficiently using cost/knowledge
minimax -> choose actions when another agent strategically responds
alpha-beta -> avoid computation that cannot affect the decision
```

The learner then made the multi-agent connection explicitly: minimax is multi-agent because MAX and MIN represent two decision-making agents with opposed objectives in the standard two-player model.

### Evidence boundary after afternoon block

**Stronger than the morning handoff:**
- UCS goal-popped termination returned cold;
- admissibility returned cold on the first changed example;
- A* optimality intuition can be reconstructed from consistency -> nondecreasing f -> goal h=0;
- completeness vs optimality distinction is understood;
- BFS/DFS time-vs-space intuition has been introduced and reasoned through;
- minimax turn-taking and bottom-up propagation became correct after a deliberate reset;
- alpha-beta pruning intuition was demonstrated on changed examples after turn ownership stabilised.

**Still fragile / do not over-promote:**
- consistency classification still had one immediate changed-example label inversion;
- accumulated `g` had one arithmetic/semantic slip;
- exact completeness theorem assumptions are not cold memorised;
- BFS complexity `d` vs DFS `m` notation slipped on immediate recap;
- adversarial turn ownership initially caused repeated inversions;
- alpha-beta whole-subtree pruning needed correction before the learner articulated the correct MIN-choice reason;
- no minimax/alpha-beta implementation has been attempted;
- adversarial-search material is pre-lecture preparation unless/until the live course confirms the exact taught scope.

## Next retrieval / continuation

Do not repeat the whole search block immediately.

After spacing, briefly retrieve:

1. consistency from the local-edge intuition and why it makes `f` nondecreasing;
2. BFS `O(b^d)` vs DFS `O(b^m)` time and `O(bm)` space;
3. MAX/MIN as alternating agents/turns;
4. one small minimax tree;
5. one alpha-beta cutoff explained in player-choice language before using the inequality.

Use the live AIMS5701 lecture to confirm the exact adversarial-search scope before adding implementation work.


## Post-session implementation boundary

After the formal session, the learner explicitly reflected on whether implementation reconstruction should be the next priority.

For BFS/DFS/UCS/A*, the current strategy is **not** to immediately reconstruct all four implementations again. The conceptual/search-theory layer was the weaker target today, while prior repository evidence already includes:

- independent BFS reconstruction;
- implemented DFS with targeted debugging;
- guided passing UCS implementation;
- guided A* implementation.

The useful standard is therefore:

> Can the learner derive an implementation from the algorithmic model, using ordinary API lookup when needed, rather than reproduce exact Python from memory?

Occasional blank-file changed-graph reconstruction remains valuable as an operational spot check, especially for UCS/A* priority and cheaper-route update mechanics, but repeated full rewrites would currently displace higher-value JIT work.

Minimax is different. No implementation has yet been attempted, and turn alternation/ownership was a genuine same-session fragility. If the live lecture confirms minimax/alpha-beta as substantive course material, one bounded manual recursive implementation is likely valuable evidence:

```text
terminal state -> utility
MAX turn       -> max(recursive child values)
MIN turn       -> min(recursive child values)
```

Only after plain minimax is semantically stable should alpha-beta be added to the same implementation. Treat this as a short consolidation/diagnostic exercise, not a new multi-hour project.

Lecture-gap reconciliation should come first: record what the lecturer actually covers beyond or differently from the pre-lecture bridge, then decide whether the implementation exercise fills a real course-facing gap.


## Post-lecture reconciliation — actual Lecture 2 scope

**Source boundary:** learner report from the live 23 Sep AIMS5701 lecture plus the user-supplied Lecture 2 slide deck inspected after class. This is lecture calibration, not new independent mastery evidence.

The live lecture was largely familiar after the day's preparation. The actual deck covered planning/search formulation, state-space graphs vs search trees, DFS/BFS/UCS, iterative deepening, heuristics, greedy best-first, A*, admissibility, heuristic construction/dominance, graph search, consistency and safe closing. It did **not** cover minimax or alpha-beta.

This changes the immediate interpretation of the pre-lecture adversarial-search work:

- keep minimax/alpha-beta as useful extra classical-AI exposure;
- do not schedule a minimax implementation merely because it was pre-studied;
- treat adversarial search as parked until the live course or another explicit requirement calls for it.

The learner reported that most of the lecture felt familiar, but identified three mathematical gaps that still deserve deliberate work:

1. consistency still does not feel fully intuitive;
2. the proof that consistency implies admissibility needs to be broken down and reconstructed;
3. the inequality-based proof that admissible A* tree search returns an optimal goal needs reinforcement.

A systematic reconciliation pass should also briefly verify smaller lecture topics that were not pre-studied in depth, because live familiarity can hide gaps:

- search-problem formulation and state abstraction;
- state-space graph vs search-tree distinction;
- iterative deepening;
- greedy best-first as priority by `h(n)`;
- relaxed-problem heuristics;
- heuristic dominance / max-combination;
- graph search / closed sets;
- admissible-but-inconsistent A* and reopening/safe-closing intuition.

### Next AIMS5701 block

Hard-cap the reconciliation at **90 minutes**.

Suggested order:

```text
small-gap diagnostic sweep
    -> consistency intuition
    -> consistency => admissibility
    -> A* optimality contradiction / inequality proof
    -> consistency => nondecreasing f => safe closing
```

Do not replay full BFS/DFS/UCS/A* implementations. After this reconciliation, move search into spaced maintenance and shift the AIMS5701 JIT lead to linear/logistic retrieval -> decision trees -> random forests for the following week's lecture.
