# Full learning-state sync

This file defines the compact conversational command for running the repository's complete end-of-session/update workflow.

`SESSION_WORKFLOW.md` remains the canonical operating protocol. This file is the **explicit shortcut/trigger** that makes the dashboard reconciliation step hard to forget.

## User command

The preferred command is:

> **Sync learning state.**

Treat these as equivalent explicit triggers:

- `Sync learning state.`
- `Update our learning state.`
- `Close the session and sync learning.`
- `Sync learning state and Atlas.`

When one of these is requested after substantive learning, do **not** interpret it as “edit only `LEARNING_STATE.md`.” It means run the complete workflow below.

## Full sync workflow

## Hard safety rules for structured syncs

Before editing `learning_progress.yaml`, `deadlines.yaml`, or dashboard-visible state:

- read the current target-branch version first;
- inspect the relevant schema/validator and regression tests in `dashboard/build.py` and `dashboard/test_build.py` when changing enums, lanes, deadline state, or dashboard-visible labels;
- never invent enum/status values; use only values accepted by the validator;
- when writing free-text YAML scalars that contain `:` or other ambiguous syntax, quote them or use a folded block (`>-`) rather than relying on a plain scalar;
- preserve unrelated structured records and prefer field-level edits over broad range/string replacements;
- if a dashboard-visible label or structural state changes, search the regression tests for expectations tied to the old value.

Required Atlas invariants include:

```text
lanes == continue -> parallel -> protect
all lane targets/topics exist
all deadline statuses are schema-valid
delivery state remains separate from learning/mastery evidence
```

Treat a sync like a transaction: substantive content edits first, source hashes after source content is final, and `meta.source_ref` last.

### 0. Start from current repository state

- read the latest `main` / target branch rather than relying on an earlier snapshot;
- detect concurrent/background changes before writing;
- preserve other agents' work and resolve conflicts by evidence/source responsibility rather than choosing one version wholesale.

### 1. Preserve detailed evidence

For substantive learning, update/create the smallest appropriate focused record:

- numbered/cross-course learning -> `lesson_logs/lessonNN_*.md`;
- live course work -> `lesson_logs/<course_code>/...`;
- durable implementation + tests when implementation itself was part of the learning evidence.

Record outcomes, support needed and evidence boundaries; do not turn logs into transcripts.

### 2. Update `LEARNING_STATE.md`

Always update after a substantive session.

Keep the operational handover current:

- what changed;
- what is comfortable vs fragile;
- evidence strength (independent / guided / same-session / historical / new);
- current Continue / Parallel / Protect priorities;
- next useful step;
- delivery pressure only where it changes planning.

### 3. Reconcile the structured Atlas projection every time

Every explicit learning-state sync must inspect `learning_progress.yaml` even when the conclusion is “no topic status changed.”

Ask, for every affected area:

- did a topic cross a structured evidence boundary?
- did evidence/review date change?
- did the evidence summary, boundary or next action change materially?
- did Continue / Parallel / Protect change?
- did course anchors/remaining requirements or scope change?
- did a new taught topic need its own topic record?
- did the timeline gain a material learning event?

If yes, update only the affected structured records.

Whether or not topic states change, if `LEARNING_STATE.md` changed during the sync:

- refresh `sources.state.sha` to the reviewed blob;
- keep `meta.evidence_through` aligned with the handover's `Learning evidence through` date;
- set `meta.reviewed_on` to the actual reconciliation date;
- update `meta.review_note` to say what was reviewed;
- refresh hashes for any other reviewed source that changed.

This is a reviewed projection, not an automatic mastery inference. Never promote guided work merely because code/tests exist.

### 4. Reconcile delivery planning

Inspect `deadlines.yaml` whenever a due date, submission status, collaboration mode or workload consequence changed.

Deadline urgency can resize study lanes but must not be converted into learning/mastery evidence.

### 5. Check syllabus / roadmap only when warranted

- `MSC_SYLLABUS_MAP.md`: update when actual teaching sequence, upcoming requirement, assignment reality or readiness mapping materially changes.
- `LEARNING_ROADMAP.md`: update only for meaningful strategy/dependency changes, not ordinary session chronology.
- `ARCHITECTURE.md` / `SESSION_WORKFLOW.md`: update only when the learning system or operating protocol changes.

### 6. Validate before calling the sync complete

At minimum:

```bash
python -m pytest dashboard/test_build.py dashboard/test_projection_sync.py
python dashboard/build.py
```

Run relevant learning/practice tests when implementation changed. Run browser smoke when dashboard rendering/interaction changed.

Review the **complete resulting diff** for accidental deletion, stale source hashes, unrelated status promotions, missing lanes, and broad structured-file churn.

After opening/updating the PR, wait for the required GitHub Actions workflows:

```text
Tests
Learning dashboard
```

A sync is **in progress** while either required workflow is queued or running. A sync has **failed** if either required workflow fails.

On CI failure:

1. inspect the actual failed job and logs;
2. identify the root cause rather than retrying or patching blindly;
3. fix the root cause;
4. refresh any source hashes / `source_ref` invalidated by the fix;
5. wait for the new CI run.

Do not report the sync as complete or green until both required workflows have completed successfully.

### 7. Use a branch / PR

Unless the user explicitly requests otherwise:

- make the sync on a current branch;
- open/update a PR;
- report the evidence changes, projection changes and any intentionally unchanged boundaries.

After merge to `main`, GitHub Actions should rebuild/deploy the Learning Atlas.

## Invariant

A learning-state sync is **not complete** while any of the following is true:

- the operational handover says learning evidence is newer than the Atlas projection;
- the Atlas points at an older reviewed `LEARNING_STATE.md` blob;
- required structured invariants are broken;
- the PR's **Tests** or **Learning dashboard** workflow is queued, running, or failed.

The dashboard sync test exists to catch projection drift; the broader schema/regression tests catch structural mistakes. CI success is the final completion gate.
