# Learning Dashboard

This directory contains a small static dashboard generated from `learning_progress.yaml`.

## Why it exists

The Markdown learning-state files remain the durable narrative/context layer. The dashboard is only a visual projection of the structured learning state:

- **Current focus** — what to study now / next.
- **MSc readiness** — upcoming syllabus topics and their weakest prerequisite state.
- **Knowledge map** — topic status plus separate retrieval status.
- **Timeline** — chronological view of the lesson sequence.

The dashboard deliberately avoids fake mastery percentages. Statuses are qualitative and should change only when the learning evidence changes.

## Source of truth

Edit:

```text
learning_progress.yaml
```

Do not hand-edit `dashboard/site/index.html`; it is generated.

## Build locally

```bash
python dashboard/build.py
```

The generated site is written to:

```text
dashboard/site/
```

## GitHub Pages

`.github/workflows/dashboard.yml` builds and deploys the site from `main` using GitHub Pages.

The repository must have **Settings → Pages → Build and deployment → Source: GitHub Actions** enabled for deployment to succeed.

## End-of-session convention

When a lesson materially changes a topic's learning/retrieval state, update `learning_progress.yaml` alongside the normal `LEARNING_STATE.md` / lesson-log handover. Routine lesson detail still belongs in `lesson_logs/`, not in the dashboard file.
