# Learning State — Current Handover

_Last maintained: 2026-09-15. Learning evidence through 2026-09-15._

Read `SESSION_WORKFLOW.md` for tutoring rules. `learning_progress.yaml` is the structured dashboard projection; focused lesson/course notes remain the detailed evidence source. Do not infer mastery from code presence alone.

## Three parallel commitments

| Lane | Next useful work | Why / boundary |
|---|---|---|
| Continue | **FTEC5660 HW1 receipt-chain engineering project** | Apply Tutorial 1 principles to a real multimodal assignment: image → structured artifact → validation/deterministic compute → aggregation, with TDD/evals established early. Learn multimodal LangChain input explicitly. |
| Parallel | **AIMS5702 representation translation + light tensor maintenance** | Shape reasoning remains the anchor; train diagram ↔ shapes ↔ indices ↔ PyTorch when course work resumes. |
| Protect | **Search theory + a small relevant maths retrieval block** | Search implementation is complete through Lesson 33 but guarantees/complexity remain due; keep January AIMS5704 prerequisites alive without a broad restart. |

These lanes coexist; they are not one sequential queue.

## FTEC5660 / LangChain — current trajectory

Detailed sources:

- `lesson_logs/lesson32_lcel_basics.md`
- `lesson_logs/ftec5660/tutorial01_study_plan.md`
- `lesson_logs/ftec5660/lesson34_stateful_lcel_2026_09_14.md`
- `lesson_logs/ftec5660/lesson35_tutorial01_architecture_2026_09_14.md`
- `lesson_logs/ftec5660/hw1_receipt_chain_project_plan_2026_09_15.md`

### Established before HW1

Lesson 34 stateful LCEL practice is green with guided implementation evidence. Current mental models:

- `RunnablePassthrough.assign` preserves the current state dictionary and adds a runnable result under a named key;
- `RunnableLambda` adapts ordinary deterministic Python into an LCEL runnable stage;
- validation gates return the same state on success and fail loudly on invalid contracts;
- prompt output requirements, parser output, validator expectations and deterministic Python inputs must align;
- callable timing (`fn` vs `fn()`) remains a recurring Python/LCEL implementation fragility and should be sampled later with a changed example.

Tutorial 1 is **conceptually learned, implementation partially learned**. Durable architecture principles:

```text
messy / variable representation
        ↓
LLM: interpret / extract
        ↓
structured artifact
        ↓
Python: validate
        ↓
LLM only where further variable/domain interpretation is needed
        ↓
Python: validate / deterministic execution
        ↓
result
```

Current heuristic:

> Use the LLM where variability or ambiguity requires interpretation; use deterministic software once the problem has become deterministic.

The learner understands:

- parse → deterministic compute → explain;
- inventory vs placement vs derived computation;
- decomposition for failure localisation;
- structurally valid does not imply semantically correct;
- model-generated code can externalise knowledge into an artifact, but `exec(llm_output)` in the production process is not the preferred default;
- preferred production pattern is constrained structured artifacts + validation + trusted executors;
- if dynamic generated code is genuinely useful, isolate it in a capability-constrained disposable sandbox rather than granting ambient production authority.

Evidence boundary remains: Lesson 34 is guided + green, not delayed cold-independent; the full TaxCalcBench LCEL implementation is not independently reconstructable and US tax mechanics are intentionally out of scope.

## New active goal — FTEC5660 Homework 1 Receipt Chain

The separate `alistairkung/FTEC5660` repository contains the forked assignment. The homework provides supermarket receipt images and asks for:

1. aggregate amount actually paid after receipt rounding;
2. aggregate amount that would have been paid without discounts, adding promotions/coupons/member/app/packaging-damage/percentage discounts back but not rounding.

Only `build_chain()` and `answer_queries()` are left for the student implementation; grading uses unseen receipt folders and requires the vision-capable `deepseek-v4-flash-vision-exp` model.

The lecturer explicitly permits GenAI. The learner's goal is nevertheless to treat the assignment as a small LLM-engineering project rather than simply generate the missing functions.

### Learner's initial architecture transfer

The learner independently proposed:

```text
receipt JPEG
    ↓
vision-capable LLM
    ↓
structured receipt artifact
    - line items / original prices
    - discount information
    ↓
deterministic Python arithmetic
    ↓
per-receipt totals
    ↓
deterministic aggregation
    ↓
two required answers
```

This is good changed-domain transfer of Tutorial 1's LLM-vs-deterministic responsibility split.

The extraction contract is **not final**. Do not silently assume every discount maps one-to-one to a line item; inspect representative public receipts to determine whether receipt-level/first-class discount entries are required.

### New technical target — multimodal LangChain

The learner explicitly wants to understand how JPEGs are fed to a vision model through LangChain rather than copy syntax blindly.

Planned spike:

```text
JPEG bytes
    ↓
base64 / data URL
    ↓
multimodal human message (text + image)
    ↓
ChatDeepSeek vision model
    ↓
raw response
```

