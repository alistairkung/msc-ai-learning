# FTEC5660 — LangChain / LCEL guided practice

**Date:** 2026-09-09  
**Status:** Guided syntax practice; independent reconstruction still pending

## Session purpose

Use a short taught block to turn yesterday's LangChain/LCEL recognition into usable syntax, following the same small-step approach used for NumPy/pandas: understand one object/operation, attempt it, repair only the local gap, then compose the pieces.

The learner used an ignored local `scratch.py` file for the guided work. No numbered implementation lesson or pytest exercise pair was created yet, so this session is evidence of **guided construction**, not independent reconstruction.

## What was understood and built with guidance

### Prompt templates

The learner correctly understood `ChatPromptTemplate` as a reusable "cookie-cutter" instruction with named placeholders. They built a payment prompt using:

```text
ChatPromptTemplate.from_template(...)
```

and understood that template construction is separate from supplying runtime data.

### Build time versus run time

A useful distinction stabilised during the session:

```text
build time:
    prompt | llm | parser

run time:
    chain.invoke({"payment": payment_text})
```

The learner initially tried to place the input dictionary inside the chain definition, then correctly moved runtime values to `.invoke(...)`.

### LCEL composition

The learner understood the pipe grammar:

```text
prompt | llm | parser
```

as data flowing from one component to the next. They built a plain-text payment chain using `StrOutputParser()` with guidance.

### Output parsers

The learner correctly distinguished:

```text
StrOutputParser()  -> Python str
JsonOutputParser() -> parsed Python structure (dict/list depending on JSON shape)
```

They then built a JSON-output payment chain using `JsonOutputParser()`.

### Invocation dictionaries

The learner independently supplied the correct runtime shape once the distinction was taught:

```text
chain.invoke({"payment": payment_text})
```

and correctly related the dictionary key `payment` to the template placeholder `{payment}`.

## Support / fragilities observed

The main difficulties were small object/function/class distinctions rather than conceptual misunderstanding:

- `build_payment_prompt` versus `build_payment_prompt()`;
- treating the passed `llm` object as though it needed `llm()`;
- `StrOutputParser` versus `StrOutputParser()`.

These should be treated as LangChain/Python API fluency gaps, not evidence that the pipeline concept is missing.

A second conceptual distinction needed explicit teaching once: **chain construction versus chain invocation**. After explanation, the learner correctly invoked both string and JSON chains with a named input dictionary.

## Pause point

The session paused immediately after introducing the next new syntax shape: mapping an earlier chain's output into a named placeholder for a second prompt.

Conceptual target for continuation:

```text
extract_chain output
    -> {"flag": extract_chain}
    -> prompt expecting {flag}
    -> llm
    -> parser
```

No independent implementation of sub-chain mapping was completed yet.

## Next session

Resume at **sub-chain mapping**, not from the beginning.

1. Reconstruct/explain a mapping such as `{"flag": extract_chain}` and why the key matches the next prompt placeholder.
2. Build one two-stage changed-domain chain with minimal hints.
3. Then create the normal tracked exercise/test pair, using deterministic/fake model components where practical so pytest tests LCEL composition rather than live-model variability.
4. Use the test-suite -> learner implementation loop for independent practice.
5. Only after that evidence should LCEL be considered independently reconstructable.

Do not expand yet into `RunnableLambda`, `RunnablePassthrough`, full ledger compute/explain wiring, gates/repair loops, or other later tutorial material.
