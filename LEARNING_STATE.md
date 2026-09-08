# Learning State — Current Handover

_Last updated: 2026-09-08_

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals start has been delayed by one week**, creating an extra preparation week before live Fundamentals teaching begins.
- Immediate courses now include **FTEC5660 Agentic AI in Finance/FinTech**, **AIMS5701 Fundamentals in AI**, and **AIMS5702 AI in Practice**.
- **FTEC5660 Lecture 1 completed 2026-09-08.** The course uses 21 agentic design patterns as a major vocabulary/spine and is being taught through finance/fintech workflow automation rather than purely autonomous software engineering.
- FTEC5660 appears **project-heavy**: learner recalls a hackathon + final project accounting for roughly **80% combined**, but exact assessment weighting still needs official verification. Treat the module as a likely source of uneven Term-1 workload spikes.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** where practical, use live FTEC5660 teaching rather than pre-learning all 21 patterns, and keep a protected January-maths continuity lane even when project load spikes.
- Lessons **01–31** all have retrieval logs; historical pre-repo maths is documented separately for calculus, JHU linear algebra and JHU probability/statistics. FTEC5660 live-course context now lives in `lesson_logs/ftec5660_course_context.md` plus per-lecture logs.

## Verified learning position

### FTEC5660 / agentic AI
- Lecture 1 baseline: agentic systems pursue goals, perceive context, reason/plan, act through tools, and learn/escalate with limited supervision.
- Course vocabulary introduced: prompt chaining, routing, parallelization, planning, goal setting/monitoring, tool use, MCP, memory, knowledge retrieval, multi-agent collaboration/communication, reflection, learning/adaptation, reasoning, exploration/discovery, exception handling/recovery, HITL, resource-aware optimisation, guardrails, evaluation/monitoring and prioritization.
- Strong personal learning lens established: place each agentic pattern beside conventional SWE, reinterpret it through cross-border payments/KYC/AML, ask what genuinely benefits from agenticity, then identify the new failure/governance/verification burden.
- Durable working hypotheses recorded in `lesson_logs/ftec5660_course_context.md`: bounded autonomy/decision rights; underspecified human prompts vs authoritative organisational constraints; tests/evals as constraints on agent autonomy; tool discovery vs authority to introduce tools; cheap implementation vs lasting operational complexity; selective rather than blanket agenticity.
- These synthesis points are **working hypotheses**, not lecturer-authored conclusions; later lectures should confirm, refine or reject them.

### Python / DSA / data
- Core Python containers/functions/comprehensions and DSA patterns practised in lessons 01–09.
- NumPy/Pandas foundations substantial (10–20, 27).
- pytest is comfortable and remains useful as learning scaffolding.

### Linear algebra
- JHU Coursera **Linear Algebra from Elementary to Advanced** was completed in 2025; treat this as established prior learning with retrieval due, not a prerequisite to restart.
- Four historical logs preserve the evidenced sequence from systems/vector spaces through eigen/diagonalization, orthogonality/projections/least squares, and symmetric matrices/quadratic forms.
- Current role: **maintenance/application lane**. Use the relevant historical log for detailed fragile points and retrieval prompts.

### Probability / statistics
- Two JHU probability modules were completed in late 2025; the recoverable historical core is established prior learning with retrieval due.
- Strong evidence covers conditional probability/Bayes, random variables/distributions, expectation/variance, joint/marginal distributions, covariance/correlation, Markov/Chebyshev inequalities, CLT, standard error and introductory hypothesis testing/p-values.
- **Evidence boundary:** Markov chains and Poisson are distinctly remembered as studied but lack enough recovered worked evidence to claim current mastery. Diagnose them cold before relying on them.
- Current role: **higher-priority retrieval/application lane**; likelihood/MLE, exponential families and formal generalisation/concentration remain genuine extensions.

### Classical ML
- sklearn logistic regression/classification workflow (21–22) and linear regression (23) implemented.
- Historical least-squares work gives useful geometry underneath regression.
- Linear/logistic regression need consolidation, not first exposure; decision trees/random forests are new.

