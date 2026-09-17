# Lesson 36 — Routing retrieval and chain-to-branch bridge

**Date:** 2026-09-17  
**Status:** Routing concept retrieved on changed examples; `RunnableBranch` syntax not yet cold-retrieved

## Taught boundary

Lecture 2 covered **Pattern 2: Routing** and the supplied Tutorial 2 was reached through the end of **Part 1: Routing** only. Parallelisation and reflection appear later in the tutorial but are not yet part of the taught/retrieval boundary.

The durable lecture distinction is:

```text
fixed chain
A -> B -> C -> D

routing
A -> B -> choose one downstream branch based on input/state
```

Routing may be rule-based, classifier-based, embedding-based or LLM-based. The tutorial's Part 1 uses an LLM-produced structured route decision followed by conditional delegation.

## Changed-domain cold retrieval

The retrieval session deliberately used a property-maintenance domain rather than the lecture/tutorial travel example.

The learner independently proposed:

```text
messy tenant message
    -> LLM triage/extraction
    -> structured issue facts
    -> validation
    -> deterministic API / job creation
```

The learner correctly recognised that schema-valid output can still be semantically wrong: allowed issue types/priorities can be swapped while passing structural checks.

This successfully retrieved the Tutorial 1 distinction:

> structurally valid does not imply semantically correct.

## Lesson 34 probe inside the routing bridge

The learner retained the main stateful-LCEL architecture and correctly retrieved:

- `RunnableLambda(validate_triage)` rather than immediately invoking the function;
- builder invocation such as `build_triage_chain(llm)` when the builder must first return a runnable;
- prompt/parser/validator/downstream type contracts must align;
- validation should return the same state on success and fail loudly on invalid input.

Fragilities still observed:

- `.assign(...)` syntax was not cold and needed correction after writing `RunnablePassthrough(...)` directly;
- nested state access briefly used `state["priority"]` rather than `state["triage"]["priority"]`;
- minor Python syntax/API rust appeared in `isinstance` and an `end` token.

Therefore Lesson 34 remains guided implementation evidence rather than delayed cold-independent LCEL reconstruction.

## Routing reasoning

The learner correctly identified why a fixed chain becomes insufficient when an earlier state determines which downstream action should run:

```text
                  -> emergency flow
triage -> validate -> router -> normal flow
                  -> human-review flow
```

A useful distinction was established between:

```text
state enrichment
    add route/contractor/category information

routing
    change which downstream runnable/flow executes
```

The learner also separated **interpretation** from **policy**:

```text
messy language
    -> LLM interprets facts
    -> validated structured state
    -> deterministic organisational policy where possible
    -> route label
```

Example reasoning: a tenant saying a gas leak can wait should not necessarily control emergency policy. The LLM may extract the factual issue type and the tenant's stated urgency, while deterministic policy can still route a gas leak to emergency handling.

The learner explicitly recognised that an LLM router is still defensible when the routing decision genuinely requires fuzzy contextual judgment, but deterministic routing is preferable when validated state plus explicit policy is sufficient.

## Route decision vs branch execution

The learner preferred a router that returns a symbolic route label over one that directly executes a branch:

```text
state -> choose_route -> "EMERGENCY"
                      -> "NORMAL"
```

with a separate mapping from labels to flows.

Reason given: the responsibility is more contained and easier to test; combining route choice with branch execution couples the decision to side effects and weakens failure localisation/observability.

## Receipt-domain transfer

On a receipt example with extracted `category` and `confidence`, the learner independently wrote the deterministic policy order:

```text
low confidence -> HUMAN_REVIEW
otherwise HOTEL -> HOTEL_FLOW
otherwise RESTAURANT -> MEAL_FLOW
otherwise GENERAL_FLOW
```

The learner correctly put the confidence gate before category-specific routing, recognising policy precedence.

They also correctly identified that routing and chaining **compose**: a router chooses which specialised chain runs next; routing does not replace chaining.

## Current evidence boundary

Strong evidence:

- routing vs fixed-chain distinction is cold-retrievable on changed domains;
- state enrichment is distinguished from execution-path selection;
- deterministic vs LLM routing can be reasoned about from policy/ambiguity requirements;
- route decision is separated from branch side effects;
- routing composes with specialised downstream chains;
- Tutorial 1 validation/decomposition philosophy transfers into routing examples.

Not established:

- independent reconstruction of Tutorial 2 Part 1 in LangChain;
- cold `RunnableBranch` syntax;
- parallelisation or reflection (not yet taught/reached).

## Next retrieval / implementation target

Use one short changed example to recover the actual Tutorial 2 Part 1 mechanism:

```text
structured route decision
    -> preserve/add route in state
    -> RunnableBranch conditions
    -> selected runnable
```

Do not move into Tutorial 2 Part 2/3 until live teaching reaches them.
