"""Build a static, evidence-led dashboard. No model calls or inferred mastery."""
from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
from hashlib import sha1, sha256
from html import escape
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
from urllib.parse import quote

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / 'learning_progress.yaml'
SITE_DIR = ROOT / 'dashboard' / 'site'
CONCEPT = {'demonstrated': 'Understanding recorded', 'taught': 'Taught / introduced',
           'historical': 'Historical learning', 'planned': 'New material planned', 'unknown': 'Coverage uncertain'}
PERFORMANCE = {'independent': 'Independent work logged', 'guided': 'Guided / partial work',
               'implemented': 'Implementation recorded', 'historical': 'Historical worked evidence',
               'pending': 'Performance not yet recorded', 'unknown': 'Evidence incomplete'}
REVIEW = {'recorded': 'Dated evidence', 'diagnostic': 'Diagnostic needed',
          'unknown': 'Recency not recorded', 'not_due': 'Not a recall target'}
ACTIONS = {'maintain': 'Maintain', 'build': 'Build / reconstruct', 'practice': 'Practise',
           'retrieve': 'Retrieve selectively', 'diagnose': 'Diagnose', 'learn': 'New teaching',
           'transfer': 'Transfer to a new task', 'confirm': 'Confirm scope'}
SCOPES = {'mapped': 'Requirements mapped', 'scope_unconfirmed': 'Scope / dates unconfirmed',
          'not_mapped': 'Mapping incomplete', 'overview': 'Overview only', 'partial_tutorial': 'Tutorial partial'}
ID_RE = re.compile(r'^[a-z][a-z0-9_]*$')
SHA_RE = re.compile(r'^[0-9a-f]{40}$')
SOURCE_TOKENS = re.compile(r'{{[A-Z_]+}}')


def esc(value: object) -> str:
    return escape(str(value), quote=True)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def iso(value: object, label: str) -> date:
    require(isinstance(value, str), f'{label}: use a quoted ISO date')
    try:
        result = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f'{label}: invalid date {value!r}') from error
    require(result.isoformat() == value, f'{label}: expected YYYY-MM-DD')
    return result


def source_path(value: str) -> PurePosixPath:
    require(isinstance(value, str) and bool(value), 'Source path must be text')
    path = PurePosixPath(value)
    require(not path.is_absolute() and '..' not in path.parts and '\\' not in value
            and ':' not in value and '?' not in value and '#' not in value,
            f'Unsafe source path: {value}')
    require(all(not part.startswith('.') and part.upper() != 'LEARNER_PROFILE.MD'
                for part in path.parts), f'Private/hidden source forbidden: {value}')
    require(path.suffix in {'.md', '.py', '.yaml', '.yml'}, f'Unsupported source: {value}')
    return path


def blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return sha1(f'blob {len(raw)}\0'.encode() + raw).hexdigest()


