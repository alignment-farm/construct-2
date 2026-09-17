"""Rescore the pinned evidence-use publication without importing its implementation."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import subprocess

PIN = 'da1233fdfb26fe6c5daa337a3dbf9f784f34f9f7'


def answer(prompt):
    lines = prompt.splitlines()
    at = next(i for i, x in enumerate(lines) if x.startswith('CURRENT='))
    current = json.loads(lines[at][8:])
    request = json.loads(next(x[8:] for x in lines[at + 1:] if x.startswith('REQUEST=')))
    rule = current['policy'][current['bindings'][request['entity']]]
    cap = rule['urgent_cap' if request['urgent'] else 'cap']
    allocated = min(cap, request['stock'], request['request'])
    surcharge = rule['surcharge'] if request['urgent'] and not request['waived'] else 0
    return [allocated, allocated * rule['price'] + surcharge if allocated else 0,
            rule['lane'] if allocated else 'NONE', request['stock'] - allocated]


def complete(raw, target):
    try:
        value = json.loads(raw)
    except ValueError:
        return False
    return (isinstance(value, list) and len(value) == 4
            and all(type(value[i]) is int for i in (0, 1, 3))
            and isinstance(value[2], str) and value == target)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert subprocess.check_output(['git', '-C', str(args.study), 'rev-parse', 'HEAD'], text=True).strip() == PIN
    hashes, runs, saved = {}, [], {}

    def read(rel):
        data = (args.study / rel).read_bytes()
        hashes[rel] = hashlib.sha256(data).hexdigest()
        return data

    for name, analysis in [('development-v2', 'development-v2-analysis-v2'),
                           ('order-diagnostic-v1', 'order-diagnostic-v1-analysis'),
                           ('fresh-v1', 'fresh-v1-analysis')]:
        rel = f'evidence/{name}/'
        manifest_hashes = json.loads(read(rel + 'hashes.json'))
        for file, expected in manifest_hashes.items():
            assert hashlib.sha256(read(rel + file)).hexdigest() == expected, file
        rows = [json.loads(x) for x in read(rel + 'events.jsonl').splitlines()]
        workload = json.loads(read(rel + 'workload.json'))
        report = json.loads(read(f'evidence/{analysis}/report.json'))
        groups = defaultdict(dict)
        for row in rows:
            if row['kind'] in ('generation', 'update'):
                expected = answer(row['prompt'])
                target = json.loads(row['target']) if row['kind'] == 'update' else row['target']
                assert expected == target
            if row['kind'] in ('generation', 'recall'):
                assert complete(row['raw'], row['target']) == row['complete']
            if row['kind'] == 'generation':
                groups[row['arm'], row['step'], row['version']][row['case']] = row
            if row['kind'] == 'executable':
                case = next(c for c in workload['cases'] if c['id'] == row['case'])
                prompt = 'CURRENT=' + json.dumps({'policy': workload['policies'][row['version']], 'bindings': case['bindings']})
                prompt += '\nREQUEST=' + json.dumps(case['request'])
                assert row['complete'] and answer(prompt) == row['result'] == row['target']
        for table in report['tables']:
            group = groups[table['arm'], table['step'], table['version']]
            assert len(group) == table['n'] == 32
            assert sum(r['complete'] for r in group.values()) == table['correct']
        for trajectory in report['candidate_trajectories']:
            uses = [r for r in rows if r['kind'] == 'generation' and r['arm'] == trajectory['arm'] and r['step'] == trajectory['step']]
            updates = [r for r in rows if r['kind'] == 'update' and r['arm'] == trajectory['arm'] and r['step'] <= trajectory['step']]
            assert sum(r['complete'] for r in uses) == trajectory['correct']
            assert abs(sum(r['seconds'] for r in uses + updates) - trajectory['total_active_seconds']) < 1e-8
        for arm in workload['histories']:
            updates = [r for r in rows if r['kind'] == 'update' and r['arm'] == arm]
            assert sorted(r['history_index'] for r in updates) == list(range(256))
        train_requests = {json.dumps(h['case']['request'], sort_keys=True) for history in workload['histories'].values() for h in history}
        assert not train_requests & {json.dumps(c['request'], sort_keys=True) for c in workload['cases']}
        runs.append({'run': name, 'checked': dict(Counter(r['kind'] for r in rows)),
                     'trajectories': report['candidate_trajectories']})
        saved[name] = (rows, groups, workload)

    blocked, shuffled = saved['development-v2'][0], saved['order-diagnostic-v1'][0]
    updates = lambda rows: Counter((r['prompt'], r['target']) for r in rows if r['kind'] == 'update' and r['arm'] == 'varied')
    controls = lambda rows: {(r['arm'], r['version'], r['case']): r['raw'] for r in rows if r['kind'] == 'generation' and r['arm'] in ('base', 'lesson-varied')}
    assert updates(blocked) == updates(shuffled)
    assert controls(blocked) == controls(shuffled)
    initial = lambda run: json.loads(read(f'evidence/{run}/initial.json'))
    assert initial('development-v2') == initial('order-diagnostic-v1')
    assert initial('fresh-v1')['adapter_digest'] != initial('development-v2')['adapter_digest']
    for file in ['protocol/development-v1.md', 'protocol/order-diagnostic-v1.md', 'protocol/final-v1.md', 'notes/final-decision.md']:
        assert read(file) == subprocess.check_output(['git', '-C', str(args.study), 'show', f'8e93219:{file}'])

    rows, groups, workload = saved['fresh-v1']
    paired, retention, endpoints = [], [], []
    for arm, step in sorted({(arm, step) for arm, step, _ in groups}):
        for version in range(3):
            group = groups[arm, step, version]
            rebound = {c['id'] for c in workload['cases'] if c['fresh'] and c['bindings'][c['request']['entity']] != workload['histories']['stable'][0]['case']['bindings'][c['request']['entity'].replace('_new_', '_old_')]}
            assert len(rebound) == 8
            fresh = {c['id'] for c in workload['cases'] if c['fresh']}
            endpoints.append({'arm': arm, 'step': step, 'version': version,
                              'complete': sum(r['complete'] for r in group.values()),
                              'fresh': sum(group[k]['complete'] for k in fresh),
                              'rebound': sum(group[k]['complete'] for k in rebound)})
            if (arm, step) == ('varied', 128):
                for reference in ['base', 'lesson-stable', 'lesson-varied']:
                    ref = groups[reference, 0, version]
                    paired.append({'version': version, 'reference': reference,
                                   'gained': sum(r['complete'] and not ref[k]['complete'] for k, r in group.items()),
                                   'lost': sum(not r['complete'] and ref[k]['complete'] for k, r in group.items())})
            if version:
                before = groups[arm, step, version - 1]
                assert all(r['changed'] == (r['target'] != before[k]['target']) for k, r in group.items())
                eligible = [r for k, r in group.items() if not r['changed'] and before[k]['complete']]
                retention.append({'arm': arm, 'step': step, 'version': version,
                                  'previously_correct_unchanged': len(eligible),
                                  'retained': sum(r['complete'] for r in eligible),
                                  'changed': sum(r['changed'] for r in group.values()),
                                  'changed_correct': sum(r['changed'] and r['complete'] for r in group.values())})
    out = {'reviewed_revision': PIN, 'runs': runs, 'fresh_endpoints': endpoints,
           'fresh_retention': retention, 'varied128_paired': paired,
           'development_order_controls_equal': True, 'protocols_precede_fresh_run': True,
           'fresh_initialization_differs': True, 'source_sha256': hashes,
           'limits': 'Independent saved-text scoring and accounting; no model, tokenizer, gradient, reload or causal mechanism reproduction.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'runs_checked': [{k: v for k, v in r.items() if k != 'trajectories'} for r in runs],
                      'fresh_endpoints': endpoints, 'varied128_paired': paired}, indent=2))


if __name__ == '__main__':
    main()
