# AIMS5702 Coding Quiz 2 — Daily study plan (23 Nov–3 Dec 2026)

**Purpose:** launch one fresh tutoring chat per **track and day**, without losing the syllabus. **Conceptual assessment** and **coding reproduction** use independent windows, grades and handovers. This is a prospective schedule, **not a record of completed learning**.

## Entry point for each new window

1. Read repo `SESSION_WORKFLOW.md`, `TUTORING_CALIBRATION.md`, `LEARNING_STATE.md` (and `ARCHITECTURE.md` only on first encounter).
2. Choose **Window A (concepts/MCQs/open reasoning)** or **Window B (coding/tutorial/cold completion)**. Read [WORKFLOW.md](WORKFLOW.md), [COVERAGE_MATRIX.md](COVERAGE_MATRIX.md), [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md) and the requested **single day file**. Do not load unrelated days.
3. Open the primary original source slides/pages required by that day. Treat revision slides and transcripts as supplementary. Use the Project's unified syllabus/TSV when available for exact atomic source ID selection.
4. Begin with the agreed day's task immediately, **one learner-owned exercise at a time**. Do not conduct a new broad planning interview. Collect evidence and hand back concise results rather than reciting the plan.

## Schedule and two-track separation

| Date | Knowledge track | Coding track | Link |
|---|---|---|---|
| 2026-11-23 | Light diagnostic | Short tensor warm-up | [Monday](2026-11-23.md) |
| 2026-11-24 | **L02/L03 exclusively:** 24 MCQs + 8 open, 120-min concepts window | Separate 3h tensor workshop: CP01–03 cold + transfer; CP04 key components | [Tuesday](2026-11-24.md) |
| 2026-11-25 | **Morning café: 90-min L05 CNN + L06 Transformer + L07 Inference MCQs (10 each)**; **afternoon onward AIMS5701 kickoff** | **No 5702 coding** | [Wednesday](2026-11-25.md) |
| 2026-11-26 | GPU foundational teaching | CP08 Conv2d weight/activation/output shapes, padding/stride/pooling/receptive field; CP09 add/multiply/ReLU and affine backward (upstream gradient, dX/dW/db); CP10 manual 2D convolution gradients as supplied-scaffold components; CP11 x+F(x) and 1×1 projection as code interpretation/component blanks. | [Thursday](2026-11-26.md) |
| 2026-11-27 | One hour full-syllabus MCQ + ethics teaching | CP12 Q/K/V projection, QK^T/sqrt(dk), key-axis softmax, attention@V, multihead split/concat; CP13 sinusoidal even/odd sin/cos and RoPE pair rotation; CP14 patch embedding/CLS sequence and ViT scaffold (component-level). | [Friday](2026-11-27.md) |
| 2026-11-28 | One hour full-syllabus MCQ | CP05 naive versus max-shift stable softmax and axis; CP06 dataset transforms, batching, DataLoader iteration and shape; CP07 nn.Module/Sequential, forward, loss, backward, optimizer.step/zero_grad, train/eval/no_grad, accuracy. Include inference-related normalization/dropout behavior as interpretive blanks. | [Saturday](2026-11-28.md) |
| 2026-11-29 | One hour full-syllabus MCQ | CP15 causal mask and LayerNorm eps/dropout train-eval semantics; CP16 quantize/dequantize/clip, fused linear expression, read ONNX model graph/export scaffolds; CP04 bilinear four-corner gather cold retry; finish any *unassessed* CP10/11/14 components before adding elaborate new applications. | [Sunday](2026-11-29.md) |
| 2026-11-30 | One hour full-syllabus MCQ | CP17 1D kernel index = blockIdx.x*blockDim.x+threadIdx.x, guard idx<n, SourceModule C string, get_function, np.float32 scalars, correct ceil number of blocks; CP18 2D x/y grid, row*width+col, guard each dimension, flattened buffer and PyCUDA wrapper with grid/block. | [Monday](2026-11-30.md) |
| 2026-12-01 | One hour full-syllabus MCQ | CP19 @triton.jit, tl.program_id, tl.arange, offset broadcast, tl.load/tl.store mask and host launch; CP20 2D tiled operands, broadcasting and tl.sum full reduction GEMM (key blank expressions); CP22 online-softmax running-max correction and tile-merge explanation. CP21 GPU fusion/memory traffic as concept+numerical, not a long kernel. | [Tuesday](2026-12-01.md) |
| 2026-12-02 | One hour full-syllabus MCQ | CP01–CP22 mixed unseen transfer from the preselected exam-like blueprint; CP23 ethics reasoning in MCQs. Include short exact-output/torch.Size and gradient/attention/CUDA/Triton blanks; never recycle examples already solved. | [Wednesday](2026-12-02.md) |
| 2026-12-03 | Final full-syllabus MCQ, if useful | Brief familiar code recall | [Thursday](2026-12-03.md) |

