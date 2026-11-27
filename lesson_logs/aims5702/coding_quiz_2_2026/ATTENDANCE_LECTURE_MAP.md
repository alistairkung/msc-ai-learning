# AIMS5702 Quiz 2 — Technical attendance MCQ bank grouped by lecture

**Built from actual** [68-question switch bank](ATTENDANCE_SWITCH_BANK.md) and [20 screenshot / 18 original-stem inventory](TECHNICAL_ATTENDANCE_BANK.md). Original lecture PDFs: L02 BasicMath, L03 DLBasics, L05 CNN, L06 Transformer, L07 ModelInference, L09 GPUProgramming. Each of the 68 questions has **one primary teaching lecture**; optional secondary links identify genuine cross-lecture distractors. Primary classification reflects where the key mechanism is most directly explained, **not necessarily the lecture in which the lecturer originally displayed the attendance quiz**. The option text is unchanged by this classification.

**68 technical questions only**. The expected eight **AI ethics** MCQs are studied separately using L07 slides 67–90 and [the ethics guide](ETHICS_EXAM_SCOPE.md). Lecture 07 technical questions and ethics are separate tracks.

## At a glance

| Primary lecture | Focus | Original screenshot families referenced | Practice questions |
|---|---|---|---:|
| **L02 — Basic Math** | Tensor broadcasting: right-aligned shapes, valid result shapes, incompatible dimensions | AQ01 | **3** |
| **L03 — Deep Learning Basics** | Cross-entropy/logits/targets, classification and regression evaluation concepts | AQ11, AQ04 | **7** |
| **L05 — CNN** | Transfer learning head versus input channels, U-Net encoder/decoder and high-resolution skip information, local max pooling | AQ04, AQ08, AQ05 | **8** |
| **L06 — Transformer** | ResNet identity shortcuts and backpropagated gradients; self-attention without positional information | AQ05, AQ06 | **4** |
| **L07 — Model Inference** | Decoder causal masking, ViT CLS, normalization and dropout, graph fusion, ONNX export, training versus inference memory | AQ02, AQ04, AQ06, AQ07, AQ08, AQ09, AQ10 | **19** |
| **L09 — GPU Programming** | Warp width/divergence, CUDA indexing, SM/Tensor Cores, block sizing, Triton offsets/masks, FlashAttention tiling/online softmax | AQ03, AQ12, AQ13, AQ14, AQ15, AQ16, AQ17, AQ18 | **27** |
| **Total** | Every question assigned exactly once | 18 unique original AQ families, with cross-lecture mapping | **68** |

**Question mode:** `exam` and `switch` retain the original A–D answer strings; `diagnostic` also retains A–D but asks you to identify a *false* distractor; `concept-switch` uses fresh answer options to test a sibling topic such as U-Net. Do not confuse an identified false claim with a valid architectural property.

## L02 — Basic Math (3 questions)

**Lecture anchors:** L02 broadcasting section, around slides 27–30.

| Origin | Concept to review | Bank question IDs | Also relevant to |
|---|---|---|---|
| **AQ01** | Broadcasting and output shapes | `AQ01-V01`, `AQ01-V02`, `X20` | — |

**Classification note:** AQ01 original is **ambiguous** (both A and B broadcast); exact-option variants specify a unique resulting shape.


## L03 — Deep Learning Basics (7 questions)

**Lecture anchors:** L03 classifier/loss/evaluation sections (attendance screenshots supply F1/ROC AUC/RMSE detail).

| Origin | Concept to review | Bank question IDs | Also relevant to |
|---|---|---|---|
| **AQ11** | Classification/regression evaluation: F1, ROC AUC and RMSE | `AQ11-V01`, `AQ11-V02`, `AQ11-V03`, `AQ11-V04`, `X13`, `X14` | — |
| **AQ04** | Pretrained CNN classifier head vs input channels; cross-lecture ONNX/BatchNorm distractor | `X05` | — |

**Classification note:** Specific F1 / ROC AUC / RMSE combinations are visible in the **attendance MCQ**, but I did not find an explicit three-metric comparison in the L03 slides. Keep this as *L03-adjacent evaluation practice*, not a claimed lecturer slide quotation.


## L05 — CNN (8 questions)

**Lecture anchors:** L05 pooling, CNN architecture and U-Net slides 95–97.

| Origin | Concept to review | Bank question IDs | Also relevant to |
|---|---|---|---|
| **AQ04** | Pretrained CNN classifier head vs input channels; cross-lecture ONNX/BatchNorm distractor | `AQ04-V01`, `AQ04-V02`, `X03`, `X04` | — |
| **AQ08** | ViT CLS token vs CNN pooling / autoregressive masking | `AQ08-V03`, `X08` | `AQ08-V03` ↔ L07; `X08` ↔ L07 |
| **AQ05** | ResNet residual identity addition and gradient preservation; U-Net contrast | `X01`, `X02` | `X01` ↔ L06; `X02` ↔ L06 |

**Classification note:** U-Net's skip connections **combine** higher-resolution encoder features with the decoder. ResNet's skip connection is a **residual identity addition** — see L06. U-Net appears in supplementary X01/X02 with **new options**, not in the original AQ05 A–D choices.


## L06 — Transformer (4 questions)

**Lecture anchors:** L06 ResNet slides 34–35; position-independence slides 83–85.

