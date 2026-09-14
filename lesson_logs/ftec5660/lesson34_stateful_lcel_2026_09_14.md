# Lesson 34 — Stateful LCEL: assign, RunnableLambda and validation gates

**Date:** 2026-09-14  
**Status:** Guided concepts introduced; learner implementation practice now scaffolded by tests; independent implementation evidence pending

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

The exact Lesson 32 API/object-role fragilities recurred:

- `ChatPromptTemplate.from_template` vs calling `ChatPromptTemplate.from_template(...)`;
- `StrOutputParser` vs `StrOutputParser()`.

The prompt-design checklist was not cold-recalled. With prompting it was recovered as:

```text
Task
Input
Constraints
Output structure
```

The learner then correctly retrieved `Input` on an immediate changed prompt. Keep this checklist as a future retrieval target rather than treating it as established cold recall.

## New concept 1 — `RunnablePassthrough.assign`

Mental model introduced:

> Keep the existing state dictionary and add the result of a runnable under a new key.

Example state evolution:

```text
{"payment_note": ...}
    -> assign extracted
{"payment_note": ..., "extracted": {...}}
    -> assign screening
{"payment_note": ..., "extracted": {...}, "screening": {...}}
```

The learner correctly traced the complete enriched dictionary.

### Independent vs dependent assignments

A useful architectural distinction emerged from the learner's suggestion to put two outputs into one `assign` call.

```text
independent enrichments
    -> can share one assign and read the same incoming state

dependent enrichments
    -> use sequential stages so the later runnable receives the earlier enriched state
```

The learner correctly reasoned that a `screen_chain` in the same assign should not be assumed to see an `extracted` key being produced alongside it.

Important refinement: `|` means sequential **runnable stages**, not necessarily sequential model calls. A runnable may be an LLM chain, ordinary Python, retrieval or another operation.

## New concept 2 — `RunnableLambda`

Mental model introduced:

> `RunnableLambda` adapts an ordinary Python function so it can participate as an LCEL runnable stage.

The learner preferred deterministic Python for an exact threshold decision rather than asking another LLM to perform it.

They implemented the underlying business function after one contract correction:

```text
amount >= 10,000 -> MANUAL_REVIEW
otherwise        -> STANDARD
```

The first attempt returned a boolean; after the required output contract was restated, the learner correctly returned the required route strings.

The state provenance model was made explicit:

```text
payment_note -> original input
extracted -> probabilistic LLM output
review_route -> deterministic Python output
```

## New concept 3 — validation gates / fail-fast boundaries

The gate contract introduced from Tutorial 1:

```text
valid state   -> return the SAME state unchanged
invalid state -> fail loudly
```

The learner's first validator attempt had Python syntax rust (`&&`, malformed `isinstance`) and initially addressed fields at the wrong nesting level, but conceptually attempted to check all required invariants.

The guided contract used:

- `extracted` exists;
- `amount` exists;
- `amount` is numeric;
- `amount >= 0`;
- `currency` exists;
- `currency` is a string of length 3.

The learner correctly identified that `"15000"` should fail because it is a string rather than a numeric value.

### Validation should not silently repair

The learner gave a strong software-engineering explanation for not silently coercing `"15000"` to a number inside the gate: it adds complexity outside the validator's responsibility and presumes the caller/producer's intended behaviour.

Durable architectural separation:

```text
extract -> validate -> explicit repair path if desired -> validate -> continue
```

rather than hiding mutation/coercion inside validation.

### Why the gate returns state

The learner correctly explained that downstream pipeline stages rely on the state. If a validator returns nothing, Python returns `None`, breaking the LCEL dataflow. A successful gate therefore returns the same state so later stages receive validated data.

Useful summary:

> Same data out, stronger guarantee about the data out.

## Python side notes recovered/introduced

- constants are conventionally uppercase (`MANUAL_REVIEW_THRESHOLD = 10_000`); Python does not enforce `const`;
- `dict[key]` fails loudly on a missing required key;
- `.get()` avoids `KeyError` but is not automatically better system design when a missing key violates a required contract;
- Python uses `and` / `or` / `not`, not JavaScript `&&` / `||` / `!`;
- `assert` is a Python language feature, not a pytest-specific feature; explicit exceptions may be clearer for production validation.

## Practice scaffold

Created:

- `agentic_ai/langchain/lesson34_stateful_lcel_practice.py`
- `agentic_ai/langchain/test_lesson34_stateful_lcel_practice.py`

The learner implementation file contains signatures/contracts only. The tests should be completed in order and require the learner to implement:

1. deterministic review routing;
2. a validation gate that returns the same valid state and rejects malformed extraction;
3. structured LLM extraction using a fake deterministic chat model;
4. state enrichment with `RunnablePassthrough.assign`;
5. gate insertion via `RunnableLambda`;
6. deterministic route enrichment after validation;
7. fail-fast behaviour when LLM extraction violates the contract.

Do not supply the finished pipeline unless the learner explicitly asks or the normal hint ladder has been exhausted.

## Current evidence boundary

`RunnablePassthrough.assign`, `RunnableLambda`, and gates are **new guided concepts today**. The learner has demonstrated good architectural reasoning about state, dependencies, deterministic/probabilistic separation and validator responsibility, but has not yet independently implemented the complete LCEL workflow.

Do not mark Lesson 34 implementation as complete until the learner works through the new tests.

## Next step

Work through `test_lesson34_stateful_lcel_practice.py` sequentially. Prefer:

```text
test -> learner implementation -> concise feedback -> next test
```

After all tests pass, cold-trace the complete state after each stage and then continue Tutorial 1 toward the compact payments/KYC workflow and the later routing bridge.
