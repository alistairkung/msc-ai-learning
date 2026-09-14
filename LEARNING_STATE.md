# Learning State — Current Handover

_Last maintained: 2026-09-14. Learning evidence through 2026-09-14._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **FTEC5660 routing / conditional workflow bridge** | Tutorial 1 chaining philosophy is now conceptually understood. Do not spend more time on US tax mechanics or compact notebook syntax; next use a changed non-tax domain to cold-recall decomposition, then move from fixed sequence to routing. |
| Parallel | **AIMS5702 representation translation + light tensor maintenance** | Shape reasoning remains the anchor; train diagram ↔ shapes ↔ indices ↔ PyTorch when course work resumes. |
| Protect | **Search theory + a small relevant maths retrieval block** | Search implementation is complete through Lesson 33 but guarantees/complexity remain due; keep January AIMS5704 prerequisites alive without a broad restart. |

These lanes coexist; they are not one sequential queue.

## FTEC5660 / LangChain — Lessons 34–35 on 14 Sep

Sources: `lesson_logs/lesson32_lcel_basics.md`, `lesson_logs/ftec5660/tutorial01_study_plan.md`, `lesson_logs/ftec5660/lesson34_stateful_lcel_2026_09_14.md`, and `lesson_logs/ftec5660/lesson35_tutorial01_architecture_2026_09_14.md`.

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

### Lesson 35 — Tutorial 1 architecture understood

A readable TaxCalcBench walkthrough was used to separate the tutorial's architecture from distracting US tax-domain details.

The learner now understands the benchmark setup as:

```text
input.json   = unseen taxpayer case / exam question
output.xml   = hidden benchmark answer key
agent        = system attempting to reconstruct the completed return
```

The raw `input.json` is a large nested, machine-readable filled questionnaire containing taxpayer facts and source-form fields. The LLM first reduces this into a smaller inventory, then makes domain placement decisions, while deterministic code handles derived arithmetic.

Durable decomposition:

```text
messy / variable representation
        ↓
LLM: interpret / extract
        ↓
structured artifact
        ↓
Python: validate
        ↓
LLM: map / supply changing domain knowledge
        ↓
Python: validate
        ↓
deterministic execution
        ↓
optional LLM explanation / formatting
```

#### Parse → compute → explain

The learner explicitly understood why exact filtering/arithmetic should move out of the LLM once the problem is structured: ordinary Python is cheaper, faster, deterministic and easier to test.

Current heuristic:

> Use the LLM where variability or ambiguity requires interpretation; use deterministic software once the problem has become deterministic.

#### Inventory vs placement

Useful generic translation:

```text
inventory  = what source facts exist?
placement  = where should each fact go under domain rules?
compute    = derive totals/decisions from validated placements/rules
```

Tax-specific terminology is intentionally not a learning target. Source "boxes" are pre-labelled source-document fields; destination "lines" are return fields chosen by the model's placement stage.

#### Structural vs semantic validation

The learner identified a major limitation in the lecturer's lightweight checks.

The checks can prove things such as:

- a numeric amount existed somewhere upstream;
- values were not silently dropped/duplicated;
- a destination field is from an allowed set;
- derived subtotal fields were not directly populated by the model.

But they do **not** prove that a real amount was attributed to the correct source field or mapped to the correct valid destination field.

Durable hierarchy:

```text
value exists upstream
    < source attribution is correct
    < semantic/domain placement is correct
```

Current principle:

> Structurally valid does not imply semantically correct.

#### Generated-code pattern — understood, not production default

The lecturer's pattern was understood as:

```text
LLM recalls/interprets rule
    ↓
LLM emits Python source as text
    ↓
source is dynamically loaded into a callable
    ↓
known sample/test validates behaviour
    ↓
validated callable participates in deterministic computation
    ↓
final benchmark result is evaluated against ground truth
```

The learner understands why this externalises model knowledge into an inspectable/testable artifact, but should **not** internalise `exec(llm_output)` inside a production process as the default architecture.

Preferred production instinct:

```text
LLM
    ↓
constrained JSON / rule configuration
    ↓
schema + semantic validation
    ↓
trusted API / application code interprets it
    ↓
deterministic execution
```

Example mental model: the LLM supplies bracket thresholds/rates as JSON; a narrow trusted API knows how to validate and apply those brackets.

If genuinely dynamic code is useful, the learner now distinguishes a more defensible architecture:

```text
JSON input
    ↓
disposable isolated sandbox
    ↓
LLM-generated program
    ↓
restricted filesystem/network/secrets/resources
    ↓
validated JSON output
    ↓
main workflow continues
```

Security framing:

> The key question is not only whether generated code is trusted, but what capabilities untrusted code can exercise if it behaves unexpectedly.

### Evidence boundary

Lesson 34 has successful **guided implementation + passing tests + immediate state tracing + architectural synthesis**. It is not yet delayed cold-independent implementation.

Tutorial 1 is now **conceptually learned, implementation partially learned**.

Strong evidence:

- can explain one-shot baseline vs decomposed chain;
- can explain parse → deterministic compute → explain;
- understands inventory vs placement vs derived computation;
- understands failure localisation and validation boundaries;
- understands structural validity vs semantic correctness;
- understands model-generated code as an artifact that can be tested;
- distinguishes unsafe in-process execution from capability-constrained sandbox execution;
- prefers structured contracts + trusted executors as the production default;
- can translate the tax example into a generic enterprise/fintech architecture.

Not established:

- line-by-line recall of the lecturer's compact TaxCalcBench implementation;
- independent reconstruction of the full TaxCalcBench LCEL chain;
- US tax-domain knowledge (intentionally out of scope).

### FTEC5660 next step

Do not immediately rebuild the same pipeline or continue learning US tax mechanics.

Next useful work:

1. cold-recall Tutorial 1 architecture using a changed non-tax domain;
2. probe Lesson 34 callable timing / assign / validation with a changed example;
3. bridge from fixed sequential prompt chains to routing/conditional paths: when should input determine which branch runs next?;
4. revisit generated artifacts later only if a new mechanism such as sandbox execution, repair loops or tool routing is required.

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
- **Agentic/LCEL:** Lesson 32 basics are partly cold-retrievable; Lesson 34 stateful composition/gates have guided passing implementation evidence; Tutorial 1 architecture is conceptually understood but full implementation is not independently reconstructable yet.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain new work.

## Parked / must return

- **FTEC5660:** active now. Next bridge is routing/conditional workflows after one changed-domain recall of Tutorial 1 architecture.
- **AIMS5701/search:** guarantees/complexity still due after the current Agentic AI block.
- **AIMS5702:** representation translation remains the next substantive course-specific review target.
- **Maths:** selective LA/calculus/probability maintenance; later MLE/formal-theory extensions.

## Handover discipline

After the next substantive FTEC5660 block, update the focused course log and this handover. Update `learning_progress.yaml` only when the structured dashboard state materially changes. Do not label Lesson 34 cold-independent until delayed changed-domain reconstruction supports that claim, and do not label the TaxCalcBench implementation mastered merely because the readable reference implementation exists in the repo.
