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

Review the diff for accidental deletion, stale source hashes and unrelated status promotions.

### 7. Use a branch / PR

Unless the user explicitly requests otherwise:

- make the sync on a current branch;
- open/update a PR;
- report the evidence changes, projection changes and any intentionally unchanged boundaries.

After merge to `main`, GitHub Actions should rebuild/deploy the Learning Atlas.

## Invariant

A learning-state sync is **not complete** while the operational handover says learning evidence is newer than the Atlas projection, or while the Atlas still points at an older reviewed `LEARNING_STATE.md` blob.

The dashboard sync test exists to catch exactly that drift.