### Search — reactivation in progress
- BFS, DFS and A* were originally implemented in lessons 24–26.
- **2026-09-06 theory reactivation complete:** BFS/DFS traversal intuition survived; A* `g/h/f` recovered; UCS introduced; admissibility, consistency, completeness and optimality added at course-appropriate introductory depth.
- **2026-09-06 implementation continuation:** BFS was reconstructed incrementally without inspecting the old implementation; DFS was correctly derived from the same skeleton by changing frontier removal to LIFO `pop()` and reasoning about neighbour-order reversal.
- **Independent BFS reconstruction is now complete:** the retained skipped practice test was used successfully without committing the solution. Future BFS reconstruction should be periodic maintenance, not an immediate repeat.
- UCS implementation is the next genuinely new coding step; A* follows as UCS + heuristic priority.
- AIMS5701 Week 2 also includes **“searching with other agents”**, which remains genuinely new. Plan a dedicated adversarial/multi-agent search block after closing UCS/A*; confirm the course framing from lecture materials when available rather than assuming more detail than the syllabus title supports.

### Calculus / optimisation / PyTorch
- Power/product rules, partial derivatives, gradients, chain rule and manual backprop understood.
- Autograd/manual GD (28), standard linear training loop (29), synthetic binary MLP (30) and real-data classification workflow (31) implemented.
- Lesson 31 includes stratified train/validation/test splitting, train-only scaling, tensor/DataLoader preparation, MLP training/validation and held-out evaluation; verified tests/dashboard passed on 2026-09-04.

## Fragile under cold recall

- **FTEC5660:** exact retrieval of the 21-pattern vocabulary is new; prioritise conceptual grouping and examples over list-order memorisation. Keep course material separate from personal synthesis when recalling.
- **Linear algebra:** procedural details around RREF/free variables, determinant/eigen arithmetic, Gram–Schmidt/projections, least-squares equations and quadratic-form representation. See `lesson_logs/historical_linear_algebra_*.md`.
- **Probability/statistics:** Bayes conditioning direction/denominator, PDF vs probability, expectation weighting, covariance vs correlation, CLT/sampling-distribution interpretation and p-value language. Markov chains/Poisson are diagnostic-needed. See `lesson_logs/historical_probability_statistics_*.md`.
- **Practical ML/tensors:** `nn.Linear` weight orientation, batch/reduction shapes, train-only scaler semantics, loader length vs batch size, binary accuracy and logit → probability → class distinction.
- **Search:** keep variable roles explicit during path reconstruction; keep graph adjacency separate from discovered-state membership; UCS/A* implementation remains to be demonstrated; theory fragilities remain `h(n)` semantics, consistency and guarantee assumptions.

## Active highest-value sequence

1. **UCS implementation** — weighted neighbours, priority queue, accumulated `g`, `cost_so_far`, cheaper-path updates and path reconstruction.
2. **A* reconstruction** — derive directly from UCS by adding heuristic priority `g+h` rather than rereading the old implementation.
3. **Search theory consolidation** — short re-test of completeness/optimality/admissibility/consistency plus time/space complexity and assumptions where useful.
4. **Searching with other agents** — dedicated new-material block before the delayed Week-2 lecture. If the course means standard adversarial search, build game-tree intuition → minimax → alpha-beta pruning; use actual course materials to confirm scope when available.
5. **Integrated pre-lecture search review** — choose/trace algorithms across unweighted, weighted, heuristic and multi-agent scenarios; do not repeat full BFS drilling.
6. **FTEC5660 live-course loop** — after each lecture, short cold recall of taught material + 2–3 personal-synthesis prompts; connect to one payments/KYC/AML example. Do not pre-study all 21 patterns by default.
7. **Then use remaining buffer** for Week-1 logic/reasoning and the Week-3 decision-tree/random-forest gap.
8. **Probability runway for Weeks 4–5 + January** — short Bayes/random-variable retrieval; diagnose Markov chains/Poisson before HMM/particle-filtering work; then extend toward likelihood/MLE. Preserve this lane through FTEC5660 project spikes, even if temporarily reduced.

# PARKED / MUST RETURN

