# Learning State — Current Handover

_Last maintained: 2026-09-09. Learning evidence through 2026-09-09._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson logs remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **UCS implementation → A* reconstruction** | BFS independent reconstruction already succeeded. Do not restart BFS or broad search theory. |
| Parallel | **Resume LCEL at sub-chain mapping**, then create a small pytest-driven reconstruction exercise; also keep a short AIMS5701 logic preview | The 9 Sep session moved LCEL from recognition into guided construction, but independent reconstruction is still pending. |
| Protect | **A small relevant maths retrieval block** | Keep January AIMS5704 prerequisites alive even if live-course/project workload changes. |

These lanes coexist; they are not one sequential queue.

## Course timing / planning uncertainty

- MSc Term 1 is recorded as **7 Sep–4 Dec 2026**.
- **AIMS5701 Fundamentals** is reported to start one week later than originally planned; exact revised dates are not independently confirmed.
- **AIMS5704 Machine Learning Theory** starts **11 Jan 2027** in the stored syllabus.
- FTEC5660 remains a live learning source, but continued enrolment is now uncertain because the learner may be unable to commit to the hackathon final/pitch day. Do not let that uncertainty erase useful agentic-AI learning, but if the module is dropped then course-specific FTEC syntax/project preparation should lose priority relative to AIMS5701/AIMS5702 and January maths.
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

## FTEC5660 / LangChain — current taught boundary

Sources: `lesson_logs/ftec5660_pattern01_prompt_chaining.md` and `lesson_logs/ftec5660_lcel_guided_practice_2026_09_09.md`.

### Prompt chaining concept

- Stable sequential stages, structured/checkable handoffs, deterministic validation/normalisation between LLM stages, context engineering, and cost/latency/failure trade-offs are taught.
- Expense-ledger anchor remains **LLM parse → Python compute → LLM explain**; class reached successful parsing of 120 rows into JSON, not the full pipeline.
- The 21-pattern catalogue remains orientation/reference, not a recall backlog.

### LCEL guided practice — 9 Sep

The learner completed a short taught syntax session in an ignored local `scratch.py` file.

Now demonstrated with guidance:

- `ChatPromptTemplate.from_template(...)` as a reusable prompt with named placeholders;
- build-time chain composition versus run-time invocation;
- LCEL `prompt | llm | parser` data flow;
- `StrOutputParser()` → Python string;
- `JsonOutputParser()` → parsed Python dict/list depending on JSON shape;
- `.invoke({"payment": payment_text})` and matching invocation keys to template placeholders;
- construction of a plain-string payment chain and a JSON payment chain with guidance.

Observed support needs were mostly API/object-role slips: function vs function call (`build_payment_prompt` vs `build_payment_prompt()`), passed model object vs calling `llm()`, and parser class vs parser instance (`StrOutputParser` vs `StrOutputParser()`). Treat these as syntax/API fluency gaps, not conceptual failure.

**Pause point:** sub-chain mapping was introduced but not implemented. Resume directly at a shape such as:

```text
{"flag": extract_chain}
    -> prompt expecting {flag}
    -> llm
    -> parser
```

Then create a tracked pytest-driven exercise/implementation pair using changed examples and deterministic/fake model components where practical. Do not mark LCEL independent until the learner can reconstruct the small grammar without this level of guidance.

Still outside the fair boundary: substantive `RunnableLambda`, `RunnablePassthrough`, full ledger compute/explain wiring, gates/repair loops, TaxCalcBench and later notebook abstractions.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice in Lessons 01–20 and 27. Python/API syntax can still be less automatic than long-used backend languages.
- **Linear algebra:** historical JHU foundation established; retrieve small relevant blocks rather than restart. Fragilities include RREF/free variables, eigen/determinant arithmetic, projections/Gram–Schmidt, normal equations and quadratic forms.
- **Probability/statistics:** Bayes, distributions, joint moments, inequalities and CLT/inference have strong historical evidence. Markov chains and Poisson remain diagnostic-needed rather than proven current mastery.
- **Calculus:** slope → derivatives → partials → gradients → chain rule/backprop is historically established; keep notation/algebra slips separate from conceptual gaps.
- **Practical ML:** linear/logistic regression and the Lesson 31 train/validation/test workflow are implemented. Transfer ability should be tested on changed tasks rather than inferred from code.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain genuinely new work.

## Parked / must return

- **AIMS5701:** light logic preview before W1; finish search before W2; trees/random forests before W3; Bayes retrieval before W4; Markov diagnostic before W5.
- **AIMS5702:** scientific-Python/representation work before W3; CNN/RNN preview before W4; transfer the real-data workflow to neural regression before W5.
- **FTEC5660:** resume LCEL at sub-chain mapping; then one small independent pytest-driven reconstruction. Reassess course-specific priority if enrolment changes.
- **Maths:** selective LA/calculus/probability maintenance; later MLE and formal-theory extensions.

## Handover discipline

After the next substantive session, update its focused log and this handover. Update `learning_progress.yaml` only when a structured evidence dimension/action materially changes; guided work does not automatically become independent performance. Historical detail belongs in logs, not this file.