def validate(data: dict, root: Path | None = ROOT) -> list[str]:
    """Validate structure and references. A changed source is a warning, not a failed learner.

    root=None permits schema-only validation for isolated tests/previews. Production
    builds always provide the repository root and verify real source paths/hashes.
    """
    require(isinstance(data, dict) and data.get('schema_version') == 2, 'Expected schema_version: 2')
    for key in ('meta', 'sources', 'topics', 'courses'):
        require(isinstance(data.get(key), dict) and bool(data[key]), f'Missing/nonempty mapping: {key}')
    meta = data['meta']
    reviewed = iso(meta.get('reviewed_on'), 'meta.reviewed_on')
    through = iso(meta.get('evidence_through'), 'meta.evidence_through')
    require(through <= reviewed, 'Evidence cutoff is after review date')
    require(bool(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', meta.get('repository', ''))), 'Invalid repository')
    require(bool(SHA_RE.fullmatch(meta.get('source_ref', ''))), 'source_ref must be a full commit SHA')
    require(type(meta.get('stale_after_days')) is int and meta['stale_after_days'] > 0, 'Invalid stale threshold')
    warnings = []
    for key, source in data['sources'].items():
        require(bool(ID_RE.fullmatch(key)), f'Invalid source id: {key}')
        path = source_path(source.get('path'))
        require(bool(SHA_RE.fullmatch(source.get('sha', ''))), f'{key}: source SHA is required')
        if root is not None:
            local = (root / path).resolve()
            require(local.is_relative_to(root.resolve()) and local.is_file(), f'Missing/unsafe source: {path}')
            if blob_sha(local) != source['sha']:
                warnings.append(f'{path} changed since the evidence record was reviewed. Reconcile affected targets; do not assume mastery changed.')
    topics = data['topics']
    for key, topic in topics.items():
        require(bool(ID_RE.fullmatch(key)), f'Invalid topic id: {key}')
        for field in ('name', 'area', 'evidence', 'boundary', 'next'):
            require(isinstance(topic.get(field), str) and bool(topic[field].strip()), f'{key}: missing {field}')
        for field, choices in [('concept', CONCEPT), ('performance', PERFORMANCE), ('review', REVIEW), ('action', ACTIONS)]:
            require(topic.get(field) in choices, f'{key}: invalid {field}')
        sources = topic.get('sources')
        require(isinstance(sources, list) and bool(sources) and all(s in data['sources'] for s in sources), f'{key}: invalid sources')
        deps = topic.get('depends_on', [])
        require(isinstance(deps, list) and all(d in topics and d != key for d in deps), f'{key}: invalid dependencies')
        when = topic.get('evidence_on')
        if when is not None:
            require(iso(when, key) <= through, f'{key}: event exceeds evidence cutoff')
        if topic['review'] == 'recorded':
            require(when is not None, f'{key}: recorded evidence needs a date')
        if topic['concept'] == 'planned':
            require(topic['review'] == 'not_due' and topic['performance'] == 'pending', f'{key}: untaught topic cannot be overdue or mastered')
        if topic['performance'] == 'independent':
            require(when is not None and topic['concept'] == 'demonstrated', f'{key}: independent evidence needs date and demonstrated concept')
    done, visiting = set(), set()
    def visit(key: str) -> None:
        require(key not in visiting, f'Dependency cycle at {key}')
        if key in done:
            return
        visiting.add(key)
        for dep in topics[key].get('depends_on', []):
            visit(dep)
        visiting.remove(key)
        done.add(key)
    for key in topics:
        visit(key)
    lanes = data.get('lanes', [])
    require([lane.get('id') for lane in lanes] == ['continue', 'parallel', 'protect'], 'Exactly three ordered study lanes are required')
    for lane in lanes:
        require(lane.get('target') in topics, 'Unknown lane target')
        for task in lane.get('tasks', []):
            require(all(t in topics for t in task['topics']), 'Unknown task topic')
    for code, course in data['courses'].items():
        weeks = course.get('weeks', [])
        ids = [week['week'] for week in weeks]
        expected = course.get('expected_weeks', [])
        require(bool(expected) and len(expected) == len(set(expected)) and set(ids) == set(expected) and len(ids) == len(set(ids)), f'{code}: syllabus coverage missing or duplicated')
        for week in weeks:
            require(week.get('scope') in SCOPES, f'{code}: invalid scope')
            for field in ('anchors', 'remaining'):
                require(isinstance(week.get(field), list) and all(t in topics for t in week[field]), f'{code} {week["week"]}: missing topic reference')
            require(not set(week['anchors']) & set(week['remaining']), f'{code}: a requirement is in both columns')
            if week.get('due_on') is not None:
                iso(week['due_on'], f'{code} due_on')
            require(bool(week['anchors'] or week['remaining'] or week.get('note')), f'{code}: unexplained empty requirement')
    for route in data.get('paths', []):
        require(all(t in topics for t in route['topics']), 'Unknown learning-path topic')
    return warnings


def badge(label: str, colour: str = 'muted') -> str:
    return f'<span class="tag {esc(colour)}">{esc(label)}</span>'


def target_link(key: str, topics: dict, label: str | None = None) -> str:
    return f'<a href="#record-{esc(key)}" data-open="{esc(key)}">{esc(label or topics[key]["name"])}</a>'


def source_url(data: dict, key: str, ref: str) -> str:
    return f'https://github.com/{data["meta"]["repository"]}/blob/{ref}/{quote(data["sources"][key]["path"], safe="/")}'


def detail_html(key: str, topic: dict, data: dict, ref: str) -> str:
    sources = ''.join(f'<a href="{esc(source_url(data, s, ref))}" target="_blank" rel="noopener noreferrer">{esc(data["sources"][s]["path"])} ↗</a>' for s in topic['sources'])
    deps = ' · '.join(target_link(dep, data['topics']) for dep in topic.get('depends_on', []))
    return (f'<h3>Recorded evidence</h3><p>{esc(topic["evidence"])}</p>'
            f'<h3>Evidence boundary</h3><p class="boundary">{esc(topic["boundary"])}</p>'
            f'<h3>Next useful action</h3><p class="next-step">{esc(topic["next"])}</p>'
            + (f'<h3>Related prerequisites</h3><p>{deps}</p>' if deps else '')
            + f'<h3>Sources · repository snapshot</h3><div class="sources">{sources}</div>')


def current_ref(data: dict, root: Path) -> str:
    candidate = os.environ.get('GITHUB_SHA', '')
    if not SHA_RE.fullmatch(candidate):
        try:
            candidate = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], stderr=subprocess.DEVNULL, text=True).strip()
        except (OSError, subprocess.CalledProcessError):
            candidate = data['meta']['source_ref']
    return candidate if SHA_RE.fullmatch(candidate) else data['meta']['source_ref']


