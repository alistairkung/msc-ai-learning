# FTEC5660 HW1 — Receipt Chain session 2

**Date:** 2026-09-22  
**Status:** Multimodal extraction vertical slice green for receipt 1; validation/batching/E2E remain

## Session objective

Continue the receipts homework from the green deterministic calculator. The learner explicitly requested a short cold LCEL/LangChain warm-up before introducing multimodal syntax, then aimed to get one real receipt image through DeepSeek into the structured extraction contract.

## Cold retrieval before new material

Changed-domain payment extraction was used rather than replaying the receipt implementation.

Retrieved immediately:
- chain architecture as `prompt | llm | output_parser`;
- `{payment_note}` as the prompt placeholder/upstream contract;
- `ChatPromptTemplate`;
- `JsonOutputParser`;
- `RunnablePassthrough.assign` conceptually as state-preserving enrichment;
- passing a runnable into `.assign(...)` rather than invoking it eagerly.

Needed correction / reminder:
- invocation initially used a raw string; the learner then re-established that a named placeholder expects a mapping such as `chain.invoke({"payment_note": ...})`;
- `JsonOutputParser()` needs an instance, not the class.

This is useful delayed retrieval evidence: the LCEL architecture and most component roles survived spacing, while invocation-map syntax remains a small fragility.

## Multimodal LangChain learning

The learner unpacked the supplied `image_data_url()` helper:

```text
JPEG -> read bytes -> base64 encode -> ASCII string
     -> data:image/jpeg;base64,... URL
```

New mental model:

```text
HumanMessage
  - text content block
  - image_url content block
```

The learner initially guessed that the image data URL belonged inside a normal text placeholder. After teaching the multimodal content-block distinction, they constructed the `HumanMessage` correctly and understood that a concrete message can be sent directly with `llm.invoke([message])`.

A disposable `spikes/multimodal_receipt.py` was written by the learner in the homework repo. Environment/import plumbing required incidental support: project-local `.venv`, requirements installation, module execution with `python -m`, and `.env` loading. These are not Agentic-AI conceptual gaps.

The first live spike succeeded: DeepSeek correctly described receipt 1, including the HK grocery context, subtotal/final rounded amount, bulk/percentage discounts and Octopus payment.

## Reusable extraction chain

The learner defined the component interface as:

```text
image path / image data URL
    -> receipt extraction component
    -> structured receipt JSON / Python dict
```

The extraction prompt was collaboratively refined around the learner's v0 contract. Important constraints include:
- positive pre-discount `original_line_amount`;
- use receipt-provided extended line totals when quantity is shown;
- positive discount magnitudes;
- discounts may be item- or receipt-level without inventing associations;
- signed rounding;
- final post-rounding amount;
- exclude wallet/card/payment-balance metadata;
- use `null` for unreadable required monetary values rather than silently coercing uncertainty to zero.

The learner understood why `null` creates a later validation responsibility rather than allowing silent incorrect arithmetic.

The assistant generated low-value test/fake scaffolding in `test/test_receipt_extractor.py` and an unimplemented `lib/receipt_extractor.py` builder. The learner then implemented the reusable chain:

```text
multimodal ChatPromptTemplate
    | llm
    | JsonOutputParser()
```

with runtime contract `{"image_url": "..."}`.

The learner correctly used `ChatPromptTemplate.from_messages(...)`, a runtime `{image_url}` placeholder inside the image content block, and `JsonOutputParser()`.

### Test/debugging evidence

Initial extractor tests failed because the prompt contained literal JSON braces, which collided with ChatPromptTemplate's format placeholders. Escaping literal JSON braces as `{{` / `}}` fixed template parsing.

One remaining test failure was caused by the assistant-written test incorrectly comparing pre-render template text (escaped braces) with rendered message text. The test was corrected to assert semantic prompt content rather than byte-for-byte source-template identity. All three extractor contract tests then went green.

This preserves an important evidence boundary: the learner's chain implementation was conceptually correct; one implementation issue was newly taught template escaping, and one failure was in generated test scaffolding rather than learner code.

