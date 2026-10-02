# Private Client Graph — AI implementation delegation strategy, 2 Oct 2026

## Context

The project is moving from architecture/benchmark design into implementation.

The learner explicitly loosened an earlier guardrail that required writing most implementation personally.

Reason:

> LangChain framework fluency is not itself the course objective. The higher-value learning is in problem framing, contracts, deterministic-vs-probabilistic boundaries, evaluation and interpreting failures.

This is a deliberate change in the human/AI division of labour, not an abandonment of understanding.

## Current delegation principle

The learner retains ownership of:

- problem definition;
- benchmark design;
- relationship semantics;
- extraction contracts;
- provenance requirements;
- deterministic/LLM responsibility boundaries;
- validation meaning;
- evaluation meaning;
- architecture changes prompted by observed failures.

AI assistance may be more aggressive for:

- Pydantic/framework syntax;
- LangChain structured-output plumbing;
- repetitive implementation;
- straightforward tests/scaffolding;
- file loading and integration glue.

The minimum comprehension standard for AI-written core code is that the learner can explain:

1. what goes in;
2. what comes out;
3. why the stage exists;
4. why the operation is probabilistic or deterministic;
5. what a failure would mean.

## Planned coding-agent experiment

The learner intends to use a coding agent for increasingly autonomous implementation.

The immediate phase is **bounded implementation**, not architectural delegation.

The agent should:

- inspect existing decisions before coding;
- preserve frozen contracts;
- implement one bounded slice at a time;
- run tests;
- show diffs;
- stop rather than silently redesign semantics when it finds a perceived blocker.

The first planned delegated slice is:

```text
Case 01 source.txt
    ↓
LLM structured output
    ↓
RelationshipCandidate[]
```

Validation, entity construction, normalisation, retries, routing and UI are deliberately excluded from that first task.

## Future productisation handoff

Once the core extraction/evaluation architecture is stable, the learner expects a larger coding-agent handoff for peripheral product work such as:

- graph visualisation;
- source/evidence viewer;
- click edge -> provenance interaction;
- evaluation dashboard;
- upload/run UX;
- styling;
- deployment/integration plumbing.

The intended boundary is:

```text
learner owns semantics + interfaces + acceptance criteria + review
coding agent owns bounded implementation volume
```

Core extraction/evaluation semantics should be protected from casual redesign during UI/productisation.

## Guardrails for larger autonomous work

Before handing over larger slices:

- freeze/document the relevant interfaces;
- provide explicit acceptance criteria;
- identify protected files/contracts;
- require tests and CI;
- prefer bounded PRs;
- require the agent to plan/inspect before editing;
- review dependencies/state flow/core-interface changes;
- periodically reconstruct the resulting architecture without relying on the agent's explanation.

If the learner can no longer explain how data flows through the resulting system, delegation has gone too far and implementation should pause for a comprehension checkpoint.

## Reflection value

A useful reflective thread is emerging:

> The learner changes the human/AI division of labour as uncertainty decreases.

Early/high uncertainty:
- retain human control over meaning and architecture.

Middle phase:
- use AI as tutor/pair implementer around learner-owned contracts.

Later/lower semantic uncertainty but higher implementation volume:
- delegate larger productisation slices behind tests and frozen interfaces.

This mirrors the project's software principle:

> Do not delegate deterministic work to an LLM unnecessarily.

At the development-process level:

> Do not delegate high-value learning and architectural judgement to a coding agent unnecessarily.

The point is not whether AI wrote code. The reflective question is **where delegation created leverage, what remained under human control, and which guardrails preserved understanding and correctness**.

## Tool/resource allocation decision

The learner plans to use Claude for heavy autonomous coding/productisation work, preserving OpenAI usage primarily for tutoring, architectural reasoning, learning-state continuity and reflective analysis.

This is an explicit resource-allocation choice rather than a technical dependency of the project.

## Next checkpoint

After the first coding-agent implementation slice:

- inspect the diff;
- verify it stayed inside the semantic contract;
- check tests;
- explain the implemented data flow;
- record any unexpected agent decisions;
- decide whether to widen or tighten delegation for the next slice.
