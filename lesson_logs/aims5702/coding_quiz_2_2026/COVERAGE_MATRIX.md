# Quiz 2 — Syllabus coverage and code pattern matrix

**Sources and labels:** see [SOURCE_MANIFEST.md](SOURCE_MANIFEST.md). These 45 families group **699 source-level entries** in the unified audit; this is *planning coverage*, not independent mastery. A day marked 'primary' means it must teach or test representative atomic targets; it does not imply every entry in that family was tested. Daily 27 Nov–3 Dec **30-question** MCQs rotate all families with different atomic targets. **24 Nov Window A** assesses only L02/L03 (24 MCQs + eight open); **24 Nov Window B** is a separate tensor coding workshop.

## Every audited competency family

| ID | Exact competency family | Primary scheduled contact | Reinforcement / retrieval |
|---|---|---|---|
| F01 | Learning problem/dataset scale | 24 Nov | MCQ 27 Nov–3 Dec |
| F02 | Image/labels representation | 24 Nov | 28 Nov and mixed MCQs |
| F03 | Numeric formats and precision | 23–24 Nov | Mixed MCQs |
| F04 | Tensor/model memory accounting | 24 Nov | 28 Nov and mixed MCQs |
| F05 | Tensor creation/shape/arithmetic | 23–24 Nov | 27 Nov onward |
| F06 | Broadcasting/singletons | 23–24 Nov | 27 Nov onward |
| F07 | Basic/advanced indexing | 23–24 Nov | 27 Nov onward |
| F08 | Storage/strides/views/contiguity | 23–24 Nov | 30 Nov CUDA preconditions and mixed MCQs |
| F09 | Reshape/transpose/concat | 24 Nov | 29 Nov and mixed MCQs |
| F10 | Reductions/einsum | 24 Nov | 27 Nov attention and 1 Dec Triton |
| F11 | Bilinear interpolation | 24 Nov component | 29 Nov cold retry |
| F12 | Code conventions/testing/reproducibility | 23–24 Nov | 29 Nov and mixed MCQs |
| F13 | Host/device operations | 24 Nov | 28 and 30 Nov |
| T01 | Dataset transforms/batching | 24 Nov survey | 28 Nov coding |
| T02 | Linear models/MLP | 24 Nov survey | 28 Nov coding |
| T03 | Activations/norm/dropout | 24 Nov survey | 28–29 Nov |
| T04 | Softmax/cross-entropy/stability | 24 Nov survey | 28 Nov coding |
| T05 | Optimization/training/evaluation | 24 Nov survey | 28 Nov coding |
| C01 | Convolution params | 27 Nov–3 Dec concepts rotation | 26 Nov coding |
| C02 | CNN padding/stride/output shape | 27 Nov–3 Dec concepts rotation | 26 Nov coding |
| C03 | Pooling | 27 Nov–3 Dec concepts rotation | 26 Nov coding |
| C04 | Receptive field/U-Net/segmentation | 27 Nov–3 Dec concepts rotation | 26 Nov coding |
| C05 | ResNet/architecture design | 27 Nov–3 Dec concepts rotation | 26 Nov coding |
| G01 | Autograd/elemental backward | 27 Nov–3 Dec concepts rotation | 26 Nov coding |
| G02 | Manual linear gradients | 27 Nov–3 Dec concepts rotation | 26 Nov coding |
| G03 | Manual convolution gradients | 27 Nov–3 Dec concepts rotation | 26 Nov components + 29 Nov buffer |
| R01 | QKV/attention | 27 Nov–3 Dec concepts rotation | 27 Nov coding |
| R02 | Multi-head shapes/modules | 27 Nov–3 Dec concepts rotation | 27 Nov coding |
| R03 | Positional encodings/RoPE | 27 Nov–3 Dec concepts rotation | 27 Nov coding |
| R04 | Patch/CLS/text application | 27 Nov–3 Dec concepts rotation | 27 Nov components + 29 Nov buffer |
| R05 | Causal masks/decoding | 27 Nov–3 Dec concepts rotation | 29 Nov components |
| I01 | Inference/training differences | 27 Nov–3 Dec concepts rotation | 29 Nov |
| I02 | Quantization/fusion | 27 Nov–3 Dec concepts rotation | 29 Nov |
| I03 | ONNX/IR | 27 Nov–3 Dec concepts rotation | 29 Nov |
| I04 | Annotation/augmentation | 27 Nov–3 Dec concepts rotation | 29 Nov |
| E01 | AI governance frameworks | 27 Nov teaching | 27 Nov–3 Dec mixed MCQs |
| E02 | Synthetic content/copyright/provenance | 27 Nov teaching | 27 Nov–3 Dec mixed MCQs |
| E03 | Human-centred ethics/dependency | 27 Nov teaching | 27 Nov–3 Dec mixed MCQs |
| U01 | GPU foundations/SIMD-SIMT | 26 Nov teaching | 27 Nov–3 Dec mixed MCQs |
| U02 | GPU warp/grid/block/SM launch | 26 Nov teaching | 30 Nov code + mixed MCQs |
| U03 | CUDA indexing/PyCUDA | 26 Nov teaching | 30 Nov cold code |
| U04 | GPU traffic/fusion | 26 Nov teaching | 30 Nov + 1 Dec |
| U05 | Triton elementwise/tile | 1 Dec teaching | 1 Dec cold + Dec 2 mock |
| U06 | Triton GEMM/reduction tiling | 1 Dec teaching | 1 Dec component cold |
| U07 | FlashAttention/online softmax | 1 Dec teaching | 1 Dec numerical + mixed MCQs |

