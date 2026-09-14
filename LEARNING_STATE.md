# Learning State — Current Handover

_Last maintained: 2026-09-14. Learning evidence through 2026-09-14._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **FTEC5660 Lesson 34 implementation practice** | Agentic AI resumed 14 Sep. Work through the new stateful-LCEL tests: deterministic route → validation gate → extraction → `assign`/`RunnableLambda` pipeline. |
| Parallel | **AIMS5702 representation translation + light tensor maintenance** | Shape reasoning remains the anchor; train diagram ↔ shapes ↔ indices ↔ PyTorch when course work resumes. |
| Protect | **Search theory + a small relevant maths retrieval block** | Search implementation is complete through Lesson 33 but guarantees/complexity remain due; keep January AIMS5704 prerequisites alive without a broad restart. |

These lanes coexist; they are not one sequential queue.

## FTEC5660 / LangChain — resumed 14 Sep

Sources: `lesson_logs/lesson32_lcel_basics.md`, `lesson_logs/ftec5660/tutorial01_study_plan.md`, and `lesson_logs/ftec5660/lesson34_stateful_lcel_2026_09_14.md`.

### Lesson 32 cold retrieval

The short resume check worked as intended rather than replaying the whole lesson.

**Retrieved cold:**

- conceptual `prompt template -> model -> output parser` pipeline;
- `JsonOutputParser()` produces Python structured data / dict for object JSON;
- `.invoke({...})` runtime input mapping;
- two-stage mapping with `{"risk_summary": extract_chain}`. This is stronger evidence than on 9 Sep, when the mapping required conceptual support.

**Still fragile:**

- builder call vs function object (`from_template` vs `from_template(...)`);
- parser class vs instance (`StrOutputParser` vs `StrOutputParser()`);
- `Task -> Input -> Constraints -> Output structure` was not cold-recalled and needed reactivation.

Do not replay Lesson 32 again; sample these fragilities later with changed examples.

### Lesson 34 new concepts — guided, implementation pending

#### `RunnablePassthrough.assign`

Mental model:

> Preserve the current state dictionary and add a runnable's result under a named key.

The learner successfully traced nested/enriched state and understood the distinction between independent enrichments in one `assign` and dependent sequential assignments. Important correction retained: `|` means sequential runnable stages, not necessarily sequential LLM calls.

#### `RunnableLambda`

Mental model:

> Adapt ordinary deterministic Python into an LCEL runnable stage.

The learner correctly preferred deterministic Python for an exact threshold rule and implemented the underlying route function after one output-contract correction (`True/False` initially, then required `MANUAL_REVIEW`/`STANDARD`).

#### Validation gates

Contract:

```text
valid state   -> return same state unchanged
invalid state -> fail loudly
```

The learner understood why downstream code should only receive state that passed the contract, why a successful gate must return state rather than `None`, and why validation should not silently repair/coerce malformed LLM output. Their explanation emphasized single responsibility and avoiding assumptions about producer intent.

Python syntax in the first validator attempt was rusty (`&&`, `isinstance` syntax, nesting), so implementation evidence is still pending.

### Practice now queued

Files created on the current practice branch:

- `agentic_ai/langchain/lesson34_stateful_lcel_practice.py` — learner scaffold only;
- `agentic_ai/langchain/test_lesson34_stateful_lcel_practice.py` — sequential practice tests.

Work through tests in order:

1. deterministic `determine_review_route`;
2. valid-state gate returns the identical state;
3. malformed extraction fails fast;
4. structured extraction chain;
5. complete stateful pipeline preserving input + adding `extracted` + validated deterministic `review_route`;
6. low-value route case;
7. malformed LLM extraction fails before routing.

Do not provide the finished implementation up front. Use the normal hint ladder and let the learner own the orchestration.

### Current evidence boundary

`RunnablePassthrough.assign`, `RunnableLambda`, and validation gates are **new guided concepts**, not independently implemented yet. Architectural reasoning is promising; implementation/tests will determine whether they transfer into executable LCEL.

## AIMS5702 — current state

Sources: `lesson_logs/aims5702/lecture01_02_prelecture_bridge.md` and `lesson_logs/aims5702/tensor_cold_review_2026_09_11.md`.

- Shape reasoning remains the primary anchor; index/diagram fluency should be trained as translation, not replacement.
- 11 Sep tensor review found strong broadcasting/reduction/semantic-shape reasoning with slicing/API rust that recovered quickly.
- `keepdim=True` and tuple-dimension reductions were newly introduced on 11 Sep.
- dtype memory, flat storage, stride/view/contiguity and basic einsum remain guided pre-read material rather than Lecture 1-covered material.
- Next substantive course review should train actual Lecture 1 diagram -> shape -> parameter-count -> index/PyTorch translation.

## Search — implementation complete through Lesson 33, theory due

- BFS has strongest current independent evidence.
- DFS was reconstructed with refreshed/guided evidence.
- UCS/A* are implemented with passing practice tests but remain guided rather than cold-independent.
- Next search block: completeness/optimality, UCS non-negative-cost assumptions, A* admissibility vs consistency, goal popped vs discovered, and qualitative/formal complexity.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice; syntax/API fluency can be less automatic than the learner's long-used backend languages. Today's `&&`/`isinstance` validator slips fit this boundary rather than indicating an architectural misunderstanding.
- **Linear algebra:** historical JHU foundation established; retrieve selectively.
- **Probability/statistics:** strong historical evidence across major foundations; Markov chains/Poisson remain diagnostic-needed.
- **Calculus:** historical derivative/gradient/chain-rule/backprop foundation established.
- **Practical ML:** linear/logistic regression and train/validation/test workflow implemented; changed-task transfer still useful.
- **Agentic/LCEL:** Lesson 32 basics now partly cold-retrievable; stateful composition/gates are the active new implementation target.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain new work.

## Parked / must return

- **FTEC5660:** active now. Finish Lesson 34 tests before moving deeper into the Tutorial 1 architecture or routing.
- **AIMS5701/search:** guarantees/complexity still due after the current Agentic AI block.
- **AIMS5702:** representation translation remains the next substantive course-specific review target.
- **Maths:** selective LA/calculus/probability maintenance; later MLE/formal-theory extensions.

## Handover discipline

After the Lesson 34 tests are complete, update `lesson_logs/ftec5660/lesson34_stateful_lcel_2026_09_14.md` and this handover with independent/guided implementation evidence. Update `learning_progress.yaml` only if the structured dashboard state materially changes; merely creating the practice scaffold does not establish implementation mastery.
