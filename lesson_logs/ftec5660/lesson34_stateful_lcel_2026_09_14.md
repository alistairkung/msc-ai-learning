# Lesson 34 — Stateful LCEL: assign, RunnableLambda and validation gates

**Date:** 2026-09-14  
**Status:** Guided concepts + learner implementation complete; all Lesson 34 practice tests green; delayed cold reconstruction still due

## Resume context

Agentic AI resumed after being deliberately parked following Lesson 32. The session began with the stored short cold check rather than replaying LCEL basics.

## Lesson 32 cold retrieval

### Retrieved successfully

The learner cold-reconstructed the conceptual LCEL sequence:

```text
prompt template -> model -> output parser
```

They correctly recalled:

- `JsonOutputParser()` for structured JSON output and expected a Python `dict`;
- `.invoke({"note": ...})` style runtime dictionaries;
- two-stage mapping with `{"risk_summary": extract_chain}` where the earlier chain is supplied as a runnable value producer;
- the distinction that the runnable chain itself belongs in the mapping rather than an already-invoked value.

This is stronger evidence for the two-stage mapping than on 9 Sep, when conceptual support was needed.

### Still fragile

The exact Lesson 32 API/object-role fragilities recurred during the initial cold check:

- `ChatPromptTemplate.from_template` vs calling `ChatPromptTemplate.from_template(...)`;
- `StrOutputParser` vs `StrOutputParser()`.

The prompt-design checklist was not cold-recalled. With prompting it was recovered as:

```text
Task
Input
Constraints
Output structure
```

Keep this checklist as a future retrieval target rather than treating it as established cold recall.

## New concept 1 — `RunnablePassthrough.assign`

Mental model:

> Keep the existing state dictionary and add the result of a runnable under a new key.

The learner successfully traced state evolution and later implemented the pattern in the complete pipeline.

### Independent vs dependent assignments

A useful architectural distinction emerged from the learner's suggestion to put two outputs into one `assign` call:

```text
independent enrichments
    -> can share one assign and read the same incoming state

dependent enrichments
    -> use sequential stages so the later runnable receives the earlier enriched state
```

The learner correctly reasoned that a `screen_chain` in the same assign should not be assumed to see an `extracted` key being produced alongside it.

Important refinement retained: `|` means sequential **runnable stages**, not necessarily sequential model calls.

## New concept 2 — `RunnableLambda`

Mental model:

> `RunnableLambda` adapts an ordinary Python function so it can participate as an LCEL runnable stage.

The learner correctly preferred deterministic Python for an exact threshold rule and implemented:

```text
amount >= 10,000 -> MANUAL_REVIEW
otherwise        -> STANDARD
```

The first attempt returned a boolean; after the required output contract was restated, the learner correctly returned the required route strings.

State provenance remained clear:

```text
payment_note -> original input
extracted -> probabilistic LLM output
review_route -> deterministic Python output
```

## New concept 3 — validation gates / fail-fast boundaries

Gate contract:

```text
valid state   -> return the SAME state unchanged
invalid state -> fail loudly
```

The learner implemented validation for:

- required `amount` and `currency` keys;
- numeric non-negative amount;
- three-character string currency.

The first implementation exposed useful Python rust: directly reading a missing `currency` key raised `KeyError`, so the learner changed the gate to assert key membership before value/type checks.

The learner correctly identified that `"15000"` should fail because it is a string rather than a numeric value.

### Validation should not silently repair

The learner gave a strong software-engineering explanation for not silently coercing `"15000"` to a number inside the gate: it adds complexity outside the validator's responsibility and presumes the producer's intended behaviour.

Durable separation:

```text
extract -> validate -> explicit repair path if desired -> validate -> continue
```

rather than hiding mutation/coercion inside validation.

### Why the gate returns state

The learner correctly explained that downstream pipeline stages rely on the state. A successful gate returns the same state rather than `None` so LCEL can continue with validated data.

Useful summary:

> Same data out, stronger guarantee about the data out.

## Implementation evidence — all tests green

The learner worked through `test_lesson34_stateful_lcel_practice.py` sequentially and reported the full suite green.

