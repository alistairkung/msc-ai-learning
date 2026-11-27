# AIMS5702 Quiz 2 — attendance option-inversion question bank

**Source:** all 20 original student-provided attendance screenshots, representing 18 distinct stems; course sources L02, L03, L05, L06, L07, L09. **Authored:** 27 November 2026. **Total:** 68 questions: 48 exact-option variants and 20 concept-switch questions (new options). **27** exact-option questions have a different intended key from the screenshot (including diagnostic questions). This is an authored practice bank, not a prediction of the paper.

**Find your lecture's questions:** [L02/L03/L05/L06/L07/L09 index](ATTENDANCE_LECTURE_MAP.md) (includes cross-lecture distractor links).\n\n**Do not open [the answer key](ATTENDANCE_SWITCH_KEY.md) before a cold attempt.** Exact-option questions reuse the original **A–D text from the repository's screenshot transcription**. Check source screenshots for exact punctuation if literal fidelity matters. New-option concept switches are **separate** from the lecturer's exact-option guarantee.

Mode definitions: **exam** = altered stem, valid positive answer; **switch** = altered concept with another valid original choice; **diagnostic** = identify a specific false claim/bug in the original options (do not treat that false statement as true); **concept-switch** = new A–D answers based on another course-taught topic.

## 48 exact-option changed-stem questions

### AQ01-V01 — AQ01 Broadcasting shapes [exam]

Which broadcastable pair produces result shape (5,6,4)?

A. (5,1,4) and (6,4)

B. (2,4,1) and (4,2)

C. (4,3) and (3,4)

D. (5,3,4) and (5,4)

### AQ01-V02 — AQ01 Broadcasting shapes [switch]

Which broadcastable pair produces result shape (2,4,2)?

A. (5,1,4) and (6,4)

B. (2,4,1) and (4,2)

C. (4,3) and (3,4)

D. (5,3,4) and (5,4)

### AQ02-V01 — AQ02 Operation fusion [exam]

Two adjacent operations are fused so an intermediate tensor is no longer written to GPU global memory. What benefit results?

A. Disable GPU execution providers

B. Replace dynamic shapes with loops

C. Increase total floating-point operations

D. Reduce memory read/write traffic

### AQ02-V02 — AQ02 Operation fusion [switch]

An inefficient rewrite duplicates matrix multiplications. Which listed change increases arithmetic work?

A. Disable GPU execution providers

B. Replace dynamic shapes with loops

C. Increase total floating-point operations

D. Reduce memory read/write traffic

### AQ02-V03 — AQ02 Operation fusion [switch]

Which listed change affects GPU execution-provider availability rather than operation fusion?

A. Disable GPU execution providers

B. Replace dynamic shapes with loops

C. Increase total floating-point operations

D. Reduce memory read/write traffic

### AQ03-V01 — AQ03 FlashAttention IO [exam]

A GPU attention kernel no longer materialises a full attention score matrix in HBM. Which outcome is it seeking?

A. Avoids large global memory reads/writes

B. Changes exact softmax into linear sum

C. Limits sequence length to one token

D. Removes the need for query projections

### AQ03-V02 — AQ03 FlashAttention IO [exam]

FlashAttention keeps K/V tiles on chip between fused computations. What explains the IO improvement?

A. Avoids large global memory reads/writes

B. Changes exact softmax into linear sum

C. Limits sequence length to one token

D. Removes the need for query projections

### AQ04-V01 — AQ04 Pretrained CNN head [exam]

The input is still RGB but the pretrained ImageNet CNN must emit logits for 12 rather than 1000 classes. Which change fits?

A. Removing the softmax activation from nn.CrossEntropyLoss because PyTorch requires one-hot targets

B. Changing the input channel count of the first convolutional layer to 12 to match the number of character classes

C. Replacing the final classification layer so its output dimension matches 12 classes instead of 1,000 ImageNet classes

D. Removing all batch normalization layers so the model can be exported to ONNX format

### AQ04-V02 — AQ04 Pretrained CNN head [diagnostic]

