# AIMS5702 Quiz 2 — L02/L03 concepts diagnostic, 24 November 2026

**Evidence:** learner-supplied handover from a dedicated Concepts Window A, taken as the session assessment record. These slide references come from that window's lecture review, **not independently reaudited against the original PDFs in this log**. [Planned question blueprint](coding_quiz_2_2026/2026-11-24.md). The unified 699-atom master audit was unavailable to the tutor; use the provided slide anchors, **not invented atomic IDs**.

## Status and score (original cold attempts)

- **MCQs: 24/24 attempted; 15 correct (62.5%), nine incorrect.**
- **Lecture 02: 8/12 cold; Lecture 03: 7/12 cold.** The designed mix was eight recall, ten applied, six numeric/multistep, but this log does not reconstruct per-question depth labels not supplied in the handover.
- **All nine misses received review and some changed follow-up exercises.** Those follow-ups are *same-session after teaching*; never add them to the 15/24 cold score or claim delayed retention.
- **Open questions: O1–O8 all unattempted.** O1 was shown, but no answer supplied; O2–O8 not shown. Preserve the original eight-task blueprint; replace numbers in O1 before any cold attempt.
- **Coding evidence:** none established by this concepts-only window. The separately planned CP01–CP04 tensor workshop was deferred; do not mark it completed.
- **Source boundary:** original L02/L03 slide references appear in the handover; the larger syllabus/master atomic index remains a separate Project artifact.

## Question-by-question original cold record

| ID | Lecture and slide anchors | Assessed operation | Original cold result |
|---|---|---|---|
| M01 | L02 10–11 | Signed int8 range/two's complement | **Miss:** C → B |
| M02 | L02 12–18 | Exponent range versus fraction precision | **Pass:** D |
| M03 | L02 9, 29–30 | Mixed-dtype weights and MiB capacity | **Miss:** reported 5 MiB/fits; correct 16 MiB/over capacity |
| M04 | L02 26–28 | Incompatible broadcasting | **Pass:** A |
| M05 | L02 39, 62 | Singleton placement for outer addition | **Pass:** D |
| M06 | L02 37–38, 45 | Boolean indexing and resulting shape | **Pass:** C |
| M07 | L02 48–52 | Reshape then axis-1 concat | **Pass:** B |
| M08 | L02 42–47 | Slice view mutation, advanced-index copy, contiguity | **Pass:** D |
| M09 | L02 40, 43–44 | Storage offset and final flat index | **Miss:** B → A; omitted known offset 10 from displacement 20 |
| M10 | L02 55–59 | Reduction axes, amax/argmax/keepdim | **Miss:** B → C; confused axis 1 with axis 0 |
| M11 | L02 60–62 | Pairwise row-dot-product `einsum` recognition | **Pass:** B |
| M12 | L02 68 | Named constants versus mutable module state | **Pass:** A |
| M13 | L03 5–8, 10 | RGB flattening and intensity scaling | **Miss:** A → D; scale correct, channel count omitted |
| M14 | L03 19–20 | One-hot *true target* versus predicted class | **Miss:** A → B; encoded prediction |
| M15 | L03 15, 33–34, 80–81 | Weight orientation and param count | **Miss:** C → A; 43 parameters correct, used PyTorch stored-weight ordering instead of specified input-first convention |
| M16 | L03 20–21, 77–81 | Hidden ReLU and final prediction | **Pass:** C |
| M17 | L03 20, 22–26 | True-class probability/cross-entropy | **Miss:** B → D; started vector subtraction |
| M18 | L03 22–26, 39 | Entropy vs cross-entropy | **Miss:** guessed D → C |
| M19 | L03 21–26 | Numerically stable max-shift softmax | **Pass:** B |
| M20 | L03 46–50 | Gradient direction and learning rate | **Pass:** A |
| M21 | L03 56–61 | Validation tuning and untouched test data | **Pass:** C |
| M22 | L03 68–73 | Epoch/update counts incl. partial batch | **Pass:** B |
| M23 | L03 52–55, 68, 73–74 | Supervised training-step order | **Pass:** D |
| M24 | L03 56–61 | Diverging train/validation loss and overfitting | **Pass:** A |

## Changed exercises after teaching — not original cold evidence

