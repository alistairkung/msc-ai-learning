# AI-Assisted Engineering Workflow

> A living record of how we build software together during the MSc.
>
> This is not a fixed methodology. It should evolve as coursework, projects, research, and experience reveal better ways to combine human engineering judgement with AI assistance.

## Why this exists

The learning repo already records **what** is being learned and **what comes next**. This document records a different question:

**How should we build software with AI without outsourcing the engineering judgement we are trying to develop?**

The goal is not to minimise AI involvement. It is to use AI aggressively where it creates leverage while keeping understanding, architectural decisions, behavioural intent, and verification explicit.

## Current principles

### 1. Understand before outsourcing

For concepts that matter to the learning goal, I should be able to explain the important idea before delegating the implementation wholesale.

This does not mean manually writing every line. Boilerplate and mechanical work can be delegated. The distinction is whether delegation would remove the thing I am supposed to learn.

### 2. Build in small, coherent increments

Prefer bounded vertical slices over large autonomous missions.

A useful loop is:

```text
choose one behaviour
        ↓
reason about it
        ↓
define/test it
        ↓
implement
        ↓
run tests
        ↓
inspect failures
        ↓
refactor / commit
        ↓
next behaviour
```

The receipts exercises are the initial reference point for this style: progress feature by feature, keep the feedback loop short, and understand the code as it grows.

### 3. Add a specification step when behaviour is non-trivial

Traditional TDD gives us:

```text
RED → GREEN → REFACTOR
```

For meaningful feature or component boundaries, experiment with:

```text
SPEC → RED → GREEN → REFACTOR
```

Before writing tests, make the intended behaviour explicit:

- **Responsibility** — what is this component for?
- **Inputs / preconditions** — what may callers provide or assume?
- **Outputs / postconditions** — what must be true after success?
- **Failure behaviour** — what errors or exceptional states are part of the contract?
- **Undefined / unresolved cases** — what have we not decided yet?

The unresolved section is particularly important. An AI agent should not silently turn an ambiguous requirement into a product or architectural decision.

The human resolves meaningful ambiguity; tests then encode the agreed behaviour.

### 4. Do not create specification bureaucracy

The explicit SPEC step is not required for every tiny helper, exercise, or obvious implementation detail.

Use it when it buys clarity: feature boundaries, APIs, components with meaningful failure behaviour, cross-service interfaces, or places where an agent could plausibly make a reasonable but incorrect assumption.

If writing the specification costs more attention than the ambiguity it removes, skip it.

### 5. Treat tests as executable knowledge

Tests are not only regression protection. They are also machine-readable constraints for coding agents.

Different levels answer different questions:

- **Unit tests:** does local behaviour remain correct?
- **Integration tests:** does the component work with its real dependencies?
- **Contract tests:** are independently changing components still compatible?
- **End-to-end tests:** does the actual user/system workflow still work?

Prefer fast, local feedback for most development, with broader and more expensive tests providing confidence at system boundaries.

### 6. Prefer explicit interfaces to enormous context

More context is not automatically better agent context.

Types, schemas, OpenAPI/protobuf definitions, contracts, tests, ADRs, and dependency metadata can compress architectural knowledge far more effectively than asking an agent to repeatedly rediscover intent from an entire codebase.

The target is:

> Give the agent enough context to discover what matters, then give it the relevant context.

Not:

> Give the agent everything and hope it reconstructs the architecture.

### 7. Keep architectural and product decisions human-visible

AI can propose architecture and can implement agreed architecture aggressively.

Important decisions should still surface explicitly:

- ownership and boundaries;
- data models and contracts;
- failure semantics;
- security/reliability trade-offs;
- irreversible or expensive choices;
- behaviour not determined by the requirements.

The point is not that the human must always choose the AI's alternative. The point is that the decision should not disappear inside an autonomous implementation run.

### 8. Use failures as part of learning

During the MSc, a failing test, mistaken tensor shape, broken implementation, or incorrect assumption can be more educational than immediately receiving the finished answer.

When the failure touches the learning objective:

1. inspect it;
2. predict the cause;
3. test the hypothesis;
4. fix it;
5. record recurring points of fragility when useful.

AI should shorten unproductive struggle, not erase every useful struggle.

## Agent-friendly distributed systems

A monorepo can make cross-component discovery easy, but agents do not make multi-repo systems obsolete.

Distributed teams already solve the analogous human problem with:

- explicit service boundaries;
- API/schema definitions;
- ownership;
- backwards-compatibility rules;
- contract and integration testing;
- CI;
- system documentation.

For agents, these artifacts become valuable context.

A multi-repo agent workflow can use a coordinator to determine blast radius and then hand bounded changes to repo-specific workers:

```text
system / dependency map
          ↓
identify affected contracts and repos
          ↓
┌─────────┼─────────┐
↓         ↓         ↓
repo A    repo B    repo C
agent     agent     agent
↓         ↓         ↓
tests     tests     tests
└─────────┼─────────┘
          ↓
integration / contract / E2E verification
```

The architectural goal is not universal visibility. It is **cheap discovery of dependencies plus strong executable boundaries**.

## Structural vs behavioural contracts

Structural contracts such as protobuf, OpenAPI, JSON Schema, and types are excellent compressed context:

- fields;
- types;
- serialization;
- optionality;
- compatibility rules.

They do not necessarily capture every semantic behaviour a consumer relies upon.

Behavioural constraints may live in:

- consumer/provider contract tests;
- integration tests;
- domain invariants;
- examples;
- explicit specifications.

A useful question when adding another contract mechanism is:

**What information does this encode that our schema, types, and existing tests do not?**

Avoid duplicating artifacts merely because an agent can generate them.

## Working pattern for future projects

For a non-trivial feature, start with this default:

```text
1. Clarify the goal
        ↓
2. Identify relevant system boundaries
        ↓
3. Write a lightweight behavioural spec if needed
        ↓
4. Resolve meaningful ambiguity
        ↓
5. Derive focused tests
        ↓
6. Implement a bounded slice
        ↓
7. Run tests and inspect failures
        ↓
8. Refactor
        ↓
9. Commit
        ↓
10. Repeat
```

This is a default, not a ritual. Tiny changes can skip steps. Difficult or distributed changes may need additional design work.

## Experiments to run during the MSc

Treat this document as hypotheses to test rather than doctrine.

### Spec → RED → GREEN → REFACTOR

Try the explicit specification step on the next suitable project feature. Compare it with the receipts workflow:

- Did it expose ambiguity earlier?
- Did the tests become better?
- Did the AI make fewer invented assumptions?
- Did it improve understanding?
- Was the extra ceremony worth it?

### Context minimisation

When using coding agents on larger projects, compare:

- broad repository context;
- targeted files plus contracts/tests;
- architectural/dependency summaries.

Observe whether smaller, higher-quality context reduces wandering and rework.

### Generated tests/contracts

Explore whether agents can derive useful tests or behavioural contracts from agreed specifications and consumer behaviour without creating redundant maintenance burden.

## Evolution log

### 2026-09-26 — Initial version

Created after discussing:

- the incremental workflow used while building the receipts homework;
- TDD and specification-driven test generation;
- explicit preconditions, postconditions, failure behaviour, and unresolved cases;
- testing as an agent feedback mechanism;
- protobuf/schema contracts versus behavioural contracts;
- monorepo versus multi-repo agent workflows;
- context quality versus context quantity.

Initial hypothesis: **good AI-assisted engineering looks less like giving an agent the whole problem and more like making intent and boundaries explicit, then allowing the agent to move quickly inside them.**
