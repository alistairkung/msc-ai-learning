# Learning Atlas

A static, evidence-led dashboard generated from **`learning_progress.yaml` (schema v2)** plus a separate **`deadlines.yaml` delivery-planning record**. No runtime API, database, analytics or external frontend dependencies. The approved concept's dark visual design is retained; the records are repository data rather than hard-coded demo objects.

## Build and inspect

```bash
python -m pip install 'PyYAML>=6,<7' pytest
python -m pytest dashboard/test_build.py
python dashboard/build.py
python -m http.server 8000 --directory dashboard/site
```

Output is ignored in Git. CSS/JavaScript use content-hashed filenames so new deployments cannot reuse old asset names. GitHub Actions uploads a downloadable PR preview; deployment remains a separate main-only job. A PR does not publish over the live page.

The Python API's `source_root=None` supports isolated preview/tests and prominently warns that source-file verification was not performed. The CLI and CI never opt out: missing source files fail, changed reviewed hashes warn.

## Browser checks

```bash
python -m pip install 'playwright==1.57.0'
python -m playwright install chromium
python dashboard/browser_smoke.py dashboard/site
```

These checks exercise the actual generated page: filters, empty state/reset, topic detail, Escape/focus return, tab keyboard navigation, syllabus expansion, mobile overflow and no-JavaScript fallback. They do not assess the learner. Screenshots are preview artifacts, not tracked source files.

## Data responsibilities

`meta.reviewed_on` is the structured learning-record review date; `evidence_through` is the latest included learning event. Neither is a build timestamp or proof of fresh recall. `source_ref` is the fallback provenance snapshot; CI uses the checked-out commit for source links.

Every topic has independent dimensions:

- `concept`: `demonstrated`, `taught`, `historical`, `planned`, `unknown`.
- `performance`: `independent`, `guided`, `implemented`, `historical`, `pending`, `unknown`.
- `review`: `recorded`, `diagnostic`, `unknown`, `not_due`.
- `action`: `maintain`, `build`, `practice`, `retrieve`, `diagnose`, `learn`, `transfer`, `confirm`.

Also record a concise evidence summary, an explicit boundary, a useful next action, source IDs, optional actual event date and prerequisite topic IDs. Performance may mean explaining, calculating, deriving or coding. Syntax/API lookup is not the same as conceptual scaffolding. Never label existing code as independent work without supporting evidence.

A source record contains a public repository `path` and reviewed Git blob `sha`. Compute the SHA with `git hash-object path/to/file` (or `dashboard.build.blob_sha`). Refresh it only after checking the source change against the affected records. If the hash changes, the dashboard warns; it never infers that learner knowledge changed. Hidden/private paths and `LEARNER_PROFILE.md` are forbidden as sources.

## Delivery deadlines are a separate planning plane

`deadlines.yaml` exists because a due date answers a different question from a learning-evidence record.

```text
learning_progress.yaml
    -> what learning evidence is recorded?

Continue / Parallel / Protect
    -> what learning should happen next?

deadlines.yaml
    -> what external delivery constraints resize the available time?
```

The dashboard therefore renders **Upcoming assessed work** as a delivery lane beside, but not inside, the three study lanes. Adding a deadline must not create a fake learning topic, promote a skill, or change concept/performance status.

Deadline entries contain an ID, course, title, ISO `due_on` date, status, provenance, mode and a short planning note. Current provenance values distinguish learner-reported dates from course-material or official dates. Learner-reported dates are useful workload constraints even when official weighting/scope still needs separate verification.

When a deadline changes, update `deadlines.yaml` and the operational handover if the change affects priorities. Do **not** move learning evidence dates forward or edit mastery state merely because an assignment is urgent.

### Updating after a lesson or planning change

1. Update the focused lesson log and the concise handover first for substantive learning.
2. Change only affected topics' evidence, support/performance, date, boundary and next action. Guided success is not automatically independent retrieval.
3. Update the Continue/Parallel/Protect lanes or course requirements only when learning priorities change.
4. Update `deadlines.yaml` when an assessed-work date/status changes; keep provenance explicit.
5. Review and refresh hashes of changed learning sources only when reconciling the learning projection. Do not move old event dates forward to clear an age warning.
6. Run schema/source validation, build tests and relevant browser checks. Review the diff for unrelated deletions.

Markdown remains the nuanced evidence trail. The learning YAML is maintained deliberately, not generated from prose. Deadline planning is also explicit rather than inferred from syllabus week numbers. Rendering, reference checks and recency prompts are deterministic. Browser recency prompts keep working even without a new deployment; age does not automatically demote knowledge.

## Course requirements, not whole-week mastery

Each course entry records **anchors**, **remaining requirements**, scope, an explanatory note and an optional **confirmed** due date. They reference the same topic IDs used by the knowledge map. Anchors are not a “ready” verdict; older foundations may still need a diagnostic. No minimum/average topic score is calculated.

`scope` is `mapped`, `scope_unconfirmed`, `not_mapped`, `overview` or `partial_tutorial`. An incomplete mapping must remain visibly incomplete. MLE, convergence and adaptive optimisation have their own targets; basic probability, autograd or a training loop cannot silently stand in for them.

Course `expected_weeks` plus regression tests protect the recorded sequence. AIMS5701 and AIMS5702 currently have 12 syllabus entries; AIMS5704 has 13. FTEC5660 uses lecture/pattern/project entries rather than invented weekly dates. An intentional syllabus revision requires updating the source map and coverage test together, not silently shrinking the map.

The original v1 topics are retained, with finer historical maths targets and explicit missing-theory targets added. Overview topics are navigational aggregates—not extra independent achievements to count. Timeline history is retained separately. No percentage, overall knowledge score or comprehensive-MSc-coverage claim is produced.

## Interface and privacy

Default view shows active learning-lane targets; Show all/reset exposes every recorded target. Search also searches course IDs. Topic dialogs show evidence, boundaries, next steps, sources and prerequisites. The Study & delivery view shows the deadline lane first and the three evidence-backed study lanes underneath it. Views and topics have hash links. Native dialog keyboard behaviour and explicit tab navigation support keyboard use. Without JavaScript, the full table, course panels and source-backed topic details remain readable.

There are no trackers, external assets or automatic remote requests. The build reads only explicitly listed public learning sources plus the repository-local deadline record; it never scans or embeds a local private learner profile. The practice BFS solution remains uncommitted and the exercise stays skipped for CI.
