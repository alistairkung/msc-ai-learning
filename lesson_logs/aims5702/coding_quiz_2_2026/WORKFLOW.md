# AIMS5702 Quiz 2 — Daily tutoring and assessment contract

This folder is a *study plan*, not a new learning-state authority. First read repo `SESSION_WORKFLOW.md`, `TUTORING_CALIBRATION.md`, and `LEARNING_STATE.md`; then this folder's `README.md`, `COVERAGE_MATRIX.md`, the selected day file and the smallest relevant lecture/assignment source. **Don't load every daily file into each tutoring window.** The exact daily file governs that session's scope.

## Fixed rules

1. **Syllabus-driven assessments.** Select the day's cold questions before seeing the learner's performance. The 45 family IDs F01–U07 navigate the 699 original atomic IDs. Questions should sample *atomic targets* within a family; a passed question never upgrades a whole family or all linked skills automatically.
2. **Coding is always tutorial → guided reconstruction → cold completion → unseen variation → later cold recall.** Teach using a *different complete worked example*, then give the learner a scaffold/requirements to implement. Don't write the assessed target solution before the learner attempts it. Hints only after the attempt, with support labelled. A passing supplied test or copied code is not independent recall.
3. **Study depth:** A = full essential code or numerical pattern reconstructed cold and changed; B = key expressions and components reconstructed within a supplied scaffold; C = independently interpret code, outputs, formulas, limitations and numerical results. A lower depth never means outside the quiz.
4. **Cold means** no notes, no answer exposure, no hints, no copied prior implementation. A fresh changed input or task tests transfer. Repetition of a known scaffold without change is not transfer.
5. **Record evidence honestly:** not encountered / taught / guided / cold-completed / transferred / delayed-retained. Mark *not tested* where no attempt occurred. Record syntax, representation-translation, numerical, time-pressure, source-error and conceptual errors separately.
6. **New material:** Ethics and GPU concepts get actual instruction before being judged. Early MCQs may sample them to show the eventual whole-syllabus distribution, but label those misses *not yet taught*, not evidence of regression.
7. **Respect source boundaries.** Original PDFs/assignments primary; revision/transcripts supplementary. Do not treat known incorrect source formula or an unpassed completed notebook cell as the answer key. Lecture 01 is an unresolved source gap.
8. **Minimal coordinator handover:** today's assessed skill IDs and question types, unprompted results, hints used, transfer results, deferred untested IDs, specific next-day recall. Write a course lesson log and update `LEARNING_STATE.md` after an actual substantive session under the repository workflow. Do not pre-fill progress YAML or mastery from this plan.

## First three days and protected cross-course time

- **23 Nov:** 45–60 min ease-in, not a full five-hour day.
- **24 Nov:** one accelerated 90–120 min diagnostic of previously covered concepts through inference, then a 3h tensor coding workshop. A diagnostic sweep cannot demonstrate independent mastery of every item; log untested items.
- **25 Nov:** completely protected for **AIMS5701 project kickoff**; no AIMS5702 work.
- **26 Nov:** 90–120 min *new* GPU concept teaching, then 3h CNN/backprop code.

## Daily MCQs, 27 Nov–3 Dec

One hour of **full-syllabus** MCQs daily. Baseline blueprint: 28 unseen questions, target ~45 min answers + 15 min review, distributed **4 F numeric/tensor; 4 T training; 4 C/G CNN/backprop; 4 R transformers; 3 I inference; 4 E ethics; 5 U GPU**. These are practice quotas, **not a forecast** of exam topic weighting. Within each quota, preselect changing original atomic IDs and include code-reading/shape/numeric MCQs, not just definition recognition. Do not reuse items across days. At least one explicit source-coverage check each day: which targeted atomic IDs were actually tested, which remain untested? Any untrained 27 Nov ethics/GPU content receives a teaching label, not an incorrect-mastery label. On exam morning, reduce or stop if fatigue would worsen performance.

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
### AIMS5702 Quiz 2 — YYYY-MM-DD study handover
Sources consulted (exact lecture slides, assignment pages):
Questions attempted (original skill IDs / CP IDs / form):
Independent cold results (correct / partially correct / incorrect / not attempted):
Hints/tutoring provided (clearly distinguish from cold evidence):
Unseen transfer results:
Errors by type (concept / syntax / shape / arithmetic / representation / time / answer format):
Untested or deferred atomic targets:
Source discrepancies encountered:
Next planned delayed recall:
What should be recorded in lesson_logs/aims5702 and LEARNING_STATE.md:
```
