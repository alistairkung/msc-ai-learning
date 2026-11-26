# Technical attendance-quiz question bank — AIMS5702 Quiz 2

**Origin:** student-uploaded screenshots from two recent in-class attendance quizzes (20 screenshots, **18 distinct question stems**). Original images remain in the ChatGPT Project; this text is a **manual transcription of what was visible**, not an independently supplied lecturer answer sheet. Two screenshots repeat previous stems: `IMG_7082(2).jpeg` duplicates AQ04, and `IMG_7002.jpeg` duplicates AQ13. Verify transcribed punctuation against the original screenshot before claiming byte-for-byte exactness.

**Lecturer guidance, 26 Nov 2026:** of 16 quiz MCQs, eight focus on AI ethics; at least **six of the eight technical MCQs** will be variants of recent attendance questions **with the same answer options**. These are practice-bank statements, **not guaranteed verbatim exam stems**. Preserve each AQ item's four option meanings and wording; vary only the *question* in a way that leaves **exactly one** defensible correct option. Recompute the key; do not assume the original letter remains correct for every variant. When an option set cannot support a legitimate unique-answer variant, flag it rather than inventing one.

## Original question inventory (18 distinct)

### AQ01 — Broadcasting shapes

**Screenshot:** `IMG_7068(1).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Which pair of tensor shapes can be added using standard element-wise broadcasting rules?

| Option | Original answer option |
|---|---|
| A | (5,1,4) and (6,4) |
| B | (2,4,1) and (4,2) |
| C | (4,3) and (3,4) |
| D | (5,3,4) and (5,4) |

**Original conceptual key:** A and B. **Tutor caution:** AMBIGUOUS original: both A and B broadcast successfully. Do not use this exact stem as a single-answer MCQ; revised stem must make one of A/B uniquely correct while retaining ALL four options.

### AQ02 — Operation fusion

**Screenshot:** `IMG_7069(1).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Why do graph optimizers fuse consecutive operations during model deployment?

| Option | Original answer option |
|---|---|
| A | Disable GPU execution providers |
| B | Replace dynamic shapes with loops |
| C | Increase total floating-point operations |
| D | Reduce memory read/write traffic |

**Original conceptual key:** D. **Tutor caution:** Graph/operator fusion reduces intermediate reads and writes.

### AQ03 — FlashAttention IO

**Screenshot:** `IMG_7070(1).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Why tile K/V blocks instead of materializing a full N×N attention score matrix?

| Option | Original answer option |
|---|---|
| A | Avoids large global memory reads/writes |
| B | Changes exact softmax into linear sum |
| C | Limits sequence length to one token |
| D | Removes the need for query projections |

**Original conceptual key:** A. **Tutor caution:** Conceptual recognition only; not a production FlashAttention implementation target.

### AQ04 — Pretrained CNN head

**Screenshot:** `IMG_7071(1).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** For 12 Traditional Chinese character classes, what structural change is required to adapt a 1,000-class pretrained CNN?

| Option | Original answer option |
|---|---|
| A | Removing the softmax activation from nn.CrossEntropyLoss because PyTorch requires one-hot targets |
| B | Changing the input channel count of the first convolutional layer to 12 to match the number of character classes |
| C | Replacing the final classification layer so its output dimension matches 12 classes instead of 1,000 ImageNet classes |
| D | Removing all batch normalization layers so the model can be exported to ONNX format |

**Original conceptual key:** C. **Tutor caution:** Output classes belong to final classifier; number of input channels is independent of class count.

### AQ05 — Residual identity

**Screenshot:** `IMG_7074(1).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Why does identity shortcut y=F(x)+x help deeper training?

| Option | Original answer option |
|---|---|
| A | Identity branches double channels |
| B | Residual paths replace softmax |
| C | Skip connections eliminate activations |
| D | Identity paths preserve gradients |

**Original conceptual key:** D. **Tutor caution:** Additive skip creates an identity gradient path when dimensions permit.

### AQ06 — Unmasked attention permutation

**Screenshot:** `IMG_7075(2).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** If tokens are permuted with no positional encodings or mask, how do attention weights behave?

| Option | Original answer option |
|---|---|
| A | Weights permute with inputs |
| B | Weights zero out future tokens |
| C | Weights become uniform constants |
| D | Weights remain identical in order |

