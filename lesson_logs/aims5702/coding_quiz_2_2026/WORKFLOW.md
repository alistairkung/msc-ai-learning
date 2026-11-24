# AIMS5702 Quiz 2 — Daily tutoring and assessment contract

This folder is a *study plan*, not a new learning-state authority. First read repo `SESSION_WORKFLOW.md`, `TUTORING_CALIBRATION.md`, and `LEARNING_STATE.md`; then this folder's `README.md`, `COVERAGE_MATRIX.md`, the selected day file and the smallest relevant lecture/assignment source. **Don't load every daily file into each tutoring window.** Select **Window A concepts** or **Window B coding** before asking any question; each uses its own assessment protocol and handover. The exact daily file governs that session's scope.

## Fixed rules

1. **Separate assessment windows.** Window A uses conceptual MCQs, written reasoning, calculations and diagram/code *interpretation*, but no code-completion tutoring. Window B uses worked code tutorials, guided reconstruction, unhinted coding and unseen code transfer, but no broad conceptual MCQ sets. Both may explain prerequisite ideas; neither can claim the other track's competence. Preserve separate results.
2. **Syllabus-driven assessments.** Select the day's cold questions before seeing the learner's performance. The 45 family IDs F01–U07 navigate the 699 original atomic IDs. Questions should sample *atomic targets* within a family; a passed question never upgrades a whole family or all linked skills automatically.
3. **Coding is always tutorial → guided reconstruction → cold completion → unseen variation → later cold recall.** Teach using a *different complete worked example*, then give the learner a scaffold/requirements to implement. Don't write the assessed target solution before the learner attempts it. Hints only after the attempt, with support labelled. A passing supplied test or copied code is not independent recall.
4. **Study depth:** A = full essential code or numerical pattern reconstructed cold and changed; B = key expressions and components reconstructed within a supplied scaffold; C = independently interpret code, outputs, formulas, limitations and numerical results. A lower depth never means outside the quiz.
5. **Cold means** no notes, no answer exposure, no hints, no copied prior implementation. A fresh changed input or task tests transfer. Repetition of a known scaffold without change is not transfer.
6. **Record evidence honestly:** not encountered / taught / guided / cold-completed / transferred / delayed-retained. Mark *not tested* where no attempt occurred. Record syntax, representation-translation, numerical, time-pressure, source-error and conceptual errors separately.
7. **New material:** Ethics and GPU concepts get actual instruction before being judged. Early MCQs may sample them to show the eventual whole-syllabus distribution, but label those misses *not yet taught*, not evidence of regression.
8. **Respect source boundaries.** Original PDFs/assignments primary; revision/transcripts supplementary. Do not treat known incorrect source formula or an unpassed completed notebook cell as the answer key. Lecture 01 is an unresolved source gap.
9. **Minimal coordinator handover:** today's assessed skill IDs and question types, unprompted results, hints used, transfer results, deferred untested IDs, specific next-day recall. Write a course lesson log and update `LEARNING_STATE.md` after an actual substantive session under the repository workflow. Do not pre-fill progress YAML or mastery from this plan.

## First three days and protected cross-course time

- **23 Nov:** 45–60 min ease-in, not a full five-hour day.
- **24 Nov Window A:** **Lectures 02 and 03 only**, up to 120 min, **24 MCQs + eight open responses**, with an explicit per-lecture source audit. Do **not** assess L05–L07 or Ethics/GPU in this window.
- **24 Nov Window B:** after a break, a *separate* 180-minute tensor coding workshop CP01–04 with tutorial → guided construction → cold completion → changed transfer.
- **25 Nov one-off exception:** **morning 90-minute concepts-only Window A** between school drop-off and pickup (30 unseen MCQs: L05 CNN 10, L06 Transformer 10, L07 Inference **excluding ethics** 10; 12 recall + 12 applied + 6 multistep; 60 min cold + 20 review + 10 handover). **Afternoon onward strictly protected for AIMS5701 project kickoff. No AIMS5702 coding that day.** Tuesday's deferred coding is not silently considered completed.
- **26 Nov:** 90–120 min *new* GPU concept teaching, then 3h CNN/backprop code.

## Wednesday 25 Nov café-only exception

The [25 Nov day plan](2026-11-25.md) supersedes the earlier *all-day* AIMS5701 reservation **only for the morning 90-minute café interval**. It is an **L05/L06/L07 (inference only)** test, ten questions per source, with 12 recall / 12 applied / 6 numerical. Select atomic targets before any answers, give no intermediate tutoring, and finish with source-specific assessed/untested handover. Strict 60 + 20 + 10 minutes. Afternoon onward remains AIMS5701 work; do not add a coding workshop or take overflow time.

