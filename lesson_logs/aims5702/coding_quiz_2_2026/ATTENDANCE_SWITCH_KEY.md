# AIMS5702 — Attendance option-switch answer key and feasibility audit

**Companion to [the question-only bank](ATTENDANCE_SWITCH_BANK.md)**. Do not show this document during cold MCQ testing. It contains explanations and source limitations, plus a 4-choice-level audit.

## Can the lecturer make a distractor correct?

| AQ | Original key | Alternate target(s) with same choices | Limitation / learning trap |
|---|---|---|---|
| AQ01 | **A and B** (ambiguous original) | A or B separately if question specifies resulting shape | C/D incompatible shapes |
| AQ02 | D | A = provider setting; C = extra FLOPs | Optimizer fusion does not imply A/B/C |
| AQ03 | A | None compelling at lecture depth | Exact FlashAttention ≠ linear-sum approximation |
| AQ04 | C | B/D **diagnostic false-claim identification only** | Class count ≠ input channels; BatchNorm removal not necessary |
| AQ05 | D | A **diagnostic** only | **U-Net does not appear in the ResNet screenshot's A–D**; see X01/X02 |
| AQ06 | A | B = causal mask; C = uniform logits | Positionless unmasked attention permutes with input |
| AQ07 | B | A **diagnostic** only | Causal masks prevent future access; do not eliminate position |
| AQ08 | C | A = causal text mask; B = 2×2 CNN max pooling | CLS vs decoder mask vs pooling |
| AQ09 | B | C **diagnostic** only | Running statistics claim is BatchNorm-specific |
| AQ10 | B | C **diagnostic** only | ONNX graph/verification ≠ training hyperparameter tuning |
| AQ11 | A | B/C/D under explicit changed task constraints | F1/class decisions vs AUC/scores vs RMSE/regression |
| AQ12 | B | D **diagnostic** only | Masked warp divergence has potential utilisation cost |
| AQ13 | C | A/B/D for fractions/multiples of a warp | Warp width itself remains 32 |
| AQ14 | B | None compelling | Tilewise softmax cannot be naively concatenated |
| AQ15 | A | C **diagnostic** only | 32 threads/warp ≠ limit on grid dimensionality |
| AQ16 | A | C **diagnostic** only | Triton masks don't change dtype |
| AQ17 | C | A/B/D **bug identification only** | Wrong formulas must not be taught as correct index formulas |
| AQ18 | C | A = ALU; B = scheduler; D = execution threads | Distinguish hardware and logical execution concepts |

**Important:** An *incorrect* original statement cannot become a truthful fact through changing the question. Diagnostic items ask you to *identify the false claim or bug*, which is different from switching to another true concept. Where the desired alternative (e.g. **U-Net**) is not an original option, concept-switch X questions necessarily have newly written answer choices. This was cross-checked against original uploaded screenshots and lecture slides **L05 pp.95–97,108; L06 p.34; L07 pp.30,49–51; L09 pp.38,47,66–68,75**.

## Full answer key and explanations

