from pathlib import Path

import yaml

from dashboard.build import DATA_PATH, build, build_topic_lookup


def test_learning_progress_course_topics_exist():
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    topics = build_topic_lookup(data)

    for course in data["courses"].values():
        for week in course["weeks"]:
            assert set(week["topics"]).issubset(topics)


def test_dashboard_builds_without_template_tokens():
    output = build()
    html = Path(output).read_text(encoding="utf-8")

    assert "<h1>MSc AI Learning Dashboard</h1>" in html
    assert "{{" not in html
    assert "Lesson 31" in html
