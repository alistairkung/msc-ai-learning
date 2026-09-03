from __future__ import annotations

from html import escape
from pathlib import Path
import shutil

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "learning_progress.yaml"
TEMPLATE_PATH = ROOT / "dashboard" / "template.html"
STYLE_PATH = ROOT / "dashboard" / "static" / "styles.css"
SITE_DIR = ROOT / "dashboard" / "site"

STATUS_ORDER = {
    "planned": 0,
    "developing": 1,
    "established": 2,
    "strong": 3,
}

STATUS_LABEL = {
    "strong": "Strong",
    "established": "Established",
    "developing": "Developing",
    "planned": "Planned",
}

RETRIEVAL_LABEL = {
    "current": "Retrieval current",
    "due": "Retrieval due",
    "not_started": "Not started",
    "n/a": "N/A",
}


def esc(value: object) -> str:
    return escape(str(value), quote=True)


def status_badge(status: str) -> str:
    return (
        f'<span class="badge status-{esc(status)}">'
        f'<span class="dot"></span>{esc(STATUS_LABEL.get(status, status.title()))}</span>'
    )


def retrieval_badge(retrieval: str) -> str:
    return (
        f'<span class="badge retrieval-{esc(retrieval)}">'
        f'{esc(RETRIEVAL_LABEL.get(retrieval, retrieval.replace("_", " ").title()))}</span>'
    )


def lesson_badges(lessons: list[str]) -> str:
    if not lessons:
        return '<span class="muted">No lesson yet</span>'
    return "".join(f'<span class="lesson-chip">L{esc(lesson)}</span>' for lesson in lessons)


def build_topic_lookup(data: dict) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for domain_name, domain in data["domains"].items():
        for topic_id, topic in domain["topics"].items():
            if topic_id in lookup:
                raise ValueError(f"Duplicate topic id: {topic_id}")
            lookup[topic_id] = {**topic, "id": topic_id, "domain": domain_name}
    return lookup


def overall_status(topic_ids: list[str], topics: dict[str, dict]) -> str:
    statuses = [topics[topic_id]["status"] for topic_id in topic_ids]
    return min(statuses, key=lambda status: STATUS_ORDER[status])


def render_focus(data: dict) -> str:
    cards = []
    for item in data["focus"]:
        cards.append(
            f"""
            <article class="focus-card">
              <div class="eyebrow">{esc(item["stage"])}</div>
              <h3>{esc(item["title"])}</h3>
              <p>{esc(item["detail"])}</p>
            </article>
            """
        )
    return "\n".join(cards)


def render_readiness(data: dict, topics: dict[str, dict]) -> str:
    course_cards = []
    for course_id, course in data["courses"].items():
        weeks = []
        for week in course["weeks"]:
            topic_ids = week["topics"]
            missing = [topic_id for topic_id in topic_ids if topic_id not in topics]
            if missing:
                raise ValueError(
                    f"{course_id} references missing topics: {', '.join(missing)}"
                )
            status = overall_status(topic_ids, topics)
            topic_chips = "".join(
                f'<span class="topic-chip status-border-{esc(topics[topic_id]["status"])}">'
                f'{esc(topics[topic_id]["label"])}</span>'
                for topic_id in topic_ids
            )
            weeks.append(
                f"""
                <div class="week-row">
                  <div class="week-label">
                    <span class="week-number">W{esc(week["week"])}</span>
                    <div>
                      <strong>{esc(week["label"])}</strong>
                      <div class="topic-chip-row">{topic_chips}</div>
                    </div>
                  </div>
                  {status_badge(status)}
                </div>
                """
            )
        course_cards.append(
            f"""
            <article class="course-card">
              <div class="course-heading">
                <div>
                  <div class="eyebrow">{esc(course_id)} · {esc(course["term"])}</div>
                  <h3>{esc(course["name"])}</h3>
                </div>
              </div>
              <div class="week-list">
                {''.join(weeks)}
              </div>
            </article>
            """
        )
    return "\n".join(course_cards)


