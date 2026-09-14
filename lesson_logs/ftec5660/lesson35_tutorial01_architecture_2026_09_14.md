# Lesson 35 — Tutorial 1 architecture: decomposition, trust boundaries, and generated code

**Date:** 2026-09-14  
**Status:** Conceptual architecture understood; lecturer implementation not line-by-line mastered

## Session goal

Continue FTEC5660 Tutorial 1 after Lesson 34 and understand the larger TaxCalcBench example at the architectural level rather than memorising US tax details or compact notebook syntax.

## Baseline experiment

The tutorial first establishes a known-answer task and compares a one-shot LLM solution against a decomposed workflow.

Durable mental model:

```text
known input
    ↓
model/system under test
    ↓
answer
    ↓
compare against benchmark ground truth
```

The key point is not that one-shot prompting is always bad. The experiment establishes a baseline so that decomposition can be judged on reliability, inspectability, cost and failure localisation.

## Parse → compute → explain

The ledger example became clear once responsibilities were separated:

```text
messy/variable representation
        ↓
LLM: interpret / parse
        ↓
structured state
        ↓
Python: exact filtering + arithmetic
        ↓
trusted numbers
        ↓
LLM: explain / communicate
```

The learner explicitly connected `RunnableLambda` to this principle: once the problem is deterministic, ordinary Python is cheaper, faster, easier to test, and more reliable than another model call.

Durable heuristic:

> Use the LLM where variability/ambiguity requires interpretation; use deterministic software once the problem has been converted into something deterministic.

## TaxCalcBench mental model

The raw `input.json` is an unseen benchmark case: a large nested, machine-readable filled taxpayer questionnaire containing facts from forms such as W-2 and 1099-G plus other taxpayer answers.

The benchmark also has an expected completed return (`output.xml`) used as an answer key by the evaluator. The agent receives the input facts, not the answer key.

Useful abstraction:

```text
input.json   = exam question
output.xml   = hidden mark scheme
agent        = system taking the exam
```

The tutorial decomposes the task roughly as:

```text
raw taxpayer JSON
    ↓
LLM: inventory relevant facts
    ↓
Python: check inventory
    ↓
LLM: place facts onto destination tax-form fields
    ↓
Python: check placement structure/completeness
    ↓
LLM: externalise changing domain rules as code
    ↓
validate/test generated artifact
    ↓
Python: deterministic return arithmetic
    ↓
benchmark evaluation
```

## Source boxes vs destination lines

Important domain translation recovered during the walkthrough:

- **box** = a pre-labelled field on a source tax document, already present in the input;
- **line** = a destination field on the final tax return;
- the model's placement step decides how source facts map to destination lines.

The tax-specific names were distracting, so the transferable abstraction is:

```text
source field/value
    ↓
model mapping decision
    ↓
destination business field
```

## Validation strength — structural vs semantic

A major conceptual gain was distinguishing increasingly strong validation claims.

The lecturer's lightweight checks can establish things such as:

- an extracted numeric value existed somewhere in the source JSON;
- no source amounts were dropped or duplicated during placement;
- a destination line is from an allowed set;
- the model did not directly populate derived subtotal lines.

But these checks do **not** prove semantic correctness.

For example, a real source amount can still be mapped to the wrong valid destination line and pass structural checks.

Durable hierarchy:

```text
value existence check
    < source-attribution check
    < semantic/domain-placement correctness
```

Useful principle:

> Structurally valid does not imply semantically correct.

## Why the example is agentic

The taxpayer supplies relatively stable facts: income, withholding, filing status, dependants, deductions/allowances, etc. The difficult domain layer is deciding what those facts mean under potentially changing tax rules.

The transferable problem is therefore:

```text
facts
    ↓
changing / convoluted domain knowledge
    ↓
structured decisions and rules
    ↓
deterministic execution
```

The value of the model is not arithmetic. It is interpreting/mapping facts and supplying domain knowledge that would otherwise live in a large changing rules engine.

## Generated code pattern

The lecturer demonstrates:

```text
LLM recalls/interprets rule
    ↓
LLM emits Python source as text
    ↓
source is loaded into a callable
    ↓
known sample/test validates behaviour
    ↓
validated callable participates in deterministic computation
    ↓
final result is evaluated against benchmark ground truth
```

The learner understood the mechanism: model output is initially just text; Python can dynamically load that text into a callable (for example with `exec`).

However, this should **not** be internalised as the default production architecture.

## Production interpretation

Preferred default:

```text
LLM
    ↓
constrained JSON / rule configuration
    ↓
schema + semantic validation
    ↓
trusted application/API interprets the contract
    ↓
deterministic execution
```

Example mental model:

```text
LLM outputs bracket thresholds/rates as JSON
    ↓
POST to a narrow API/tool
    ↓
trusted calculator constructs/applies brackets
```

This keeps model-supplied knowledge separate from executable authority.

Generated source code itself is not always wrong, but executing arbitrary model-generated code with ambient production permissions is a strong antipattern.

A more defensible dynamic-code architecture is:

```text
chain state JSON
    ↓
isolated disposable sandbox
    ↓
LLM-generated program
    ↓
restricted compute / network / credentials
    ↓
validated JSON output
    ↓
main chain
```

Key security reframing:

> Do not ask only whether generated code is trusted. Ask what capabilities untrusted code can exercise if it behaves unexpectedly.

A sandbox can provide high programming flexibility with low real-world authority. The sandbox should be disposable and explicitly constrained by filesystem, network, secrets, CPU, memory and time limits.

## Current evidence boundary

Tutorial 1 is now **conceptually learned, implementation partially learned**.

Strong evidence:

- understands why one-shot prompting is used as a baseline;
- can explain parse → deterministic compute → explain;
- understands inventory vs placement vs derived computation;
- understands structural checks vs semantic correctness;
- understands generated code as an inspectable/testable artifact;
- can distinguish unsafe in-process dynamic execution from constrained sandbox execution;
- prefers structured contracts + trusted executors as the production default;
- can translate the tax example into a generic enterprise architecture.

Not established:

- line-by-line recall of the lecturer's compact TaxCalcBench notebook;
- independent reconstruction of the full tax workflow in LCEL;
- tax-domain knowledge itself (intentionally not a learning target).

## Next FTEC5660 step

Do not spend more time memorising US tax forms or reproducing the notebook syntax.

Next useful move:

1. cold-recall the architecture using a changed non-tax domain;
2. bridge from fixed sequential chains to routing/conditional paths;
3. revisit generated artifacts later only if a new mechanism (sandbox/tool routing/repair loop) is required.
