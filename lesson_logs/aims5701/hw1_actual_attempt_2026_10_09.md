# AIMS5701 — HW1 actual-assignment attempt — 2026-10-09

## Scope and evidence boundary

Source: learner's attempted HW1 answers, handwritten pictures and dialogue during the 9 October AI tutoring chat, using the actual AIMS5701 HW1 problem sheet. The learner requested diagnosis of gaps, not complete prewritten solutions. This is an **outcome/evidence log, not a transcript**. Tutor feedback occasionally disclosed complete checks, specific path values and parts of the modification; do not label all outcomes cold-independent. The homework requires acknowledgement and a full unedited AI conversation attached to the submission.

## Observed work

- **Q1 state representation**: learner identified position, direction and inclusive velocity range, and correctly excluded action history/turn state because the transition rules already use velocity and heading. Initially omitted one grid dimension in the multiplicative cardinality, immediately corrected. For the Euclidean heuristic, independently recognised that travel per action can exceed one cell; guided construction of a valid accelerate/decelerate corridor sequence and coordinate substitution repaired how to show an actual admissibility counterexample. The learner articulated why a single valid instance refutes a universal claim.
- **Q2 BFS, DFS, UCS**: handwritten queue/stack/frontier and parent traces inspected. BFS versus DFS solution cost was not misinterpreted as DFS optimality. UCS frontier cheaper-path updates, parent reassignment, and the goal-*popped* stop condition were understood. DFS alphabetical generation versus LIFO expansion convention was noted.
- **Q3 A***: independently prepared a paper `g/h/f` frontier trace, cheaper path and parent updates, with tutor review. Clearly articulated why a heuristic can prioritise a node with higher accumulated cost.
- **Q4**: wrote every local consistency inequality and per-node optimal remaining-cost comparison; recalled consistency implies admissibility but not conversely. No evidence of an independent proof reconstruction here.
- **Q6(b)(i)**: independently derived the qualitative failure mechanism: an admissible but inconsistent heuristic may make a node B close on a worse path; later expansion of A finds a cheaper `g(B)` that no-reopen graph search discards. Created a four-node directed example through several revisions. The challenging repairs were distinguishing `g(B)` via a new parent from `g(G)` already in the frontier, retaining the cheaper current goal candidate, and making the closed set cumulative rather than merely the most recently popped node. The learner's final graph/trace was reviewed as a valid counterexample showing suboptimal returned path. This was iterative, assisted correctness, not unaided first-pass proof.
- **Q6(b)(ii)**: proposed reopening a closed node if a strictly cheaper path is found. The tutor supplied explicit update/reinsert/propagate steps. Later independent transfer untested.

## Gaps and learning diagnostics

- Conceptual strength: separates heuristic admissibility (global lower bound) from consistency (local edge inequality), distinguishes discovery from safe termination, and understands the reason for reopening with inconsistent heuristics.
- Fragility: under multi-step graph traces, confusing a candidate successor with an actual frontier entry, using wrong parent/cost for goal after rediscovery, and initially omitting factors in symbolic state-space counts. Explicit paper frontier + parent + cumulative closed-set columns help.
- Representation translation: needed explicit starting/goal coordinates substituted into Euclidean distance, rather than treating motion distance as self-evidently equal to the formula.
- The tutor gave encouraging score-like statements (e.g., “conceptually complete”) which should **not** be converted into marks awarded or delayed-independent mastery.

## Remaining assignment work and next retrieval

- Q5 and Q6(a) were not attempted in the visible dialogue; complete independently.
- Independently draft/verify the final solutions; check Q6(b) trace makes rejected closed-node candidates distinct from frontier entries.
- A short later cold changed-example check on UCS/A* parent-cost consistency and the relation consistency -> nondecreasing f would establish transfer better than immediately replaying the assessed graph.
- Evidence compliance: the user encountered Chrome print “images still loading”; a readable reconstruction was combined with four pages of original browser screenshots locally. They are **not** a guaranteed substitute for a complete unedited ChatGPT transcript; verify coverage and lecturer requirements. These local PDF artifacts are not uploaded to the GitHub repository in this PR.
