# AIMS5702 Quiz 2 — GPU concepts and PyCUDA practice, 28 November 2026

**Provenance:** learner-supplied end-of-session handover from dedicated GPU tutor; source study used L09 GPU Programming and A05. This is **reported tutoring evidence**, not an independent execution or source slide-by-slide audit. Code was **statically reviewed**, not compiled or run on a GPU. No MCQ attendance-bank IDs were attempted in this session.

## Session and evidence boundary

The learner completed substantial GPU architecture/execution teaching and an extended **CUDA/PyCUDA** coding workshop, stopping due to reported fatigue. **Triton:** only the basic tile/program/offset ideas introduced; **no independent Triton code**. **FlashAttention:** not taught. **ONNX coding:** not part of this session.

This session uses the tutor's *local* CP01–CP04 labels for its exercise steps. **Do not map those to the master syllabus CP01–04 (PyTorch tensors).** Master mapping here is **CP17 (1D PyCUDA), CP18 (2D PyCUDA), CP19 (Triton, teaching only), CP21 (GPU memory/fusion concepts), CP22 (FlashAttention untested).**

## Conceptual coverage

| Concept | Observed or reported outcome | Boundary |
|---|---|---|
| CPU/GPU work models, throughput vs latency | CPU/GPU parallelism and memory-vs-FLOPs reasoning explained; latency-vs-throughput vocabulary taught | Vocabulary itself not fully retested |
| SM, threads, warps, blocks and grids | Explained block distribution and parallel execution | Strong under taught circumstances; no delayed assessment |
| Warp width and partial warps | Later independent numerical exercises correct after remediation | Initial corrections noted |
| Warp divergence | Independently explained branch-path masking | Conceptual success, not attendance MCQ AQ12 completed |
| Warp scheduler and latency hiding | Correct understanding check | Tensor Core/ALU/scheduler distinctions not independently tested as a whole |
| Global index, grid launch and bounds | 1D index correctly produced; 2D row/col, flattening and guards later produced cold | Grid ceiling division became unreliable at end |
| Registers, shared memory, L1/L2/global, coalescing | Taught, shared-memory reuse explained | Full hierarchy, cache distinctions and coalescing not cold-secured |
| Fusion and memory traffic | Independently computed fused vs unfused read/write counts | Separate standalone fusion kernel unattempted |
| Triton: program IDs, `tl.arange`, vector offsets | Introduced conceptually | No independent numerical mask/tile or implementation test |
| FlashAttention | Not taught | Full conceptual overview still due |

SIMD was background only, consistent with lecturer-reported exclusion from Quiz 2 drills.

## Independent coding demonstrated (after earlier teaching)

**1D kernel:** correctly wrote global indexing, bounds guard, elementwise computation and output assignment in fresh practice; initially forgot C semicolons.

**1D host wrapper:** after teaching mistakes in block/grid roles, ceil division, signature, scalar conversions and transfer modes, later independently wrote a correct variant using:

```python
num_blocks = (n + threads_per_block - 1) // threads_per_block
kernel(
    cuda.In(a), cuda.In(b), cuda.Out(c),
    np.int32(n), np.float32(alpha), np.float32(beta),
    block=(threads_per_block, 1, 1),
    grid=(num_blocks, 1, 1),
)
```

An accompanying kernel still contained a *sign error* and minor syntax mistakes. A separate accumulation task demonstrated correct `cuda.InOut` selection.

**2D CUDA kernel:** after correcting x/y, row/col, width-vs-block dimensions, guard AND-vs-OR and flattening, subsequently wrote this logical pattern independently:

```cpp
int col = blockIdx.x * blockDim.x + threadIdx.x;
int row = blockIdx.y * blockDim.y + threadIdx.y;
int i = row * width + col;
if (row < height && col < width) {
    c[i] = alpha * a[i] - b[i];
}
```

**2D PyCUDA launch:** independently used correctly:

```python
num_blocks_x = (width + block_width - 1) // block_width
num_blocks_y = (height + block_height - 1) // block_height
block = (block_width, block_height, 1)
grid = (num_blocks_x, num_blocks_y, 1)
```

**Final integrated 2D kernel+wrapper task:** all pieces except **both** ceiling-division expressions were correct; learner substituted multiplication for addition. This was **not** a fully correct cold integrated submission. Prior correct isolated responses do not erase this late failure.

## Known gaps (priority ordered)

1. **Ceiling division:** fresh cold numeric and expression checks required: `(n + block_size - 1) // block_size`, and width/height variants. Late errors also included omitted parentheses and floor-rounding.
2. **Integrated precision:** signs/coefficients, C semicolons, argument order/scalar types, host `cuda.In/Out/InOut`, matrix width vs block width, 2D AND guards.
3. **Compilation API:** standalone `SourceModule` compilation and `.get_function` were **not** independently tested. Workshop provided precompiled kernel handles.
4. **Incomplete Triton:** first teach masks, partial tiles, `tl.load`/`tl.store` and `other`, grid, 2D tile indices/broadcast/masks, then test new code.
5. **FlashAttention:** entire conceptual section outstanding — Q/K/V shapes, NxN intermediates, IO/HBM tiling, online normalizer and stable max, weighted sums. Not a full implementation target.
6. **Concept retrieval:** Tensor Core vs CUDA core vs scheduler, latency/throughput, coalescing, cache/shared memory.
7. **ONNX:** export and verification scaffold remain unassessed this weekend; do not infer mastery from conceptual MCQs.

## Revised tutoring sequence

**First 10–15 minutes next GPU session:** one unhinted ceiling-division problem (1D + 2D) and one *short* unseen integrated CUDA example. If broken, explain just the gap and retry with changed values; no full GPU architecture restart.

**Then** Triton program/tile index numerical demo → masked 1D load/store and `other` → 2D indexing/masks → independently fill an Assignment-5-style Triton kernel and launch.

**Then** FlashAttention conceptual walkthrough at lecture level, with at least one independent explanation of why tilewise softmax needs running max/denominator and how global IO is reduced.

**Separately** an ONNX export-and-verification cold scaffold; keep the three lecturer-signalled code areas (ONNX/PyCUDA/Triton) distinct. Sunday is *targeted initial coverage*, not a requirement to fabricate a cold pass if time runs out.

**Future conceptual MCQs:** use AQ03 and AQ12–AQ18 *after* teaching, preserving original A–D options where relevant. None were attempted during this session. The user also requests CNN + Transformer slide-based conceptual review, especially Transformers; retain a bounded separate slot rather than silently deleting it.

## Conditions

No code was executed on actual GPU hardware. `SourceModule` and `get_function` need independent recall. No simulated CI/test success is implied. No broad skill-status promotion from same-session guided corrections or paper-based checks. Stop on fatigue, return later for delayed assessment.
