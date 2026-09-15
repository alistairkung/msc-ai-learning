# FTEC5660 HW1 — Receipt Chain project plan

**Date:** 2026-09-15  
**Status:** Next active Agentic AI project; architecture direction chosen, implementation not started

## Assignment context

The separate `alistairkung/FTEC5660` repository is a fork of Homework 1. The assignment supplies supermarket receipt images and asks for two aggregate answers:

1. total amount actually spent, where amount spent is the final payment after receipt rounding;
2. total amount that would have been paid without discounts, where discounts/promotions/coupons/member/app/packaging-damage/percentage discounts are added back but rounding is not.

The starter intentionally leaves only `build_chain()` and `answer_queries()` for the student solution and requires the vision-capable `deepseek-v4-flash-vision-exp` model. Grading uses unseen receipt folders.

The lecturer explicitly allows GenAI for the assignment; the learner nevertheless wants to use the homework as a genuine engineering/learning project rather than merely generate the two missing functions.

## Learner's initial architecture hypothesis

The learner independently proposed the following decomposition after Tutorial 1:

```text
receipt JPEG
    ↓
vision-capable LLM
    ↓
structured receipt artifact
    - line items / prices
    - discounts or other relevant monetary facts
    ↓
deterministic Python
    ↓
per-receipt totals
    ↓
deterministic aggregation across receipts
    ↓
two required answers
```

This is promising transfer of the Tutorial 1 principle:

> Use the LLM to interpret variable/visual information; once the problem is represented as numbers with known semantics, prefer deterministic code for arithmetic.

The exact extraction schema is **not yet decided**. In particular, do not prematurely assume every discount maps neatly to one line item. The assignment includes multiple discount types, so the public receipts should be inspected to determine whether discounts need to be first-class receipt entries or can reliably be attached to items.

## New technical learning target — multimodal LangChain input

The learner has not yet covered how images are passed to chat models through LangChain and explicitly wants this broken down rather than cargo-culted.

Planned mini-lesson / spike:

```text
receipt.jpg
    ↓
read bytes
    ↓
base64 encode
    ↓
data:image/jpeg;base64,...
    ↓
multimodal human message
    - text block
    - image block
    ↓
ChatDeepSeek vision model
    ↓
inspect raw response
```

Start with **one receipt → one raw model response** before building the complete chain.

## Development philosophy — TDD + evals early

The learner wants old red/green/refactor instincts to guide the project. Establish a guiding integration-level contract/evaluation early rather than developing by prompt eyeballing.

Keep two feedback loops distinct:

### Deterministic software loop

```text
integration/unit test red
    ↓
implementation
    ↓
green
    ↓
refactor
```

Use fake/stubbed model outputs where appropriate so deterministic validation, calculation and aggregation can be tested without API/network variance.

### Model-system eval loop

```text
simple model baseline
    ↓
run public eval set
    ↓
record field/stage failures
    ↓
form a hypothesis
    ↓
change prompt/architecture
    ↓
rerun evals
```

Do not treat live-model evals as deterministic pytest tests.

The supplied public ground truth is especially useful because it contains both final aggregate answers and per-receipt values for amount paid after rounding, subtotal before rounding, discount total and amount without discounts. Use this for failure localisation rather than only checking the final aggregate.

Public receipts are a development/evaluation set, **not evidence of generalisation**; grading uses unseen receipt folders. Avoid prompt logic tailored to the seven known receipts.

## Collaboration / evidence boundary

The learner wants to own:

- architecture and component responsibilities;
- intermediate contracts;
- deterministic vs probabilistic boundaries;
- where unit/integration tests belong and what behaviour they should assert;
- evaluation strategy;
- failure analysis and architecture changes.

The assistant may generate low-learning-value scaffolding when directed, including:

- pytest syntax/boilerplate;
- fixtures;
- fake models/mocks;
- repetitive test cases;
- evaluation-runner plumbing.

If scaffolding requires an unresolved design decision, surface it to the learner rather than silently choosing it. Generated boilerplate is not evidence that the learner independently knows the syntax.

## Project budget

Target approximately **9 focused hours**, with a **12-hour hard ceiling** to avoid over-engineering a small homework.

High-value objective is not repository polish; it is the engineering cycle:

```text
design → implement → evaluate → localise failure → change architecture → evaluate again
```

## Planned first session (~3 hours)

1. Re-read assignment contract and sketch system boundary.
2. Design the intermediate receipt extraction contract collaboratively; learner leads.
3. Learner specifies the first guiding integration test and important deterministic cases; assistant can scaffold pytest/mocks.
4. Multimodal LangChain mini-lesson and one-JPEG DeepSeek spike.
5. Observe raw model behaviour before over-designing prompts/schema.
6. Establish the simplest reasonable structured-extraction baseline.
7. Run against public receipts / ground truth and record baseline failures.

## Likely later work

- deterministic receipt calculator and aggregation;
- schema/semantic validation boundaries;
- unit tests for arithmetic/rounding/discount edge cases;
- integration tests for component contracts;
- per-receipt model eval report;
- prompt iteration based on observed failure categories;
- consider reflection/routing/repair only if baseline evidence justifies the added complexity;
- final implementation must continue to satisfy the homework's `build_chain()` / `answer_queries()` interface and unseen-folder requirement.

## Next prompt for tutoring

Begin with the system contract and extraction schema. Do **not** write the homework solution immediately. Ask the learner to decide what information one successful receipt extraction must contain so downstream Python can answer both questions without looking at the image again. Then inspect representative public receipts specifically to test whether that proposed contract can represent their discount/rounding structures.
