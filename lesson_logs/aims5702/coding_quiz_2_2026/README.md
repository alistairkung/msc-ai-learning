# AIMS5702 Coding Quiz 2 — front-loaded exam-focus plan (27 Nov–3 Dec 2026)

**Lecture-grouped technical MCQ index:** [Browse all 68 questions by primary lecture](ATTENDANCE_LECTURE_MAP.md) (L02/L03/L05/L06/L07/L09).

**Daily technical MCQ bank:** [68 inversion/alternative-concept questions, student-facing](ATTENDANCE_SWITCH_BANK.md) · [hidden answer key and distractor audit](ATTENDANCE_SWITCH_KEY.md) · [machine-readable JSON](ATTENDANCE_SWITCH_BANK.json). The [original 20-screenshot/18-stem transcript](TECHNICAL_ATTENDANCE_BANK.md) remains the provenance record. Use the new bank for daily altered-option practice; only the **exact-option** items simulate the lecturer's retained A–D constraint.


**Updated 28 Nov (actual GPU session):** the dedicated GPU tutor taught and assessed the CUDA execution model plus 1D/2D PyCUDA indexing/launches, with a late **ceiling-division error in the integrated wrapper**. **Triton remains only conceptually introduced; FlashAttention not taught; ONNX code not yet assessed.** Full reported evidence: [28 Nov GPU session log](../quiz2_gpu_concepts_pycuda_2026_11_28.md). The tutor's local CP01–04 names are **not** master tensor CP01–04; map these results to master **CP17/18**. The weekend plan now uses a short CUDA retrieval instead of repeating the whole tutorial, then Triton + ONNX + FlashAttention concepts. CNN/Transformer conceptual review remains requested, especially Transformers. An evening rest after reported fatigue is reasonable; do not treat unfinished sessions as performance failures.

**Latest coordinator revision, 27 Nov:** front-load the **three lecturer-signalled coding areas (ONNX, PyCUDA, Triton)** into **Sat 28–Sun 29 Nov**. Change the old sequential plan: fully connected/CNN mathematical foundations are **not removed**, but move to Mon 30 Nov, with short cold retrieval on Tue 1 Dec and in the mock. AIMS5702 Quiz 2 is **Thu 3 Dec**.

## Assessment framing — lecturer hints, not an official question paper

- **50 marks / 60 min**: **16 MCQs worth 24 marks** and **26 marks code/comment/numeric blanks**.
- Lecturer indicated **8 ethics MCQs + 8 technical MCQs**. Reportedly **at least six of those eight technical MCQs** will vary the last two lectures' attendance questions **while keeping their A–D options unchanged**. For robust training, *practise all eight technical questions daily as variations from* [the attendance bank](TECHNICAL_ATTENDANCE_BANK.md), but do **not** present all eight as guaranteed by the lecturer. Rotate **all 18 distinct stems from 20 uploaded screenshots**. Occasionally replace two technical drills with fresh source-grounded items to cover the non-guaranteed remainder.
- Lecturer strongly pointed to **ONNX, PyCUDA, Triton** as coding-blank areas (reported Q3, Q4, Q5 of five coding questions). This is the reason for prioritising their independent reproduction **by Sunday 29 Nov**; numbering and actual contents are not guaranteed.
- The lecturer also emphasised FC/CNN weight sizes, layer output shapes, parameter counting, pooling, CNN transfer learning, CUDA thread index/block/grid, Triton masked loads/stores, and LSTM tanh. Avoid dedicated `einsum`, SIMD or convolutions with nontrivial stride calculations; bilinear interpolation is deprioritised; FlashAttention deep kernel implementation is not a priority.

## Daily coordinator schedule

