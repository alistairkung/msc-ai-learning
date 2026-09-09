# Lesson 32 — LangChain / LCEL basics

**Date:** 2026-09-09  
**Status:** Guided implementation complete; changed-example pytest exercise complete with targeted support; cold reconstruction still due

## Curriculum role

This lesson converts FTEC5660 Prompt Chaining / LCEL syntax from notebook recognition into executable practice. It deliberately stays inside the taught boundary: prompt templates, LCEL pipe composition, string/JSON output parsers, invocation inputs and simple sub-chain mapping. Later abstractions such as `RunnableLambda`, `RunnablePassthrough`, full ledger compute/explain wiring and repair/gate loops remain future material.

Source implementation: `agentic_ai/langchain/lesson32_lcel_basics.py`  
Source tests: `agentic_ai/langchain/test_lesson32_lcel_basics.py`

## Learning workflow

The session used the same pattern that worked for NumPy/pandas:

```text
taught micro-example
-> changed-example pytest requirement
-> learner implementation
-> concise feedback only where needed
-> next test
```

`FakeListChatModel` kept the tests deterministic and made the target LCEL composition rather than real-model behaviour, API keys, cost or response variance.

## What was implemented

The learner built and passed tests for:

- `ChatPromptTemplate.from_template(...)` with named placeholders;
- a plain-text summary chain: `prompt | llm | StrOutputParser()`;
- an extraction prompt requesting structured risk fields;
- a JSON extraction chain: `prompt | llm | JsonOutputParser()`;
- `.invoke({...})` input dictionaries matching prompt placeholders;
- a two-stage chain where the extraction chain's result is mapped into a named input for the next prompt;
- a second-stage recommendation prompt returning a plain string.

The committed exercise uses a payments/risk domain rather than copying the class expense-ledger example.

## Demonstrated understanding

The learner correctly explained that:

- `ChatPromptTemplate` is a reusable parameterised prompt rather than the runtime input itself;
- chain construction and `.invoke(...)` happen at different times;
- `StrOutputParser()` produces a Python string;
- `JsonOutputParser()` converts a JSON object/array response into Python structured data;
- the invocation dictionary key must match the prompt placeholder;
- in `{"risk_summary": earlier_chain}`, the earlier chain is a runnable value producer: its result becomes the value supplied to `{risk_summary}` in the next prompt;
- `extract_chain` is the runnable pipeline definition, not the already-invoked output value.

## Support / fragilities observed

### 1. Function object versus function call

The recurring implementation slip was omitting `()` on builder functions, for example:

```text
build_extraction_prompt     -> function object
build_extraction_prompt()   -> returned ChatPromptTemplate

build_extraction_chain      -> builder function
build_extraction_chain(llm) -> returned runnable chain
```

This appeared several times across the taught and exercise portions. The intended LCEL architecture was usually correct. Treat this as Python/API fluency rust worth retesting, not evidence that the learner failed to understand chaining.

### 2. Class versus instance / supplied object versus constructor

During the taught pass there were similar slips around `StrOutputParser` vs `StrOutputParser()` and a passed `llm` object vs `llm()`. These were repaired once the object roles were made explicit.

### 3. Two-stage mapping needed conceptual support

The learner initially tried to pipe the extraction prompt directly into the escalation prompt and later tried to hard-code an empty JSON shape. After clarification, they correctly explained the mapping semantics and implemented:

```text
{"risk_summary": build_extraction_chain(llm)}
    -> prompt expecting {risk_summary}
    -> llm
    -> StrOutputParser()
```

Because this required guidance, the completed two-stage implementation is not yet evidence of unaided cold reconstruction.

## Prompt-design retrieval target

The learner explicitly asked to make this a future cold-recall target:

```text
Task
Input
Constraints
Output structure
```

The goal is not only to recite the four labels. Future retrieval should give a vague prompt and ask the learner to improve it using all four dimensions.

Prompt improvements applied to the exercise included:

- state the task precisely;
- label the input clearly;
- make constraints explicit;
- specify expected keys/types or a constrained action vocabulary;
- separate extraction from recommendation rather than asking one prompt to do everything.

## Evidence boundary

The committed code and passing tests show successful implementation during this session, but support was provided during construction, especially for builder invocation and two-stage mapping. Do **not** mark LCEL performance as independent yet.

The next evidence step should be a short cold reconstruction on a changed domain without looking at this implementation. Do not replay the entire lesson.

## Future retrieval

A short check should sample:

1. Explain build-time chain construction versus runtime `.invoke()`.
2. Reconstruct `prompt | llm | StrOutputParser()` from a changed requirement.
3. Switch to structured output and explain the resulting Python type.
4. Given a second prompt placeholder, construct the mapping from an earlier runnable chain.
5. Diagnose a deliberate bare-function-name bug (`builder` vs `builder()`).
6. Cold-recall **Task → Input → Constraints → Output structure** and use it to repair a vague prompt.

## Next step

Stop adding new LCEL syntax for now. At a later maintenance point, do one short changed-example cold reconstruction. If that succeeds with little/no conceptual support, update LCEL performance evidence accordingly. Course-specific FTEC work should still be reassessed if enrolment changes.
