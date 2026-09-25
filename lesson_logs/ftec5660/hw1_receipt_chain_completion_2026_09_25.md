# FTEC5660 HW1 — Receipt Chain completion and post-submission extraction

**Date:** 2026-09-25  
**Status:** Homework implementation complete and submitted; public E2E green; post-submission standalone refactor started

## Session outcome

The receipts homework moved from a one-receipt multimodal baseline to a complete evaluated pipeline.

Final homework architecture:

```text
receipt image
  -> multimodal extraction
  -> JsonOutputParser
  -> deterministic ReceiptValidator
       - structure / presence
       - Decimal normalisation
       - sign/domain checks
       - arithmetic reconciliation
  -> validation-gated semantic retry
  -> raw extraction fallback if retries exhaust
  -> deterministic ReceiptCalculator
  -> exact Q1/Q2 response format
  -> results.csv
```

The final public run processed all seven receipts, all seven validated on that run, 27/27 deterministic tests passed, and the public answers were correct:

- amount paid: HK$1974.30;
- amount without discounts: HK$2348.20.

The submitted repository was then frozen. A separate `receipt-agent` repository was created for post-submission refactoring so experimentation does not alter the submitted work.

## Validator implementation

The learner first defined the validator contract and implemented most of the structure/presence mechanics themselves before explicitly asking to skip repetitive private-function implementation.

The validator now:
- requires the expected top-level, item and discount fields;
- rejects required null values;
- deep-copies and normalises known monetary fields to `Decimal`;
- accepts zero-value item/discount marker lines but rejects negative item/discount values;
- rejects negative subtotal/final paid values;
- reconciles `sum(items) - sum(discounts)` with the printed subtotal;
- reconciles `subtotal + rounding` with final paid.

Important evidence boundary: the learner independently developed the overall validator shape and nested `all(...)` pattern with support/correction. The assistant supplied the later repetitive sign/reconciliation helper implementations at the learner's explicit request. This is implementation evidence, not a claim of cold independent reconstruction of every helper.

A real batch exposed that the original `item > 0` invariant was too strict: receipts contained legitimate zero-value markers such as COUPON/VCODE. The invariant was changed to non-negative, and explicit zero-value regression tests were later added. This was an evidence-driven domain correction rather than speculative cleanup.

## Batch evaluation and model failure localisation

The first multi-receipt run produced only 3/7 valid receipts. After correcting the zero-value invariant, subsequent runs exposed genuine stochastic extraction failures.

Observed failures included:
- a real line amount being read as zero on one run;
- quantity lines being interpreted as per-unit prices rather than extended totals;
- the same image producing different numeric interpretations on repeated calls.

The validator was therefore useful as a semantic quality gate: parseable JSON was not treated as trustworthy merely because it had the right shape.

The quantity rule in the extraction prompt was strengthened only after this failure mode appeared:

```text
quantity > 1
-> original_line_amount is the total for the full purchased quantity
-> do not return unit price
-> do not divide the displayed line total
-> prefer an explicit extended line total
```

## LCEL composition and retry

A useful design disagreement was resolved through implementation.

The learner wanted validation/retry to remain part of the LangChain composition rather than moving immediately to an ordinary Python retry loop. The final per-receipt chain became conceptually:

```text
prompt
| llm
| JsonOutputParser
| RunnableLambda(validator.validate)
.with_retry(...)
```

This proved to be a good fit: validation raises `ValueError`, and retry re-runs the whole probabilistic extraction rather than re-validating the same bad dict.

This is meaningful changed-domain LCEL transfer. It should still not be recorded as blanket cold mastery of the broader Runnable API or Routing syntax.

## Availability vs correctness trade-off

The lecturer stated that grading would run the script once and that crashing without producing `results.csv` was worse than returning an imperfect answer.

That changed the failure policy.

The final homework exposes:
- a validated/retrying chain as the preferred path;
- a raw extraction chain as a graceful fallback after semantic retries exhaust.

Batch orchestration catches exhausted validation per receipt, uses a raw best-effort extraction, continues the remaining folder, and still writes the final CSV.

The learner explicitly reasoned about this as a system-design trade-off rather than treating validator failure as automatically fatal.

## Final integration and submission packaging

The homework starter's `build_chain()` and `answer_queries()` were completed. The learner recognised that the extraction LCEL was already encapsulated behind `build_receipt_extraction_chain`, then pushed further to compose validation/retry into the runnable itself.

The lecturer required the submitted implementation to live in one Python file. The clean modular extractor/validator/calculator implementation was therefore flattened into `hw1.py` as a submission constraint. Tests were repointed to the single-file implementation and remained green.

Final local verification:

```text
python -m pytest
27 passed

python hw1.py --image-folder public_test
7 receipts processed
Q1 HK$1974.30 correct
Q2 HK$2348.20 correct
```

The learner also noted that `python -m pytest` reliably resolves the repository root in this environment whereas the bare `pytest` executable did not.

## Post-submission refactor

After submission, the learner deliberately separated experimentation from assessed work by creating a new standalone `receipt-agent` repository from the pre-flattened architecture.

The new direction:
- explicit README attribution to the FTEC5660 homework fork/course scaffold;
- remove the homework-specific runner;
- restore modular extractor / validator / calculator boundaries;
- add a standalone `receipt_agent` package and `python -m receipt_agent <folder>` CLI;
- put integration/retry/fallback into a dedicated `ReceiptPipeline`;
- preserve deterministic tests and add pipeline-level tests.

This is a useful software-engineering reflection: the single-file submission shape is not being mistaken for the preferred architecture.

## Reflection / transferable learning

The learner's own reflection was that AI made writing straightforward code to a clear specification dramatically faster, including repetitive validator/test implementation. However, the important work remained:
- deciding which responsibilities belong to the LLM versus deterministic code;
- defining a data contract;
- designing invariants that can detect plausible-but-wrong model output;
- changing an invariant when real receipt semantics disproved it;
- deciding when retries are justified by stochastic behaviour;
- deciding when availability should beat strict fail-closed correctness;
- shaping LCEL composition rather than merely accepting generated glue code.

This session therefore provides stronger evidence for **system decomposition and changed-domain LCEL transfer** than for independent recall of every Python/LangChain API detail.

## Evidence boundary

Strong evidence today:
- learner-owned validator architecture and trust-boundary reasoning;
- live failure localisation using arithmetic invariants;
- evidence-driven correction of zero-value and quantity assumptions;
- recognition that validation should gate semantic retries;
- changed-domain use of `RunnableLambda` + `.with_retry()` after challenging an initially more conservative orchestration proposal;
- explicit availability/correctness trade-off for a one-shot grader;
- successful E2E integration, deterministic tests and public evaluation;
- post-submission separation of course artifact from a cleaner standalone architecture.

Still not claimed:
- delayed blank-file reconstruction of the full multimodal/validator chain;
- cold recall of all LCEL/Runnable syntax;
- `RunnableBranch` implementation mastery;
- generalisation beyond the public receipt distribution merely because the public run is green.

## Next learning step

Receipts leaves the active assessed-work lane. Do not keep polishing it for mastery evidence.

Return to the planned JIT sequence:
1. brief regression retrieval;
2. decision trees;
3. random forests;
while the FTEC5660 hackathon remains the next delivery pressure.