**Original conceptual key:** A. **Tutor caution:** Self-attention is permutation equivariant without position or order-dependent masking.

### AQ07 — Causal attention mask

**Screenshot:** `IMG_7076(2).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Why mask scores above the main diagonal in autoregressive attention?

| Option | Original answer option |
|---|---|
| A | Eliminate positional embeddings |
| B | Prevent attending to future tokens |
| C | Replace softmax normalization |
| D | Reduce hidden dimension size |

**Original conceptual key:** B. **Tutor caution:** Future positions are hidden before softmax.

### AQ08 — ViT aggregation

**Screenshot:** `IMG_7077(2).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** What commonly aggregates image information for the final ViT classifier?

| Option | Original answer option |
|---|---|
| A | Using causal triangular masks |
| B | Using 2×2 max pooling |
| C | Using a learnable CLS token |
| D | Using fixed int8 lookup tables |

**Original conceptual key:** C. **Tutor caution:** ViT CLS-token architecture covered in lecture; other aggregation designs exist but not this MCQ's focus.

### AQ09 — train/eval

**Screenshot:** `IMG_7078(3).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** What happens to normalization and dropout layers when switching model.train() to model.eval()?

| Option | Original answer option |
|---|---|
| A | Batch stats and no normalization |
| B | Frozen stats and no dropout |
| C | Batch stats and higher dropout |
| D | Running stats and zeroed weights |

**Original conceptual key:** B. **Tutor caution:** Original shorthand refers to BatchNorm running stats + dropout disabled in eval. LayerNorm does NOT freeze running batch stats; restrict variants to BatchNorm.

### AQ10 — ONNX export/verify

**Screenshot:** `IMG_7081(1).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** What is the main reason for exporting and verifying a trained CNN in ONNX?

| Option | Original answer option |
|---|---|
| A | To compress the handwritten character dataset into a single lossless .zip archive |
| B | To serialize the model into a framework-agnostic computation graph and confirm its numerical outputs match PyTorch |
| C | To automatically search for optimal learning rates and batch sizes during training |
| D | To convert convolutional layers into Triton online softmax kernels |

**Original conceptual key:** B. **Tutor caution:** ONNX portable graph and cross-runtime output consistency; not a dataset archiver.

### AQ11 — Classification metrics

**Screenshot:** `IMG_7083(1).jpeg`  
**Visible question (faithful paraphrase where abbreviated):** For Traditional Chinese character recognition, which metrics apply? (I) F1 (II) ROC AUC (III) RMSE

| Option | Original answer option |
|---|---|
| A | (I) and (II) only |
| B | (I) and (III) only |
| C | (II) and (III) only |
| D | (I), (II) and (III) |

**Original conceptual key:** A. **Tutor caution:** Multiclass classifier may use F1 and appropriately configured ROC AUC; RMSE is not standard class-label assessment.

### AQ12 — Warp divergence

**Screenshot:** `IMG_6996.jpeg`  
**Visible question (faithful paraphrase where abbreviated):** How does CUDA handle divergent branch paths within one warp?

| Option | Original answer option |
|---|---|
| A | By dynamically splitting the warp into independent hardware cores instantly |
| B | Via execution masking by the compiler, serializing the execution of both branches |
| C | By running branches concurrently on separate L2 caches |
| D | Branching has zero performance penalty on modern GPUs |

**Original conceptual key:** B. **Tutor caution:** Lecture-level description: inactive lanes masked during divergent paths; compiler/hardware details can be nuanced.

### AQ13 — Warp width

**Screenshot:** `IMG_6995.jpeg`  
**Visible question (faithful paraphrase where abbreviated):** How many threads typically form an NVIDIA warp?

| Option | Original answer option |
|---|---|
| A | 4 threads |
| B | 16 threads |
| C | 32 threads |
| D | 64 threads |

**Original conceptual key:** C. **Tutor caution:** 32.

### AQ14 — Tiled softmax

**Screenshot:** `IMG_6994.jpeg`  
**Visible question (faithful paraphrase where abbreviated):** What is the mathematical challenge with tiling softmax across independent blocks?

| Option | Original answer option |
|---|---|
| A | Softmax has a negative derivative everywhere. |
| B | Softmax is not an associative property |
| C | Softmax cannot be evaluated using floating-point numbers. |
| D | Exponential terms may encounter division by zero on GPU accelerators. |