## Live structured extraction and model configuration failure

The first real structured extraction initially failed at `JsonOutputParser` because DeepSeek returned empty `.content`.

The learner inspected the raw `AIMessage`. Evidence showed:
- at `max_tokens=500`, all 500 completion tokens were reasoning tokens;
- at 2,000, all 2,000 were reasoning tokens;
- at 6,000, all 6,000 were reasoning tokens;
- each run ended with `finish_reason='length'` and empty final content.

The reasoning trace showed the model repeatedly transcribing, reconciling, manually summing, debating grouping/descriptions and re-checking receipt semantics. Increasing token budget was therefore rejected as the architectural fix.

The model configuration was investigated and thinking/reasoning was disabled for this extraction task. With non-thinking extraction, the same prompt immediately returned valid JSON.

Transferable lesson:

> Model reasoning mode is part of responsibility allocation. For this stage, the LLM should interpret/transcribe/normalise the visual receipt; deterministic Python owns arithmetic/reconciliation.

## Receipt 1 live baseline

The first non-thinking structured extraction matched the manually established receipt-1 values:

- original positive item-line total: 480.20;
- discount total: 85.48;
- subtotal after discounts: 394.72;
- rounding: -0.02;
- final amount paid: 394.70.

It also correctly:
- kept repeated items as repeated lines;
- used extended quantity totals;
- returned discounts as positive magnitudes;
- retained the receipt-level 5% discount;
- excluded wallet/payment metadata.

This is one-receipt live-model baseline evidence only. It does **not** establish generalisation to the other public receipts or unseen grading receipts.

## Validation design discussed but not implemented

The next boundary was designed conceptually:

```text
DeepSeek
  -> JsonOutputParser
  -> untrusted extraction dict
  -> validation + normalisation
  -> trusted receipt representation
  -> ReceiptCalculator
```

Planned validation responsibilities:
- required structure/types;
- non-null required monetary fields;
- positive original line amounts;
- non-negative discount magnitudes;
- Decimal normalisation;
- reconciliation:
  - sum(original lines) - sum(discounts) == subtotal_after_discounts;
  - subtotal_after_discounts + rounding == amount_paid_after_rounding.

Initial failure policy should be simple and explicit: fail/raise rather than silently repair. Retry/reflection/routing should be added only if batch evaluation produces evidence that they are needed.

## Evidence boundary

Strong same-session evidence:
- delayed retrieval of core LCEL composition and prompt/assign concepts;
- successful transfer from text-only prompt placeholders to multimodal content blocks after teaching;
- learner-authored working raw multimodal spike;
- learner-authored reusable multimodal extraction chain;
- understanding of image data URL transport;
- diagnosis through stage-localised evidence rather than random prompt changes;
- understanding that reasoning mode was misallocated for an extraction/transcription stage.

Still guided/new:
- multimodal message syntax was taught this session;
- invocation mapping needed one cold-recall correction;
- literal-brace escaping in ChatPromptTemplate was newly encountered;
- fake-model/pytest scaffolding was assistant-generated;
- DeepSeek reasoning-mode configuration was researched/taught rather than independently recalled;
- validation/normalisation is designed but not implemented;
- no batching, all-receipt evaluation, `hw1.py` orchestration or final E2E run yet.

Do not promote this to delayed cold-independent multimodal LangChain mastery.

## Next session

1. Implement and test validation + Decimal normalisation.
2. Connect extraction -> validation -> already-green calculator.
3. Batch/process the receipt folder.
4. Wire the path into the homework's `build_chain()` / `answer_queries()` interface.
5. Run the full public eval and localise failures per receipt/stage.
6. Make one evidence-driven prompt/architecture iteration if needed.
7. Only add retry/routing/reflection if validation/eval evidence justifies the complexity.
8. Cleanup, full tests and final submission run.

Estimated remaining focused work: approximately **2.5–3.5 hours**, with multi-receipt model behaviour now the main uncertainty.