Which proposal wrongly equates the number of input image channels with the number of output classes?

A. Removing the softmax activation from nn.CrossEntropyLoss because PyTorch requires one-hot targets

B. Changing the input channel count of the first convolutional layer to 12 to match the number of character classes

C. Replacing the final classification layer so its output dimension matches 12 classes instead of 1,000 ImageNet classes

D. Removing all batch normalization layers so the model can be exported to ONNX format

### AQ04-V03 — AQ04 Pretrained CNN head [diagnostic]

Which proposal incorrectly treats deleting all BatchNorm layers as mandatory for ONNX export?

A. Removing the softmax activation from nn.CrossEntropyLoss because PyTorch requires one-hot targets

B. Changing the input channel count of the first convolutional layer to 12 to match the number of character classes

C. Replacing the final classification layer so its output dimension matches 12 classes instead of 1,000 ImageNet classes

D. Removing all batch normalization layers so the model can be exported to ONNX format

### AQ05-V01 — AQ05 Residual identity [exam]

A deep residual network uses y=F(x)+x. Which listed explanation most directly accounts for easier optimisation?

A. Identity branches double channels

B. Residual paths replace softmax

C. Skip connections eliminate activations

D. Identity paths preserve gradients

### AQ05-V02 — AQ05 Residual identity [diagnostic]

Which listed statement falsely assumes an identity skip connection necessarily doubles the channel dimension?

A. Identity branches double channels

B. Residual paths replace softmax

C. Skip connections eliminate activations

D. Identity paths preserve gradients

### AQ06-V01 — AQ06 Unmasked attention permutation [exam]

Reordering input tokens in attention without masks or positional encodings should cause which change in the attention weights?

A. Weights permute with inputs

B. Weights zero out future tokens

C. Weights become uniform constants

D. Weights remain identical in order

### AQ06-V02 — AQ06 Unmasked attention permutation [switch]

After adding a causal future-token mask to attention, what happens at forbidden future positions?

A. Weights permute with inputs

B. Weights zero out future tokens

C. Weights become uniform constants

D. Weights remain identical in order

### AQ06-V03 — AQ06 Unmasked attention permutation [switch]

If all unmasked attention logits for a query are equal and no attention mask is applied, what happens to the softmax attention weights?

A. Weights permute with inputs

B. Weights zero out future tokens

C. Weights become uniform constants

D. Weights remain identical in order

### AQ07-V01 — AQ07 Causal attention mask [exam]

An autoregressive decoder masks the upper triangle of its attention scores. What leakage does this prevent?

A. Eliminate positional embeddings

B. Prevent attending to future tokens

C. Replace softmax normalization

D. Reduce hidden dimension size

### AQ07-V02 — AQ07 Causal attention mask [diagnostic]

Which claim incorrectly confuses causal masking with removing positional embeddings?

A. Eliminate positional embeddings

B. Prevent attending to future tokens

C. Replace softmax normalization

D. Reduce hidden dimension size

### AQ08-V01 — AQ08 ViT aggregation [exam]

A ViT appends a learnable global token whose final representation serves classification. Which option describes this?

A. Using causal triangular masks

B. Using 2×2 max pooling

C. Using a learnable CLS token

D. Using fixed int8 lookup tables

### AQ08-V02 — AQ08 ViT aggregation [switch]

An autoregressive text model hides tokens to the right. Which listed technique is used?

A. Using causal triangular masks

B. Using 2×2 max pooling

C. Using a learnable CLS token

D. Using fixed int8 lookup tables

### AQ08-V03 — AQ08 ViT aggregation [switch]

A convolutional network reduces each 2-by-2 region to its single largest activation. Which operation matches?

A. Using causal triangular masks

B. Using 2×2 max pooling

C. Using a learnable CLS token

D. Using fixed int8 lookup tables

### AQ09-V01 — AQ09 train/eval [exam]

A network containing BatchNorm with tracked running statistics and Dropout switches to eval(). What is expected?

A. Batch stats and no normalization

B. Frozen stats and no dropout

C. Batch stats and higher dropout

