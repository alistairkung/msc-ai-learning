"""Schema, source integrity, safe rendering and curriculum regression checks."""
from copy import deepcopy
import json
from pathlib import Path
import re

import pytest
import yaml

from dashboard.build import (ROOT, DATA_PATH, blob_sha, build, render,
                             source_path, validate)


@pytest.fixture
def data():
    return yaml.safe_load(DATA_PATH.read_text(encoding='utf-8'))


def test_real_schema(data):
    assert validate(data, root=None) == []


def test_repository_source_files_exist(data):
    # CI runs this against the real checkout, never substitute generated fixtures.
    validate(data, root=ROOT)  # source drift warns; missing source paths fail


@pytest.mark.parametrize('field,value', [
    ('concept', 'mastered'), ('performance', 'perfect'),
    ('review', 'overdue_forever'), ('action', 'panic')])
def test_invalid_states_rejected(data, field, value):
    data['topics']['bfs'][field] = value
    with pytest.raises(ValueError, match=f'invalid {field}'):
        validate(data, root=None)


@pytest.mark.parametrize('path', [
    '../outside.md', '/tmp/outside.md', 'x/../../file.md', 'x\\file.md',
    '.env', 'LEARNER_PROFILE.md', 'notes/learner_profile.md',
    'https://example.com/file.md', 'notes/.private/file.md'])
def test_private_and_unsafe_sources_forbidden(path):
    with pytest.raises(ValueError):
        source_path(path)


def test_bad_source_reference(data):
    data['topics']['bfs']['sources'] = ['nonexistent']
    with pytest.raises(ValueError, match='sources'):
        validate(data, root=None)


def test_missing_course_requirement(data):
    data['courses']['AIMS5704']['weeks'][4]['remaining'] = ['untracked_theory']
    with pytest.raises(ValueError, match='missing topic'):
        validate(data, root=None)


def test_missing_week_rejected(data):
    data['courses']['AIMS5702']['weeks'].pop()
    with pytest.raises(ValueError, match='syllabus coverage'):
        validate(data, root=None)


def test_duplicate_week_rejected(data):
    data['courses']['AIMS5702']['weeks'].append(deepcopy(data['courses']['AIMS5702']['weeks'][0]))
    with pytest.raises(ValueError, match='syllabus coverage'):
        validate(data, root=None)


def test_curriculum_coverage_cannot_shrink_by_changing_metadata(data):
    for code, count in [('AIMS5701', 12), ('AIMS5702', 12), ('AIMS5704', 13)]:
        assert [w['week'] for w in data['courses'][code]['weeks']] == list(map(str, range(1, count+1)))
        section = re.split(r'^# ', (ROOT/'MSC_SYLLABUS_MAP.md').read_text(), flags=re.M)
        section = next(s for s in section if s.startswith(code + ' '))
        assert set(re.findall(r'^\| W(\d+) \|', section, flags=re.M)) == set(map(str, range(1, count+1)))


def test_new_theory_is_an_explicit_requirement(data):
    weeks = {w['week']: w for w in data['courses']['AIMS5704']['weeks']}
    assert 'mle' in weeks['2']['remaining']
    assert 'exponential_families' in weeks['2']['remaining']
    assert 'convergence' in weeks['5']['remaining']
    assert 'adaptive_optimisation' in weeks['6']['remaining']
    for key in ['mle', 'convergence', 'adaptive_optimisation']:
        assert data['topics'][key]['concept'] == 'planned'
        assert data['topics'][key]['review'] == 'not_due'


def test_unknown_is_not_failed_and_overview_is_not_a_backlog(data):
    for key in ['markov', 'poisson']:
        assert data['topics'][key]['concept'] == 'unknown'
        assert data['topics'][key]['review'] == 'diagnostic'
    entries = data['courses']['FTEC5660']['weeks']
    assert next(w for w in entries if w['week'] == 'Later')['scope'] == 'overview'
    assert 'other_agents' in data['courses']['AIMS5701']['weeks'][1]['remaining']


