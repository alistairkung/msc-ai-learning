# AIMS5702 Quiz 2 — Coding Window B: 60-minute tensor warm-up, 24 November 2026

**Provenance:** learner-supplied end-of-session handover from the dedicated AIMS5702 coding tutor. The tutor named Lecture 02 and Assignments 1 (pp. 1–3) and 2 (pp. 2–4) as sources. This record preserves reported attempts and support **without claiming independent reinspection of those PDF pages**. No grading execution or independent code/test run is documented here. See [the planned full workshop](coding_quiz_2_2026/2026-11-24.md) for CP01–CP04 scope.

## Actual scope and outcome

A **short 60-minute** coding session covered portions of CP01, CP02 and CP03, including tutor-worked examples, guided construction, cold code completion and one changed transfer. **The original 180-minute workshop was not completed. CP04 bilinear interpolation was not attempted.** The conceptual MCQ evidence (15/24 L02/L03) is independently recorded in `quiz2_concepts_l02_l03_2026_11_24.md` and must **not** be cross-credited as cold coding competence.

| Pattern | Cold, independent learner code | Tutoring and changed transfer | Evidence level |
|---|---|---|---|
| **CP01 — creation/metadata/memory** | `torch.arange(4, 15, 2, dtype=torch.float32)` produced correct values/dtype; `x.shape`, `x.dtype` correct. Initial construction omitted `reshape` and printed output; attempted `x.count` and `x.bytes` | With guidance, supplied `.reshape(2, 3)`; `x.numel()` and `x.element_size() * count` after API/method cues. Correct conceptual dims `(2,3)`; tutor supplied exact `torch.Size([2, 3])` print form | **Partial cold**, assisted repair; no independent full-format or bytes API reproduction |
| **CP02 — indexing/storage/broadcast** | Independently wrote basic-slice view `a[:, :7:3]`, advanced-index copy `a[:, [0, 3, 6]]`, and `shared.is_contiguous()` | **Changed transfer successful:** `readings + offsets.unsqueeze(1)` with readings `(2,4,3)`, offsets `(4,)`. Guided sensor task needed help with insertion axis and actually using returned `unsqueeze` view | **Cold completion and unseen transfer for the tested subset**; broader CP02 storage/stride operations not certified |
| **CP03 — reductions/einsum** | Correct `torch.einsum("ij,kj -> ik", readings, weights)`. Incorrectly used `scores.amax()` when task required per-sample maximum plus index (global value only) | After example `scores.max(dim=0)`, identified `scores.max(dim=1)` for best rule per sample. In changed transfer, correctly chose axis `2` but used `max` instead of `sum` for a requested total; tutor supplied `adjusted.sum(dim=2)` | **Mixed/partial**: cold `einsum` succeeded; reductions require unhinted operator-plus-axis checks |

### Worked and guided teaching (not cold results)

Tutor showed tensor creation and dtype bytes; stepped slicing/storage offsets; advanced indexing and separate storage; transpose/contiguous copies; and pairwise dot products via broadcasting and `einsum`. In guided sensor work, the row mean was correct at first attempt; offset broadcasting needed assistance. During creation practice, a nested-list constructor syntax error was repaired, and the learner then independently constructed a `float16` zeros tensor using `torch.full`.

## Specifically untested cold operations

- **CP01:** device placement; shared-storage byte accounting; exact `torch.Size([...])` printed formatting on fresh input; uncued `numel/element_size` byte calculation.
- **CP02:** numerical transpose stride/offset traces, `.contiguous()` copy effects, reshape copy vs view, `None` insertion, advanced-index result contiguity, more complex independent stride and storage-offset checks.
- **CP03:** unhinted `sum` versus `mean` selection with correct axes; correct `max(dim=...)` returning value and index; pairwise dot-product loop and broadcast alternatives; changed `einsum` labels/output axes.
- **CP04:** **all** bilinear interpolation work deferred; no tutorial, cold code or transfer evidence.

Do not infer that these untested operations were failed. Do not infer that examples shown by the tutor were independently reproduced. The learner's conceptual tensor-storage corrections in Window A do not certify code-writing ability.

## Two priority delayed coding checks (use fresh values/requirements)

1. **CP01 cold blank:** independently construct a typed tensor, calculate `numel` and byte usage using the actual methods (without cues), and report the **exact printed** `torch.Size([...])`. Distinguish incorrect requested format from wrong dimensions.
2. **CP03 cold blank:** on a new batched tensor, implement **one total** and **one maximum plus argmax index**, independently choosing **both operator and reduction axis** from the requested output. Keep `sum` versus `max` and `dim` distinct.

When resuming wider coding, select remaining **CP02 transpose/stride/offset and `.contiguous()`** cases from the predetermined syllabus inventory before adding optional depth. Preserve the original coding workshop's CP04 interpolation for later, not as completed.

## Coordinator handover and scheduling

- **24 Nov concepts Window A:** 24/24 MCQs, original **15/24**; all nine misses reviewed; **O1–O8 unattempted**.
- **24 Nov coding Window B:** completed a **60-minute partial workshop**; cold progress was genuine in CP02's tested items and `einsum`, with separate guided repairs in CP01/CP03. **Full CP01–CP04 coverage remains incomplete.**
- **25 Nov:** morning L05/L06/L07 café MCQs; afternoon protected for AIMS5701 project kickoff. No coding catch-up allocated there.
- Later coding scheduling needs to explicitly recover the **untested and deferred** CP elements; avoid treating this shortened workshop as the planned full three-hour session.

This log is qualitative evidence, not a direct change to the Learning Atlas mastery classifications.