D. Running stats and zeroed weights

### AQ09-V02 — AQ09 train/eval [diagnostic]

Which listed option falsely claims that entering eval() increases dropout?

A. Batch stats and no normalization

B. Frozen stats and no dropout

C. Batch stats and higher dropout

D. Running stats and zeroed weights

### AQ10-V01 — AQ10 ONNX export/verify [exam]

A trained CNN is exported for a runtime outside PyTorch and then its predictions are compared. What is the purpose?

A. To compress the handwritten character dataset into a single lossless .zip archive

B. To serialize the model into a framework-agnostic computation graph and confirm its numerical outputs match PyTorch

C. To automatically search for optimal learning rates and batch sizes during training

D. To convert convolutional layers into Triton online softmax kernels

### AQ10-V02 — AQ10 ONNX export/verify [diagnostic]

Which option describes tuning batch size and learning rate rather than model export?

A. To compress the handwritten character dataset into a single lossless .zip archive

B. To serialize the model into a framework-agnostic computation graph and confirm its numerical outputs match PyTorch

C. To automatically search for optimal learning rates and batch sizes during training

D. To convert convolutional layers into Triton online softmax kernels

### AQ11-V01 — AQ11 Classification metrics [exam]

For a multiclass classifier with class labels and probability scores but no real-valued regression targets, which metric set fits?

A. (I) and (II) only

B. (I) and (III) only

C. (II) and (III) only

D. (I), (II) and (III)

### AQ11-V02 — AQ11 Classification metrics [switch]

A grading contract explicitly requires F1 on hard class predictions and RMSE on a numeric prediction, excluding rank metrics. Which set?

A. (I) and (II) only

B. (I) and (III) only

C. (II) and (III) only

D. (I), (II) and (III)

### AQ11-V03 — AQ11 Classification metrics [switch]

A model outputs binary classification scores and real-valued regression predictions, but no hard classification threshold is chosen. Which metrics can be computed directly?

A. (I) and (II) only

B. (I) and (III) only

C. (II) and (III) only

D. (I), (II) and (III)

### AQ11-V04 — AQ11 Classification metrics [switch]

A multi-task model has a scored classifier and a regressor. Which of the three metrics could be useful across both tasks?

A. (I) and (II) only

B. (I) and (III) only

C. (II) and (III) only

D. (I), (II) and (III)

### AQ12-V01 — AQ12 Warp divergence [exam]

Within a warp, threads choose both sides of a conditional. Which execution mechanism is described in the GPU lecture?

A. By dynamically splitting the warp into independent hardware cores instantly

B. Via execution masking by the compiler, serializing the execution of both branches

C. By running branches concurrently on separate L2 caches

D. Branching has zero performance penalty on modern GPUs

### AQ12-V02 — AQ12 Warp divergence [diagnostic]

Which option wrongly claims conditional divergence carries no performance penalty on modern GPUs?

A. By dynamically splitting the warp into independent hardware cores instantly

B. Via execution masking by the compiler, serializing the execution of both branches

C. By running branches concurrently on separate L2 caches

D. Branching has zero performance penalty on modern GPUs

### AQ13-V01 — AQ13 Warp width [exam]

A standard NVIDIA warp has how many threads?

A. 4 threads

B. 16 threads

C. 32 threads

D. 64 threads

### AQ13-V02 — AQ13 Warp width [switch]

If one warp's 32 threads are partitioned into eight equal groups, how many threads per group?

A. 4 threads

B. 16 threads

C. 32 threads

D. 64 threads

### AQ13-V03 — AQ13 Warp width [switch]

How many threads belong to half of a standard NVIDIA warp?

A. 4 threads

B. 16 threads

C. 32 threads

D. 64 threads

### AQ13-V04 — AQ13 Warp width [switch]

How many threads are contained in two full NVIDIA warps?

A. 4 threads

B. 16 threads

C. 32 threads

D. 64 threads

### AQ14-V01 — AQ14 Tiled softmax [exam]

A GPU uses a separate softmax denominator for every tile. Why cannot the separately normalized tile results just be concatenated?