## Daily MCQs, 27 Nov–3 Dec

One hour of **full-syllabus** MCQs daily **in Window A only**. Baseline blueprint: **30 unseen questions** (45–50 min answers + 10–15 min review), distributed **4 F numeric/tensor, 4 T training, 5 C/G CNN/backprop, 5 R transformers, 4 I inference, 4 E ethics, 4 U GPU**. Aim for **12 recall/distinction, 12 application/edge-case and 6 multistep/numerical** items. These quotas do **not** apply to 24 Nov's separate L02/L03 assessment. These are practice quotas, **not a forecast** of exam topic weighting. Within each quota, preselect changing original atomic IDs and include code-reading/shape/numeric MCQs, not just definition recognition. Do not reuse items across days. At least one explicit source-coverage check each day: which targeted atomic IDs were actually tested, which remain untested? Any untrained 27 Nov ethics/GPU content receives a teaching label, not an incorrect-mastery label. On exam morning, reduce or stop if fatigue would worsen performance.

## Tuesday 24 Nov — fixed conceptual assessment (Window A only)

**L02 (all 83 original slides):** 12 MCQs and four open problems. Test number formats and memory; broadcasting compatibility including failure; basic versus advanced/boolean slicing; strides, offsets, view/copy and contiguity; transpose/reshape/concat; reductions with `keepdim`, `max`/`argmax`, `einsum`; code conventions and reproducibility. Avoid multiple questions on the same easy subskill.

**L03 (all 93 original slides):** 12 MCQs and four open problems. Test image/label representations and normalization, perceptron/MLP weight shapes and bias, activations/classifier predictions, softmax and cross-entropy, gradient descent and learning rate, batches/epochs, loss curves, overfitting, and training/evaluation semantics.

**Depth:** among 24 MCQs, **8 precise recall, 10 applied/edge cases, 6 numerical/multistep**. Eight open tasks independently construct L02 (memory/precision, broadcasting, storage/flat offset, reductions/einsum) and L03 (linear outputs/parameter count, complete softmax/loss, gradient update, loss-curve/training interpretation).

**Timebox:** 35 min MCQs + 50 min open responses + 25 min targeted repair and fresh verification + 10 min coverage ledger/handover = 120 min. Select exact atomic targets with slide references in advance, record whether each was independently correct or required help, and explicitly list untested atomic skills. Keep the 23 Nov C02 CNN and I02 quantization preview questions deferred to a later date; they are not part of L02/L03.

## Standard three-hour coding workshop

- 45 min full *worked analogue*, tutor explains math, dims, syntax and failure modes, one connected example rather than hiding context.
- 30 min guided learner reconstruction of a different example, hints in increasing specificity.
- 45 min closed-book, unhinted completion of a preselected scaffold (mark when hints begin).
- 40 min unseen input/shape/task transfer under time pressure.
- 20 min feedback, evidence capture and handover. Insert a brief break inside the three hours as needed (time allocations approximate).

Rotate previously studied CP patterns for delayed recall for ~10–15 minutes within workshops, without displacing the new daily Tier A targets. If time runs short, cut additional worked examples or optional extension implementations, **not** the first independent cold assessment of a core code family.

## Pre-quiz evaluation

2 Dec includes **one separate 60-minute exam-shaped mock**: 16 MCQs/24 marks and 26 marks of code/comment/numerical blanks, in addition to (or replacing part of, if tired) the daily full-syllabus MCQ rotation. Keep a predetermined question blueprint and unseen values/variables. Use 3 Dec only for familiar recall, not new material.

## Handover template (copy after study)

```md
### AIMS5702 Quiz 2 — YYYY-MM-DD Window A concepts / Window B coding
Sources consulted (exact lecture slides and assignment pages):
Predetermined original skill IDs / CP IDs and question types:
Independent cold results (correct / partial / incorrect / not attempted):
Guided explanations/repair (not counted as initial cold success):
Fresh verification or changed coding-transfer results:
Errors by type (concept / syntax / shape / arithmetic / representation / time / answer format):
**Scheduled atomic skills that remained untested:**
Source discrepancies encountered:
Next delayed recall:
Recommended lesson log / LEARNING_STATE.md updates after actual study:
```