| Origin | Concept to review | Bank question IDs | Also relevant to |
|---|---|---|---|
| **AQ05** | ResNet residual identity addition and gradient preservation; U-Net contrast | `AQ05-V01`, `AQ05-V02` | `AQ05-V01` ↔ L05; `AQ05-V02` ↔ L05 |
| **AQ06** | Permutation-equivariant attention; equal-score softmax; causal-mask crossover | `AQ06-V01`, `AQ06-V03` | — |

**Classification note:** L06 explicitly teaches ResNet gradient benefits (slides 34–35). The attention-permutation question belongs with L06 position-ignorance discussion; causal masks are explained more directly in L07.


## L07 — Model Inference (19 questions)

**Lecture anchors:** L07 slides 3–7, 23–27, 29–30, 37–41 and ONNX section.

| Origin | Concept to review | Bank question IDs | Also relevant to |
|---|---|---|---|
| **AQ02** | Inference graph optimisations: operation fusion, provider configuration, unused-op deletion | `AQ02-V01`, `AQ02-V02`, `AQ02-V03`, `X11` | — |
| **AQ04** | Pretrained CNN classifier head vs input channels; cross-lecture ONNX/BatchNorm distractor | `AQ04-V03` | `AQ04-V03` ↔ L05 |
| **AQ06** | Permutation-equivariant attention; equal-score softmax; causal-mask crossover | `AQ06-V02`, `X06` | `AQ06-V02` ↔ L06; `X06` ↔ L06 |
| **AQ07** | Causal future-token attention mask vs positional information | `AQ07-V01`, `AQ07-V02`, `X07` | `AQ07-V01` ↔ L06; `AQ07-V02` ↔ L06; `X07` ↔ L06 |
| **AQ08** | ViT CLS token vs CNN pooling / autoregressive masking | `AQ08-V01`, `AQ08-V02` | `AQ08-V01` ↔ L06; `AQ08-V02` ↔ L06 |
| **AQ09** | train/eval modes: BatchNorm, LayerNorm and dropout | `AQ09-V01`, `AQ09-V02`, `X09`, `X10` | `AQ09-V01` ↔ L03; `AQ09-V02` ↔ L03; `X09` ↔ L03; `X10` ↔ L03 |
| **AQ10** | ONNX portable computation graphs and numerical output verification | `AQ10-V01`, `AQ10-V02`, `X12` | — |

**Classification note:** **Important uncovered link from user discussion:** slide 41 describes freeing intermediate *activation tensors* after use during inference, versus retaining them for backprop in training. This is different from deleting *activation functions* and from ResNet skip connections. It is an **identified revision point**, not yet one of the 68 bank items. L07 also includes ethics slides 67–90, covered by a separate ethics bank, not counted here.


## L09 — GPU Programming (27 questions)

**Lecture anchors:** L09 GPU architecture, CUDA/Triton and FlashAttention sections.

| Origin | Concept to review | Bank question IDs | Also relevant to |
|---|---|---|---|
| **AQ03** | FlashAttention IO awareness and attention tiling | `AQ03-V01`, `AQ03-V02`, `X18` | `AQ03-V01` ↔ L06; `AQ03-V02` ↔ L06; `X18` ↔ L06 |
| **AQ12** | Warp divergence and masked branch execution | `AQ12-V01`, `AQ12-V02` | — |
| **AQ13** | NVIDIA warp width and fractions/multiples of a warp | `AQ13-V01`, `AQ13-V02`, `AQ13-V03`, `AQ13-V04` | — |
| **AQ14** | Tiled softmax: shared denominator, non-associativity shorthand | `AQ14-V01`, `AQ14-V02`, `X19` | `AQ14-V01` ↔ L06; `AQ14-V02` ↔ L06; `X19` ↔ L06 |
| **AQ15** | CUDA block size multiples of 32 and underfilled warps | `AQ15-V01`, `AQ15-V02` | — |
| **AQ16** | Triton vector offsets, tl.load/tl.store masks, OOB prevention | `AQ16-V01`, `AQ16-V02`, `X17` | — |
| **AQ17** | CUDA global thread ID, blockIdx/blockDim/threadIdx and 2D flat indexing | `AQ17-V01`, `AQ17-V02`, `AQ17-V03`, `AQ17-V04`, `X16` | — |
| **AQ18** | SM hardware: Tensor Cores, warp scheduler, ALU, threads | `AQ18-V01`, `AQ18-V02`, `AQ18-V03`, `AQ18-V04`, `X15` | — |

**Classification note:** FlashAttention mixes attention mathematics from L06 with GPU IO/tiling in L09; its *primary* exam question belongs to L09. Triton and CUDA are distinct coding topics as well as MCQ recognition.

## How to use this map for daily revision

Each day, draw **eight technical questions** from the bank using changing lecture allocations. To avoid a 27/68 GPU-heavy bias, review **at least one** from L02/L03/L05/L06/L07 across a two-day span and select GPU questions according to the separate ONNX/CUDA/Triton coding workshops. On practice days that need tighter exam resemblance, select **6–8 exact-option** variants; reserve sibling `Xxx` questions for deliberate concept-contrast teaching. Do not show [answer key](ATTENDANCE_SWITCH_KEY.md) during first attempts.

**Model inference vs CNN distractor contrast:** a ResNet skip helps gradient propagation (L06); U-Net encoder–decoder feature reuse helps recover spatial detail (L05); freeing no-longer-needed activations is an **inference memory** optimisation (L07). They are not interchangeable definitions.

**Evidence limit:** categorisation is a study index, not proof that every specific metric, bug-identification stem or synthetic variant appeared verbatim in the lecture. The 68 bank questions are tutor-authored based on screenshots and the corresponding slide concepts.