A. Softmax has a negative derivative everywhere.

B. Softmax is not an associative property

C. Softmax cannot be evaluated using floating-point numbers.

D. Exponential terms may encounter division by zero on GPU accelerators.

### AQ14-V02 — AQ14 Tiled softmax [exam]

FlashAttention-style exact tiled softmax tracks a running max and denominator. What conceptual challenge motivates the correction?

A. Softmax has a negative derivative everywhere.

B. Softmax is not an associative property

C. Softmax cannot be evaluated using floating-point numbers.

D. Exponential terms may encounter division by zero on GPU accelerators.

### AQ15-V01 — AQ15 Block-size multiple [exam]

A CUDA kernel uses 48 threads per block, underfilling its last warp. Why might a multiple-of-32 block size help?

A. To prevent wasted threads within warps

B. To bypass global memory capacity limits

C. Because the maximum grid dimensionality is strictly 32

D. To force the compiler to compile using PyCUDA instead of NVCC

### AQ15-V02 — AQ15 Block-size multiple [diagnostic]

Which proposed reason incorrectly says CUDA's maximum grid dimensionality must be 32?

A. To prevent wasted threads within warps

B. To bypass global memory capacity limits

C. Because the maximum grid dimensionality is strictly 32

D. To force the compiler to compile using PyCUDA instead of NVCC

### AQ16-V01 — AQ16 Triton mask [exam]

A Triton vector tile has offsets beyond a length N in its last program. Why mask the load and store?

A. To prevent out-of-bounds memory errors.

B. To encrypt the data stream passing through the L2 cache.

C. To switch between FP32 and FP64 precision automatically.

D. To satisfy Python syntax requirements for loop unrolling.

### AQ16-V02 — AQ16 Triton mask [diagnostic]

Which option incorrectly asserts that an explicit load/store mask converts FP32 into FP64?

A. To prevent out-of-bounds memory errors.

B. To encrypt the data stream passing through the L2 cache.

C. To switch between FP32 and FP64 precision automatically.

D. To satisfy Python syntax requirements for loop unrolling.

### AQ17-V01 — AQ17 CUDA global index [exam]

Which 1D CUDA indexing formula is correct for multiple blocks of arbitrary block width?

A. int i = blockIdx.x + threadIdx.x;

B. int i = threadIdx.x * blockDim.x + blockIdx.x;

C. int i = blockIdx.x * blockDim.x + threadIdx.x;

D. int i = gridDim.x * blockIdx.x + threadIdx.x;

### AQ17-V02 — AQ17 CUDA global index [diagnostic]

Which buggy formula simply adds block index to local thread index, ignoring block width?

A. int i = blockIdx.x + threadIdx.x;

B. int i = threadIdx.x * blockDim.x + blockIdx.x;

C. int i = blockIdx.x * blockDim.x + threadIdx.x;

D. int i = gridDim.x * blockIdx.x + threadIdx.x;

### AQ17-V03 — AQ17 CUDA global index [diagnostic]

Which buggy formula incorrectly multiplies the local thread index by block width before adding block index?

A. int i = blockIdx.x + threadIdx.x;

B. int i = threadIdx.x * blockDim.x + blockIdx.x;

C. int i = blockIdx.x * blockDim.x + threadIdx.x;

D. int i = gridDim.x * blockIdx.x + threadIdx.x;

### AQ17-V04 — AQ17 CUDA global index [diagnostic]

Which candidate incorrectly substitutes gridDim.x for blockDim.x in the block stride?

A. int i = blockIdx.x + threadIdx.x;

B. int i = threadIdx.x * blockDim.x + blockIdx.x;

C. int i = blockIdx.x * blockDim.x + threadIdx.x;

D. int i = gridDim.x * blockIdx.x + threadIdx.x;

### AQ18-V01 — AQ18 Tensor Cores [exam]

Which SM unit is specialised for fast matrix multiplication?

A. Arithmetic Logic Unit (ALU)

B. Warp Scheduler

C. Tensor Core

