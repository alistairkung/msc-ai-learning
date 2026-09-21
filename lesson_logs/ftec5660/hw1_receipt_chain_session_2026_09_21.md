# FTEC5660 HW1 — Receipt Chain session 1

**Date:** 2026-09-21  
**Status:** Deterministic half designed and green; multimodal extraction not yet implemented

## Session objective

Begin the receipts homework as a small LLM-engineering project rather than filling the two starter functions immediately. The learner wanted an early red/green feedback loop and to own architecture/test intent while delegating low-value fixture and pytest scaffolding.

## Contract discovery from real receipts

The learner inspected public receipt images and identified original item amounts, discounts, receipt subtotal/balance, rounding, and wallet/payment-balance lines. They separated purchase facts from wallet metadata and proposed printed receipt totals as validation evidence.

A key architecture decision: the printed final amount after rounding is authoritative for Q1 rather than being reconstructed from every item and discount.

The initial item-centric discount schema was pressure-tested against receipt 4. The learner noticed a receipt-level 5% coupon/discount, showing that not every discount can be attached cleanly to one item. Discounts therefore became first-class receipt entries rather than necessarily item-owned.

Quantity lines were also inspected. Where a receipt shows quantity, the corresponding positive amount is already the line total. The contract therefore uses `original_line_amount`, not unit price × quantity, avoiding unnecessary reconstruction.

## Extraction contract v0

ReceiptExtraction:
- `items[]`: `description`, `original_line_amount`
- `discounts[]`: `description`, `discount_amount`
- `subtotal_after_discounts`
- `rounding`
- `amount_paid_after_rounding`

Semantic decisions:
- `original_line_amount` is the positive pre-discount line amount, already incorporating quantity where the receipt does so;
- `discount_amount` is a positive magnitude even if the receipt prints a negative adjustment;
- description is retained for traceability/debugging/future extensibility rather than arithmetic;
- `amount_paid_after_rounding` is authoritative for Q1;
- Q2 is the sum of original positive item line amounts;
- discounts, subtotal and rounding are primarily reconciliation/debugging evidence.

Core calculations: Q1 = sum of receipt `amount_paid_after_rounding`; Q2 = sum of all item `original_line_amount` values.

## Testing architecture

The learner distinguished three feedback levels: real-image E2E eval to `results.csv`; deterministic integration test from known extracted receipt artifacts to both query totals; and smaller unit tests for deterministic calculation/validation behaviours.

The supplied homework runner already covers much of the outer E2E/evaluation harness, so no duplicate E2E framework is needed.

For the first deterministic integration test, the learner chose public receipts 1 and 2. The assistant generated/transcribed fixture boilerplate after the learner demonstrated the fixture idea manually. This generated fixture content is not evidence of independent receipt transcription skill.

Expected aggregate behaviour: receipt 1 paid 394.70 / original positive lines 480.20; receipt 2 paid 316.10 / original positive lines 392.20; therefore Q1 = 710.80 and Q2 = 872.40. The fixture also reconciles exactly against known discount/subtotal/rounding values.

## Deterministic calculator implementation

A separate homework branch, `hw1-receipt-calculator-scaffold`, contains `lib/receipt_calculator.py` and `test/test_receipt_calculator.py`. The assistant scaffolded the files/test fixture; the learner implemented the calculator.

The learner's first implementation correctly traversed receipts -> receipt -> items -> item and accumulated the authoritative final paid amount separately. The first green attempt exposed a floating-point money issue: `872.3999999999996 != 872.40`.

The learner chose Python `Decimal` inside the calculator rather than weakening the assertion with approximate float comparison. `Decimal(str(value))` was explained as converting through the decimal string representation rather than preserving the underlying binary float approximation. The pushed calculator is green for the guiding receipts 1+2 integration test.

### Current implementation-quality note

The algorithm is clear and idiomatic enough for the current stage. One cleanup remains: the calculator return annotation still says `dict[str, float]` even though it returns `Decimal` values.

A future boundary improvement is to move float/string -> `Decimal` normalisation into validation/normalisation so the calculator can assume trusted money-domain values. Do not refactor this before the extraction boundary exists merely for architectural neatness.

## Learner-owned evidence

Strong same-session evidence:
- independently transferred Tutorial 1's LLM-vs-deterministic decomposition to a new multimodal receipts domain;
- identified authoritative vs reconciliation data;
- noticed receipt-level discounts and revised the schema rather than forcing item-level structure;
- chose line-total semantics that avoid unnecessary quantity reconstruction;
- designed the deterministic integration-test boundary and expected behaviour;
- implemented the deterministic multi-receipt calculator after scaffolding;
- recognised that Q1 should use the authoritative printed post-rounding total;
- chose exact decimal arithmetic after the test exposed float accumulation error.

Support / generated scaffolding:
- assistant generated pytest/file scaffolding and transcribed the two receipt fixtures after the learner demonstrated the idea;
- assistant guided the initial loop correction from iterating `receipts` to `receipt["items"]`;
- assistant highlighted that discounts are not required inputs to either authoritative calculation;
- `Decimal` construction details were taught during debugging.

## Evidence boundary

This is **same-session architecture transfer + learner implementation evidence**, not delayed cold LangChain mastery.

No multimodal LangChain call, DeepSeek extraction chain, structured parser, validation/normalisation boundary, batching or end-to-end homework run was implemented in this session. The receipt contract is v0 and should change if live evaluation exposes a concrete failure.

## Next session

The learner explicitly prefers to resume with a short **cold recall of existing LangChain syntax** before adding multimodal extraction.

Recommended sequence:
1. 15–20 minute changed-example cold recall of `ChatPromptTemplate`, placeholder/input contracts, model -> `JsonOutputParser`, `.invoke({...})`, brief `RunnablePassthrough.assign` / `RunnableLambda`, and callable vs invocation (`fn` vs `fn()`).
2. Introduce one new mechanism: multimodal human message containing text + receipt image/data URL.
3. Get one receipt image -> raw DeepSeek response working.
4. Constrain one-receipt output into v0 `ReceiptExtraction`.
5. Add validation/normalisation, including the money representation boundary.
6. Batch independent receipt extractions.
7. Feed `list[ReceiptExtraction]` into the already-green deterministic calculator.
8. Run the public E2E eval, localise failures, and make one evidence-driven iteration before adding routing/reflection/repair complexity.

Estimated remaining focused work: approximately **3.5–4.5 hours**, with API/model behaviour the main uncertainty.