def render_knowledge_map(data: dict) -> str:
    domain_cards = []
    for domain_name, domain in data["domains"].items():
        topic_rows = []
        for topic_id, topic in domain["topics"].items():
            gap_html = ""
            if topic.get("gaps"):
                gap_html = (
                    '<ul class="gap-list">'
                    + "".join(f"<li>{esc(gap)}</li>" for gap in topic["gaps"])
                    + "</ul>"
                )
            note_html = (
                f'<p class="topic-note">{esc(topic["note"])}</p>'
                if topic.get("note")
                else ""
            )
            topic_rows.append(
                f"""
                <article class="topic-row" id="topic-{esc(topic_id)}">
                  <div class="topic-main">
                    <div class="topic-title-row">
                      <h4>{esc(topic["label"])}</h4>
                      <div class="badge-row">
                        {status_badge(topic["status"])}
                        {retrieval_badge(topic["retrieval"])}
                      </div>
                    </div>
                    {note_html}
                    {gap_html}
                  </div>
                  <div class="lesson-links">{lesson_badges(topic.get("lessons", []))}</div>
                </article>
                """
            )
        domain_cards.append(
            f"""
            <section class="domain-card">
              <div class="domain-heading">
                <h3>{esc(domain_name)}</h3>
                <p>{esc(domain.get("description", ""))}</p>
              </div>
              <div class="topic-list">{''.join(topic_rows)}</div>
            </section>
            """
        )
    return "\n".join(domain_cards)


def render_timeline(data: dict) -> str:
    items = []
    for entry in data["timeline"]:
        active_class = " active" if entry.get("active") else ""
        active_label = '<span class="active-label">Current</span>' if entry.get("active") else ""
        items.append(
            f"""
            <article class="timeline-item{active_class}">
              <div class="timeline-marker"></div>
              <div class="timeline-content">
                <div class="timeline-lessons">Lessons {esc(entry["lessons"])} {active_label}</div>
                <h4>{esc(entry["label"])}</h4>
                <p>{esc(entry["detail"])}</p>
              </div>
            </article>
            """
        )
    return "\n".join(items)


def render_legend(data: dict) -> str:
    statuses = "".join(
        f"""
        <div class="legend-item">
          {status_badge(key)}
          <span>{esc(description)}</span>
        </div>
        """
        for key, description in data["status_definitions"].items()
    )
    retrieval = "".join(
        f"""
        <div class="legend-item">
          {retrieval_badge(key)}
          <span>{esc(description)}</span>
        </div>
        """
        for key, description in data["retrieval_definitions"].items()
    )
    return f"""
      <div class="legend-column">
        <h4>Learning state</h4>
        {statuses}
      </div>
      <div class="legend-column">
        <h4>Retrieval state</h4>
        {retrieval}
      </div>
    """


def build() -> Path:
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    topics = build_topic_lookup(data)

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    replacements = {
        "{{TITLE}}": esc(data["meta"]["title"]),
        "{{LAST_UPDATED}}": esc(data["meta"]["last_updated"]),
        "{{CURRENT_LESSON}}": esc(data["meta"]["current_lesson"]),
        "{{STRATEGY}}": esc(data["meta"]["strategy"]),
        "{{FOCUS}}": render_focus(data),
        "{{READINESS}}": render_readiness(data, topics),
        "{{KNOWLEDGE_MAP}}": render_knowledge_map(data),
        "{{TIMELINE}}": render_timeline(data),
        "{{LEGEND}}": render_legend(data),
    }

    for token, value in replacements.items():
        template = template.replace(token, value)

    leftovers = [token for token in replacements if token in template]
    if leftovers:
        raise ValueError(f"Unreplaced template tokens: {leftovers}")

    SITE_DIR.mkdir(parents=True, exist_ok=True)
    output_path = SITE_DIR / "index.html"
    output_path.write_text(template, encoding="utf-8")
    shutil.copy2(STYLE_PATH, SITE_DIR / "styles.css")
    return output_path


if __name__ == "__main__":
    path = build()
    print(f"Built dashboard: {path.relative_to(ROOT)}")