D. Threads

### AQ18-V02 — AQ18 Tensor Cores [switch]

Which listed SM component selects and schedules ready warps?

A. Arithmetic Logic Unit (ALU)

B. Warp Scheduler

C. Tensor Core

D. Threads

### AQ18-V03 — AQ18 Tensor Cores [switch]

Which listed item is a general arithmetic/logic circuit rather than a tensor specialised unit?

A. Arithmetic Logic Unit (ALU)

B. Warp Scheduler

C. Tensor Core

D. Threads

### AQ18-V04 — AQ18 Tensor Cores [switch]

Which listed item is a software execution entity, not a dedicated arithmetic circuit?

A. Arithmetic Logic Unit (ALU)

B. Warp Scheduler

C. Tensor Core

D. Threads


## 20 concept-switch items (new options, for distractor-depth practice)

### X01 — U-Net role [concept-switch; linked AQ05]

A segmentation architecture downsamples feature maps and then upsamples while reusing high-resolution encoder features. Which architecture?

A. ResNet

B. U-Net

C. ONNX

D. FlashAttention

### X02 — ResNet versus U-Net [concept-switch; linked AQ05]

Which distinction matches the two architectures as presented in the CNN/Transformer lectures?

A. ResNet uses additive identity residuals; U-Net upsamples and combines encoder details

B. ResNet uses only a contracting path; U-Net deletes all high-resolution features

C. Both networks are defined by causal attention masking

D. Both architectures are model-export graph formats

### X03 — Output classes versus channels [concept-switch; linked AQ04]

An RGB pretrained CNN changes from 1000 ImageNet classes to 12 categories. Which network dimension must change?

A. The first convolution input channels

B. The final classifier output dimension

C. The number of input spatial channels and classes must always match

D. The image width must become 12

### X04 — Input channels versus classes [concept-switch; linked AQ04]

A pretrained CNN's first convolution expects 3 input channels, but a new sensor produces 5. Labels are unchanged. Which dimension changes?

A. Final classifier number of classes

B. Pooling stride

C. First convolution input channels

D. Softmax temperature

### X05 — CrossEntropyLoss API [concept-switch; linked AQ04]

For standard PyTorch CrossEntropyLoss with integer class targets, what should the classifier produce?

A. Raw logits (B,C) and integer target class indices

B. Softmax probabilities and mandatory one-hot target matrices

C. A single regression scalar and a continuous target

D. A fully exported ONNX graph as the loss input

### X06 — Causal versus permutation [concept-switch; linked AQ06]

Without positional information self-attention is permutation equivariant. Which *additional* mechanism forbids a decoder attending to later tokens?

A. Reordering token vectors

B. A causal future-position mask

C. Increasing embedding width

D. Adding a CLS token

### X07 — Positional encoding versus mask [concept-switch; linked AQ07]

How do positional information and causal masking differ in their function?

A. Position encodings convey order; causal masks hide future-token access

B. Both remove the need for Q/K projections

C. Both make attention weights uniform

D. Position encodings are only a way to set the dropout probability

### X08 — ViT versus pooling [concept-switch; linked AQ08]

A CNN reduces each 2×2 spatial neighborhood to its maximum. Which operation is this, rather than the ViT global-token mechanism?

A. Learnable CLS aggregation

B. 2×2 max pooling

C. Causal masking

D. ONNX exporting

### X09 — BatchNorm versus LayerNorm [concept-switch; linked AQ09]

A model in eval() contains BatchNorm and LayerNorm. Which statement is accurate?

A. Both freeze learned weights to zero

B. BatchNorm may use stored running statistics; LayerNorm does not depend on running batch means

C. LayerNorm becomes Dropout

D. BatchNorm must be deleted to export ONNX

### X10 — Dropout evaluation [concept-switch; linked AQ09]

Standard PyTorch Dropout switches to eval(). What happens to its random masking?

A. It doubles the mask rate

B. It masks every activation

C. It stops masking and acts as identity

D. It changes channels

### X11 — ONNX unused op deletion [concept-switch; linked AQ02]