## All 23 pattern families and reproduction commitments

| CP | Reusable coding or reasoning pattern | First substantial date | Depth |
|---|---|---|---|
| CP01 | Tensor shape/dtype/size/device | 24 Nov | A: cold+transfer |
| CP02 | Broadcast/reshape/storage | 24 Nov | A: cold+transfer |
| CP03 | Reductions/einsum | 24 Nov | A: cold+transfer |
| CP04 | Bilinear interpolation | 24 then 29 Nov | B: component cold/transfer |
| CP05 | Naive/stable softmax | 28 Nov | A: cold+transfer |
| CP06 | DataLoader/transforms | 28 Nov | B: component cold |
| CP07 | MLP train/eval | 28 Nov | A: cold+transfer |
| CP08 | Conv shapes/params/pool/RF | 26 Nov | A: cold numerical+code |
| CP09 | Elemental/linear backprop | 26 Nov | A: cold+transfer |
| CP10 | Conv backward | 26 and 29 Nov | B: critical gradient expressions |
| CP11 | Residual projection | 26/29 Nov | B: component cold |
| CP12 | Scaled attention/multihead | 27 Nov | A: cold+transfer |
| CP13 | Sinusoidal/RoPE | 27 Nov | A: key expressions cold |
| CP14 | ViT patches/CLS | 27 and 29 Nov | B: component cold |
| CP15 | Causal masks/LayerNorm/dropout | 29 Nov | B/C: blanks and interpretation |
| CP16 | Quantization/fusion/ONNX | 29 Nov | B/C: calculation and scaffold reading |
| CP17 | CUDA 1D/PyCUDA launch | 30 Nov | A: kernel + wrapper cold |
| CP18 | CUDA 2D flattened | 30 Nov | A: kernel + wrapper cold |
| CP19 | Triton offsets/masked tiles | 1 Dec | A: kernel cold+transfer |
| CP20 | Triton GEMM/tl.sum | 1 Dec | B: tile/reduction blanks |
| CP21 | GPU fusion/memory hierarchy | 26/30 Nov | C: numerical/explanation |
| CP22 | Online softmax/FlashAttention | 1 Dec | B/C: numerical/explanation |
| CP23 | Ethics case distinctions (non-code) | 27 Nov | MCQ case reasoning |

## Explicit scope reductions for the 25 Nov AIMS5701 kickoff

- Preserve a *first independent cold completion* of CP01–03, CP05, CP07–09, CP12–13, CP17–19. These are high-priority, not claims of examiner weighting.
- Reduce CP04, CP06, CP10–11, CP14–16 and CP20 to **component-level** cold checks; keep individual maths, indices and code operations eligible for quiz items. CP21–23 are numerical/interpretation/ethics, not blank-file app builds.
- Do not require complete implementations of A04 optional text/ONNX extensions, A05 optional Problems E/F or full production FlashAttention. Their independently assessable concepts stay in this matrix and in rotated MCQs.
- An unresolved **required** operation (e.g., full-reduction `tl.sum` or four-corner interpolation) must not be silently dropped because its parent exercise is assigned depth B.
- 29 Nov is a protected buffer for genuinely untested high-priority components, not a guaranteed day of new optional applications.

## Risks and source integrity

- **A05 CUDA launch:** the completed LeakyReLU wrapper's blocks arithmetic omits the division; correctly use ceiling division and an index guard.
- **A03:** the completed Linear+ReLU gradient test reportedly fails; diagnose rather than treating printed values as a reliable key.
- **L05:** preserve standard floor-based Conv2d dimensional calculation; an orally suggested ceiling convention is not a universal PyTorch rule.
- **L02/L11:** float16 and bfloat16 exponent/fraction tables contain inconsistent figures; original diagrams plus tested data-format definitions should govern, and any disagreement should be labelled.
- **L07 ethics:** distinguish lecturer's example classifications from authoritative legal guidance; assess the lecturer's taught framework without asserting all simplified legal claims as facts.

The source-level TSV and three audited reports are not duplicated inside this PR; they remain separate Project documents. A new tutor should retrieve them when exact atomic ID wording is needed, or flag that the evidence is unavailable instead of fabricating it.

## Independent conceptual and coding assessments

- **Tuesday 24 Nov Window A:** **L02 12 MCQs + 4 open, L03 12 MCQs + 4 open**, 120 min maximum, with MCQ depth **8 precise / 10 applied / 6 multistep**. The 8 open questions require constructed solutions (memory/precision, broadcasting, storage offsets/contiguity, reductions/einsum, affine layer/parameters, softmax/loss, gradient step, training/validation diagnosis). See [the daily locked blueprint](2026-11-24.md). **No C/G/R/I/E/U questions.**
- **Tuesday 24 Nov Window B:** CP01–03 essential code tutoring → cold reproduction → new transfer, CP04 scaffold-level interpolation. Results stay separate from Window A.
- **27 Nov–3 Dec Window A:** 30 full-syllabus MCQs daily, **F4 T4 C/G5 R5 I4 E4 U4**, with depth **12 recall / 12 applied / 6 multistep**. Track tested and untested original atomic IDs; do not infer mastery of an untested atom from its family.
- **Window B on other days:** dedicated 3h coding workshops as dated, maintaining tutorial → guided construction → unhinted cold completion → changed transfer. MCQ success never marks a CP mastered.
