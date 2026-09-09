# FTEC5660 Tutorial 1 — follow-up study plan

**Created:** 2026-09-09  
**Status:** Parked after Lesson 32; resume **one day before the next FTEC5660 lecture**. Exact return date is intentionally not invented here.

## Why this plan exists

Tutorial 1 contains useful agentic/LCEL ideas, but its later US-tax example mixes unfamiliar domain logic, long state dictionaries, generated Python, validation helpers and one large composed chain. The useful learning goal is therefore to extract the **architecture and LangChain mechanisms**, not memorise Form 1040 logic or reproduce the notebook line by line.

The attached tutorial notebook was reviewed on 9 September 2026 and a separate annotated copy was produced for study. **That notebook is not committed to this repository.** This Markdown file preserves only the durable learning plan.

## Current position

Lesson 32 already covered, with guided implementation and changed-example pytest practice:

- `ChatPromptTemplate.from_template(...)`;
- prompt placeholders and `.invoke({...})` input dictionaries;
- `prompt | llm | StrOutputParser()`;
- `prompt | llm | JsonOutputParser()`;
- `{"next_variable": earlier_chain}` for feeding one runnable into the next prompt;
- free-text → structured JSON extraction;
- a two-stage extraction → recommendation chain;
- prompt-design retrieval target: **Task → Input → Constraints → Output structure**.

The first four tests transferred cleanly. Two-stage mapping needed conceptual support, and function-object versus function-call (`fn` vs `fn()`) remains a small Python/API fragility. LCEL should therefore remain **guided**, not independent.

## Resume protocol — one day before the next lecture

Do **not** replay all of Lesson 32.

Start with a short 5–10 minute changed-example cold check:

1. build one prompt template from a blank file;
2. compose `prompt | llm | parser`;
3. invoke it with the correct placeholder dictionary;
4. map one earlier chain into a second prompt;
5. cold-recall **Task → Input → Constraints → Output structure** and improve one vague prompt;
6. deliberately check `fn` vs `fn()` and parser class vs parser instance.

If that comes back with little support, move straight into the new material below.

---

# Study sequence

## Phase 1 — LCEL basics maintenance

**Purpose:** retain the small grammar already learned, not deepen syntax for its own sake.

Cold-recall:

```text
ChatPromptTemplate.from_template(...)
prompt | llm | StrOutputParser()
prompt | llm | JsonOutputParser()
chain.invoke({"placeholder": value})
{"next_variable": earlier_chain}
```

**Evidence target:** changed-example reconstruction with minimal conceptual help.

---

## Phase 2 — Stateful chains with `RunnablePassthrough.assign`

This is the next major LangChain mechanism to learn.

Mental model:

```text
existing state dictionary
    -> run one step
    -> keep existing state
    -> add the result under a new key
```

Example shape:

```text
{"payment": ...}
    -> add extracted_fields
{"payment": ..., "extracted_fields": ...}
    -> add screening_result
{"payment": ..., "extracted_fields": ..., "screening_result": ...}
```

**Cold-recall sentence:**

> `RunnablePassthrough.assign(name=step)` keeps the current dictionary and adds the result of `step` under `name`.

**Learning priority:** high. Read long chains by asking what keys exist **before and after each assign**, rather than reading the whole expression at once.

---

## Phase 3 — Ordinary Python inside LCEL with `RunnableLambda`

Learn that a LangChain pipeline does **not** have to be a sequence of LLM calls.

Mental model:

```text
structured state
    -> normal Python function
    -> updated / checked value
    -> next chain stage
```

**Cold-recall sentence:**

> `RunnableLambda` lets ordinary Python logic participate as a runnable LCEL stage.

Use a tiny payments example rather than the tax workbook. The constructor syntax is secondary to understanding the role.

---

## Phase 4 — Gates and fail-fast validation

Build the key reliability pattern from Tutorial 1:

```text
LLM produces structured state
    -> deterministic check
    -> PASS: keep the same state and continue
    -> FAIL: stop before bad state contaminates later stages
```

A gate should conceptually:

1. inspect the current state;
2. run assertions / validation;
3. fail if the contract is violated;
4. return the same state unchanged if valid.

**Learning target:** an LLM output does not automatically earn downstream authority merely because it looks plausible.

This connects directly to the earlier Prompt Chaining lesson: reliability comes from **checkable interfaces between stages**.

---

## Phase 5 — One compact payments/KYC workflow

Use familiar domain knowledge to combine the previous mechanisms:

```text
unstructured payment/KYC exception
    -> LLM extracts structured facts
    -> gate validates required facts
    -> deterministic Python policy / amount / lookup step
    -> gate validates result
    -> LLM writes a concise investigator recommendation
```

Keep it deliberately small.

For every boundary, be able to answer:

- What is the input type?
- What does this stage do?
- What is the output type?
- Which state keys exist before and after it?
- What is deterministic versus probabilistic?
- What check prevents an upstream error from silently propagating?

**Success criterion:** draw the state dictionary after every stage without reading the implementation.

---

## Phase 6 — Model-generated code as an architectural concept

The tax example later asks the model to express domain knowledge as executable Python and then lets deterministic code validate/execute it.

Study the pattern, not the tax rules:

```text
model recalls rule
    -> model expresses rule as code
    -> extract/load code
    -> run deterministic tests
    -> PASS: allow artifact into workflow
```

Durable ideas:

- knowing a rule is different from reliably executing it;
- generated code is an **artifact to validate**, not authority by default;
- scaffolding reduces the model's search space;
- less scaffolding increases autonomy **and** possible failure modes;
- tests should check important business requirements, not merely that code runs.

If implementation practice is useful, use a tiny safe fee-tier example rather than reproducing Form 1040.

---

## Phase 7 — Re-read the large tax chain as architecture only

Do not reproduce the tax arithmetic.

Label each stage with one role:

```text
extract
choose / place
generate rule
validate
compute
format / evaluate
```

If the long notebook can be reduced mentally to those roles plus state enrichment, it has served its learning purpose.

Key Tutorial 1 conclusions to retain:

- establish a simple baseline before adding orchestration;
- well-formed output is not proof of correctness;
- use deterministic scorers/ground truth where possible;
- LLM for interpretation/extraction, code for exact computation, LLM for language is often a strong division of labour;
- validate intermediate artifacts at stage boundaries;
- constrain decision spaces where possible;
- failure localisation is a major benefit of explicit stages;
- chaining has cost/latency/maintenance overhead and is not automatically better than one strong call.

---

## Phase 8 — Later cold reconstruction

After another gap, reconstruct a small validated chain on a changed domain.

Probe specifically:

- `fn` versus `fn()`;
- parser class versus parser instance;
- mapping key matching the next prompt placeholder;
- state before/after `assign`;
- deterministic gate behaviour;
- **Task → Input → Constraints → Output structure**.

Only upgrade LCEL performance evidence after this can be done with little/no conceptual support.

---

## Phase 9 — Bridge to routing

The Tutorial 1 workbook says the next tutorial moves to **routing**.

Carry forward this question:

> When should a workflow be a fixed sequence of stages, and when should the input determine which chain/path runs next?

That is the conceptual bridge from Prompt Chaining to Routing.

## What not to memorise

Do not spend preparation time memorising:

- US tax/Form 1040 line arithmetic;
- the exact TaxCalcBench pipeline;
- generated tax-rule code;
- long composed LCEL expressions as opaque syntax;
- every model/provider configuration field.

The durable target is to recognise the small mechanisms and explain **why each stage exists, what state it consumes/produces, and what earns permission to continue**.