def render(data: dict, warnings: list[str], ref: str) -> str:
    topics = data['topics']
    focus = ''.join(f'<article class="focus-card{ " first" if i == 0 else ""}"><div class="eyebrow">{esc(lane["label"])}</div><h2>{esc(lane["title"])}</h2><p>{esc(lane["summary"])}</p><div class="jump">{target_link(lane["target"], topics, "Inspect the evidence →")}</div></article>' for i, lane in enumerate(data['lanes']))
    rows, noscript, details = [], [], {}
    memberships = {key: [] for key in topics}
    for code, course in data['courses'].items():
        for week in course['weeks']:
            for key in week['anchors'] + week['remaining']:
                if code not in memberships[key]: memberships[key].append(code)
    active = set()
    for lane in data['lanes']:
        active.add(lane['target'])
        for task in lane['tasks']: active.update(task['topics'])
    for key, topic in topics.items():
        details[key] = {'title': topic['name'], 'area': topic['area'], 'html': detail_html(key, topic, data, ref)}
        text = ' '.join([topic['name'], topic['area'], topic['evidence'], topic['next'], *memberships[key]]).casefold()
        kind = 'independent' if topic['performance'] == 'independent' else 'future' if topic['concept'] == 'planned' else 'historical' if topic['review'] == 'diagnostic' else 'practice' if topic['action'] in {'build', 'practice'} else 'other'
        review = REVIEW[topic['review']] + (f' · {topic["evidence_on"]}' if topic['evidence_on'] else '')
        rows.append(f'''<tr data-id="{key}" data-search="{esc(text)}" data-area="{esc(topic['area'])}" data-kind="{kind}" data-focus="{str(key in active).lower()}">
<td><a class="topic-button" href="#record-{key}" data-open="{key}">{esc(topic['name'])}</a><div class="topic-sub">{esc(topic['area'])}</div></td>
<td data-label="Concept">{badge(CONCEPT[topic['concept']], 'green' if topic['concept']=='demonstrated' else 'muted' if topic['concept'] in {'planned','unknown'} else 'blue')}</td>
<td data-label="Performance">{badge(PERFORMANCE[topic['performance']], 'green' if topic['performance']=='independent' else 'muted' if topic['performance'] in {'pending','unknown'} else 'blue')}</td>
<td data-label="Recency"><span class="date" data-event="{esc(topic['evidence_on'] or '')}">{esc(review)}</span></td>
<td data-label="Next action">{badge(ACTIONS[topic['action']], 'amber' if topic['action'] in {'build','practice'} else 'muted' if topic['action'] in {'maintain','learn'} else 'blue')}</td>
<td><a class="arrow" href="#record-{key}" data-open="{key}" aria-label="Details for {esc(topic['name'])}">↗</a></td></tr>''')
        noscript.append(f'<article id="record-{key}"><h2>{esc(topic["name"])}</h2>{details[key]["html"]}</article>')
    courses = []
    for code, course in data['courses'].items():
        weeks = []
        for week in course['weeks']:
            anchors = ' · '.join(target_link(t, topics) for t in week['anchors']) or 'No specific evidence mapped'
            remaining = ' · '.join(target_link(t, topics) for t in week['remaining']) or 'See the scope note; no completeness claim'
            due = f'<p>Confirmed date: {esc(week["due_on"])}</p>' if week.get('due_on') else ''
            weeks.append(f'<div class="requirement"><div class="week">{esc(week["week"])}</div><div><div class="req-title"><b>{esc(week["title"])}</b>{badge(SCOPES[week["scope"]], "muted")}</div><p><strong>Anchors:</strong> {anchors}</p><p><strong>Work / checks:</strong> {remaining}</p><p>{esc(week["note"])}</p>{due}</div></div>')
        more = f'<details><summary>Show {len(weeks)-3} more syllabus entries</summary>{"".join(weeks[3:])}</details>' if len(weeks)>3 else ''
        courses.append(f'<article class="course"><div class="course-top"><div class="eyebrow">{esc(code)}</div><h3>{esc(course["name"])}</h3><p>{esc(course["timing"])}</p></div>{"".join(weeks[:3])}{more}</article>')
    lanes = []
    for lane in data['lanes']:
        tasks = ''.join(f'<div class="task"><h4>{esc(task["title"])}</h4><p>{esc(task["detail"])}</p><p class="task-links">{" · ".join(target_link(t, topics) for t in task["topics"])}</p>{badge(task["when"], "muted")}</div>' for task in lane['tasks'])
        lanes.append(f'<article class="queue-col"><div class="eyebrow">{esc(lane["label"])}</div><h3>{esc(lane["title"])}</h3><p>{esc(lane["summary"])}</p>{tasks}</article>')
    paths = ''.join(f'<article><h3>{esc(route["title"])}</h3><p>{" → ".join(target_link(t, topics) for t in route["topics"])}</p><p class="footnote">{esc(route["note"])}</p></article>' for route in data.get('paths', []))
    timeline = ''.join(f'<p><strong>{esc(item["label"])}</strong> — {esc(item["detail"])}</p>' for item in data.get('timeline', []))
    payload = {'details': details, 'meta': data['meta'], 'warnings': warnings}
    safe_json = json.dumps(payload, ensure_ascii=True).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    replacements = {'TITLE':esc(data['meta']['title']), 'SUBTITLE':esc(data['meta']['subtitle']), 'REVIEWED':esc(data['meta']['reviewed_on']), 'THROUGH':esc(data['meta']['evidence_through']), 'REVIEW_NOTE':esc(data['meta']['review_note']), 'REF':ref[:7], 'REPO_URL':f'https://github.com/{data["meta"]["repository"]}/tree/{ref}', 'FOCUS':focus, 'ROWS':''.join(rows), 'COUNT':str(len(topics)), 'AREAS':''.join(f'<option>{esc(area)}</option>' for area in sorted({t['area'] for t in topics.values()})), 'COURSES':''.join(courses), 'LANES':''.join(lanes), 'PATHS':paths, 'TIMELINE':timeline, 'NOJS_DETAILS':''.join(noscript), 'DATA':safe_json, 'QUALITY':f'{len(warnings)} record warning(s)' if warnings else 'Source checks passed', 'WARNINGS':''.join(f'<p>{esc(w)}</p>' for w in warnings) or '<p>Source references and reviewed hashes match this checkout. This checks record integrity, not the truth of every learning claim or your current retention.</p>'}
    template = (ROOT/'dashboard/template.html').read_text(encoding='utf-8')
    # Replace only known template tokens, never arbitrary double braces in source text.
    return SOURCE_TOKENS.sub(lambda m: replacements.get(m[0][2:-2], m[0]), template)


def build(data_path: Path = DATA_PATH, output: Path = SITE_DIR, *, source_root: Path | None = ROOT) -> Path:
    data = yaml.safe_load(data_path.read_text(encoding='utf-8'))
    warnings = validate(data, source_root)
    if source_root is None:
        warnings.append('Local preview: filesystem source verification was not run. Production builds verify all source paths and hashes.')
    ref = current_ref(data, source_root or ROOT)
    html = render(data, warnings, ref)
    output.mkdir(parents=True, exist_ok=True)
    for filename, token in [('styles.css', '{{STYLE}}'), ('app.js', '{{SCRIPT}}')]:
        raw = (ROOT/'dashboard/static'/filename).read_bytes()
        name = f'{Path(filename).stem}.{sha256(raw).hexdigest()[:12]}{Path(filename).suffix}'
        (output/name).write_bytes(raw)
        html = html.replace(token, name)
    require(not SOURCE_TOKENS.search(html), 'Unreplaced template token')
    target = output/'index.html'
    target.write_text(html, encoding='utf-8')
    (output/'.nojekyll').write_text('')
    for message in warnings:
        print(f'WARNING: {message}')
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=SITE_DIR)
    args = parser.parse_args()
    print(f'Built dashboard: {build(output=args.output)}')
