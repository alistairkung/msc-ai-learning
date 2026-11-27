# AIMS5702 Quiz 2 — weekend ONNX, PyCUDA and Triton triad contract (28–29 November)

**Why:** the lecturer flagged these as the likely focus of **three out of five coding questions**, so the coordinator moved them forward from Mon/Tue to the Sat/Sun workshop. This is a **priority inference from lecturer hints**, not confirmed questions or exact marks.

## Before beginning

Use original course PDFs and examples:
- L07 `AIMS5702_2026-27_07_ModelInference(1).pdf`, plus Inference/Ethics transcript, relevant ONNX sections.
- L09 `AIMS5702_2026-27_09_GPUProgramming(1).pdf`, `GPU transcript.rtf`.
- `AIMS_5702_2026_27_Assignment_5.ipynb+-+Colab.pdf` and `AIMS5702_2026-27_11_Revision.pdf`.
- For necessary course-specific signature/code details, **reinspect original uploaded sources rather than substituting generic framework examples**. Work within what was taught. External library versions may vary.

## Required levels

| Focus | Teach | Cold end condition | Common failure |
|---|---|---|---|
| **ONNX** | Whole PyTorch export and output verification worked example; input/output names, eval, ONNX Runtime session and numeric comparison | New partially blank export + verification scaffold reconstructed independently | Explains ONNX but cannot recall method names, argument order or check outputs |
| **PyCUDA** | Full `SourceModule` C string + 1D index `blockIdx.x * blockDim.x + threadIdx.x`, guard, computation and host get_function/grid/block | Fresh 1D elementwise C kernel + Python launcher with correct N and boundary | Global vs local index, `blockDim` typo, missing bounds, floor instead of ceil launch |
| **Triton** | Full `@triton.jit` kernel, `tl.program_id(0)`, `tl.arange`, offsets/mask, loads and store and `grid` | Fresh changed operation with every index/mask/load/store and launch expression | Wrong mask condition, missing store mask, incorrect program offset or decorators |

## Teaching and evidence

First show a **complete worked analogue**, not isolated hints; explain syntax and shapes at enough length for genuine understanding. Then guided changed example. Then **new cold unseen quiz-style blanks** without method hints, with full correction and a new retry for missed logic. Record cold versus guided outcomes separately. Don't jump to a new topic while the student is still processing an error.

Saturday: ONNX and PyCUDA teaching + independent attempts. Sunday: Triton, then one independent ONNX, PyCUDA and Triton assessment each. Set aside approximately 45–60 min Sunday for the triad.

## Daily MCQs throughout weekend

**8 ethics** (from L07 transcript/risk tables and original lecturer examples) + **8 technical** changed stem questions sampled from [18-question screenshot bank](TECHNICAL_ATTENDANCE_BANK.md). The lecturer stated **at least six**, not necessarily all eight, will be attendance-derived. Practice can use all eight to strengthen coverage. **Keep options identical** but check for a single defensible answer; AQ01/AQ09 caveats remain.

## On Sunday report to coordinator

| Area | Cold first attempt | Corrected/assisted | Fresh transfer | Untested/syntax gaps |
|---|---|---|---|---|
| ONNX |  |  |  |  |
| PyCUDA |  |  |  |  |
| Triton |  |  |  |  |

**Plan if incomplete:** no panic catch-up backlog. Prioritize missed high-yield blanks in Tue 1 Dec retrieval, leaving Mon reserved for essential network maths.