**Original conceptual key:** B. **Tutor caution:** Means independently normalized tile softmax outputs cannot simply be combined. Online max/normalizer rescaling is needed; question wording is simplified.

### AQ15 — Block-size multiple

**Screenshot:** `IMG_6999.jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Why choose CUDA block sizes as multiples of 32?

| Option | Original answer option |
|---|---|
| A | To prevent wasted threads within warps |
| B | To bypass global memory capacity limits |
| C | Because the maximum grid dimensionality is strictly 32 |
| D | To force the compiler to compile using PyCUDA instead of NVCC |

**Original conceptual key:** A. **Tutor caution:** Avoid underfilled last warp within a block; not an absolute requirement or a guarantee of best performance.

### AQ16 — Triton mask

**Screenshot:** `IMG_7001.jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Why use explicit mask with tl.load/tl.store vectors?

| Option | Original answer option |
|---|---|
| A | To prevent out-of-bounds memory errors. |
| B | To encrypt the data stream passing through the L2 cache. |
| C | To switch between FP32 and FP64 precision automatically. |
| D | To satisfy Python syntax requirements for loop unrolling. |

**Original conceptual key:** A. **Tutor caution:** Final tile can include offsets >= N; mask guards load and store.

### AQ17 — CUDA global index

**Screenshot:** `IMG_6998.jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Which C expression gives global 1D thread index?

| Option | Original answer option |
|---|---|
| A | int i = blockIdx.x + threadIdx.x; |
| B | int i = threadIdx.x * blockDim.x + blockIdx.x; |
| C | int i = blockIdx.x * blockDim.x + threadIdx.x; |
| D | int i = gridDim.x * blockIdx.x + threadIdx.x; |

**Original conceptual key:** C. **Tutor caution:** Mandatory cold fill-in expression with correct capitalization.

### AQ18 — Tensor Cores

**Screenshot:** `IMG_6997.jpeg`  
**Visible question (faithful paraphrase where abbreviated):** Which NVIDIA H100 SM hardware accelerates matrix calculations?

| Option | Original answer option |
|---|---|
| A | Arithmetic Logic Unit (ALU) |
| B | Warp Scheduler |
| C | Tensor Core |
| D | Threads |

**Original conceptual key:** C. **Tutor caution:** Tensor Cores accelerate matrix-multiply-accumulate workloads.


## Important QA guards

1. **AQ01 broadcasting is genuinely ambiguous:** both `(5,1,4)+(6,4)` and `(2,4,1)+(4,2)` are compatible, so the screenshot as-is has two defensible answers. If preserving identical options, a new question must specify an additional unique criterion; otherwise exclude it from *single-select* graded drills.
2. **AQ09 applies to BatchNorm:** in `eval()`, BatchNorm normally uses saved running statistics and dropout stops randomly dropping units. LayerNorm behavior is different; do not generalize frozen running statistics to all normalization layers.
3. **AQ14 tiled softmax** is a lecture-level shorthand. Correct conceptual target is that independently normalized blocks cannot simply be glued together, motivating the online max/denominator correction.
4. **AQ04 / AQ13 duplicates** are duplicates, not extra independent syllabus targets.
5. **Original answer options same** does *not* mean memorise the old letter; the tutor must author changed reasoning questions, check all four choices and preserve lecture-faithful scope.
6. Do not use this bank to claim coding ability. ONNX/PyCUDA/Triton code blanks need independent *production*, not MCQ recognition.

## Practice blueprint

- **Eight ethics MCQs:** generated solely from the Lecture 07 taught material and lecturer-referenced risk-level sources in [ETHICS_EXAM_SCOPE.md](ETHICS_EXAM_SCOPE.md).
- **Eight technical MCQs:** select **six** question families from this bank, produce valid unseen variants with the exact four original option texts, and use two additional source-grounded questions from the broader teaching (or valid attendance variants if appropriate). Do not repeatedly test the same source item each day.
- Keep an ID-level log: `AQxx`, source screenshot, variation premise, all four options, recomputed correct option(s), first cold result, reviewed result, and whether the question was invalid/ambiguous.
- **Exam-format mock:** 16 MCQs = 24 marks, 26 code/comment/numerical marks. No per-MCQ marks are inferred beyond the 24-mark total.
