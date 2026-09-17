"""Regression guard for operational-state -> Learning Atlas drift.

The dashboard is a reviewed structured projection, not an automatic mastery parser.
This test therefore does not infer topic status from Markdown. It only enforces that a
completed explicit learning-state sync reviewed the current handover and aligned the
evidence cutoff with the handover's own evidence-through date.
"""

from datetime import date
import re

import yaml

from dashboard.build import DATA_PATH, ROOT, blob_sha


STATE_PATH = ROOT / "LEARNING_STATE.md"
EVIDENCE_THROUGH_RE = re.compile(
    r"Learning evidence through (\d{4}-\d{2}-\d{2})\."
)


def test_learning_state_projection_is_synchronised():
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    state_text = STATE_PATH.read_text(encoding="utf-8")

    match = EVIDENCE_THROUGH_RE.search(state_text)
    assert match, "LEARNING_STATE.md must declare a Learning evidence through date"

    state_evidence_through = match.group(1)
    assert data["meta"]["evidence_through"] == state_evidence_through, (
        "learning_progress.yaml is stale: meta.evidence_through must match "
        "LEARNING_STATE.md after a full learning-state sync"
    )

    assert data["sources"]["state"]["sha"] == blob_sha(STATE_PATH), (
        "learning_progress.yaml still points at an older LEARNING_STATE.md blob. "
        "Run the full 'Sync learning state' workflow and reconcile the Atlas."
    )

    reviewed_on = date.fromisoformat(data["meta"]["reviewed_on"])
    evidence_through = date.fromisoformat(state_evidence_through)
    assert reviewed_on >= evidence_through
