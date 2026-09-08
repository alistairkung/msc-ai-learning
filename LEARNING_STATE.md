# Learning State — Current Handover

_Last updated: 2026-09-08_

> Update this file at the end of **every study session**. Keep it short. It should answer: **Where am I now, what is fragile, what is parked, and what should happen next?**

## Current phase

- MSc Term 1: **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals start has been delayed by one week**, creating an extra preparation week before live Fundamentals teaching begins.
- Immediate courses now include **FTEC5660 Agentic AI in Finance/FinTech**, **AIMS5701 Fundamentals in AI**, and **AIMS5702 AI in Practice**.
- **FTEC5660 Lecture 1 completed 2026-09-08.** The introductory catalogue of 21 agentic design patterns is an overview/reference map, not a list-recall target from the introduction.
- **Pattern 1: Prompt Chaining has now been substantively taught.** Concept coverage includes decomposition into sequential focused stages, explicit/checkable handoffs, deterministic validation/normalisation between LLM stages, context engineering, when chaining is/is not appropriate, and latency/cost/failure trade-offs.
- The accompanying LangChain tutorial was only **partially completed in class**: setup/basic LCEL was introduced and the expense-ledger chain reached a successful LLM parse into structured JSON. Later notebook sections (Python compute, `RunnablePassthrough.assign`, full chain wiring, TaxCalcBench, gates, etc.) are **not yet taught/mastered** merely because they exist in the supplied notebook.
- FTEC5660 is being taught through finance/fintech workflow automation rather than purely autonomous software engineering.
- FTEC5660 appears **project-heavy**: learner recalls a hackathon + final project accounting for roughly **80% combined**, but exact assessment weighting still needs official verification. Treat the module as a likely source of uneven Term-1 workload spikes.
- **Machine Learning Theory (AIMS5704)** starts **11 Jan 2027**; probability/statistics/LA preparation must run during Term 1.
- Strategy: stay roughly **1–2 syllabus weeks ahead** where practical, let live FTEC5660 lectures/projects determine which individual patterns become retrieval targets, and keep a protected January-maths continuity lane even when project load spikes.
- Lessons **01–31** all have retrieval logs; historical pre-repo maths is documented separately for calculus, JHU linear algebra and JHU probability/statistics. FTEC5660 live-course context now lives in `lesson_logs/ftec5660_course_context.md` plus focused lecture/pattern logs.

## Verified learning position

### FTEC5660 / agentic AI
- Lecture 1 baseline: agentic systems pursue goals, perceive context, reason/plan, act through tools, and learn/escalate with limited supervision.
- Lecture 1 showed a broad catalogue spanning prompt chaining, routing, parallelisation, planning, goal setting/monitoring, tool use, MCP, memory, knowledge retrieval, multi-agent collaboration/communication, reflection, learning/adaptation, reasoning, exploration/discovery, exception handling/recovery, HITL, resource-aware optimisation, guardrails, evaluation/monitoring and prioritisation.
- **Retrieval boundary for the catalogue:** it was introductory orientation, not 21 concepts taught in depth. Do not quiz enumeration. Add individual patterns to cold recall only after later lectures/projects teach or apply them substantively.
- **Prompt chaining is now an active retrieval topic.** Core concept: split a complex task into stable, focused, checkable stages; pass outputs forward; use structured interfaces and deterministic processing/validation where appropriate rather than making every stage an LLM call.
- Expense-ledger tutorial anchor: a single prompt produced plausible but wrong totals; the decomposition proposed `LLM parse -> Python compute -> LLM explain`. Class reached the first step and successfully parsed 120 ledger rows into JSON.
- LangChain syntax encountered so far: `ChatDeepSeek`, `ChatPromptTemplate.from_template(...)`, LCEL `|`, `StrOutputParser()`, `JsonOutputParser()`, `.invoke({...})`, and mapping an earlier sub-chain into a later prompt variable. **Recognition is ahead of independent reconstruction.**
- `RunnableLambda` / `RunnablePassthrough` were imported in the notebook but their substantive tutorial sections had not yet been reached in class; do not test them as learned syntax yet.
- Strong personal learning lens established: place newly taught agentic patterns beside conventional SWE, reinterpret them through cross-border payments/KYC/AML, ask what genuinely benefits from agenticity, then identify the new failure/governance/verification burden.
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

