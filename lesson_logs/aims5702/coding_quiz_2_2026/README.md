# AIMS5702 Coding Quiz 2 — Daily study plan (23 Nov–3 Dec 2026)

**Purpose:** launch a fresh, small study chat for a single day without re-planning or losing the syllabus coverage. This is a prospective schedule, **not a record of completed learning**.

## Entry point for each new window

1. Read repo `SESSION_WORKFLOW.md`, `TUTORING_CALIBRATION.md`, `LEARNING_STATE.md` (and `ARCHITECTURE.md` only on first encounter).
2. Read **only** [WORKFLOW.md](WORKFLOW.md), [COVERAGE_MATRIX.md](COVERAGE_MATRIX.md), [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md) and the requested **single day file** below; load more only if evidence demands it.
3. Open the primary original source slides/pages required by that day. Treat revision slides and transcripts as supplementary. Use the Project's unified syllabus/TSV when available for exact atomic source ID selection.
4. Begin with the agreed day's task immediately, **one learner-owned exercise at a time**. Do not conduct a new broad planning interview. Collect evidence and hand back concise results rather than reciting the plan.

## Schedule and two-track separation

| Date | Knowledge track | Coding track | Link |
|---|---|---|---|
| 2026-11-23 | Light diagnostic | Short tensor warm-up | [Monday](2026-11-23.md) |
| 2026-11-24 | Prior concepts L02–L07 breadth diagnostic | CP01 tensor shape/dtype/device/memory; CP02 broadcasting, basic vs advanced indexing, offset/strides, views/copies, contiguity, transpose/reshape; CP03 sums/dot/einsum and Assignment 1 pairwise-dot implementations. CP04 bilinear interpolation | [Tuesday](2026-11-24.md) |
| 2026-11-25 | AIMS5701 kickoff | No 5702 | [Wednesday](2026-11-25.md) |
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
- **Wed 25 Nov is entirely reserved for AIMS5701 project kickoff.** 23 Nov is light. Never make up fictional work performed on those dates.
- 24 Nov's abbreviated broad concept repair cannot certify the entire pre-inference syllabus. Remaining knowledge gaps are exposed in **daily full-syllabus MCQs from 27 Nov through quiz day**.
- Coding gets explicit tutoring and **unhinted cold completion**, then unseen transfer. Optional assignment problems stay within the source inventory but are time-compressed, never silently excluded.
- AI Ethics and GPU require actual teaching rather than assuming prior knowledge.
- `COVERAGE_MATRIX.md` contains *all 45 competency families and 23 CP families* with a primary scheduling obligation. This PR changes planning documentation only; it must not mark `learning_progress.yaml` or `LEARNING_STATE.md` as if sessions occurred.

## Outcome contract

Each tutoring window returns **actual** inspected source refs, assessed original skill IDs/CP IDs, supported vs independent attempts, unseen transfer, untested items and next recall. Only after a substantive real session should the normal repo workflow update the lesson log and current learning state through a separate change.
