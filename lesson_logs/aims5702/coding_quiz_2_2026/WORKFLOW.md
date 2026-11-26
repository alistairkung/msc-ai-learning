# AIMS5702 Quiz 2 — tutor operating contract, revised after lecturer guidance

This file is a **task-specific supplement** to the repository's `SESSION_WORKFLOW.md` and `TUTORING_CALIBRATION.md`. The current [README](README.md), [coverage matrix](COVERAGE_MATRIX.md), and one selected daily file override earlier plans where they differ. Prior 23–26 Nov daily notes are historical; do not report them as completed because a new schedule exists.

## Separate windows, separate evidence

**Window B (coding):** teach essential math and syntax with a fully visible worked *analogue* → learner constructs guided variation → learner independently fills fresh code/shape/number blanks without cues → unseen transfer → delayed retrieval. One question/implementation task at a time. Do not provide the assessed answer until a learner attempt. Track actual Python/CUDA/Triton syntax separately from whether conceptual mechanism was understood.

**Window A (concepts):** lecturer-grounded AI ethics **eight questions**, technical attendance **eight questions**, including **at least six** valid changed stems selected from [technical bank](TECHNICAL_ATTENDANCE_BANK.md) using **unchanged answer-option text**. Never use screenshot options mechanically if a variant has multiple valid responses. Present one item at a time; collect cold response, give feedback, and keep timeboxed. No coding tutorials here.

**Exam-shaped mock (2 Dec):** 16 MCQs / 24 marks + 26 marks coding/comment/numeric blanks in 60 minutes. Original 26-mark coding distribution not independently known; use lecturer-signalled patterns, do not invent official marks by topic.

## Ethics syllabus boundary

Use **L07 slides 67–90**, `Inference and Ethics Transcript.rtf`, especially ~2:07–2:13, and lecturer-linked EU and HK references. Memorize **EU unacceptable/prohibited, high/conformity assessment, limited/transparency, minimal/code of conduct** and lecturer examples; HK internal Government ethical AI framework, China three laws/modular/scenario-specific and examples. Use the original lecturer's level and categories without injecting untaught legal subclauses. For changed examples, teach only distinctions that the sources actually support. See [ETHICS_EXAM_SCOPE.md](ETHICS_EXAM_SCOPE.md).

## Coding requirements by level

**A, independent full:** 
- CP01–03 core tensor creation/dtype/shape, memory, view/copy, broadcasting, `sum`/max-with-index axes. **No dedicated `einsum` drills** (explicit exclusion).
- CP05 stable softmax and CP07 minimal MLP/train loop.
- FC and CNN **whole-network shape/weight/bias/parameter counting**, with two unseen examples each and later changed retrieval.
- CP17–19 PyCUDA/Triton essential kernels with exact index/masks and host launch.
  
**B, key code blanks:** CP04 interpolation, CP06 dataset batches, CP09/10 gradients, CP11 residual, CP12–16 transformer/ONNX/inference, CP20 tiled GEMM elements.

**C, concept/math:** CP21 memory fusion, CP22 FlashAttention tiled softmax/IO; CP23 ethics. Lower depth = reduced time, **not automatic exclusion**.

## Mandatory shape / parameter worksheet

For each unseen model show this table (learner populates all cells):

| Layer | Input activation | Weight tensor (lecture vs PyTorch where relevant) | Bias shape | Output activation | Trainable parameter count |
|---|---|---|---|---|---|

- `nn.Linear(d_in,d_out)` with bias: `(B,d_in) → (B,d_out)`; lecture input-first `(d_in,d_out)`; stored `(d_out,d_in)`; params `d_in*d_out+d_out`.
- `nn.Conv2d(C_in,C_out,(K_h,K_w))` with bias, ungrouped: stored `(C_out,C_in,K_h,K_w)`; output `(B,C_out,H_out,W_out)`; params `C_out*(C_in*K_h*K_w+1)`. Image H/W affect activations but **not conv trainable weight count**.
- `MaxPool2d` vs `AvgPool2d`: no learned weights; maximum vs mean of each window. `Flatten` yields `(B,C*H*W)`. ReLU, tanh, softmax as used here add no trainable weights.
- Practice **stride-one** convolution output size; the lecturer stated convolution stride calculation is not on the next quiz.
- Never accept a lone total with no intermediate shapes as a fully demonstrated cold pass. On 28–29 Nov require **two distinct unseen networks** and an altered example on a later day.

## Lecturer hint precedence and ambiguities

- Explicit exclusions: `einsum`, SIMD, convolution stride calculations. Don't delete historical evidence; simply reduce current quiz drill priority.
- Explicit emphasis: LSTM **tanh**, FC vs convolution W sizes, mean/max pooling, output size, CUDA `int i = blockIdx.x * blockDim.x + threadIdx.x;`, grid/block, Triton `@triton.jit`, offset calculation and `tl.load/tl.store(mask=...)`, ONNX.
- FlashAttention deep implementation *unlikely*, but two screenshot questions cover IO/tiled softmax: assess concept, not kernel from scratch.
- Bank screenshots contain an ambiguous single-answer broadcasting original (AQ01 both A/B valid), and a BatchNorm-specific train/eval shorthand (AQ09). Flag rather than teaching wrong absolutes.
- When evidence sources disagree, stay faithful to lecturer's exam framing while clearly labeling an ambiguous/invalid question. Never invent a new legal rule or "official answer" that the lecturer did not provide.

## End-of-window handover

```md
Date / window / actual duration:
Original source slides and attendance AQ ID(s):
Preselected atomic or CP targets (not mastery):
Unhinted code/calculation or cold MCQ answers:
Tutorial/guided corrections (separate):
Unseen transfer (fresh, not recycled):
FC/CNN per-layer worksheet evidence (when assigned):
Not yet tested or deferred skills:
Top 1–3 delayed retrieval prompts:
Any ambiguous source question or exact-answer-format error:
```

**No actual study → no lesson evidence.** A planned workshop never updates `LEARNING_STATE.md` or `learning_progress.yaml` by itself.