- **FTEC5660 Prompt Chaining concept:** make sure the value of chaining is not reduced to “more prompts”; retrieve checkable boundaries, deterministic processing, structured interfaces, context engineering and trade-offs.
- **FTEC5660 LangChain syntax:** currently familiar from guided tutorial but **not yet independently reconstructable**. This week practise `ChatPromptTemplate`, `|`, parsers, `.invoke()` and sub-chain mapping from a blank file using changed examples.
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
6. **This week: one focused LangChain syntax reconstruction session** — use `lesson_logs/ftec5660_pattern01_prompt_chaining.md`; build from tiny `prompt -> llm -> parser` pieces, then a two-stage chain, from memory. Use a changed finance/payments example rather than copying tutorial code.
7. **FTEC5660 live-course loop** — after each lecture, short cold recall of concepts actually taught + 2–3 personal-synthesis prompts; connect to one payments/KYC/AML example. Promote individual patterns into retrieval only when they have been substantively covered.
8. **Then use remaining buffer** for Week-1 logic/reasoning and the Week-3 decision-tree/random-forest gap.
9. **Probability runway for Weeks 4–5 + January** — short Bayes/random-variable retrieval; diagnose Markov chains/Poisson before HMM/particle-filtering work; then extend toward likelihood/MLE. Preserve this lane through FTEC5660 project spikes, even if temporarily reduced.

# PARKED / MUST RETURN

- [~] **BFS / DFS / A\*** — BFS independent reconstruction complete; DFS mechanics derived; A* reconstruction follows UCS.
- [~] **UCS** — concept introduced and traced correctly; implementation is next.
- [~] **Search guarantees / heuristic theory** — admissibility, consistency, completeness and optimality introduced; consolidate after implementation and attach assumptions carefully.
- [ ] **Searching with other agents** — AIMS5701 Week 2; genuinely new. Confirm exact lecture scope, likely adversarial/game-tree search if course materials support that interpretation.
- [~] **FTEC5660 pattern overview** — Lecture 1 showed the catalogue as orientation to later course coverage. Reference only; individual patterns become active retrieval topics as taught.
- [~] **FTEC5660 Pattern 1: Prompt Chaining** — concept now taught and fair for cold recall; tutorial reached successful JSON parsing.
- [ ] **LangChain/LCEL syntax reconstruction** — **do this this week**. Independently reproduce the syntax taught up to the JSON-parser boundary: prompt templates, pipe composition, parsers, invocation dictionary and simple sub-chain mapping. Do not jump ahead to `RunnablePassthrough`/full tutorial wiring until this base grammar is durable.
- [ ] **Finish later Prompt Chaining tutorial sections** — Python compute, complete chain wiring and later benchmark/gating sections remain future material; do not mark them complete from notebook availability alone.
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
- Lecture 1 introduction complete: retain agent definition/loop, why agentic systems need structure, complexity levels and the finance-workflow framing.
- **Pattern 1 Prompt Chaining is now substantively covered:** retrieve decomposition, checkable/structured stage boundaries, deterministic processing between stages, when to use/not use chaining, context engineering and risks/trade-offs.
- **Tutorial boundary matters:** class reached successful JSON parsing in the expense-ledger decomposition. Do not assume later notebook code has been learned.
- Schedule a LangChain syntax-reconstruction session this week so `ChatPromptTemplate`, LCEL `|`, parsers and `.invoke()` can be produced rather than merely recognised.
- Use prior payments/KYC/AML experience as a domain anchor when reconstructing examples.
- Project load is likely substantial; once hackathon/final-project dates are confirmed, explicitly rebalance weekly preparation around them.
- Preserve the distinction between **course material**, **tutorial progress**, and **personal working hypotheses** in future logs.

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

Also reserve one separate block **this week** for the Prompt Chaining/LangChain syntax reconstruction; it does not need to displace the immediate UCS continuation.

## End-of-session update

- **FTEC5660 Pattern 1 activated:** Prompt Chaining has now been taught in depth enough to become a retrieval topic.
- **Tutorial boundary recorded:** class stopped after successful expense-ledger parsing into JSON; later notebook cells are future material.
- **New this-week learning debt:** independently reconstruct the LangChain/LCEL syntax already encountered, using the same small-step retrieval approach used for NumPy.
- **Immediate implementation priority unchanged:** UCS, then A* reconstruction.
- **Long-range constraint preserved:** January ML-Theory maths preparation remains a protected continuity lane even when FTEC5660 work rises.