The model-inference lecture lists both fusion and unused-op deletion. Which is an example of unused-op deletion?

A. Fuse linear with LayerNorm

B. Remove a redundant dropout operator

C. Increase floating-point operations

D. Disable GPU execution providers

### X12 — ONNX numerical verification [concept-switch; linked AQ10]

Which result verifies that an exported ONNX model behaves like its original PyTorch model?

A. ONNX Runtime outputs agree numerically with PyTorch outputs

B. Training dataset becomes ZIP

C. Batch size gets tuned automatically

D. Convolutions become Triton softmax

### X13 — Regression metric [concept-switch; linked AQ11]

Which metric assesses a continuous-valued regression target such as energy usage prediction?

A. F1 score

B. ROC AUC

C. RMSE

D. Classification accuracy

### X14 — Ranking metric [concept-switch; linked AQ11]

For binary classification scores, which metric evaluates ranking performance across thresholds rather than one chosen threshold?

A. F1 at a fixed threshold

B. ROC AUC

C. RMSE

D. Pixel-wise max pooling

### X15 — Warp scheduler [concept-switch; linked AQ18]

What role does the warp scheduler have inside a streaming multiprocessor?

A. Perform every tensor multiply

B. Select ready warps for execution

C. Store the ONNX graph

D. Set every warp size to 64

### X16 — CUDA 2D flattened index [concept-switch; linked AQ17]

A row-major 2D tensor has width W and coordinate (row,col). Which flattened offset should a CUDA kernel use?

A. row+col

B. row*W+col

C. col*W+row

D. gridDim.x*row+col

### X17 — Triton offsets [concept-switch; linked AQ16]

For 1D Triton elementwise processing, which expression creates current program's vectorised offsets?

A. blockIdx.x + threadIdx.x

B. tl.program_id(0)*BLOCK_SIZE + tl.arange(0,BLOCK_SIZE)

C. torch.argmax(x,dim=0)

D. gridDim.x*blockIdx.x + threadIdx.x

### X18 — FlashAttention memory [concept-switch; linked AQ03]

Which best describes the FlashAttention performance idea as taught?

A. Keep fused tiled attention intermediates in fast on-chip storage to reduce HBM traffic

B. Approximate every attention softmax using only linear sums

C. Require a one-token sequence

D. Discard query projections

### X19 — Softmax normaliser [concept-switch; linked AQ14]

Why must tiled exact softmax track a running normaliser across blocks?

A. Different tiles have different partial denominators

B. Softmax needs integer inputs

C. All future tokens must be masked

D. Exponentials cannot run on a GPU

### X20 — Broadcasting trap [concept-switch; linked AQ01]

Which shape pair fails right-aligned broadcasting?

A. (5,1,4) and (6,4)

B. (2,4,1) and (4,2)

C. (4,3) and (3,4)

D. (2,1,5) and (1,3,5)


## Tutor protocol

**Daily technical practice:** eight questions, primarily **exact-option** variants; rotate all 18 AQ families over 2–3 sessions; include alternative correct letters where legitimately supported. Limit diagnostic/error-spotting items to 1–2 per daily set to avoid shallow cue matching. Add concept-switch questions on topics such as U-Net/ResNet or BatchNorm/LayerNorm as supplementary checks; they **do not** preserve the original options and must never be misrepresented as guaranteed lecturer-style items.

**Daily ethics:** eight separate lecture-faithful L07 ethics questions using [ETHICS_EXAM_SCOPE.md](ETHICS_EXAM_SCOPE.md). Original lecturer guidance was **8 ethics + 8 technical MCQs, with at least six technical** drawn from altered attendance questions; practising eight attendance variants is a *study choice*, not a guaranteed exam prediction.

**Cold evidence:** one question at a time; record ID, first answer, timing and confidence, *then* reveal answer and explain every choice. Missing an originally wrong choice that becomes right in a new question indicates a concept-inversion gap. Avoid repeat identical stems within 72 hours. 2 Dec mock should still include 1–2 out-of-bank technical transfer questions.
