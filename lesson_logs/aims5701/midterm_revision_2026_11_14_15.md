# AIMS5701 Midterm — Revision evidence, 14–15 November 2026

**Assessment:** Written midterm Wednesday 18 November, HW1–HW4. **Source:** learner-reported answers and tutor checks in interactive practice, including the learner's supplied 15 Nov session-status update. Questions were analogous, not copied from assessed sheets. This log documents outcomes, not a transcript.

## HW1 search
- **State spaces:** Early attempts omitted direction/scanner, miswrote `K²` rather than `2^K`, or stored fixed capacity/card configuration. Repair focused on distinguishing fixed instance parameters from varying information needed for actions, transitions, goals. Later independent passes: hospital robot `s=(r,b,P)`, `|S|=R(B+1)3^K`; directional cleaning robot `s=(m,n,d,w,C)`, `|S|=4MN(W+1)2^K`, with `M=5,N=6,W=3,K=4` giving 1920. Full verbal justifications not always submitted. Continue brief delayed cold retention.
- **BFS/DFS/UCS/A*:** Fresh graph diagnostic. BFS expanded S,A,B,C,D,E,G, returned S→A→C→G, cost 11; DFS S,A,C,G, cost 11. UCS expansion order S,B,A,C,D,E,G correct but learner returned wrong path/cost after missing visually unclear B→A(1) edge in graph; correct S→B→D→G, cost 9. A* independently returned S,B,A,D,G expanded, S→B→D→G cost 9. Preserve graphical ambiguity versus search-procedure error distinction; revisit cheaper-path parent updates briefly if useful.
- **Finite-graph admissibility:** Independently calculated `h*(S,A,B,C,G)=(8,5,7,3,0)` for `h=(7,6,7,2,0)`, correctly disproved admissibility at A: `6>5`. Terminology slip: calling satisfied admissibility nodes “consistent.”
- **General admissibility:** Unavoidable lifting cost example `h(s)=4r(s)`; initially invented `h*(s)=(4+e)r(s)`, then corrected to `h*(s)=4r(s)+M*(s)`, `M*≥0`. Subsequently explained lower-bound logic. Independently counterexampled `h=4D` with unit move cost 3 and `D=1`: `4>3=h*`.
- **Finite-graph consistency:** Independently checked edges and found `A→C:6>2+2` and `B→C:7>4+2`; others passed.
- **General consistency:** Manhattan `h=3D` and moves of exactly cost 3: after scaffold on `D(s)≤1+D(s')`, produced proof, omitted explicit `h(G)=0`. Corridor shortest-hop `h=5d`, edges cost **at least** 5: learner formed `5d(s)≤5+5d(s')`, but initially treated `c(s,s')=5` rather than `≥5` and did not justify hop-distance inequality. Correct argument: candidate route from s follows edge s→s' then shortest route to goal; `d(s)≤1+d(s')`. Thus `5d(s)≤5+5d(s')≤c(s,s')+5d(s')`. **Retest general proof cold; not mastered.**
- A* closed-set reopening with inconsistent heuristic not consolidated in this window.

## HW2–HW4 learner self-ratings (9 confident, 9 review; not automatic mastery)

| HW | Confident | Needs review |
|---|---|---|
| HW2 | Q1 chain rule/Bayes; Q4 d-separation | Q2 factorisation/inference; Q3 parameter counting; Q5 double marginalisation; Q6 local Markov/exhaustive independences |
| HW3 | Q3 prior/rejection; Q6 transitions | Q1 VE; Q2 enumeration; Q4 likelihood weighting/ESS; Q5 Gibbs |
| HW4 | Q1 stationary; Q2 HMM forward; Q4 PF elapse; Q5 observe/resample; Q6 comparison | Q3 HMM conditional independence |

Recent exercise nuances: HW2 Q1 independent Bayes diagnostic cold pass after prior transcription repair; two chain-rule orderings independently correct. HW2 Q5 numerical eight-row enumeration succeeded procedurally but prior/CPT row alignment slipped. HW3 Q1 remaining-factor multiplication needed a prompt. HW3 Q4 ESS solution understood but independent full ESS computation not verified. HW3 Q5 Gibbs MB and candidate scores mostly correct with arithmetic slip and prompted normalisation. HW4 Q4–Q5 full fresh PF exercise self-reported correct against tutor worked key. Distinguish supplied solution/review from an observed independently written solution.

## Current tutoring workflow and exact next task

Preserve **tabular solution representations** specified in `lesson_logs/aims5701/tutoring_handover_2026_11_15.md`. One meaningful step at a time, avoid giving answer before attempt. Learner may ask for a worked answer after independent completion; don't invalidate that attempt retrospectively.

**Resume HW2 Q2**, fresh manufacturing graph `T→A→D` and `A→V`, all binary. Prompt already posed: `P(T,A,D,V)=?` **Await learner factorisation without hints or answer.** Then proceed on same graph with newly supplied CPTs and tables for numerical marginalisation. Focus four-hour HW2–HW4 consolidation after HW1 proofs. Recheck HW1 general consistency cold before 18 Nov.

## Response calibration
Recent anxious performance in another course's quiz informs exam technique (read requested output, show intermediate working, check all parts, move on from stalls), not a reason to repeatedly discuss anxiety or lower assessment standards. Separate cold independent, guided, independent after repair, and delayed independent evidence.
