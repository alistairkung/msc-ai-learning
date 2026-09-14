# Learning State — Current Handover

_Last maintained: 2026-09-14. Learning evidence through 2026-09-14._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **FTEC5660 Tutorial 1 architecture → routing bridge** | Lesson 34 stateful LCEL implementation is green. Consolidate contracts/state/failure localisation, then continue toward generated-code architecture and routing rather than adding syntax for its own sake. |
| Parallel | **AIMS5702 representation translation + light tensor maintenance** | Shape reasoning remains the anchor; train diagram ↔ shapes ↔ indices ↔ PyTorch when course work resumes. |
| Protect | **Search theory + a small relevant maths retrieval block** | Search implementation is complete through Lesson 33 but guarantees/complexity remain due; keep January AIMS5704 prerequisites alive without a broad restart. |

These lanes coexist; they are not one sequential queue.

## FTEC5660 / LangChain — Lesson 34 implemented 14 Sep

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

### Lesson 34 — stateful LCEL implementation complete

The learner worked sequentially through the new practice suite and reported **all tests green**.

Implemented:

```text
determine_review_route
validate_extraction
build_extraction_chain
build_payment_pipeline
```

Final architecture:

```text
initial {payment_note}
    ↓
RunnablePassthrough.assign(extracted = LLM extraction)
    ↓
{payment_note, extracted}
    ↓
RunnableLambda(validate_extraction)
    ↓
{payment_note, extracted}       # unchanged but validated
    ↓
RunnablePassthrough.assign(review_route = deterministic Python)
    ↓
{payment_note, extracted, review_route}
```

#### `RunnablePassthrough.assign`

Current mental model:

> Preserve the current state dictionary and add a runnable's result under a named key.

The learner understands independent enrichments can share an incoming state in one assign, while dependent enrichments need sequential stages so the later runnable sees earlier enriched state.

#### `RunnableLambda`

Current mental model:

> Adapt ordinary Python into a runnable that LCEL can invoke with runtime state.

The learner correctly chose deterministic Python for exact threshold policy rather than spending another LLM call on exact computation.

#### Validation gates

Current model:

```text
valid state   -> return same state unchanged
invalid state -> fail loudly
```

The learner implemented required-key/type/value checks, repaired missing-key handling after a test exposed `KeyError`, and correctly rejected a string `"15000"` where numeric amount was required.

They also articulated why validation should not silently repair/coerce malformed model output: it violates single responsibility and assumes producer intent. An explicit repair path should be separate if desired.

### Support / fragilities during implementation

The overall three-stage architecture was chosen correctly by the learner, but implementation still needed targeted support for:

- `build_extraction_chain(llm)` builder invocation;
- `RunnableLambda(determine_review_route)` callable vs `determine_review_route()` immediate invocation;
- prompt output fields/types matching downstream validator/Python contracts;
- required-key checks before dictionary value access.

Callable timing (`fn` vs `fn()`) remains the clearest recurring Python/LCEL fragility. Keep this as a short future changed-example probe.

### Post-green conceptual synthesis

Immediate state tracing was correct:

```text
{payment_note}
-> {payment_note, extracted}
-> {payment_note, extracted}       # gate
-> {payment_note, extracted, review_route}
```

The learner then articulated an important interface model:

- `{placeholder}` variables in a `ChatPromptTemplate` describe structural inputs expected from upstream;
- `.invoke({...})` supplies the initial runtime inputs at the outer boundary;
- inside a composed chain, mappings and `assign` stages can construct/enrich the state required by downstream prompts;
- prompt placeholders alone are a weak structural contract; semantic/type guarantees require validation;
- prompt output requirements, parser output, validation contract and deterministic Python input contract need to agree.

This is a meaningful shift from memorising LangChain syntax toward reading LCEL as **state evolving through stages and contracts**.

### Evidence boundary

Lesson 34 now has successful **guided implementation + passing tests + immediate state tracing + architectural synthesis**. It is not yet delayed cold-independent implementation. Later reconstruction should use a changed domain and probe `assign`, `RunnableLambda`, callable timing, gate semantics and contract alignment.

### FTEC5660 next step

Do not immediately rebuild the same pipeline. Continue Tutorial 1 conceptually:

1. reason about failure localisation and why/when explicit stages justify cost/latency;
2. extend the compact payments/KYC architecture only if a new mechanism is required;
3. inspect model-generated code as a validated artifact pattern rather than memorising tax rules;
4. bridge from fixed prompt chaining to routing: when should the input determine which path runs next?

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

- **Python / NumPy / pandas:** substantial practice; syntax/API fluency can be less automatic than the learner's long-used backend languages. Callable timing remains a recurring implementation fragility.
- **Linear algebra:** historical JHU foundation established; retrieve selectively.
- **Probability/statistics:** strong historical evidence across major foundations; Markov chains/Poisson remain diagnostic-needed.
- **Calculus:** historical derivative/gradient/chain-rule/backprop foundation established.
- **Practical ML:** linear/logistic regression and train/validation/test workflow implemented; changed-task transfer still useful.
- **Agentic/LCEL:** Lesson 32 basics are partly cold-retrievable; Lesson 34 stateful composition/gates have guided passing implementation evidence and strong immediate conceptual synthesis.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain new work.

## Parked / must return

- **FTEC5660:** active now. Continue Tutorial 1 architecture/routing bridge; later cold-reconstruct Lesson 34 on a changed domain rather than replaying it immediately.
- **AIMS5701/search:** guarantees/complexity still due after the current Agentic AI block.
- **AIMS5702:** representation translation remains the next substantive course-specific review target.
- **Maths:** selective LA/calculus/probability maintenance; later MLE/formal-theory extensions.

## Handover discipline

After the next substantive FTEC5660 block, update the focused course log and this handover. Update `learning_progress.yaml` only when the structured dashboard state materially changes; Lesson 34 should not be labelled cold-independent until delayed changed-domain reconstruction supports that claim.