- **AQ01-V01** (exam) → **A**. A aligns (6,4) with (5,1,4) to yield (5,6,4).
- **AQ01-V02** (switch) → **B**. B aligns (2,4,1) with (4,2), giving (2,4,2).
- **AQ02-V01** (exam) → **D**. Fusion saves intermediate reads and writes.
- **AQ02-V02** (switch) → **C**. Duplicated math increases total FLOPs.
- **AQ02-V03** (switch) → **A**. Disabling a GPU execution provider changes execution configuration.
- **AQ03-V01** (exam) → **A**. Tiling on-chip reduces HBM/global-memory traffic.
- **AQ03-V02** (exam) → **A**. The on-chip strategy avoids large global memory reads/writes.
- **AQ04-V01** (exam) → **C**. Replace the final classification layer to emit 12 outputs.
- **AQ04-V02** (diagnostic) → **B**. B confuses the first Conv input channel count with class count.
- **AQ04-V03** (diagnostic) → **D**. D is a false claim; BatchNorm is exportable.
- **AQ05-V01** (exam) → **D**. The additive identity path supports gradient propagation.
- **AQ05-V02** (diagnostic) → **A**. ResNet identity addition requires compatible shapes, not channel doubling.
- **AQ06-V01** (exam) → **A**. Unmasked self-attention without position is permutation equivariant.
- **AQ06-V02** (switch) → **B**. Softmax weights of masked future positions are zero.
- **AQ06-V03** (switch) → **C**. Equal logits give uniform attention weights.
- **AQ07-V01** (exam) → **B**. The query must not see later tokens.
- **AQ07-V02** (diagnostic) → **A**. Causal masking changes access, not the existence of positional encodings.
- **AQ08-V01** (exam) → **C**. A learnable CLS token is the ViT classification representative.
- **AQ08-V02** (switch) → **A**. Causal triangular masking blocks future attention.
- **AQ08-V03** (switch) → **B**. This is local 2×2 max pooling.
- **AQ09-V01** (exam) → **B**. BatchNorm uses running statistics and Dropout stops random masking.
- **AQ09-V02** (diagnostic) → **C**. Dropout is disabled during inference, not increased.
- **AQ10-V01** (exam) → **B**. ONNX provides a portable graph and output verification checks agreement.
- **AQ10-V02** (diagnostic) → **C**. C describes hyperparameter tuning, not ONNX.
- **AQ11-V01** (exam) → **A**. F1 and suitably configured ROC AUC assess classes; RMSE is for regression.
- **AQ11-V02** (switch) → **B**. I and III correspond to F1 and RMSE.
- **AQ11-V03** (switch) → **C**. ROC AUC uses scores and RMSE uses real values; F1 needs hard decisions.
- **AQ11-V04** (switch) → **D**. All three may apply across classification and regression outputs.
- **AQ12-V01** (exam) → **B**. Warp divergence uses execution masks to process branch paths.
- **AQ12-V02** (diagnostic) → **D**. D is an over-absolute and false description.
- **AQ13-V01** (exam) → **C**. One warp contains 32 threads.
- **AQ13-V02** (switch) → **A**. 32/8 = 4 threads.
- **AQ13-V03** (switch) → **B**. 32/2 = 16 threads.
- **AQ13-V04** (switch) → **D**. 2*32 = 64 threads.
- **AQ14-V01** (exam) → **B**. Tilewise normalized attention lacks one common denominator.
- **AQ14-V02** (exam) → **B**. Softmax does not simply compose from independently normalised blocks.
- **AQ15-V01** (exam) → **A**. A multiple of warp width avoids a partly populated final warp.
- **AQ15-V02** (diagnostic) → **C**. This confuses 32-thread warp size with grid dimensionality.
- **AQ16-V01** (exam) → **A**. Masking prevents out-of-bounds memory access.
- **AQ16-V02** (diagnostic) → **C**. A mask controls participation in memory access, not precision.
- **AQ17-V01** (exam) → **C**. Global index = blockIdx.x*blockDim.x+threadIdx.x.
- **AQ17-V02** (diagnostic) → **A**. A neglects the per-block stride.
- **AQ17-V03** (diagnostic) → **B**. B swaps the terms.
- **AQ17-V04** (diagnostic) → **D**. D uses number of blocks rather than threads per block.
- **AQ18-V01** (exam) → **C**. Tensor Cores accelerate matrix calculations.
- **AQ18-V02** (switch) → **B**. A warp scheduler issues ready warp instructions.
- **AQ18-V03** (switch) → **A**. An ALU performs general arithmetic and logic.
- **AQ18-V04** (switch) → **D**. Threads describe execution entities, not a physical ALU/Tensor Core.
- **X01** (concept-switch) → **B**. U-Net encoder/decoder and feature recombination provide fine spatial detail. *(Lecture: L05 CNN slides 95–97.)*
- **X02** (concept-switch) → **A**. U-Net restores resolution for segmentation; ResNet identity skips support deep optimisation. *(Lecture: L05 CNN slides 95–97,108; L06 slide 34.)*
- **X03** (concept-switch) → **B**. Output class count sets final logits; image channels remain RGB. *(Lecture: Original AQ04 and L05 CNN.)*
- **X04** (concept-switch) → **C**. The data channel count determines in_channels of first Conv. *(Lecture: L05 CNN shapes.)*
- **X05** (concept-switch) → **A**. CrossEntropyLoss accepts logits directly and normally integer indices. *(Lecture: L03 DL basics; AQ04 distractor A.)*
- **X06** (concept-switch) → **B**. Causal mask blocks future keys; permutation is a separate property. *(Lecture: L06 attention and AQ06/07.)*
- **X07** (concept-switch) → **A**. Order information differs from visibility restriction. *(Lecture: L06 Transformer and AQ06/07.)*
- **X08** (concept-switch) → **B**. Max pooling is local spatial reduction. *(Lecture: L05 pooling and AQ08.)*
- **X09** (concept-switch) → **B**. Running statistics belong to BatchNorm, not LayerNorm. *(Lecture: L07 normalisation; AQ09.)*
- **X10** (concept-switch) → **C**. Dropout is inactive in evaluation. *(Lecture: L07 inference and AQ09.)*
- **X11** (concept-switch) → **B**. Slide 30 explicitly names dropout as an unused operation to delete. *(Lecture: L07 inference slide 30.)*
- **X12** (concept-switch) → **A**. Compare output tensors of original and exported models. *(Lecture: L07 ONNX slides 49–51 and AQ10.)*
- **X13** (concept-switch) → **C**. RMSE quantifies regression error. *(Lecture: AQ11 and L07 inference.)*
- **X14** (concept-switch) → **B**. ROC AUC summarises discrimination across thresholds. *(Lecture: AQ11 and L07 inference.)*
- **X15** (concept-switch) → **B**. Warp scheduler coordinates instruction issue. *(Lecture: L09 slides 38,47.)*
- **X16** (concept-switch) → **B**. row*width+col is correct for row-major contiguous storage. *(Lecture: L09 CUDA indexing and Assignment 5.)*
- **X17** (concept-switch) → **B**. Program ID selects a tile, arange creates vector offsets within tile. *(Lecture: L09 Triton slides 66–68.)*
- **X18** (concept-switch) → **A**. IO-aware tiling reduces global-memory traffic without redefining attention. *(Lecture: L09 GPU slide 75.)*
- **X19** (concept-switch) → **A**. The global softmax denominator must combine all tiles. *(Lecture: L09 FlashAttention; AQ14.)*
- **X20** (concept-switch) → **C**. The original AQ01 erroneously admitted two true answers for 'can broadcast'. *(Lecture: L02 broadcasting; AQ01.)*

## Quality controls

- In **AQ01**, both original choices A and B actually broadcast (A→(5,6,4), B→(2,4,2)). Do not score the original 'which pair can broadcast?' question as unique-answer.
- In **AQ09**, BatchNorm normally uses running estimates in eval; LayerNorm does not maintain the corresponding running batch mean/variance. Don't overgeneralise the original shorthand.
- In **AQ14**, source phrasing 'softmax is not associative' is shorthand for inability to simply combine independently normalised softmax tiles; use running maximum/normaliser explanation.
- **Diagnostic questions** deliberately key an erroneous assertion. They're for *spotting the misconception*, not confirming it. Do not use too many in a mock.
- **Concept-switch X items** have new answer choices and are *not* alleged to follow the lecturer's exact-option promise. They are course-grounded preparation for adjacent targets.
- All answers here are **model-authored practice solutions**, not an independently provided lecturer answer sheet.
