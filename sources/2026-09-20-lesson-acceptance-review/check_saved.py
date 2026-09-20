"""Read-only audit of the published pilot; stdout only, no model calls.

Run with uv run check_saved.py /path/to/lesson-acceptance.
Uses the study's inspected fixture generator, but independent execution and grading.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys

sys.dont_write_bytecode = True
study = Path(sys.argv[1]).resolve()
evidence = study / 'evidence/pilot-v1'
spec = importlib.util.spec_from_file_location('fixtures', study / 'scripts/pilot.py')
fixtures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixtures)


def read(path):
    return json.loads(path.read_text())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def truth(key, rows):
    parents, children, others = ('customers', 'invoices', 'payments') if key == 'billing' else ('events', 'registrations', 'tags')
    totals = {row[0]: [row[0], row[1], 0, 0] for row in rows[parents]}
    for _, parent, amount, status in rows[children]:
        if (status != 'void') if key == 'billing' else (status == 'confirmed'):
            totals[parent][2] += amount
    for _, parent, value in rows[others]:
        totals[parent][3] += value if key == 'billing' else 1
    return [totals[parent] for parent in sorted(totals)]


executions = 0


def execute(schema, rows, sql):
    global executions
    executions += 1
    db = sqlite3.connect(':memory:')
    try:
        db.executescript(schema)
        for table, data in rows.items():
            if data:
                db.executemany(f'INSERT INTO "{table}" VALUES ({",".join("?" for _ in data[0])})', data)
        db.execute('PRAGMA query_only = ON')
        return [list(row) for row in db.execute(sql)]
    finally:
        db.close()


calls = {p.stem: read(p) for p in sorted((evidence / 'calls').glob('*.json'))}
for name, record in calls.items():
    if 'request_sha256' in record:
        assert record['request_sha256'] == hashlib.sha256(json.dumps(record['request'], sort_keys=True).encode()).hexdigest(), name
    assert record['text'] == record['response']['choices'][0]['message']['content'], name


def cost(names):
    selected = [calls[name] for name in names]
    return {
        'calls': len(selected),
        'prompt_tokens': sum(r['response']['usage']['prompt_tokens'] for r in selected),
        'completion_tokens': sum(r['response']['usage']['completion_tokens'] for r in selected),
        'model_seconds': round(sum(r['wall_seconds'] for r in selected), 6),
    }


sources = {key: read(evidence / f'{key}-source.json') for key in fixtures.HISTORIES}
policies = {key: read(evidence / f'{key}-27b.json') for key in sources}
source_probe = []
for key, source in sources.items():
    assert source['proposal'] == calls[f'{key}-proposal']['text']
    assert source['query'] == fixtures.sql(calls[f'{key}-source']['text'])
    for arm in ('cheap', 'paid'):
        assert policies[key][arm] == calls[f'{key}-{arm}-27b-direct']['text']
    for split, rows in [('source', source['task']['rows']), ('probe', policies[key]['probe']['rows'])]:
        actual = execute(source['task']['schema'], rows, source['query'])
        saved = source['execution'] if split == 'source' else policies[key]['probe']['execution']
        assert actual == saved['rows']
        source_probe.append({'history': key, 'split': split, 'actual': actual, 'expected': truth(key, rows), 'pass': actual == truth(key, rows)})

grades = []
normalize = lambda sql: re.sub(r'\s+', ' ', sql.strip().rstrip(';').lower())
saved_offline = read(evidence / 'offline-verification.json')
offline_checks = {r['file']: r for r in saved_offline['final_checks']}
saved_fixed = {(r['history'], r['seed'], r['arm']): r for r in saved_offline['fixed_program_replay']}
for path in sorted((evidence / 'grades').glob('*.json')):
    record = read(path)
    key, seed, arm = record['history'], record['seed'], record['arm']
    source, policy = sources[key], policies[key]
    schema = source['task']['schema']
    assert record['input'] == fixtures.fresh(key, seed)
    reference = truth(key, record['input'])
    assert reference == record['expected']
    row = {'case': path.stem, 'arm': arm}
    for stage, call_stage in [('initial', 'initial'), ('final', 'revision')]:
        call = calls[f'final-{key}-{seed}-{arm}-{call_stage}']
        assert record[f'{stage}_sql'] == fixtures.sql(call['text'])
        actual = execute(schema, record['input'], record[f'{stage}_sql'])
        assert actual == record[f'{stage}_execution']['rows']
        row[stage] = actual == reference
        assert row[stage] == record[f'{stage}_pass']
        request = call['request']
        assert request['model'] == 'docker.io/ai/qwen3.8:27b-q4_K_M'
        assert request['temperature'] == 0 and request['max_tokens'] == 4096
        assert request['chat_template_kwargs'] == {'enable_thinking': False}
        prompt = request['messages'][1]['content']
        retained = json.loads(prompt.split('Retained experience (may contain errors; use critically):\n', 1)[1].split('\nNew complete task:', 1)[0])
        assert retained['retained_source'] == {k: v for k, v in source.items() if k != 'proposal'}
        if arm != 'raw':
            assert retained['original_proposals'] == source['proposal']
            assert retained['acceptance'] == policy[arm]
        assert ('paid_evidence' in retained) == (arm == 'paid')
        if arm == 'paid':
            assert retained['paid_evidence'] == policy['probe']
    behavior = []
    for extra_seed in (907, 911):
        rows = fixtures.fresh(key, extra_seed)
        behavior.append(execute(schema, rows, record['final_sql']) == truth(key, rows))
    assert behavior == offline_checks[path.name]['independent_behavior_pass']
    row['both_behavior_checks'] = all(behavior)
    blocks = re.findall(r'```(?:sql|sqlite)\s*(.*?)```', policy.get(arm, ''), re.S)
    query = source['query'] if arm == 'raw' else blocks[-1].strip().rstrip(';')
    row['fixed_program'] = execute(schema, record['input'], query) == reference
    assert row['fixed_program'] == saved_fixed[(key, seed, arm)]['pass']
    row['initial_matches_source'] = normalize(record['initial_sql']) == normalize(source['query'])
    row['changed_in_revision'] = normalize(record['initial_sql']) != normalize(record['final_sql'])
    grades.append(row)

manifest = read(evidence / 'instrument-evaluate-1789862545843012000.json')
assert hashlib.sha256(manifest['source_snapshot'].encode()).hexdigest() == manifest['sha256']
for name, expected_hash in manifest['protocol_hashes'].items():
    assert digest(study / 'protocols' / name) == expected_hash
latest_review = max(r['response']['created'] for name, r in calls.items() if name.endswith('-27b-direct'))
earliest_final = min(r['response']['created'] for name, r in calls.items() if name.startswith('final-'))
assert latest_review < manifest['start_unix'] < earliest_final

deployments = {}
for arm in ('raw', 'cheap', 'paid'):
    setup = [f'{key}-source' for key in sources]
    if arm != 'raw':
        setup += [f'{key}-proposal' for key in sources] + [f'{key}-{arm}-27b-direct' for key in sources]
    deployments[arm + '_reader'] = cost(setup + [name for name in calls if name.startswith('final-') and f'-{arm}-' in name])
    deployments[arm + '_fixed'] = cost(setup)

metrics = ('initial', 'final', 'both_behavior_checks', 'fixed_program', 'initial_matches_source', 'changed_in_revision')
result = {
    'study_revision': subprocess.check_output(['git', '-C', str(study), 'rev-parse', 'HEAD'], text=True).strip(),
    'sqlite_version': sqlite3.sqlite_version,
    'sql_executions': executions,
    'outcomes': {arm: {metric: sum(r[metric] for r in grades if r['arm'] == arm) for metric in metrics} for arm in ('raw', 'cheap', 'paid')},
    'source_probe': source_probe,
    'grades': grades,
    'deployment_costs': deployments,
    'actual_response_artifact_costs': cost(calls),
    'empty_content_responses': [name for name, r in calls.items() if not r['text'].strip()],
    'interruptions': {p.name: read(p) for p in evidence.glob('*serving-interruption*.json')},
    'chronology': {'latest_curation_response_created': latest_review, 'evaluation_start': manifest['start_unix'], 'earliest_final_response_created': earliest_final},
    'checks': {'request_hashes': sum('request_sha256' in r for r in calls.values()), 'early_requests_without_saved_hash': sum('request_sha256' not in r for r in calls.values()), 'final_requests_source_parity_and_controls': 36, 'protocol_hashes': len(manifest['protocol_hashes']), 'model_calls_launched': 0},
    'study_file_sha256': {str(p.relative_to(study)): digest(p) for p in sorted(study.rglob('*')) if p.is_file() and (p.is_relative_to(evidence) or p.is_relative_to(study / 'scripts') or p.is_relative_to(study / 'protocols') or p.name in ('README.md', 'AGENTS.md', 'pilot-v1.md')) and '.git' not in p.parts},
}
print(json.dumps(result, indent=2))