| Original miss | Follow-up and remaining limitations |
|---|---|
| M01 | Independently computed five-bit two's complement endpoints **−16 to +15** and representations after explanation |
| M03 | First follow-up still had a 2^n/MiB conversion and missing group count. With `2^19 bytes = 1/2 MiB` supplied, correctly obtained **8 + 3 = 11 MiB**. **Uncued conversion still unverified** |
| M09 | Multiple retries mixed view starts/steps, view indices and strides. Useful workflow: **map view coordinate back to original indices using start + view_index × step → flatten original indices using original strides**. Final changed index **44** supplied independently but **working not shown**; retest full reasoning |
| M10 | Independently found maxima/argmax indices on changed axis-0 data, but tutor supplied bracketed output representations. Independently reported shape **(2,1,3)** for 3D axis-1 argmax with `keepdim=True` |
| M13–M15 | Fresh RGB flatten length **105**, independent distinction of true one-hot target vs predicted class after terminology repair, and input-first linear weight shapes **(5,3)** and **(3,2)**. Noted PyTorch `nn.Linear.weight` stores **(out_features,in_features)** |
| M17–M18 | After worked examples, selected correct true-class probability and evaluated **−ln(1/16)**. In another correct-prediction case, distinguished target entropy **0** from cross-entropy **−ln(3/4)** |

### What to conclude and what not to conclude

- Cold evidence was stronger on broadcasting compatibility, view/copy semantics, `einsum` *recognition*, training-loop sequence and validation concepts.
- Gaps cluster around **uncued multistep reconstruction, coordinate/axis bookkeeping, explicit representation conventions, and target/loss calculations**, not uniform inability to understand L02/L03.
- A correct same-session retest after tutoring is not delayed-secure performance. No complete softmax probability vector *and loss* was independently constructed in this window; M19 demonstrated **recognition of max-shifting only**.
- An MCQ's correctness does not certify all atomic skills within that family. A full 83+93 slide reconciliation remains a separate syllabus audit task, not completed by this 24-question sample.

## Deferred open questions — all original targets unchanged

| ID | Original source anchor | Constructed-response task | Status |
|---|---|---|---|
| O1 | L02 12–18, 29–30 | Compare dtype memory, capacity, precision and range | **Shown but no attempt; change numbers to make it cold** |
| O2 | L02 26–28, 39 | Derive valid and invalid broadcasting with axis justification | Held back |
| O3 | L02 37–49 | Trace slice vs advanced-index storage, offset, flat address and contiguity | Held back |
| O4 | L02 55–62 | Axis reduction with `keepdim` and numerical `einsum` | Held back |
| O5 | L03 11–15, 33–34, 76 | Affine forward, shapes, parameter count | Held back |
| O6 | L03 20–26 + original blueprint | **Complete** softmax vector, classification loss, and shift-invariance reasoning | Held back |
| O7 | L03 46–50 | Gradient step and learning-rate reasoning | Held back |
| O8 | L03 56–61, 68–74 | Interpret training/validation loss, batches/epochs and evaluation | Held back |

**Resumption rule:** In the next available **L02/L03 concepts-only** window, present **O1 with different numbers first**, one prompt at a time. Keep O2–O8 in original order and use the same constructs; do not silently shrink the blueprint or turn open questions into MCQs. Prioritize delayed checks for **full softmax → loss (O6), full flat-index working (O3), and uncued mixed-dtype byte/MiB conversion (O1)**. Questions not reached remain **untested** and do not count as errors.

**Schedule interaction:** The planned 25 Nov **morning** L05/L06/L07 MCQ diagnostic appears in PR #77, while 25 Nov **afternoon** remains AIMS5701 project time. Do not displace that block with O1–O8; schedule these in a later free concepts window. Likewise, preserve the separate unfinished coding-workshop demand.

## Minimal coordinator handover

24 MCQs finished, original cold **15/24**; all nine misses reviewed; **eight open responses untouched**. No independent code reconstruction measured. Core fragile distinctions: MiB conversion, flat index with offset, reduction axes, input-first vs output-first matrix weight shape, one-hot target vs prediction and cross-entropy. Maintain syllabus-driven rotation; do not allow this list to monopolize new assessments. Keep source provenance and support levels explicit.
