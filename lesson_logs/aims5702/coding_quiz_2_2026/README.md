# AIMS5702 Coding Quiz 2 — revised seven-day plan (27 November – 3 December 2026)

**Main rule:** use a fresh **Window B coding** chat and separate **Window A conceptual MCQ/ethics** chat. This study plan incorporates the lecturer's 26 Nov quiz hints and the user's wish to become *independently comfortable with fundamentals*. It supersedes the obsolete 30-question **equal-full-syllabus** daily allocation from earlier planning. The past sessions 23–26 Nov remain historical, not retroactively completed.

## Source-first entry point

Read repository `SESSION_WORKFLOW.md`, `TUTORING_CALIBRATION.md`, `LEARNING_STATE.md`; then [WORKFLOW.md](WORKFLOW.md), [COVERAGE_MATRIX.md](COVERAGE_MATRIX.md), this date's file, and the minimal required original slides/assignments. For MCQs load [TECHNICAL_ATTENDANCE_BANK.md](TECHNICAL_ATTENDANCE_BANK.md) and [ETHICS_EXAM_SCOPE.md](ETHICS_EXAM_SCOPE.md). Use the Project's full audited syllabus/TSV for atomic ID selection when available; never invent IDs.

## Lecturer-reported assessment contract (26 Nov revision)

- **16 MCQs / 24 marks**: **eight AI ethics**; **eight technical**, **at least six** variants of 20 in-class screenshot questions from the last two attendance sessions. Lecturer says the **A–D options remain the same**, but the stems will change.
- **26 further marks** in code/comment/numerical blanks, total 50 marks in 60 minutes. Lecturer explicitly emphasised FC versus CNN weight shapes and parameter counting, CNN output sizes, PyCUDA kernel strings/global indices, Triton decorators/offsets/masks, and ONNX. Exact positions Q3/Q4/Q5 were reported as ONNX/PyCUDA/Triton respectively; treat these as **guidance**, not guaranteed official prepublished questions.
- **Explicitly not on quiz, per lecturer:** `einsum`, SIMD, convolution **stride** calculations. **Shallow** FlashAttention knowledge still useful because tiling and global-memory IO appeared in attendance questions; no full kernel build. LSTM **tanh** recognition is in scope.

## Coding sequence — chronological prerequisites

| Date | Window B: coding and mathematical production | Window A: ethics + technical MCQs |
|---|---|---|
| [Fri 27 Nov](2026-11-27.md) | **CP01–04** typed tensors/shape/storage/reductions; scoped interpolation | **Teach** lecture ethics risk levels + examples; learn attendance bank |
| [Sat 28 Nov](2026-11-28.md) | **CP05–07**, stable softmax/MLP/train loop; **mandatory FC whole-network parameters** | First **8 ethics + 8 technical** set |
| [Sun 29 Nov](2026-11-29.md) | **CP08–11**, **mandatory Conv → Pool → Flatten → FC** shape/parameter tables, backprop basics | 16-question lecturer-style variants |
| [Mon 30 Nov](2026-11-30.md) | **CP12–16**, attention/ViT/causal masks, inference and **ONNX**; CUDA preview | 16-question variants + ethics examples |
| [Tue 1 Dec](2026-12-01.md) | **CP17–20**, **PyCUDA + Triton**: exact indices, masks, host grid/block; tiles scaffold | 16-question variants, GPU code-reading |
| [Wed 2 Dec](2026-12-02.md) | **60-minute exam-shaped mock**, targeted error repair; no long new kernel | Ethics risk table + bank recall only; **5701 poster discussion** |
| [Thu 3 Dec](2026-12-03.md) | 20–30 min familiar cold fragments if helpful; **evening quiz** | Light optional review, no new 30-MCQ quiz |

### Two non-negotiable foundations

**Fully connected:** calculate `d_in × d_out + d_out` (when bias); distinguish **lecture input-first** W shape `(in,out)` from **PyTorch stored** `(out,in)`. **CNN:** calculate `C_out × (C_in × K_h × K_w + 1)` for standard ungrouped bias Conv2d, propagate spatial output, pool, flatten, then parameterize FC. Two complete **unseen** networks on 28 and 29 Nov; later spaced retrieval. The tutor must make the student write every intermediate activation/weight/parameter count, not answer a recognition MCQ.

## Time and wellbeing boundaries

Coding 2–3h is an **upper target when capacity permits**, not a compulsory daily quota. Concept windows generally 30–60min; Friday ethics teaching 45–60min. 2 Dec is intentionally lighter because the 5701 poster must be displayed. PCG work runs separately with short bounded human review. Do not make up missed hours by stacking tasks onto the next day.

## Session outcomes

Return a concise **cold-versus-guided** handover per window with exact CP/atomic IDs and sources, correct syntax, unseen transfer, untested operations, and only the most useful delayed retrieval. Update `LEARNING_STATE.md` only after study actually happens. Previous 24 Nov MCQ/open-question and coding records remain valid but are not newly mastered by this schedule.
