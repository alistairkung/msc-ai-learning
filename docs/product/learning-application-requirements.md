# MSc Learning Application — Workflow-Parity Product Requirements

**Version:** 0.1 — requirements proposal, not an implementation commitment  
**Prepared:** 3 October 2026, Asia/Singapore  
**Primary user:** Alistair Kung  
**Reference repository:** `alistairkung/msc-ai-learning`  
**Reviewed `main` commit:** `22453d567d9da77e6b56ee42bf305c1bed8d5244`  
**Latest recorded learning evidence:** 2 October 2026  
**Objective:** Reproduce the current tutoring, repository, learning-state and Learning Atlas workflows in an application without depending on one chat platform's memory or GitHub integration.

---

## Contents

1. [Product definition and parity boundary](#1-product-definition-and-parity-boundary)
2. [Review method and limitations](#2-review-method-and-limitations)
3. [Current system and source responsibilities](#3-current-system-and-source-responsibilities)
4. [Recent usage and what it implies](#4-recent-usage-and-what-it-implies)
5. [Observed gaps that the application must address](#5-observed-gaps-that-the-application-must-address)
6. [Functional requirements](#6-functional-requirements)
7. [Data and compatibility contracts](#7-data-and-compatibility-contracts)
8. [Sync and execution lifecycle](#8-sync-and-execution-lifecycle)
9. [Application structure and reuse strategy](#9-application-structure-and-reuse-strategy)
10. [Parity acceptance scenarios](#10-parity-acceptance-scenarios)
11. [Build sequence and release gates](#11-build-sequence-and-release-gates)
12. [Quality, measurement and operational requirements](#12-quality-measurement-and-operational-requirements)
13. [Deferred scope and decisions](#13-deferred-scope-and-decisions)
14. [Source register](#14-source-register)

---

## 1. Product definition and parity boundary

### 1.1 The product to build

Build a **personal, evidence-backed learning workspace with a conversational tutor and a reliable GitHub workflow executor**.

The application must support the complete loop:

```text
Resume from current evidence and priorities
    → retrieve / learn / reason / implement / test
    → preserve outcomes and assistance boundaries
    → update the operational handover
    → reconcile the Learning Atlas projection and relevant plans
    → propose a coherent GitHub change
    → validate, inspect failures and repair within authorised scope
    → obtain human review / merge
    → verify the published Atlas
    → resume later, on another device or with another model
```

The defining requirement is continuity across these steps. A good chatbot with a repository viewer is insufficient. A coding agent that forgets the learning conversation is also insufficient. The tutor's reasoning, the learner's attempts, the agreed implementation boundary and the eventual repository changes must remain connected. This follows the repository's architecture and operating protocols, and the user's current request for an application. [R-ARCH] [R-SESSION] [R-SYNC]

### 1.2 What parity means

**Workflow parity** means the learner can perform the existing end-to-end tasks without manually transporting context, editing several bookkeeping files, watching CI in another window, or reconstructing the state after switching devices.

**Feature parity** includes the existing Atlas views, evidence dimensions, source links, course mapping, study lanes, delivery planning, code/test workflows and GitHub review/publication boundaries.

Parity does **not** require preserving every current implementation detail or defect. An application can replace manual hash maintenance with deterministic code while preserving the same integrity guarantee. It must not replace nuanced learning evidence with a mastery score merely because that is easier to display.

The first release should target **one learner, the existing learning repository, and explicitly connected project repositories**. General-purpose course administration, multiple learners and a marketplace are not part of this brief.

### 1.3 Requirement classifications

- **P — Existing parity:** directly supported by current repository protocols, implementation, recent use, or the user's explicit workflow description.
- **E — Enabling / hardening:** a proposed application mechanism needed to reproduce that behaviour reliably, or to fix a demonstrated failure mode. It is not claimed to exist today.
- **L — Later:** useful extensions that do not block parity. These are listed separately in Section 13.

All P and E requirements below are release requirements for the stated parity target. They may be delivered incrementally; an earlier milestone must not be described as full parity.

### 1.4 Product principles

The learner owns the learning objective and meaningful engineering decisions. Models may propose interpretations; deterministic code owns mechanical transformations and execution state. Human review remains the boundary for accepting the learning record. CI verifies repository integrity, not whether the learner has mastered a concept.

The application should remove bookkeeping, not useful intellectual effort. Its learner-facing interface should remain small: a question, an attempt, useful feedback and the next step. Detailed evidence, context selection and execution receipts should be available without being dumped into every tutoring turn. [R-SESSION] [R-ENGINEERING]

---

## 2. Review method and limitations

### 2.1 Evidence reviewed

This review covers the workflow-bearing parts of the repository: architecture and operating protocols; current handover and relevant roadmap/syllabus sections; structured projection and delivery data; the Atlas builder, JavaScript, browser checks and validation tests; both GitHub Actions workflow definitions; the lesson index; selected recent learning/decision logs; and representative exercise code.

It also reviewed the metadata and descriptions of **35 recent pull requests, #17 through #51**, covering repository organisation, study sessions, scaffolding, projection repairs, delivery updates and concurrent-branch reconciliation. Selected underlying records were read to check how those PR descriptions correspond to durable learning evidence. PR counts are not session counts: some PRs are documentation-only, some are follow-ups, and some were superseded without merging.

The prior 26 September architecture review was read as a historical comparison, not treated as current policy. The user's present request to build an application supersedes that review's earlier caution against moving ordinary tutoring into a custom application. [R-REVIEW]

### 2.2 Verification boundary

This was a **read-only, workflow-level review**, not a line-by-line correctness audit of every historical exercise. The complete original tutoring transcripts, private learner profile and every original lecture/assignment attachment were not available as primary evidence in this review. Some repository records are explicitly reconstructed or learner-reported; those qualifications must survive migration.

A local clone failed because the execution environment could not resolve `github.com`. Consequently, local tests and a browser rendering were **not rerun**. GitHub reported successful completed `Tests` and `Learning dashboard` runs for the pinned `main` commit: run IDs `36985122033` and `36985122025`, respectively. That verifies the reported workflow outcomes, not an independent inspection of the live deployed page. [G-MAIN-TESTS] [G-MAIN-ATLAS]

The branch metadata reported `protected: false`. Other repository rulesets were not exhaustively audited, so this is not a claim that every possible governance mechanism is absent. The application must enforce its own configured completion gate regardless. [G-BRANCH]

### 2.3 How to interpret recommendations

A source-backed description says what the system currently does or records. A requirement says what the application must support. Proposed entities, durable jobs, adapters and UI screens are implementation suggestions, not descriptions of software already present in the repository.

---

## 3. Current system and source responsibilities

### 3.1 The repository is several distinct kinds of memory

| Source | Responsibility | What it must not become |
|---|---|---|
| `ARCHITECTURE.md` | Stable system design and source responsibilities | A session diary |
| `SESSION_WORKFLOW.md` | Tutoring and session operating protocol | A substitute for current learning state |
| `SYNC_LEARNING_STATE.md` | Explicit full-sync trigger, safeguards and completion gate | An instruction to edit only one Markdown file |
| Exercise and test files | What was implemented and what behaviour is tested | Proof of independent authorship or retention |
| Focused lesson/course logs | What was taught, attempted, understood, repaired and supported | Invented transcripts or automatic mastery labels |
| `LEARNING_STATE.md` | Current continuation, strengths, gaps, parked work and next step | An ever-growing archive of competing current plans |
| `MSC_SYLLABUS_MAP.md` | Near-term course demand, scope and readiness mapping | Evidence that a listed topic was taught |
| `LEARNING_ROADMAP.md` | Slower-changing dependencies and strategic priorities | A source that overrides newer verified course reality |
| `learning_progress.yaml` | Reviewed, machine-readable learning projection | An automatic prose-to-mastery transformation |
| `deadlines.yaml` | Explicit external delivery constraints | A learning score or fourth learning lane |
| `dashboard/` | Read-only Learning Atlas presentation | An independent authority over the underlying evidence |
| Git branches, PRs and Actions | Proposed changes, review, mechanical validation and publication | Proof that pedagogical claims are true |

These boundaries are explicit in the existing system. Preserving them matters more than preserving Markdown versus database as a particular technology choice. [R-ARCH] [R-SESSION] [R-ATLAS]

### 3.2 Current operating pattern

A new tutor reads architecture, workflow and current state, then the smallest relevant evidence. A routine session does not need to reload the entire repository. Course-specific logs live under `lesson_logs/<course_code>/`; numbered cross-course preparation and reconstructed historical foundations have their own identity. [R-SESSION] [R-INDEX]

The study plan has exactly three ordered, concurrent lanes:

```text
Continue — the main next learning task
Parallel — another active course or useful concurrent thread
Protect  — work that must not disappear under immediate pressure
```

These are not one FIFO queue. The meaning of a protected task can include a strategically important project, not only mathematics. Delivery deadlines can change allocation without changing evidence of capability. [R-STATE] [R-SYNC]

At the reviewed snapshot, the handover points to AIMS5701 Bayes Nets I reconciliation and HMM preparation; AIMS5702 epoch/evaluation/metric orchestration before a CNN bridge; and the Private Client Graph evaluator. These are **snapshot-specific acceptance fixtures**, not application defaults. [R-STATE]

### 3.3 Existing full-sync boundary

An explicit sync must inspect the current branch, preserve focused evidence, update the handover, reconcile the Atlas projection, consider conditional planning updates, validate the complete diff and use a PR. It remains in progress while either required workflow is queued or running. A failed workflow requires diagnosis, repair and verification of the new run. [R-SYNC]

There are three distinct outcomes the application must name correctly:

1. **Validated proposal:** the sync PR has the required successful validation and is ready for review/merge.
2. **Accepted learning record:** the reviewed change has merged into the canonical branch.
3. **Published Atlas:** the corresponding main-branch build/deployment has succeeded and the published version is identified.

The current sync protocol's CI completion gate does not mean an unmerged PR has already updated the live Atlas. [R-SYNC] [R-ARCH] [R-DASH-WF]

---

## 4. Recent usage and what it implies

| Observed pattern | Evidence | Product implication |
|---|---|---|
| The repository became an external tutoring memory, not just code storage. | Course-folder reorganisation and architecture documentation, PRs #17–18. | Preserve file roles, selective loading and clean-room tutor onboarding. |
| The learner uses generated tests and incomplete exercises, then writes the implementation. | Tensor practice scaffolding, PR #25; session protocol. | Support explicit learner-owned practice with solution withholding and an expected-red exercise state. |
| Current handover and Atlas projection diverged. | PR #26 describes state through 17 September while the projection was still reviewed through 9 September. | Make reconciliation an unavoidable part of sync, even when no topic enum changes. |
| Failed bookkeeping attempts led to stricter mechanical rules. | PR #29 and the hardened sync protocol: schema checks, lane order, YAML quoting, source hashes and CI gating. | Move these checks from model memory into deterministic validation. |
| Small maintenance sessions need narrow diagnoses, not whole-topic resets. | Tensor review and 1 October lab-readiness record, PRs #19 and #49. | Preserve precisely what is fragile, what was repaired, and what not to repeat next time. |
| There are parallel sessions and divergent branches. | PR #40 reconciles #38/#39; PR #48 reconciles #46/#47. | Use version-aware reconciliation and supersession; never select one stale state wholesale. |
| Live teaching changes the planned curriculum. | PRs #43, #45 and #47; the current syllabus and 30 September record. | Separate tentative plans from verified material, and preserve out-of-scope pre-reading without claiming lecture coverage. |
| Learning includes cumulative retrieval as well as next-lecture preparation. | Search midterm-retention work on 30 September. | Maintain both next-lecture and cumulative-retention planning loops. |
| Engineering judgement increasingly matters more than repetitive implementation. | Receipts completion and 2 October delegation decision, PRs #39/#40 and #50. | Provide task-specific delegation policies rather than an inflexible “AI must never write code” rule. |
| Project work and personal reflection have different destinations. | PRs #46/#48 relocate design records; receipts work freezes a submitted repository and continues in a separate project. | Support multiple repositories, destination policies and frozen submission boundaries. |
| Implementation success is deliberately not promoted to framework mastery. | PRs #49–51 and their logs. | Record authorship, conceptual support, task scope and delayed retrieval separately from green tests. |
| The learner wants the conversation-to-PR flow from a phone and is testing model alternatives. | Current conversation and repository portability goals. | The application must own context and execution continuity; a model provider's native GitHub connector cannot be a prerequisite. |

### 4.1 The strongest recurring pattern

The system repeatedly distinguishes **what happened**, **what that supports**, and **what should happen next**. These are three different operations.

For example, the 1 October record preserves a clean final stepped-slice calculation while noting substantial same-session repair. It recommends a narrow later check rather than declaring durable independent mastery or restarting all tensor work. Similarly, the Private Client Graph records stronger architectural ownership while explicitly withholding framework-mastery claims for delegated implementation. [R-OCT1] [R-DELEGATION]

### 4.2 A workflow-parity application must preserve decisions, not just summaries

Useful memory includes the preferred intuition for a concept, which hypothesis a failed test disproved, which implementation work was deliberately delegated, why a project is frozen and which apparent next step has been superseded. A generic rolling summary is not a sufficient record of these distinctions. This is an inference from the recent logs and reconciliation history, not a claim that every conversation needs a structured event for every turn. [R-RECEIPTS] [R-OCT1] [R-DELEGATION] [P40] [P48]

---

## 5. Observed gaps that the application must address

| Finding | Evidence and qualification | Required response |
|---|---|---|
| Current and superseded instructions coexist. | The latest handover records successful live extraction, while an older section still says no model call has run. These were true at different times. | Distinguish current decisions from historical evidence and superseded next steps. |
| Navigation has drifted. | `lesson_logs/INDEX.md` is last audited 10 September and says AIMS5701 has no substantive logs; later course records exist. | Generate discovery metadata from actual files; retain semantic judgement in reviewed records. |
| Dashboard triggers omit an input. | `deadlines.yaml` is consumed by the builder but absent from both dashboard workflow path filters. | Verify trigger coverage; diagnose a missing run instead of reporting success or waiting indefinitely. |
| “Current state” is no longer small. | The reviewed handover is 46,652 bytes; the projection is 62,201 bytes. These are byte sizes, not measured model-token counts. | Serve compact current views with lazy access to history and record context usage. |
| Tests mix stable rules with changing learner facts. | Dashboard tests assert schema invariants alongside today's dates, labels, submission states and topic counts. | Separate general fixtures from intentional real-data regressions; never weaken tests merely to turn CI green. |
| Hash agreement is weaker than semantic agreement. | Projection tests compare dates/hashes, while the builder checks structure and references. | Retain evidence-backed review of claims; mechanically fresh data can still be misinterpreted. |
| “Personal repository” does not mean private. | Repository visibility is public, even though some records were moved there from a shared project. | Use explicit visibility controls for conversations, profiles, attachments and published records. |
| Original materials are not always stored in the repo. | Some logs reference supplied decks, notebooks or historical chats rather than a repository copy. | Store or reference accessible, versioned source material; distinguish verified originals from secondary records. |

These are parity-enabling improvements, not an invitation to redesign the learning method. Several were already identified in the historical architecture review and remain visible in the reviewed snapshot. [R-STATE] [R-INDEX] [R-DASH-WF] [R-BUILD] [R-TESTS] [R-SYNC-TEST] [R-TREE] [R-REVIEW]

---

## 6. Functional requirements

### 6.1 Session continuity and context selection

**CTX-01 — Fresh-session bootstrap [P].** On starting or resuming a session, load the applicable protocol and current accepted learning state, then retrieve the relevant course, lesson, code and planning evidence. A new model must not require the old conversation to discover the correct next task. [R-ARCH] [R-SESSION]

**CTX-02 — Version-aware context [E].** Every context package must identify its repository revision, selected sources, source versions and any pending proposal it includes. Accepted state and unmerged work must be visibly distinct. Refresh stale repository context before proposing writes.

**CTX-03 — Selective retrieval [P].** Support direct file/section loading, topic/course discovery, text search and structured filtering. Do not routinely send all root documents or the whole YAML file to the tutor. Load additional history when the task needs it. A query such as “what did we last study?” must distinguish an actual study session from a later maintenance PR. [R-SESSION] [R-ARCH]

**CTX-04 — Persistent conversation and device continuity [P/E].** Preserve the active session, turns, attachments, task mode, unresolved question and execution links across desktop/mobile reloads. Concurrent clients must not silently overwrite later messages or state. Unsynced session evidence must survive a connection loss.

**CTX-05 — Model portability [P/E].** Keep protocols, learner preferences, learning evidence and execution state in the application/repository, not exclusively in provider memory. Support interchangeable tutor adapters and an explicit switch between at least two configured models for the parity evaluation. Tutor and coding/repair model choices must be independently configurable, sharing only the authorised task handoff. Do not assume identical pedagogical quality or native access to another product's chat history.

**CTX-06 — Inspectable context and preferences [E].** Let the learner inspect and correct teaching preferences—including tone/warmth, pacing, concrete analogies and assistance level—alongside context selection and the concise continuation summary. Persist preferred explanations/anchors when useful. Separate private personalisation from public learning records, and make exports usable by a fresh tutor without hidden application-only instructions.

### 6.2 Tutoring and implementation modes

**TUT-01 — Small interactive learning loop [P].** Default to one bounded question/task, a learner attempt and targeted feedback. Prefer cold retrieval before explanation when appropriate. Avoid presenting the full lesson record as the learner-facing response. [R-SESSION]

**TUT-02 — Graduated assistance [P].** Support conceptual hints, stronger hints, partial scaffolds and minimal syntax/API help before full solutions. Honour an explicit request for the solution while recording that it was supplied rather than independently reconstructed. [R-SESSION]

**TUT-03 — Fair retrieval boundary [P].** Build retrieval tasks from what was actually taught or can be reasoned from that material. A concept merely appearing in code, an untaught extension or an unfamiliar incidental API must not be recorded as failed recall. Changed numbers, shapes and contexts should test transfer. [R-SESSION]

**TUT-04 — Diagnostic precision [P].** Distinguish conceptual misunderstanding, arithmetic, notation, syntax/API rust and representation-translation cost. Preserve successful anchors such as semantic tensor shapes, and repair the smallest observed gap. [R-ARCH] [R-OCT1]

**TUT-05 — Learner-owned practice [P].** Generate contracts, tests, signatures and incomplete scaffolds without filling the intended learning task. Support local-editor work, pasted code and repository-based implementation. Mark practice runs that are intentionally red separately from repository release/integrity checks; do not silently implement the exercise to make the dashboard green. [P25] [R-SESSION]

**TUT-06 — Bounded delegated engineering [P].** Allow explicit per-task delegation of repetitive code or framework plumbing after the learner owns the relevant semantics. Carry protected contracts, allowed files, exclusions, tests and stopping conditions into execution. Record delegated implementation separately from learner-authored work; surface proposed semantic redesigns rather than making them silently. [R-ENGINEERING] [R-DELEGATION]

### 6.3 Evidence capture and interpretation

**EVD-01 — Focused outcomes [P].** After substantive work, preserve the appropriate numbered lesson, course session, project decision or reflection. Capture outcomes, mistakes, useful intuitions, support required, retrieval prompts and the next boundary, not a transcript disguised as a lesson log. Preserve existing namespaces and identifiers. [R-SESSION]

**EVD-02 — Provenance and assistance [P].** Distinguish lecturer-covered material, pre-reading, personal synthesis, historical reconstruction, guided work, independent demonstration and planned/new material. Record conceptual scaffolding separately from incidental syntax lookup. One task can have mixed authorship/support across its parts. [R-ARCH] [R-OCT1] [R-DELEGATION]

**EVD-03 — Observations versus judgements [E].** Keep the observed attempt, the interpretation of it and the resulting projection change separately inspectable. The model may propose a judgement with evidence and boundaries; existence of a file, a successful test or a summary alone must not justify independence or retention.

**EVD-04 — Temporal integrity [P/E].** Preserve the learning event date, recording date and review date separately. Historical backfill, a file move or renewed source review must not fabricate a new retrieval event. Record corrections/supersession without erasing the original evidence trail. [R-ATLAS] [R-SYNC]

**EVD-05 — Correctable, proportionate capture [E].** Let the learner correct a material evidence statement before or after sync. Corrections must reconcile affected state/projections. Do not require manual annotation of every conversational turn; capture meaningful assessment or decision moments and retain uncertainty where evidence is insufficient.

### 6.4 Current learning state and selective maintenance

**STA-01 — Current handover [P].** Maintain a concise operational view of comfortable/fragile areas, active work, blockers, parked threads and the next useful session. Preserve existing boundaries rather than replacing them with a generic summary of the latest conversation. [R-STATE] [R-SESSION]

**STA-02 — Explicit current authority [E].** Mark superseded instructions and plans, and select current state using the relevant source responsibility and effective time. Do not let an older log's “next step” override a newer accepted decision because it is a better text-search match.

**STA-03 — Conditional updates [P].** Always update the handover after substantive learning and inspect the projection on every explicit sync. Update affected topic records only when warranted; update syllabus, deadlines, roadmap and architecture according to their distinct change triggers. An inspection with no semantic change is a valid outcome. [R-SYNC]

**STA-04 — Concurrent changes [P/E].** Detect intervening commits, overlapping open proposals and changes made by another session/agent. Preserve independent contributions; resolve overlapping judgements using evidence and source responsibility. Use explicit conflict review where that is insufficient, not last-writer-wins or wholesale replacement. [R-SYNC] [P40] [P48]

**STA-05 — Discovery and reference maintenance [P/E].** Keep topic/log/source links, course indexes and repository moves coherent. Generate file inventory and changed-source discovery mechanically. Moving a record must update its references without creating a new learning achievement or changing its original event date. [P17] [P46] [P48]

### 6.5 Course materials and planning

**PLN-01 — Source-material ingestion [P/E].** Accept lecture slides/documents, images/screenshots, notebooks, code and pasted text relevant to study. Preserve source identity, version and page/section/cell references where available. Make limitations explicit when only a secondary log or partial source is available. Private attachments must not automatically enter a public repository.

**PLN-02 — Live scope reconciliation [P].** Record tentative versus confirmed scope, lecturer-covered versus pre-read content, and evidence for schedule changes. A newer supplied lecture may narrow a broader term plan without erasing useful pre-reading. Unknown dates remain unknown; no date is inferred solely from week numbering. [R-SYLLABUS] [R-SEP30]

**PLN-03 — Three learning lanes [P].** Preserve exactly `continue → parallel → protect`, with valid topic targets, tasks and rationale. Support serial execution within a study block while retaining concurrent commitments. User choices can resize or temporarily reorder effort without losing parked/protected work. [R-SYNC] [R-STATE]

**PLN-04 — Delivery plane [P].** Maintain assignment/project dates, submission/completion status, provenance, collaboration mode and planning notes separately from learning evidence. Completing/submitting work must not automatically promote topic performance or refresh recall dates. [R-DEADLINES] [R-ATLAS]

**PLN-05 — Planning at multiple horizons [P].** Support the next task, near-term lecture preparation, cumulative retrieval/exam preparation and longer-term prerequisites. Incorporate available time and an explicit request to stop or reduce scope. Preserve what not to repeat, not just a list of remaining topics. [R-ROADMAP] [R-SEP30] [R-OCT1]

### 6.6 GitHub and project workflows

**GIT-01 — Authenticated repository access [P/E].** Connect explicitly selected repositories with appropriate read/write permissions. Read current files, directories, refs, commits, PRs and relevant discussions. Handle private access, revocation and permission failures clearly; inability to read a repo must not be disguised as a content summary.

**GIT-02 — Branch and diff workflow [P].** Create changes from the correct current base, preserve unrelated work, commit coherent changes and open/update a PR. Inspect the complete resulting diff and report the repository, branch, base, head and PR. If the earlier PR was already merged, start a fresh appropriate branch rather than treating it as still pending. [R-SYNC]

**GIT-03 — Review and merge continuity [P/E].** Read review feedback, propose corrections and retain the discussion-to-change link. Do not merge without the learner's explicit approval or a clearly configured approval policy. Detect manual merges and continue publication tracking from the actual merge commit. [R-ARCH]

**GIT-04 — Execution against real code [P/E].** Run relevant tests/builds in an isolated checkout, retain commands/results and inspect actual failure output. Support learner code authored outside the app. A generated code explanation is not a substitute for reading or executing the actual revision under review. [R-SESSION] [R-ENGINEERING]

**GIT-05 — Multiple repository roles [P].** Distinguish the learning repository, active project repositories, shared project repositories and frozen submissions. Route reflective records and implementation to their intended destinations. A follow-on refactor must not mutate submitted coursework merely because it is a convenient current checkout. [R-RECEIPTS] [P46]

**GIT-06 — Safe relocation and supersession [P/E].** For requested moves between repositories, verify destination preservation before any authorised source removal and record partial completion if one side fails. Track PR dependencies and superseded proposals without double-counting their evidence. Cross-repository work need not pretend to be one atomic Git transaction.

### 6.7 Full learning-state sync

**SYN-01 — One command, full workflow [P].** Recognise the existing sync phrases and an equivalent UI action. Execute the documented full protocol, not merely an edit to `LEARNING_STATE.md`. Return a persistent sync identifier that can be reopened from the conversation. [R-SYNC]

**SYN-02 — Coherent change set [P/E].** Assemble the proposed evidence, handover, projection and conditional planning changes against a recorded base revision. Preserve unrelated records. Prefer field/section-aware changes and validated serialization over broad string replacement.

**SYN-03 — Projection reconciliation every time [P].** Review affected topics, evidence summaries/boundaries/next actions, dates, lanes, course requirements and timeline. When the handover changes, refresh its reviewed blob hash and aligned metadata even if all topic enums remain unchanged. Never advance an old event date just to remove an age warning. [R-SYNC] [R-SYNC-TEST]

**SYN-04 — Ordered source finalisation [P/E].** Finalise substantive source content first, calculate reviewed source hashes from that content, then set the provenance snapshot reference. Recheck after repairs. Keep Git blob hashes, snapshot commits, PR heads and build/deployment commits distinct; do not require a file to contain the hash of the commit containing itself. [R-SYNC] [R-BUILD]

**SYN-05 — Validation and review gate [P].** Run projection/schema/source checks, the dashboard build and relevant implementation/browser checks; inspect the full diff for accidental deletions, lost lanes, invalid enums and unsupported promotions. Preserve a validation receipt. Required PR workflows must both succeed before reporting the proposal as validated. [R-SYNC]

**SYN-06 — Idempotent and meaningful reporting [E].** Retrying the same logical sync must resume or reconcile its existing proposal rather than creating duplicate logs, timeline entries or PRs. Report evidence changes, projection changes, conditional files inspected, intentionally unchanged boundaries and remaining blockers. No-op reconciliation must not invent progress.

### 6.8 Durable Actions orchestration

**RUN-01 — Execution independent of the chat turn [E].** Persist job state and resume waiting/reconciliation after a worker restart, phone lock, closed browser or model timeout. Waiting for CI must use deterministic scheduling/events, not repeated model reasoning calls. The application, not an open chat response, owns this lifecycle.

**RUN-02 — Exact run identity [P/E].** Associate validation with the correct repository, PR, revision, workflow, run and attempt. Record the actual tested revision where it differs from a branch head. A green run for an older revision or different event must not validate a new change. Reconcile current provider state rather than trusting an isolated notification.

**RUN-03 — Explicit completion policy [P/E].** Require successful execution of the configured validation work for `Tests` and `Learning dashboard`. Distinguish pending, running, failed, cancelled, timed out, blocked and missing checks. Expected publication-job skipping on a PR is different from skipping required validation. Do not substitute a generic combined commit status for inspecting the relevant Actions/check results. [R-SYNC] [R-DASH-WF] [D-CHECKS]

**RUN-04 — Missing-run and infrastructure diagnosis [E].** Detect a workflow that was not triggered, a missing permission, a stale session credential, a rate limit and a service/network failure. Use bounded retries, backoff and explicit blocked states. Provide a recovery action instead of polling forever. Audit dashboard inputs against workflow trigger paths.

**RUN-05 — Evidence-driven repair [P/E].** Fetch the failing job/steps/logs, identify a likely root cause and repair within the authorised scope. Refresh affected references and wait for the new run. Do not silently change pedagogical claims, frozen contracts or test intent to satisfy CI; escalate meaningful ambiguity. Preserve the failure and repair history. [R-SYNC] [R-DELEGATION]

**RUN-06 — Post-merge publication [P/E].** Follow the actual accepted commit through main-branch validation/build/deployment. Expose PR preview artifacts separately from the live Atlas, retain the published revision and report publication failures without undoing or concealing the accepted learning record. [R-ARCH] [R-DASH-WF]

### 6.9 Learning Atlas parity

**ATL-01 — Compatible reviewed projection [P].** Preserve schema-v2 topic dimensions, evidence, boundaries, next actions, source records, dependencies, lanes, course requirements, paths and timeline. Preserve deadline-schema-v1 semantics. Do not reduce these to one status or numeric mastery percentage. [R-ATLAS] [R-PROJECTION]

**ATL-02 — Existing navigation and detail [P].** Retain the knowledge map, active-focus default, search, area/status filters, show-all/reset, empty state, topic details, prerequisite links and source links. Searching must not silently exclude topics outside the default focus. Support stable topic/view deep links. [R-ATLAS] [R-JS]

**ATL-03 — Course, study and delivery views [P].** Retain full recorded course coverage, expandable entries, anchors versus remaining requirements, scope uncertainty, three study lanes, the separate upcoming-delivery area and learning paths/timeline. Overview topics must not inflate achievement counts. [R-ATLAS] [R-BUILD]

**ATL-04 — Integrity and freshness visibility [P].** Display evidence-through date, actual review date, published/source revision and source-integrity warnings. Age is a prompt to review, not evidence of knowledge decay. A source change must not silently mutate the learning judgement. [R-ATLAS] [R-JS]

**ATL-05 — Accessible, safe publication [P].** Preserve mobile usability, keyboard/tab/dialog behaviour, focus return and a readable static/no-JavaScript Atlas. Keep generated assets out of source evidence, retain cache-busting asset versions and isolate PR previews from live publication. Public output must include only authorised public sources. [R-BROWSER] [R-DASH-WF]

### 6.10 Application governance and operational controls

**OPS-01 — Explicit authority and permissions [E].** Define read, propose, execute, merge and publish permissions per repository and action. The user's sync command may authorise its normal bounded branch/PR workflow without confirmation at every mechanical step; it must not imply unrelated deletion, credential access or unrestricted autonomous changes.

**OPS-02 — Private/public boundary [P/E].** Keep raw conversations, private profile fields, credentials and restricted course attachments private by default. Public evidence export must use an explicit destination/visibility policy. “Personal” labels and repository names do not determine access control. [R-README] [R-ATLAS]

**OPS-03 — Untrusted-content isolation [E].** Treat repository files, attachments, PR comments and model output as data unless explicitly adopted as policy. They must not override tool permissions or instruct the app to disclose secrets. Execute code in resource-bounded isolation, separate from application credentials; restrict network and secret access to the task's needs.

**OPS-04 — Auditable operation [E].** Record context versions, model/task identity, proposed changes, approvals, commands, results, remote operation IDs, retries and failures. Allow inspection of why a learning claim changed and why a run was considered complete, without exposing secrets in logs.

**OPS-05 — Cost and autonomy budgets [E].** Track available provider usage/cost data separately from GitHub/runtime activity and distinguish measured values from estimates. Set per-task spending, context, tool and repair limits. Support cancellation at safe checkpoints. Do not equate current consumer-chat allowances with application execution budgets.

**OPS-06 — Portability and recovery [E].** Export accepted learning records and private session/context packages in documented formats. Rebuild indexes from canonical sources; back up private session/job state; support recovery after partial failure. Preserve existing Git workflows so the learner can continue outside the application during a migration or outage.

---

## 7. Data and compatibility contracts

### 7.1 Canonical storage in the first implementation

**Recommended starting boundary:** Git remains authoritative for the accepted learning record and published learning projection. The application owns private conversations, attachment storage, execution state and credentials. Its searchable learning read model is rebuildable from accepted repository revisions.

| Information | Initial authority | Application treatment |
|---|---|---|
| Accepted lesson logs, decisions, handover, roadmap and syllabus | Learning repository | Read, propose changes through PRs, index after acceptance |
| Reviewed topic projection and delivery constraints | Repository YAML | Validate and render; never maintain a competing silently writable copy |
| In-progress conversation, attempts and unsynced evidence | Private application store | Durable session state; explicit proposed changes, not accepted learning facts |
| Raw attachments and private profile | Private application store or authorised original source | Versioned, permission-aware retrieval and selective export |
| Branch/PR/run/deployment status | GitHub, with reconciled local execution records | Persist remote IDs and observed state; reconcile after missed events |
| Context manifests, discovery indexes and search caches | Derived from identified sources | Rebuildable; invalidate by revision/content version |
| Public Atlas | Build from accepted public sources | Read-only projection, labelled with its published version |

A session may continue from accepted state plus its **explicitly selected pending changes**. It must not blend all open PRs into canonical state, or hide pending work merely because it has not merged. If a database later becomes the learning system of record, that requires an explicit migration and authority decision—not an accidental dual-write implementation.

### 7.2 Logical records

These are proposed application contracts, not a requirement to create a separate database table or a new public JSON file for each row.

| Record | Minimum information |
|---|---|
| Repository binding | Repository identity; learning/project/shared/frozen role; default branch; visibility; permissions; approved commands and workflow policy |
| Source artifact | Stable identity; source kind; repository/path/ref/blob or private attachment version; location within source; access policy; original versus reconstructed/secondary provenance |
| Session | Identity; course/topics; selected repository revision; model; task/delegation mode; turns and attachments; continuation; pending sync IDs |
| Meaningful learning observation | Event and record dates; topic/task reference; attempt/result; assistance and authorship; error category; same-session/delayed context; source evidence; uncertainty; correction/supersession link |
| Reviewed learning change | Supporting observations/sources; proposed before/after state; evidence boundary; interpretation rationale; reviewer/approval record; acceptance revision |
| Current decision | Scope; current value or instruction; effective time; evidence; superseded decision; accepted versus proposed status |
| Topic projection | Existing schema-v2 fields; no new invented mastery scale |
| Course requirement | Course/entry identity; topic references; anchors/remaining; scope; source; confirmed date where available |
| Delivery constraint | Existing deadline fields; provenance; submission/completion facts and planning implications |
| Context package | Task; policy version; accepted revision; selected pending overlay; source manifest; current priorities; relevant evidence; exclusions and budget |
| Sync run | Identity/idempotency key; session/base; proposed files; stage; attempts; validation receipts; PR and run IDs; approvals; errors; publication outcome |
| Execution receipt | Command/tool; checkout/revision; environment; start/end; outcome; log/artifact references; remote operation identity; limitations |
| Published snapshot | Accepted commit; build/deployment identity; publication outcome; public URL; evidence-through date and projection version |

The evidence model must allow “concept understood, syntax supplied” and “final answer independent after substantial same-session repair.” A single assisted/unassisted boolean is insufficient for the existing workflow. Public Markdown may remain the human-readable evidence format; an internal structured observation can link to it without forcing a wholesale historical rewrite. [R-OCT1] [R-RECEIPTS]

### 7.3 Existing schema that must remain compatible

| Dimension | Accepted values at the reviewed snapshot |
|---|---|
| `concept` | `demonstrated`, `taught`, `historical`, `planned`, `unknown` |
| `performance` | `independent`, `guided`, `implemented`, `historical`, `pending`, `unknown` |
| `review` | `recorded`, `diagnostic`, `unknown`, `not_due` |
| `action` | `maintain`, `build`, `practice`, `retrieve`, `diagnose`, `learn`, `transfer`, `confirm` |
| Course `scope` | `mapped`, `scope_unconfirmed`, `not_mapped`, `overview`, `partial_tutorial` |
| Deadline `status` | `upcoming`, `submitted`, `completed`, `cancelled` |
| Deadline `provenance` | `learner_report`, `course_material`, `official` |

A topic also carries its name, area, evidence summary, explicit boundary, next action, sources, optional actual event date and prerequisite topic IDs. The projection includes review metadata, sources, lanes, courses, paths and timeline. The current YAML uses explicit anchors/merge defaults; import/export must preserve their effective meaning and avoid unnecessary whole-file churn. [R-BUILD] [R-PROJECTION]

### 7.4 Mechanical invariants

The following existing guarantees must remain, with stronger parsing where noted:

- All source/topic/course/lane references resolve; prerequisite dependencies are acyclic and not self-referential.
- The three lanes appear exactly in their prescribed order. A deadline does not become a topic or a fourth learning lane.
- A recorded evidence event has a date. Event dates do not exceed the included evidence cutoff, and the cutoff does not exceed the actual review date.
- A planned topic has pending performance and is not treated as overdue retrieval. Independent performance requires a demonstrated concept and dated evidence, while semantic support still requires review.
- Course coverage cannot silently shrink, duplicate entries or place the same requirement in both anchors and remaining work.
- Public source paths must be safe and allowed. Missing/unsafe sources fail validation. Source changes raise review needs, not automatic knowledge changes.
- A full sync requires the handover's evidence-through date and reviewed state blob to match the projection.
- Duplicate keys must not silently overwrite records. The current topic-duplicate regression is useful; the application should add a strict parser that rejects duplicate explicit keys while correctly supporting deliberate YAML merges.

These derive from the existing validator and regression tests; generalized duplicate-key rejection is proposed hardening. [R-BUILD] [R-TESTS] [R-SYNC-TEST]

### 7.5 Source hashes are not interchangeable

Store and label at least the following distinctly:

```text
source blob hash           — exact reviewed file content
context/base commit        — repository state used for the task
proposal head commit       — proposed change currently under review
tested revision/run        — actual content and execution that produced a result
accepted commit            — state merged into the canonical branch
published commit           — state represented by the live Atlas
```

`meta.source_ref` is a fallback provenance snapshot; the current builder uses the checked-out commit when available. A fallback differing from the latest `main` SHA is therefore not itself a defect. When new source files are introduced, the selected fallback must contain those sources; a sources-first commit followed by a projection-metadata commit is acceptable. Do not create a circular requirement that the projection store the final commit SHA of itself. [R-ATLAS] [R-BUILD]

---

## 8. Sync and execution lifecycle

### 8.1 Durable state machine

The proposed application should implement this as persisted execution state, not as a long prompt asking a model to keep checking:

```text
REQUESTED
    → SNAPSHOT_LOADED
    → CHANGESET_PROPOSED
    → LOCAL_VALIDATION
    → PR_OPEN
    → WAITING_FOR_REQUIRED_CI
        ├─ failure → DIAGNOSING → REPAIR_PROPOSED → validation / new CI
        ├─ missing or inaccessible → BLOCKED_WITH_RECOVERY_ACTION
        └─ success → VALIDATED_AWAITING_REVIEW_OR_MERGE
    → MERGED
    → WAITING_FOR_MAIN_BUILD_AND_PUBLICATION
        ├─ failure → PUBLICATION_FAILED
        └─ success → PUBLISHED
```

Additional terminal or paused states include rejected, cancelled, superseded and awaiting user decision. These are proposed application states, not copied GitHub status strings.

### 8.2 Step-by-step sync contract

**Capture.** Persist the session evidence to a private draft before starting remote work. Link the request to its originating session and an idempotency key. Repeated equivalent commands for the same draft resume that operation.

**Snapshot.** Read latest accepted state, relevant open proposals, affected source files and current validation contracts. Record the base revision. Do not trust the earlier chat's repository snapshot as a write base.

**Interpret.** Propose the smallest accurate lesson/state/projection updates. Preserve support boundaries and any intentionally unchanged state. Inspect conditional documents and record why they do or do not need changes.

**Validate and finalise.** Apply changes to an isolated checkout, validate the schema and diff, and finalise source content/hashes in the documented order. Check for an intervening remote change before writing or updating the PR; reconcile when necessary.

**Verify the proposal.** Associate required CI with the exact proposal and relevant run attempts. Inspect actual failures before repairing. A new content revision invalidates earlier validation receipts for completion purposes.

**Review and accept.** Present a concise semantic summary and inspectable diff. The learner can merge in the app under an authorised policy or in GitHub. Acceptance is recorded only after the actual merge is observed.

**Publish.** Track the accepted revision's main-branch build/deployment separately. Keep the existing public Atlas live while a proposal or failed publication is unresolved. Report which accepted revision is and is not published.

### 8.3 Completion and failure rules

The application's gate is stricter than “some check is completed” or “GitHub displays a green icon.” GitHub distinguishes check status from conclusion and can treat skipped work as successful for dependency/merge purposes. The application must verify the configured validation actually ran; deliberately skipped PR deployment is expected, skipped required validation is not. [D-CHECKS]

A known failing test is different from an unavailable test environment. The latter must produce “not verified here; remote validation pending/blocked,” not a fabricated local success. Temporary infrastructure failures can be retried within budget; ambiguous learning judgements or changed behavioural contracts require review.

A publication failure must not be reported as failure to preserve all learning if the record has already merged. Conversely, successful PR checks must not be reported as publication. The status surface should show these dimensions separately.

### 8.4 CI repair policy

Authorised mechanical repairs may include valid serialization, corrected source references, missing imports or a clearly identified implementation defect within the agreed contract. Repairs that change topic evidence, assignment scope, public visibility, test intent or protected project semantics need explicit review.

Tests that encode changing approved facts may legitimately need updating when those facts change. The app must explain that change and preserve the underlying invariant; it must not delete a regression because it obstructs a proposed unsupported status.

### 8.5 Duplicate and out-of-order events

A repeated command, a worker retry and a repeated remote notification must not create repeated side effects. Reconcile remote PR/run state by durable identifiers and current revision. A late success event for an old head cannot overwrite a newer failure. After a restart, inspect existing branches/PRs/commits before reissuing a write whose prior outcome is uncertain.

---

## 9. Application structure and reuse strategy

### 9.1 Recommended initial architecture

Use a small application with clear module boundaries and a durable worker. The requirement is reliable stateful orchestration, not a collection of independently deployed agents.

```text
Responsive learning workspace
    ├─ conversation / task mode / attachments
    ├─ current learning state and evidence inspection
    ├─ Atlas views
    └─ sync / PR / CI / publication status
                │
Application service
    ├─ context selection and source manifest
    ├─ tutoring model adapters
    ├─ evidence draft and reviewed-change service
    ├─ repository compatibility / validation layer
    └─ authorisation and audit
                │
Durable execution worker
    ├─ isolated repository checkout and command execution
    ├─ GitHub branch / PR / workflow operations
    ├─ deterministic wait / retry / reconciliation
    └─ publication verification
                │
Git-backed learning record + existing Atlas builder
Private session / attachment / execution storage
```

This is a proposed logical architecture. It does not require microservices, Kafka, a graph database or an LLM framework. A relational store plus a job mechanism is a reasonable starting implementation; select the concrete stack according to operational simplicity and the learner's ability to maintain it.

### 9.2 Reuse versus build

| Reuse first | Add around it | Deliberately do not build yet |
|---|---|---|
| Existing Git repository and readable formats | Version-aware repository adapter and write coordinator | A replacement canonical store without a migration need |
| Atlas builder, styles, JavaScript and behaviour tests | Authenticated workspace and clear preview/published state | A new dashboard from scratch solely for framework consistency |
| Validators and projection drift guard | Strict duplicate-key parsing, trigger-coverage checks and durable receipts | Automatic mastery grading from logs/tests |
| Existing tutoring and engineering protocols | Model adapters and task-specific context packages | A multi-agent tutor team by default |
| Existing topic IDs and prerequisite links | Deterministic inventory and structured/lexical lookup | Managed vector or graph infrastructure before a measured need |
| Existing GitHub Actions validation/publication | Durable monitoring, bounded repair and recovery | Model-driven polling loops |

The Atlas can initially remain a separately built static surface linked or integrated into the workspace. Editing learning data still produces a reviewed change; it must not turn the Atlas into a second uncontrolled state editor.

### 9.3 Minimum UI surfaces

The **session workspace** needs conversation, source/attachment access, current task, hint/delegation controls and a persistent sync action. The **learning view** needs current lanes, evidence/boundaries, next steps and the existing Atlas navigation. The **change/run view** needs the proposed semantic changes, diff, PR link, CI outcomes, repair history and publication status. **Settings** needs repositories, private preferences, model configuration, permissions and budgets.

These can be views in one responsive application rather than separate products. The static/no-JavaScript fallback requirement applies to the Atlas; the interactive tutoring workspace does not need to work without JavaScript.

### 9.4 Integration design

A GitHub App is a candidate for the repository integration, but the permission design and installation scope should be decided before implementation. Model providers should not hold unrestricted repository credentials. Expose bounded operations through the application's authorisation layer; validate model-generated arguments and proposals before executing them.

For webhook-based orchestration, GitHub recommends minimal event subscriptions, HTTPS, secret verification, prompt acknowledgement, event/action checks and handling missed deliveries. Persist delivery identity for deduplication; redeliveries retain the same delivery ID. Process durable work outside the request handler and periodically reconcile authoritative remote state. [D-WEBHOOKS]

Native consumer-chat integrations are not assumed. A selected model needs an explicitly supported access path and a validated tutoring capability profile. The app supplies the context and executor; it should not depend on that model's own ability to browse GitHub.

---

## 10. Parity acceptance scenarios

The following scenarios are the release harness. Historical examples are fixtures from the reviewed snapshot, not assumptions about the learner's future state. Mechanical behaviour should be tested automatically where possible; tutoring/evidence interpretation also requires an evidence-grounded human rubric.

| ID | Scenario | Required observable result | Main requirements |
|---|---|---|---|
| AC-01 | A fresh tutor receives only repository/app context at the pinned snapshot. | Identifies the three current lanes; does not propose first-ever extraction or decision-tree prep as the current plan. Explains its sources. | CTX-01–03, STA-01–02 |
| AC-02 | The learner resumes AIMS5702 after the 1 October session. | Targets epoch/eval/metric orchestration and bounded fragile items; does not restart the whole tensor sweep or claim independent pipeline mastery. | TUT-01–04, PLN-05 |
| AC-03 | A retrieval question requires an API/concept not previously taught. | Labels it as new teaching or incidental help, rather than recording a failed recall of taught material. | TUT-03, EVD-02 |
| AC-04 | The learner succeeds only after hints, then solves a changed example. | Preserves the assistance and same-session repair boundary; does not relabel the whole episode delayed-independent. | TUT-02, EVD-02–04 |
| AC-05 | A coding agent implements a green extraction slice behind agreed contracts. | Records architectural ownership and delegated implementation separately; does not infer LangChain mastery or silently widen the slice. | TUT-06, EVD-03, RUN-05 |
| AC-06 | A new lecture deck contradicts the tentative plan and gives no exact new due date. | Updates verified scope, retains useful pre-reading with the right provenance, and leaves the unknown date unknown. | PLN-01–02, STA-03 |
| AC-07 | The learner requests tests and stubs only. | Creates changed-example practice without the solution, shows expected-red exercise results distinctly, and does not bypass ordinary required integrity checks. | TUT-05, GIT-02–04 |
| AC-08 | A substantive session changes the handover but not topic enums. | Inspects the projection, updates reviewed source metadata/cutoff where appropriate, and reports unchanged performance boundaries. | SYN-01–05 |
| AC-09 | An edit changes the handover but leaves its projection hash stale. | Validation blocks completion; repair updates the actual reviewed source relationship, not just the displayed date. | SYN-03–05, ATL-04 |
| AC-10 | A structured update introduces a duplicate topic key or invalid lane/status. | Rejects the malformed change before acceptance; preserves unrelated records; does not invent an enum or weaken validation. | SYN-02, ATL-01 |
| AC-11 | Two sessions update different areas from the same base, as in PRs #40/#48. | Preserves both contributions, identifies any overlapping decision conflict, and produces one reconciled accepted state without double-counting superseded PRs. | STA-04, GIT-06, SYN-06 |
| AC-12 | A sync is requested again after an earlier request or ambiguous network failure. | Resumes/reconciles the existing operation; does not create duplicate logs, commits with the same effect, or a second PR. | SYN-06, RUN-01 |
| AC-13 | Old-head CI is green; the new head is running or failing. | Reports the current proposal as pending/failed; a late old-head success does not change that result. | RUN-02–03 |
| AC-14 | Only `deadlines.yaml` changes and the dashboard workflow does not start. | Identifies trigger coverage as the blocker and proposes/runs an authorised remedy; does not wait forever or mark the dashboard verified. | PLN-04, RUN-04 |
| AC-15 | A required job fails because of malformed YAML or stale references. | Shows the relevant failure, repairs within scope, refreshes affected hashes and verifies the new run before reporting validation success. | SYN-04, RUN-05 |
| AC-16 | CI repair would require changing a frozen contract or unsupported evidence claim. | Stops for review with a bounded decision; does not quietly redesign the system or promote the learner to satisfy a test. | TUT-06, RUN-05, OPS-01 |
| AC-17 | The learner locks the phone during CI and returns on another device. | Conversation, pending evidence and the same run remain available; actual remote progress is reconciled without duplicate execution. | CTX-04, RUN-01, OPS-06 |
| AC-18 | PR checks pass before merge, then a main deployment fails. | Initially says validated/awaiting merge; later says accepted but publication failed, retaining the prior published Atlas version. | GIT-03, RUN-06 |
| AC-19 | The learner marks an assignment submitted. | Removes it from upcoming delivery when appropriate, preserves its historical date/provenance and does not change unrelated learning dates/statuses. | PLN-04, ATL-03 |
| AC-20 | The learner asks to continue a submitted project as a refactor. | Uses the designated follow-on repository, preserves the frozen submission and keeps reflective records in the intended learning location. | GIT-05–06 |
| AC-21 | A private note or malicious source instruction is retrieved. | Does not publish private content, expose credentials or execute a policy-changing instruction from the source. | OPS-01–03, PLN-01 |
| AC-22 | The Atlas is used on desktop, mobile, keyboard and without JavaScript. | Existing filters, details, source links, full course coverage, three lanes, separate delivery, deep links and readable fallback all work. | ATL-01–05 |
| AC-23 | The tutor model changes while an implementation task is active. | The new model receives the same accepted state, pending overlay, task boundary and relevant evidence; the existing executor/run remains attached. | CTX-02, CTX-05–06 |
| AC-24 | Application indexes are lost or a source file is moved. | Rebuilds discovery from canonical sources, repairs references through an auditable proposal and preserves evidence identity/date. | STA-05, OPS-06 |

### 10.1 Pedagogical evaluation rubric

For representative historical sessions, a reviewer should check whether the app chooses a fair next question, preserves the taught boundary, withholds unnecessary solutions, diagnoses the right type of gap and proposes evidence changes justified by the actual attempts/support.

Do not use exact answer-string matching as the sole tutoring-quality test. Do not treat passing an application's test harness as proof of learning effectiveness. The first migration should compare against the working workflow and preserve its evidence standards; any claim of improved retention needs separate learning evidence.

---

## 11. Build sequence and release gates

### Milestone 0 — Freeze a baseline and repair known integrity gaps

Capture the reference repository revision, protocols, schema and representative fixtures. Retain current behaviour tests and add cases for deadline-trigger coverage, strict duplicate-key handling, current-versus-superseded instructions and concurrent updates. Separate mutable presentation fixtures from invariants and deliberate evidence regressions.

**Exit:** The team can say exactly what is being preserved, which failures are being fixed and which sources establish expected behaviour. No model or UI redesign is required for this milestone.

### Milestone 1 — Make the full sync executable from a structured session handoff

Build the repository adapter, permissions, coherent change-set preparation, deterministic validation, PR operations and durable Actions monitoring. Accept a supplied session handoff initially; it can come from the current tutoring conversation. Add bounded failure handling and explicit validated/accepted/published states.

**Exit:** A real end-to-end sync can reach a reviewed PR and correct publication outcome, including recovery from a representative CI failure and a client disconnect. This is executor parity for that path, not complete tutoring parity.

### Milestone 2 — Add private sessions and compact context reconstruction

Add durable conversations, attachments, preferences, current-state selection, source manifests and at least two configured tutor adapters. Implement the tutoring/delegation modes and meaningful evidence drafts.

**Exit:** A fresh model can resume representative learning tasks without the original chat, and changing device/model does not lose the active task or pending execution.

### Milestone 3 — Integrate Atlas, planning and project boundaries

Expose existing Atlas behaviour and current/pending/published state within the workspace. Add source-material reconciliation, delivery updates, full course discovery, multi-repository destination policies and frozen-submission handling.

**Exit:** The application supports ordinary study, course planning, learner-authored implementation, delegated engineering and full sync without manual bookkeeping across the canonical files.

### Milestone 4 — Validate full parity and migrate gradually

Run AC-01 through AC-24, compare tutoring decisions against the existing workflow, test restart/security/concurrency cases and verify exports. Trial the application in parallel with the existing workflow before making it the default.

**Exit:** All required scenarios meet their acceptance criteria, unresolved limitations are explicit, and an outside tutor can reconstruct accepted learning state from an export/repository. Only at this point should the product be described as having full workflow parity.

### Recommended first vertical slice

Implement **“session handoff → reviewed learning-state change → PR → exact CI gate → accepted/published status”** before building a broad chat UI. That isolates the capability the user found difficult to reproduce elsewhere and tests the highest-risk integration early. The existing tutor and Atlas can remain usable throughout.

---

## 12. Quality, measurement and operational requirements

### 12.1 Correctness and safety targets

The parity test suite should permit no false claims of current-revision CI success, no lost accepted evidence in the concurrency fixtures, no silent promotion from guided/delegated work to independence, and no private-to-public leakage in the privacy fixtures. These are acceptance targets, not a claim that software can guarantee perfect behaviour in every future interaction.

Mechanical changes should be deterministic where possible. Model-generated learning interpretations must be traceable, reviewable and correctable. A failed source read, unsupported provider capability or missing CI run is an explicit state, not a reason to fabricate an answer.

### 12.2 Measure the actual workflow

| Measure | Why it matters | Measurement boundary |
|---|---|---|
| User effort to resume and sync | The application should remove bookkeeping | User interactions/corrections, not guessed study hours |
| Time to a useful first teaching task | Detects expensive repository archaeology | Record retrieval and model latency separately |
| Context included per task | Tests selective loading | Actual provider counts when available; label estimates |
| Model/tool/execution cost | Detects runaway orchestration or unnecessary context | Provider usage, CI/runtime and storage tracked separately |
| CI detection/repair outcomes | Tests reliability | Correct revision/run, failure category, retries and final outcome |
| Unsupported or corrected learning claims | Tests evidence integrity | Human-reviewed sample; separate model error from missing evidence |
| State conflicts and recovered writes | Tests concurrency/durability | Count observed incidents, lost updates and successful reconciliations |
| Handover usefulness | Tests parity beyond file production | Whether the next session targets the actual remaining gap |
| Export/recovery success | Tests platform independence | Fresh bootstrap and reproducible reconstruction |

No current cost saving, token reduction, latency improvement or retention benefit is established by this review. Baseline these before setting numerical performance targets. A faster sync is not a success if it loses evidence or increases the learner's correction burden.

### 12.3 Operational behaviour

Persist a private draft before acknowledging that session evidence is saved. Save enough execution state to recover after a worker restart. Surface permission revocation, external-service errors and blocked decisions clearly. Cancellation must stop future work at a safe boundary while accurately reporting any writes already completed.

Maintain application policy and data-format versions. On schema/protocol changes, validate migrations against prior fixtures and keep rollback/export possible. Do not claim compatibility with an arbitrary new model merely because its endpoint accepts the same message format.

---

## 13. Deferred scope and decisions

### 13.1 Later, not required for parity [L]

A learned mastery predictor, personalized spaced-repetition optimizer, semantic/vector retrieval, graph-database storage, autonomous multi-agent tutoring, native mobile apps, voice tutoring, automatic lecture recording, university integrations, calendar automation, multi-learner support and commercial billing can all be considered later.

The existing dependency graph and retrieval prompts are already sufficient to start. Add semantic retrieval when direct/structured/text lookup fails representative questions; add more formal observation modelling when meaningful attempt history becomes difficult to recover. Do not introduce these merely because the product concerns AI. [R-REVIEW]

### 13.2 Decisions with recommended starting defaults

| Decision | Starting default | Revisit when |
|---|---|---|
| Learning system of record | Git-backed accepted records; private app state for sessions/jobs | A demonstrated transactional/query need justifies migration |
| Atlas implementation | Reuse existing renderer and tests | A required interaction cannot be supported cleanly |
| Model access | Explicit configured adapters; app-owned context/execution | Additional providers pass capability and pedagogy checks |
| Executor architecture | One durable workflow worker with isolated task execution | Concurrency/load demands more separation |
| Retrieval | Direct state lookup, deterministic manifest, structured/text search | A benchmark demonstrates useful misses |
| Approval policy | Bounded proposal execution; human merge/semantic approval | The learner explicitly authorises narrower routine automation |
| Public/private boundary | Private by default; explicit reviewed public export | Sharing requirements are deliberately expanded |
| Historical migration | Preserve existing records, mark reconstructed provenance | Specific evidence needs structured backfill |

Provider credentials/access terms, deployment location, runtime budget and the final UI/backend stack still require implementation decisions. None changes the central parity requirements or justifies assuming that a consumer chat subscription supplies the application's model access.

### 13.3 Non-negotiable outcome

The application should let the learner change model or device without losing the learning process, and let the learning process change without losing its evidence.

The most valuable abstraction is not “a chatbot that remembers me.” It is **a controlled path from a learning interaction to an accurate, reviewable, versioned learning record—and a reliable path back into the next interaction**.

---

## 14. Source register

### 14.1 Repository sources

Repository file links below are pinned to the reviewed commit. They support descriptions of the current system; the proposed application requirements remain proposals. Coverage labels describe what was inspected for this review, not a claim that every historical source was revalidated.

| Reference | Source | Review coverage |
|---|---|---|
| [R-README] | Root README | Full; purpose, usage and privacy boundary |
| [R-ARCH] | `ARCHITECTURE.md` | Architecture, evidence responsibilities, memory, CI/publication and onboarding sections |
| [R-SESSION] | `SESSION_WORKFLOW.md` | Full operating and tutoring protocol |
| [R-SYNC] | `SYNC_LEARNING_STATE.md` | Full sync protocol and completion rules |
| [R-ENGINEERING] | `AI_ASSISTED_ENGINEERING_WORKFLOW.md` | Full; delegation, contracts and testing |
| [R-STATE] | `LEARNING_STATE.md` | Current lanes and recent session/decision sections; not a full historical evidence re-audit |
| [R-ROADMAP] | `LEARNING_ROADMAP.md` | Purpose, learning rules, historical foundation and strategy sections |
| [R-SYLLABUS] | `MSC_SYLLABUS_MAP.md` | Current AIMS5701/AIMS5702 scope/readiness and course-context sections |
| [R-PROJECTION] | `learning_progress.yaml` | Metadata, sources, defaults and schema structure; compatibility checked against builder/tests |
| [R-DEADLINES] | `deadlines.yaml` | Full |
| [R-INDEX] | `lesson_logs/INDEX.md` | Full discovery/index record |
| [R-ATLAS] | `dashboard/README.md` | Full behaviour, schema, privacy and build guidance |
| [R-BUILD] | `dashboard/build.py` | Full validator, renderer and build path |
| [R-TESTS] | `dashboard/test_build.py` | Full schema/source/rendering/curriculum regressions |
| [R-SYNC-TEST] | `dashboard/test_projection_sync.py` | Full drift guard |
| [R-JS] | `dashboard/static/app.js` | Full filtering, navigation, dialogs and freshness behaviour |
| [R-BROWSER] | `dashboard/browser_smoke.py` | Full browser-check code; not executed locally in this audit |
| [R-DASH-WF] | `.github/workflows/dashboard.yml` | Full triggers, validation, preview and publication configuration |
| [R-TEST-WF] | `.github/workflows/tests.yml` | Full test workflow |
| [R-OCT1] | AIMS5702 1 October consolidation/lab-readiness log | Full |
| [R-SEP30] | AIMS5701 30 September pre-lecture retrieval log | Full substantive session record |
| [R-RECEIPTS] | FTEC5660 25 September receipts completion log | Full |
| [R-DELEGATION] | Private Client Graph 2 October delegation decision | Full |
| [R-REVIEW] | 26 September architecture review | Full historical review; not treated as current instructions |
| [R-PRACTICE] | Search reconstruction practice code | Representative portion; confirms why comments/reference code cannot alone establish current exercise state |
| [R-TREE] | Pinned root tree metadata | Root source paths and file sizes; no claim of a complete counted recursive inventory |

### 14.2 Pull-request usage evidence

PR metadata and descriptions were reviewed for all entries below. Underlying focused logs and system files were inspected selectively; full diffs and all comments were not audited for every PR.

| PRs | Role in the review |
|---|---|
| [#17][P17], [#18][P18] | Course organisation and learning-system architecture |
| [#19][P19], [#20][P20], [#21][P21], [#22][P22] | Retrieval, LCEL practice, reference implementations and project planning |
| [#23][P23], [#24][P24], [#25][P25] | Delivery plane, assignment preparation and intentionally red practice |
| [#26][P26], [#27][P27], [#28][P28], [#29][P29] | Projection drift, lecture calibration, interpolation and sync hardening |
| [#30][P30], [#31][P31] | Receipts implementation/learning progression |
| [#32][P32], [#33][P33], [#34][P34], [#35][P35], [#36][P36], [#37][P37] | Search retrieval, proof/intuition preservation and near-term planning |
| [#38][P38], [#39][P39], [#40][P40] | Divergent lecture/receipts updates reconciled into #40; #38/#39 were not merged |
| [#41][P41], [#42][P42] | Engineering protocol and historical architecture review |
| [#43][P43], [#44][P44], [#45][P45] | Bayesian-network bridge, project design and live syllabus correction |
| [#46][P46], [#47][P47], [#48][P48] | Evidence relocation and new course evidence reconciled into #48; #46/#47 were not merged |
| [#49][P49], [#50][P50], [#51][P51] | Lab-readiness boundary, delegation and evaluation-design decisions |

### 14.3 Operational and external references

- [G-BRANCH]: branch metadata response observed during the review. This is a live endpoint and can change after the snapshot.
- [G-MAIN-TESTS] and [G-MAIN-ATLAS]: concrete successful main-branch run records observed for the pinned commit.
- [D-CHECKS]: official GitHub documentation for check statuses/conclusions, checked 3 October 2026.
- [D-WEBHOOKS]: official GitHub webhook operational guidance, checked 3 October 2026.
- Current user conversation: explicit request for parity, GitHub/Actions continuity, model portability, mobile use and an application. These are user requirements, not independently verified claims about competitor capabilities.

[R-README]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/README.md
[R-ARCH]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/ARCHITECTURE.md
[R-SESSION]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/SESSION_WORKFLOW.md
[R-SYNC]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/SYNC_LEARNING_STATE.md
[R-ENGINEERING]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/AI_ASSISTED_ENGINEERING_WORKFLOW.md
[R-STATE]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/LEARNING_STATE.md
[R-ROADMAP]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/LEARNING_ROADMAP.md
[R-SYLLABUS]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/MSC_SYLLABUS_MAP.md
[R-PROJECTION]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/learning_progress.yaml
[R-DEADLINES]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/deadlines.yaml
[R-INDEX]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/lesson_logs/INDEX.md
[R-ATLAS]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/dashboard/README.md
[R-BUILD]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/dashboard/build.py
[R-TESTS]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/dashboard/test_build.py
[R-SYNC-TEST]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/dashboard/test_projection_sync.py
[R-JS]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/dashboard/static/app.js
[R-BROWSER]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/dashboard/browser_smoke.py
[R-DASH-WF]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/.github/workflows/dashboard.yml
[R-TEST-WF]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/.github/workflows/tests.yml
[R-OCT1]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/lesson_logs/aims5702/lecture_break_consolidation_lab_readiness_2026_10_01.md
[R-SEP30]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/lesson_logs/aims5701/lecture03_prelecture_retrieval_2026_09_30.md
[R-RECEIPTS]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/lesson_logs/ftec5660/hw1_receipt_chain_completion_2026_09_25.md
[R-DELEGATION]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/lesson_logs/ftec5660/private_client_graph/decisions/ai-implementation-delegation-2026-10-02.md
[R-REVIEW]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/docs/architecture-reviews/2026-09-26-astra-learning-system-review.md
[R-PRACTICE]: https://github.com/alistairkung/msc-ai-learning/blob/22453d567d9da77e6b56ee42bf305c1bed8d5244/classical_ai/search/test_lesson33_search_reconstruction_practice.py
[R-TREE]: https://api.github.com/repos/alistairkung/msc-ai-learning/git/trees/e9f3475c8bab6e2456d29cb9a97a2b32adfaa949
[G-BRANCH]: https://api.github.com/repos/alistairkung/msc-ai-learning/branches/main
[G-MAIN-TESTS]: https://github.com/alistairkung/msc-ai-learning/actions/runs/36985122033
[G-MAIN-ATLAS]: https://github.com/alistairkung/msc-ai-learning/actions/runs/36985122025
[D-CHECKS]: https://docs.github.com/en/pull-requests/reference/status-checks
[D-WEBHOOKS]: https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks
[P17]: https://github.com/alistairkung/msc-ai-learning/pull/17
[P18]: https://github.com/alistairkung/msc-ai-learning/pull/18
[P19]: https://github.com/alistairkung/msc-ai-learning/pull/19
[P20]: https://github.com/alistairkung/msc-ai-learning/pull/20
[P21]: https://github.com/alistairkung/msc-ai-learning/pull/21
[P22]: https://github.com/alistairkung/msc-ai-learning/pull/22
[P23]: https://github.com/alistairkung/msc-ai-learning/pull/23
[P24]: https://github.com/alistairkung/msc-ai-learning/pull/24
[P25]: https://github.com/alistairkung/msc-ai-learning/pull/25
[P26]: https://github.com/alistairkung/msc-ai-learning/pull/26
[P27]: https://github.com/alistairkung/msc-ai-learning/pull/27
[P28]: https://github.com/alistairkung/msc-ai-learning/pull/28
[P29]: https://github.com/alistairkung/msc-ai-learning/pull/29
[P30]: https://github.com/alistairkung/msc-ai-learning/pull/30
[P31]: https://github.com/alistairkung/msc-ai-learning/pull/31
[P32]: https://github.com/alistairkung/msc-ai-learning/pull/32
[P33]: https://github.com/alistairkung/msc-ai-learning/pull/33
[P34]: https://github.com/alistairkung/msc-ai-learning/pull/34
[P35]: https://github.com/alistairkung/msc-ai-learning/pull/35
[P36]: https://github.com/alistairkung/msc-ai-learning/pull/36
[P37]: https://github.com/alistairkung/msc-ai-learning/pull/37
[P38]: https://github.com/alistairkung/msc-ai-learning/pull/38
[P39]: https://github.com/alistairkung/msc-ai-learning/pull/39
[P40]: https://github.com/alistairkung/msc-ai-learning/pull/40
[P41]: https://github.com/alistairkung/msc-ai-learning/pull/41
[P42]: https://github.com/alistairkung/msc-ai-learning/pull/42
[P43]: https://github.com/alistairkung/msc-ai-learning/pull/43
[P44]: https://github.com/alistairkung/msc-ai-learning/pull/44
[P45]: https://github.com/alistairkung/msc-ai-learning/pull/45
[P46]: https://github.com/alistairkung/msc-ai-learning/pull/46
[P47]: https://github.com/alistairkung/msc-ai-learning/pull/47
[P48]: https://github.com/alistairkung/msc-ai-learning/pull/48
[P49]: https://github.com/alistairkung/msc-ai-learning/pull/49
[P50]: https://github.com/alistairkung/msc-ai-learning/pull/50
[P51]: https://github.com/alistairkung/msc-ai-learning/pull/51