Get **one receipt → one raw model response** working before building the full chain.

### Development approach — early red/green + eval loop

The learner wants a guiding integration-level test/evaluation in place early, in the spirit of red → green → refactor.

Maintain two distinct loops:

```text
DETERMINISTIC SOFTWARE
integration/unit test → implementation → green → refactor

MODEL SYSTEM
baseline → eval set → failure analysis → hypothesis → prompt/architecture change → rerun
```

Use fakes/stubs for deterministic integration tests rather than making live model calls part of ordinary pytest. Use the public per-receipt ground truth for model-system failure localisation, while remembering that the seven public receipts are a development/eval set and do not prove unseen generalisation.

### Collaboration boundary

The learner owns and should be actively questioned on:

- architecture;
- component responsibilities;
- intermediate contracts;
- deterministic vs probabilistic boundaries;
- where tests belong and what behaviour they should assert;
- evaluation strategy;
- diagnosis of failures and architecture changes.

The assistant may generate low-learning-value scaffolding when directed: pytest boilerplate, fixtures, fake models/mocks, repetitive cases and eval-runner plumbing. If scaffolding requires an unresolved design choice, ask rather than silently deciding. Generated scaffolding is not evidence of independent syntax mastery.

### Time budget

Target **~9 focused hours**, hard ceiling **12 hours**. Optimise for the engineering learning loop rather than turning the homework into an oversized platform.

### Next session

1. Re-state the assignment/system boundary.
2. Learner leads design of the one-receipt structured extraction contract.
3. Inspect representative public receipts to pressure-test that contract, especially discount/rounding representation.
4. Learner specifies a guiding integration test; assistant can scaffold pytest/mocks.
5. Teach multimodal LangChain message construction and run one-JPEG DeepSeek spike.
6. Establish a simple structured-extraction baseline.
7. Run early public evals and record stage-level failures before adding reflection/routing/repair complexity.

Do not write the full homework solution at the start of the next session.

## AIMS5702 — current state

Sources: `lesson_logs/aims5702/lecture01_02_prelecture_bridge.md` and `lesson_logs/aims5702/tensor_cold_review_2026_09_11.md`.

- Shape reasoning remains the primary anchor; index/diagram fluency should be trained as translation, not replacement.
- 11 Sep tensor review found strong broadcasting/reduction/semantic-shape reasoning with slicing/API rust that recovered quickly.
- `keepdim=True` and tuple-dimension reductions were newly introduced on 11 Sep.
- dtype memory, flat storage, stride/view/contiguity and basic einsum remain guided pre-read material rather than Lecture 1-covered material.
- Next substantive course review should train actual Lecture 1 diagram → shape → parameter-count → index/PyTorch translation.

## Search — implementation complete through Lesson 33, theory due

- BFS has strongest current independent evidence.
- DFS was reconstructed with refreshed/guided evidence.
- UCS/A* are implemented with passing practice tests but remain guided rather than cold-independent.
- Next search block: completeness/optimality, UCS non-negative-cost assumptions, A* admissibility vs consistency, goal popped vs discovered, and qualitative/formal complexity.

## Established foundations / remaining uncertainty

- **Python / NumPy / pandas:** substantial practice; syntax/API fluency can be less automatic than the learner's long-used backend languages. Callable timing remains a recurring implementation fragility.
- **Linear algebra:** historical JHU foundation established; retrieve selectively.
- **Probability/statistics:** strong historical evidence across major foundations; Markov chains/Poisson remain diagnostic-needed.
- **Calculus:** historical derivative/gradient/chain-rule/backprop foundation established.
- **Practical ML:** linear/logistic regression and train/validation/test workflow implemented; changed-task transfer still useful.
- **Agentic/LCEL:** Lesson 32 basics are partly cold-retrievable; Lesson 34 stateful composition/gates have guided passing implementation evidence; Tutorial 1 architecture is conceptually understood; HW1 now provides the active changed-domain multimodal application.
- **January extensions:** likelihood/MLE, exponential families, formal generalisation/concentration, convergence assumptions and proof-style derivations remain new work.

## Parked / must return

- **FTEC5660:** active through HW1 receipt-chain project. Routing/conditional workflows remain a later bridge; introduce them in HW1 only if evaluation evidence gives a genuine reason.
- **AIMS5701/search:** guarantees/complexity still due after the current Agentic AI block.
- **AIMS5702:** representation translation remains the next substantive course-specific review target.
- **Maths:** selective LA/calculus/probability maintenance; later MLE/formal-theory extensions.

## Handover discipline

After each substantive HW1 project block, update the focused HW1 log with architecture decisions, learner-owned reasoning, eval evidence, failures and next hypotheses. Update this handover when the project state materially changes. Do not promote generated scaffolding to learning evidence, and do not claim generalisation from the seven public receipts alone.