Implemented in `agentic_ai/langchain/lesson34_stateful_lcel_practice.py`:

- `determine_review_route` using named constants;
- `validate_extraction`;
- `build_extraction_chain` with `ChatPromptTemplate`, LLM and `JsonOutputParser()`;
- `build_payment_pipeline` combining state enrichment, validation and deterministic routing.

Final pipeline architecture implemented by the learner:

```text
input state
    -> RunnablePassthrough.assign(extracted = extraction runnable)
    -> RunnableLambda(validate_extraction)
    -> RunnablePassthrough.assign(review_route = RunnableLambda(determine_review_route))
    -> enriched state
```

### Support needed during implementation

Do not upgrade this to fully independent cold implementation yet. Support was still required for:

- builder function vs builder call: `build_extraction_chain` vs `build_extraction_chain(llm)`;
- callable vs invocation inside `RunnableLambda`: `determine_review_route` vs `determine_review_route()`;
- prompt output contract initially asked for stale unrelated keys, then asked for `amount` as a string before being aligned to the validator's numeric contract;
- validator missing-key behaviour as described above.

The learner nevertheless chose the correct overall three-stage pipeline architecture before these API/callable corrections.

## Post-implementation cold state trace

After all tests passed, the learner correctly traced:

```text
initial:
{payment_note}

post extraction assign:
{payment_note, extracted}

post validation:
{payment_note, extracted}   # unchanged

post route assign:
{payment_note, extracted, review_route}
```

There was one incidental key-name slip (`review_method` instead of `review_route`) in the final trace; the state evolution itself was correct.

## Conceptual synthesis after implementation

The learner explicitly connected `ChatPromptTemplate` placeholders to upstream interface requirements: variables inside `{...}` describe the keys/values the prompt expects its input to provide.

Refined model:

```text
prompt placeholder
    -> structural input requirement

upstream state / mapping
    -> supplies the required key

validation gate
    -> establishes stronger semantic/type guarantees than the placeholder alone
```

The learner also consolidated the invocation/state model:

- the outer `.invoke({...})` supplies the initial runtime dictionary;
- a prompt expects its placeholder keys to be present in the input it receives;
- inside a composed pipeline, upstream mappings/`assign` stages can construct and enrich the dictionary needed by later prompts;
- therefore not every downstream prompt needs to be manually invoked with a fresh dictionary.

This is an important conceptual shift from memorising LangChain syntax toward reading LCEL as **state evolving through stages and contracts**.

Useful interface chain:

```text
prompt output requirement
    -> parser output
    -> validation contract
    -> deterministic Python input contract
```

These contracts need to agree. A pipeline can contain individually valid components and still fail if their interfaces disagree.

## Python side notes recovered/introduced

- constants are conventionally uppercase; Python does not enforce `const`;
- `dict[key]` fails loudly on a missing required key;
- `.get()` avoids `KeyError` but is not automatically better design when absence violates a contract;
- Python uses `and` / `or` / `not`, not JavaScript `&&` / `||` / `!`;
- `assert` is a Python language feature, not pytest-specific;
- callable timing (`fn` vs `fn()`) remains the clearest recurring Python/LCEL fragility.

## Current evidence boundary

Lesson 34 now has **successful guided implementation evidence with all practice tests passing** plus correct immediate state tracing and strong architectural synthesis.

It is not yet delayed cold-independent evidence. A later changed-domain reconstruction should probe whether the learner can independently recover:

- `assign` vs `RunnableLambda` responsibilities;
- builder call vs callable object;
- state before/after each stage;
- gate behaviour;
- prompt/parser/validator contract alignment.

## Next step

Continue Tutorial 1 at the architectural level rather than adding syntax for its own sake. Good next targets:

1. extend the compact payments/KYC workflow with another deterministic/checkable boundary;
2. reason about failure localisation and when explicit stages are worth their cost/latency;
3. inspect the tutorial's larger generated-code pattern as architecture rather than memorising tax logic;
4. bridge from fixed prompt chaining to routing: when should input determine which path runs next?
