# Learning State — Current Handover

_Last maintained: 2026-09-09. Learning evidence through 2026-09-08; this dashboard migration is not a new study session._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` contains the compact evidence projection used by the dashboard; `dashboard/README.md` explains its schema. Use the focused lesson logs to recover detailed demonstrations and fragile points, not the dashboard alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **UCS implementation → A* reconstruction** | BFS independent reconstruction already succeeded. Do not restart BFS or a broad search-theory review. |
| Keep up | **One bounded LangChain/LCEL reconstruction session**, plus a short logic preview | FTEC5660 syntax recognition is ahead of unaided construction. Logic is an AIMS5701 Week-1 gap, not something to leave until all Week-2 work is finished. |
| Protect | **A small relevant maths retrieval block** | Maintain the January AIMS5704 prerequisites, resizing rather than abandoning this lane around project spikes. |

These lanes coexist; they are not one nine-item sequential queue. No calendar slots have been booked by this record.

## Course timing and goals

- MSc Term 1: **7 Sep–4 Dec 2026** in the stored plan.
- **AIMS5701 Fundamentals starts one week later than originally planned** (learner report). Exact revised dates are not independently confirmed. Do not apply the delay to the other courses or infer that every later lecture necessarily shifts unchanged.
- Live Term-1 courses include **FTEC5660**, **AIMS5701** and **AIMS5702**.
- **AIMS5704 Machine Learning Theory starts 11 Jan 2027** in the stored syllabus.
- Aim to remain roughly 1–2 syllabus weeks ahead where practical, build prerequisites before they block learning, and combine existing production engineering experience with mathematical and practical AI/ML competence.
- **FTEC5660 assessment uncertainty:** the learner recalls a hackathon and final project worth roughly 80% combined. Dates, scope and exact weighting still need official confirmation. Treat this as potentially uneven workload, not confirmed deadlines or zero demand.

## Search — continue forward

Source: `lesson_logs/search_reactivation_2026_09_06.md` and original Lessons 24–26.

- **BFS:** independent successful reconstruction is logged after debugging two state-role errors. The solution was intentionally not committed. The skipped practice test remains solution-free for occasional maintenance; do not make it a compulsory immediate repeat.
- **DFS:** traversal understanding and a BFS-to-DFS derivation with LIFO/neighbour-order reasoning are logged. This is not evidence of a separate unaided DFS reconstruction.
- **UCS:** accumulated-cost choices were traced conceptually; implementation is the next new coding step.
- **A*:** historical implementation exists; `g`, `h`, `f=g+h` were recovered. Reconstruct after UCS rather than rereading the old solution.
- **Heuristic/search theory:** admissibility, consistency, completeness and optimality were introduced at introductory depth. Consistency and guarantee assumptions still need consolidation; time/space complexity is not yet systematic.
- **Searching with other agents:** remains new. The exact course scope is unconfirmed; game trees/minimax/alpha-beta is a provisional route only if supported by course materials.

Retain two implementation fragilities: fixed search variable versus moving reconstruction cursor, and graph adjacency versus discovered-state membership. `h(n)` is remaining cost from `n`, not cost of reaching it.

**Immediate session:** build weighted neighbours, priority frontier, accumulated `g`, cheaper-path updates and path reconstruction one decision at a time. Learner writes the important code. Then derive A* using `g+h` and run small path/cost tests.

**Afterwards:** a short guarantees/complexity consolidation; confirm and teach the other-agent branch; one integrated review before AIMS5701 Week 2. Do not allow “single-agent search complete” to imply the whole syllabus line is covered.

## FTEC5660 — taught boundary matters

Sources: `lesson_logs/ftec5660_course_context.md`, `ftec5660_lecture01_introduction.md` and `ftec5660_pattern01_prompt_chaining.md` in `lesson_logs/`.

- Lecture 1 is recorded as completed **2026-09-08**. The **21-pattern catalogue is orientation/reference**, not an enumeration task or 21 mastered concepts. Activate individual patterns after substantive teaching/application.
- **Prompt Chaining is taught:** sequential focused stages, structured/checkable handoffs, deterministic validation/normalisation between LLM stages, context engineering, appropriate use and cost/latency/failure trade-offs are in scope for brief retrieval.
- Expense-ledger anchor: a single prompt produced plausible but wrong totals. The proposed decomposition was **LLM parse → Python compute → LLM explain**. Class reached successful parsing of **120 rows into JSON**; the full pipeline was not completed.
- Encountered syntax: `ChatDeepSeek`, prompt templates, LCEL `|`, string/JSON parsers, `.invoke({...})` and simple sub-chain mapping. **Recognition is ahead of independent reconstruction.** Provider-specific configuration is not the main memorisation target.
- `RunnableLambda` / `RunnablePassthrough` imports do not establish taught use. Later Python compute, full wiring, TaxCalcBench, gates and repair-code sections remain future material.
- Practice this week: a tiny chain, structured output, then two stages with changed examples. Do not hand over finished orchestration code to copy.
- Use the learning lens **lecturer definition → conventional SWE analogue → payments/KYC/AML example → genuine benefit of agenticity → new verification/governance burden**.
- Personal synthesis about decision rights, authoritative constraints, tests/evals, tool authority and operational complexity remains **working hypotheses**, not lecturer-authored conclusions or proven expertise.

## Established foundations and remaining uncertainty

- **Python / NumPy / pandas:** substantial practice in Lessons 01–20 and 27. Python-specific syntax may be less automatic than long-used backend languages. Complexity, recursion/tree fluency and unfamiliar scientific-Python reading still need work.
- **Linear algebra:** completed JHU study is documented in four historical logs. Retrieve the smallest relevant block rather than restarting the course. Fragilities include RREF/free variables, eigen/determinant arithmetic, projections/Gram–Schmidt, normal equations and quadratic-form representation.
- **Probability/statistics:** two completed JHU modules and recovered worked learning cover Bayes, distributions, joint moments, inequalities and CLT/inference. Retrieve conditioning direction/denominators, PDF versus probability, expectation weighting, covariance/correlation and sampling/p-value language. **Markov chains and Poisson are diagnostic-needed**, not failed or proven mastered.
- **Calculus:** slope, differentiation rules, partials, gradients and chain-rule/manual-backprop understanding are historically documented. Keep notation direction, constants, powers and algebra separate from conceptual gaps.
- **Practical ML:** linear/logistic regression and evaluation workflows are implemented. Lesson 31 connects stratified splitting, train-only scaling, tensors/DataLoader, training/validation and held-out evaluation. Code presence alone does not prove unaided authorship or transfer.
- **Practical ML fragilities:** weight orientation, batch/reduction shapes, train-only scaler semantics, loader length versus batch size, accuracy and logit → probability → class.
- **January extensions:** logs/exponentials, likelihood/MLE, exponential families, formal risk/generalisation/concentration, convergence assumptions and proof-style derivations are new work—not historical recall expectations.

## Parked / must return

- **AIMS5701:** logic before W1; full search coverage before W2; decision trees/random forests before W3; Bayes retrieval then graphical-model material before W4; Markov diagnostic before HMM/particle filtering in W5.
- **AIMS5702:** scientific Python/representations before W3; CNN/RNN preview before W4; transfer the real-data workflow to neural regression before W5. Full W6–12 syllabus coverage is restored in `MSC_SYLLABUS_MAP.md`.
- **FTEC5660:** bounded LCEL practice now; later tutorial sections only when actually studied; record assessment dates/weighting when verified.
- **Maths:** selective LA/calculus/probability maintenance; diagnose Poisson separately when relevant; later MLE and formal-theory extensions.
- **Optional, not blockers:** best-validation-checkpoint restoration when teaching model selection; vector/Jacobian calculus when needed.

## Handover discipline

This maintenance pass changes representation and repairs planning coverage, not learning outcomes. After the next substantive session, update its log and this handover, then update only affected evidence dimensions, actions and source-review hashes in `learning_progress.yaml`. Never change an event date to make the dashboard look fresh. Keep historical detail in the logs.