| Date | Coding Window B | Concepts Window A |
|---|---|---|
| [Fri 27 Nov](2026-11-27.md) | **CP01–03 tensor consolidation already reported completed**; no additional full tensor workshop. Ethics preparation priority for the remainder. | Teach L07 ethics risk-level table and examples + **8 changed attendance-bank technical questions**; 8 taught ethics questions if time |
| [Sat 28 Nov](2026-11-28.md) | **Done (reported): GPU concepts and PyCUDA 1D/2D**, with integrated ceiling division still fragile. ONNX/Triton not completed. | No separate technical/ethics MCQ result reported for 28 Nov |
| [Sun 29 Nov](2026-11-29.md) | **Triton essential code + short CUDA recall**; **ONNX export/verification** still outstanding; FlashAttention concepts if time. | Daily changed attendance MCQs + short EU/HK delayed ethics recall if time |
| [Mon 30 Nov](2026-11-30.md) | **Mandatory FC/CNN shapes and trainable parameter counts**; stable softmax/training loop as time permits; any unfinished ONNX cold scaffold | 8 ethics + 8 changed technical MCQs; bounded CNN/Transformer conceptual review if not completed earlier |
| [Tue 1 Dec](2026-12-01.md) | **Transformer conceptual review** (especially rusty points), delayed CUDA/Triton/ONNX cold code fragments, plus weakest FC/CNN gaps | 8 ethics + 8 changed technical MCQs |
| [Wed 2 Dec](2026-12-02.md) | **60-minute exam-shaped mock** with 16 MCQs and 26 code/numerical marks; targeted repair only. AIMS5701 poster discussion. | Mock replaces separate daily MCQ practice |
| [Thu 3 Dec](2026-12-03.md) | Brief familiar code/shape/ethics recall, not new lessons; evening Quiz 2. | Optional short recall only |

## Sunday night milestone — evidence, not intuition

- **ONNX:** unhinted completion of a model export + numerical output comparison scaffold, correctly identifying important export / inference / comparison lines.
- **PyCUDA:** unhinted `SourceModule` C kernel string (global index, guard, operation), host function and shape-correct block/grid launch; one changed problem.
- **Triton:** unhinted `@triton.jit`, `tl.program_id`, `tl.arange` offsets, mask, `tl.load`/`tl.store`, grid and launch on a changed operation.
- Mark **demonstrated cold**, **guided**, **not attempted**, and **still incorrect** separately. Exposure alone is not mastery. Any gaps get **targeted Tue 1 Dec repair**, not an entire lost day.

## Daily MCQ method — vary wording, not answers by rote

The 20 screenshot images contain **18 distinct question themes** and two repeated captures. Each day's 8 technical MCQs should draw from the [bank](TECHNICAL_ATTENDANCE_BANK.md) with **unchanged A–D texts**, new *valid* stems and checked single correct answers. Record the bank ID and changed premise; spaced retrieval should adapt the reasoning, not simply memorise answer letters. AQ01 original broadcasting problem has two valid choices; AQ09's BatchNorm/eval shorthand is not true for LayerNorm: apply the bank's quality safeguards.

Ethics: eight questions use the L07 slides/transcript, with original **EU risk-level tables and examples**, HK Government framework and mainland China distinctions; [ETHICS_EXAM_SCOPE.md](ETHICS_EXAM_SCOPE.md) sets the taught boundary. The source hierarchy is **lecture content first**, lecturer-linked EU/HK pages supporting, no untaught legal nuance.

## Study style and scope boundaries

Two separate windows: coding is worked full example → guided variation → **cold independent** answer → changed transfer; MCQs require a genuinely cold first answer then a reasoned review. **Full explanations** after mistakes; don't advance until the student understands the correction. The user reports repo `AGENTS.md`-driven tutor behaviour was too terse; new tutor handovers should **explicitly provide this teaching style** and can use only the required source PDFs/plan, not inherit irrelevant agent rules.

Workshops may be split; coding **2–3h maximum target if capacity permits**, concepts 30–60min. Weekend triad has first priority; remaining coursework commitments (FTEC HW4 due 1 Dec, AIMS5701 poster display 2 Dec) remain bounded. No missed-time debt.

Historical evidence: Tue 24 Nov partial tensor workshop; **Fri 27 Nov user's handover** reports new independent CP01–03 improvements and **4/5 independently correct steps** on mixed transfer, with final `argmax` corrected after explanation. This reported handover has not yet been independently entered into `LEARNING_STATE.md`; do not silently promote to durable mastery. See dated [27 Nov file](2026-11-27.md).

Tutor source selection: repository `SESSION_WORKFLOW.md` and `TUTORING_CALIBRATION.md` provide bookkeeping conventions, but **the user prefers longer worked explanations**. If a new tutor is not doing GitHub bookkeeping, the coordinator can provide a direct handover without loading the whole repo. Coverage ledger: [COVERAGE_MATRIX.md](COVERAGE_MATRIX.md).