- [~] **BFS / DFS / A\*** — BFS independent reconstruction complete; DFS mechanics derived; A* reconstruction follows UCS.
- [~] **UCS** — concept introduced and traced correctly; implementation is next.
- [~] **Search guarantees / heuristic theory** — admissibility, consistency, completeness and optimality introduced; consolidate after implementation and attach assumptions carefully.
- [ ] **Searching with other agents** — AIMS5701 Week 2; genuinely new. Confirm exact lecture scope, likely adversarial/game-tree search if course materials support that interpretation.
- [~] **FTEC5660 pattern spine** — Lecture 1 introduced 21 patterns; learn them through live course/project use rather than front-loading the full list. Course context + Lecture 1 cold-recall prompts now exist.
- [ ] **FTEC5660 hackathon / final-project planning** — dates, scope and exact assessment weighting still need official confirmation; add explicit weekly capacity plan once known.
- [ ] **Logic/reasoning** — Fundamentals Week 1 preview; extra start-delay runway means this can follow the core search implementation work without being rushed.
- [ ] **Decision trees / random forests** — Fundamentals Week 3.
- [x] **Real-data PyTorch classification** — Lesson 31 complete; best-validation-checkpoint restoration is optional continuation work.
- [~] **Historical linear algebra retrieval** — established and documented; retrieve in short targeted blocks rather than relearn from zero.
- [~] **Historical probability/statistics retrieval** — core foundation established; Markov chains and Poisson require diagnostics before being treated as current.
- [ ] **Likelihood / log-likelihood / MLE** — extend historical probability/statistics for AIMS5704.
- [ ] **NN regression / housing-price workflow** — AI in Practice Week 5.
- [ ] **CNN/RNN architecture preview** — AI in Practice Week 4.
- [ ] **Formal complexity / graph-tree DSA** — reinforce around search.
- [ ] **Vector/Jacobian calculus** — defer until needed.

## Near-term syllabus runway

### FTEC5660
- Lecture 1 complete: retrieve agent definition/loop, pattern purpose, 21-pattern grouping and complexity levels.
- Use prior payments/KYC/AML experience as a domain anchor rather than memorising abstract pattern names.
- Project load is likely substantial; once hackathon/final-project dates are confirmed, explicitly rebalance weekly preparation around them.
- Preserve the distinction between **course material** and **personal working hypotheses** in future logs.

### Fundamentals
- **Start delayed by one week:** use the added runway to close single-agent search implementation/theory and begin the untouched “searching with other agents” branch before it appears live.
- W1: introduction, logic, reasoning, learning → logic remains unfamiliar; preview after the immediate UCS/A* implementation block rather than displacing it.
- W2: uninformed/informed/searching with other agents → BFS/DFS reactivated; UCS/A* implementation next; guarantees/complexity consolidation after; multi-agent/adversarial branch still new.
- W3: linear/logistic regression, decision trees, random forests → first two practised; trees/forests are the gap.
- W4: Bayesian networks/inference/sampling → historical Bayes/probability foundation exists; reactivate, then learn graphical-model semantics/inference.
- W5: HMMs/particle filtering → diagnose Markov-chain recall before relying on it.

### AI in Practice
- W1–2: simple ML + vector/matrix/tensor/NumPy → strong preparation; historical JHU LA makes the matrix layer retrieval/application rather than first exposure.
- W3: representations + SciPy/matplotlib/PyTorch → PyTorch base strong; plotting/SciPy not systematic.
- W4: MLP/CNN/RNN → MLP ahead; CNN/RNN pending.
- W5: housing-price prediction → transfer Lesson 31's preprocessing/validation discipline to regression.

### ML Theory — January risk lane
- Linear algebra and core probability/statistics are established historical foundations with retrieval due.
- Larger new gaps: likelihood/log-likelihood/MLE/exponential-family notation, formal risk/generalisation/concentration, convergence assumptions and proof-style derivations.
- GD/backprop mechanics are an advantage.
- FTEC5660 project spikes may reduce available preparation hours; protect continuity rather than demanding a fixed weekly volume.

## Next session target

> **Continue directly into UCS implementation.** Do not repeat the BFS practice or restart broad theory retrieval. Build weighted neighbours, priority frontier, accumulated `g` and cheaper-path updates incrementally; then derive A* as `g+h`.

For the next FTEC5660 lecture, use `lesson_logs/ftec5660_lecture01_introduction.md` for a short cold recall rather than rereading the whole slide deck.

## End-of-session update

- **FTEC5660 now live:** Lecture 1 completed and recorded with separate course-material vs personal-synthesis recall.
- **Course planning change:** FTEC5660 is now visible as a project-heavy Term-1 workload source; hackathon/final-project exact dates and weighting remain to verify.
- **Learning-method change:** use the conventional-SWE + payments/KYC/AML side-by-side lens to make agentic patterns durable.
- **Long-range constraint preserved:** January ML-Theory maths preparation remains a protected continuity lane even when FTEC5660 project load rises.
- **Immediate next:** UCS implementation, then A* reconstruction.