def test_original_topic_ids_preserved(data):
    old = {'python_fluency','dsa_patterns','numpy','pandas','linear_algebra','calculus',
           'scientific_python','probability','linear_regression','logistic_regression',
           'evaluation','decision_trees','random_forests','bayesian_networks','hmm',
           'particle_filtering','bfs','dfs','astar','ucs','logic','tensor_operations',
           'autograd','pytorch_training','mlp_classification','real_data_classification',
           'neural_regression','cnn','rnn'}
    assert old <= data['topics'].keys()


def test_actual_event_dates_preserved(data):
    assert data['topics']['bfs']['evidence_on'] == '2026-09-06'
    assert data['topics']['prompt_chaining']['evidence_on'] == '2026-09-08'
    assert data['topics']['bayes']['evidence_on'] is None
    assert data['topics']['real_data_classification']['performance'] != 'independent'


def test_future_date_rejected(data):
    data['topics']['bfs']['evidence_on'] = '2099-01-01'
    with pytest.raises(ValueError, match='cutoff'):
        validate(data, root=None)


def test_dated_evidence_needs_date(data):
    data['topics']['bfs']['evidence_on'] = None
    with pytest.raises(ValueError, match='needs a date'):
        validate(data, root=None)


def test_planned_topic_cannot_be_overdue(data):
    data['topics']['mle']['review'] = 'diagnostic'
    with pytest.raises(ValueError, match='untaught'):
        validate(data, root=None)


def test_cycle_rejected(data):
    data['topics']['bfs']['depends_on'] = ['astar']
    with pytest.raises(ValueError, match='cycle'):
        validate(data, root=None)


def test_three_parallel_lanes_required(data):
    data['lanes'].pop()
    with pytest.raises(ValueError, match='three'):
        validate(data, root=None)


def test_source_changes_warn_without_mutating_learning(data, tmp_path):
    for source in data['sources'].values():
        p = tmp_path/source['path']; p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('fixture source\n')
        source['sha'] = blob_sha(p)
    original = deepcopy(data['topics'])
    assert validate(data, root=tmp_path) == []
    (tmp_path/data['sources']['search']['path']).write_text('changed fixture\n')
    warnings = validate(data, root=tmp_path)
    assert len(warnings) == 1 and 'changed' in warnings[0]
    assert data['topics'] == original


def test_missing_source_fails(data, tmp_path):
    with pytest.raises(ValueError, match='Missing/unsafe source'):
        validate(data, root=tmp_path)


def test_render_escapes_text_and_json(data):
    attack = '</script><script>alert("x")</script><img src=x onerror=alert(1)>'
    data['topics']['bfs']['name'] = attack
    data['topics']['bfs']['evidence'] = attack
    html = render(data, [], data['meta']['source_ref'])
    assert attack not in html
    assert '&lt;/script&gt;' in html
    raw = re.search(r'<script type="application/json" id="atlas-data">(.*?)</script>', html, re.S)[1]
    assert json.loads(raw)['details']['bfs']['title'] == attack
    assert '\\u003c' in raw


def test_build_has_hashed_assets_and_fallback(tmp_path):
    page = build(output=tmp_path, source_root=None)
    html = page.read_text()
    assert '<h1>What you know. What needs work.</h1>' in html
    assert '{{' not in html
    assert 'filesystem source verification was not run' in html
    for name in re.findall(r'(?:href|src)="((?:styles|app)\.[a-f0-9]{12}\.(?:css|js))"', html):
        assert (tmp_path/name).is_file()
    assert len(list(tmp_path.glob('styles.*.css'))) == 1
    assert len(list(tmp_path.glob('app.*.js'))) == 1
    assert '<noscript>' in html
    assert 'id="record-bfs"' in html
    assert 'data-view="queue"' in html
    assert 'Grade' not in html
    assert (tmp_path/'.nojekyll').is_file()


def test_code_does_not_average_or_minimise_readiness():
    source = (ROOT/'dashboard/build.py').read_text()
    assert 'overall_status' not in source
    assert 'STATUS_ORDER' not in source


def test_review_metadata_is_not_future_evidence(data):
    assert data['meta']['reviewed_on'] >= data['meta']['evidence_through']
    assert data['topics']['bfs']['performance'] == 'independent'
    assert data['topics']['ucs']['performance'] == 'pending'
