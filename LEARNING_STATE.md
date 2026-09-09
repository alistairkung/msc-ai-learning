# Learning State — Current Handover

_Last maintained: 2026-09-09. Learning evidence through 2026-09-09._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson logs remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **UCS implementation → A* reconstruction** | BFS independent reconstruction already succeeded. Do not restart BFS or broad search theory. |
| Parallel | **LCEL Lesson 32 complete for now; later do one short cold reconstruction**, plus a short AIMS5701 logic preview | Changed-example LCEL tests now pass, but two-stage composition needed guidance and should not be labelled independent yet. |
| Protect | **A small relevant maths retrieval block** | Keep January AIMS5704 prerequisites alive even if live-course/project workload changes. |

These lanes coexist; they are not one sequential queue.

## Course timing / planning uncertainty

- MSc Term 1 is recorded as **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals** is reported to start one week later than originally planned; exact revised dates are not independently confirmed.
- **AIMS5704 Machine Learning Theory** starts **11 Jan 2027** in the stored syllabus.
- FTEC5660 remains a live learning source, but continued enrolment is uncertain because the learner may be unable to commit to the hackathon final/pitch day. Do not let that uncertainty erase useful agentic-AI learning, but if the module is dropped then course-specific FTEC syntax/project preparation should lose priority relative to AIMS5701/AIMS5702 and January maths.
- The learner recalls a hackathon and final project worth roughly 80% combined; dates/scope/exact weighting still need official confirmation.

## Search — continue forward

Source: `lesson_logs/search_reactivation_2026_09_06.md` and Lessons 24–26.

- **BFS:** independent successful reconstruction logged after debugging two state-role errors; retained solution-free practice test is for occasional maintenance only.
- **DFS:** traversal/LIFO reasoning and a guided BFS→DFS derivation are logged; no separate unaided DFS reconstruction is claimed.
- **UCS:** accumulated-cost reasoning is taught; implementation remains the next coding step.
- **A\*:** historical implementation exists; `g`, `h`, `f=g+h` were recovered. Reconstruct after UCS.
- **Theory:** admissibility, consistency, completeness and optimality are introduced; consistency/guarantee assumptions and complexity still need consolidation.
- **Searching with other agents:** still new; exact course framing remains unconfirmed.

Retain two implementation fragilities: fixed search variable versus moving reconstruction cursor, and graph adjacency versus discovered-state membership. `h(n)` is remaining cost from `n`, not cost of reaching it.

**Next search session:** weighted neighbours → priority frontier → accumulated `g` → cheaper-path updates → path reconstruction. Learner writes the important implementation. Then derive A* using `g+h`.

## FTEC5660 / LangChain — Lesson 32 complete for now

Sources: `lesson_logs/ftec5660_pattern01_prompt_chaining.md`, `lesson_logs/ftec5660_lcel_guided_practice_2026_09_09.md`, and `lesson_logs/lesson32_lcel_basics.md`.

### Prompt chaining concept

- Stable sequential stages, structured/checkable handoffs, deterministic validation/normalisation between LLM stages, context engineering, and cost/latency/failure trade-offs are taught.
- Expense-ledger anchor remains **LLM parse → Python compute → LLM explain**; class reached successful parsing of 120 rows into JSON, not the full pipeline.
- The 21-pattern catalogue remains orientation/reference, not a recall backlog.

### LCEL implementation — 9 Sep

A tracked Lesson 32 implementation/test pair now exists under `agentic_ai/langchain/`. The learner completed changed-example pytest exercises using `FakeListChatModel` rather than real API calls.

Implemented and tested:

- `ChatPromptTemplate.from_template(...)` with named placeholders;
- `prompt | llm | StrOutputParser()`;
- `prompt | llm | JsonOutputParser()`;
- invocation dictionaries matching prompt placeholders;
- free-text risk extraction into a Python dict;
- a two-stage chain mapping an earlier extraction chain into a named input for a recommendation prompt.

The first prompt/chain exercises transferred cleanly. The recurring fragility was **function object vs function call** (`builder` vs `builder()`), with similar taught-pass slips around parser class vs instance and passed `llm` object vs `llm()`. The learner's intended LCEL composition was generally correct; treat these as Python/API fluency rust rather than a conceptual LCEL failure.

Two-stage mapping required conceptual support before the learner successfully implemented the passing version. Therefore **do not mark LCEL independent yet**. The next evidence step is one short changed-domain cold reconstruction later, not another full lesson now.

### Prompt-design retrieval target

The learner explicitly wants this four-part checklist cold-retrievable:

```text
Task
Input
Constraints
Output structure
```

Future retrieval should test transfer by giving a vague prompt and asking the learner to improve it using the four dimensions, rather than only asking for list recitation.

Still outside the fair boundary: substantive `RunnableLambda`, `RunnablePassthrough`, full ledger compute/explain wiring, gates/repair loops, TaxCalcBench and later notebook abstractions.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice in Lessons 01–20 and 27. Python/API syntax can still be less automatic than long-used backend languages; Lesson 32 exposed recurring bare-function-name invocation slips.
- **Linear algebra:** historical JHU foundation established; retrieve small relevant blocks rather than restart. Fragilities include RREF/free variables, eigen/determinant arithmetic, projections/Gram–Schmidt, normal equations and quadratic forms.
- **Probability/statistics:** Bayes, distributions, joint moments, inequalities and CLT/inference have strong historical evidence. Markov chains and Poisson remain diagnostic-needed rather than proven current mastery.
- **Calculus:** slope → derivatives → partials → gradients → chain rule/backprop is historically established; keep notation/algebra slips separate from conceptual gaps.
- **Practical ML:** linear/logistic regression and the Lesson 31 train/validation/test workflow are implemented. Transfer ability should be tested on changed tasks rather than inferred from code.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain genuinely new work.

## Parked / must return

- **AIMS5701:** light logic preview before W1; finish search before W2; trees/random forests before W3; Bayes retrieval before W4; Markov diagnostic before W5.
- **AIMS5702:** scientific-Python/representation work before W3; CNN/RNN preview before W4; transfer the real-data workflow to neural regression before W5.
- **FTEC5660:** Lesson 32 is enough LCEL syntax work for now; later run one short cold reconstruction and reassess course-specific priority if enrolment changes.
- **Maths:** selective LA/calculus/probability maintenance; later MLE and formal-theory extensions.

## Handover discipline

After the next substantive session, update its focused log and this handover. Update `learning_progress.yaml` only when a structured evidence dimension/action materially changes. Lesson 32 adds richer guided implementation evidence but does not yet justify changing LCEL from `performance: guided` to `independent`. Historical detail belongs in logs, not this file.