## Exam / feasibility boundaries

- Lecturer's revision slide lists 16 MCQs (24 marks = 48%) and 26 marks (52%) of code/comment/numerical blanks in 60 minutes. No lecturer-approved per-topic distribution is available.
- **Thu 3 Dec** is our working exam date based on class timetable and conversation; verify against the official assessment notice.
- **Wed 25 Nov is a one-off morning exception:** exactly one **90-minute concepts-only** L05/L06/L07 MCQ assessment in the café between school drop-off and pickup. **Afternoon onward is protected for AIMS5701 project kickoff.** No 5702 coding or cross-course catch-up that day. 23 Nov remains a light session. Never invent completed work.
- **24 Nov is L02 and L03 only in the concepts window** (12 MCQs + 4 open per original lecture). Do not import CNN/Transformers/Inference/GPU/Ethics questions from the old plan; their coverage starts later.
- **24 Nov coding is a separate three-hour window**, not a continuation of the conceptual questions. It can use Assignment 1/2 implementations.
- 27 Nov–3 Dec retains daily full-syllabus MCQs, with its own rotating atom-level coverage ledger.
- Coding gets explicit tutoring and **unhinted cold completion**, then unseen transfer. Optional assignment problems stay within the source inventory but are time-compressed, never silently excluded.
- AI Ethics and GPU require actual teaching rather than assuming prior knowledge.
- `COVERAGE_MATRIX.md` contains *all 45 competency families and 23 CP families* with a primary scheduling obligation. This PR changes planning documentation only; it must not mark `learning_progress.yaml` or `LEARNING_STATE.md` as if sessions occurred.

## Outcome contract

Each **concepts** window returns assessed atomic skill IDs and MCQ/open-question results, clearly separating original cold attempts from repaired attempts and untested material. Each **coding** window separately returns CP IDs, worked/guided/cold/transfer results and deferred implementation patterns. Neither track may claim the other's mastery. Only after a substantive real session should the normal repo workflow update the lesson log and current learning state through a separate change.

## Locked conceptual assessment depth

- **Tuesday 24 Nov:** 24 MCQs (12 L02, 12 L03) plus **8 short open questions** (4 per lecture), **120 min maximum**. MCQ levels: **8 recall, 10 application/edge case, 6 numerical/multistep**. Blueprint in [2026-11-24.md](2026-11-24.md).
- **Wednesday 25 Nov:** **30 unseen MCQs, 10 each L05 CNN, L06 Transformer, L07 Inference**, with depth 12 recall / 12 applied / 6 numeric or multistep, capped at 90 minutes (60 cold + 20 review + 10 handover). The inference part excludes the L07 Ethics section; see [Wednesday's day file](2026-11-25.md).
- **Friday 27 Nov to Thursday 3 Dec:** **30 unseen full-syllabus MCQs daily**, normally ~45–50 min answering and 10–15 min review; **12 precise distinctions, 12 applied questions, 6 calculations/multistep**. Domain allocation **4 F, 4 T, 5 C/G, 5 R, 4 I, 4 E, 4 U**. This is a practice rotation, **not the lecturer's weighting**. The quiz-day set may be shortened for fatigue.
- **Syllabus accounting:** every assessment question identifies an exact source atom/slide or clearly flags missing evidence; explicitly list scheduled but untested items. Answering one item never covers its entire competency family.
