"""Replay published actions in disposable workspaces; no model loading or training.

Usage: uv run --no-project --python 3.13.12 python review.py SNAPSHOT OUTPUT
SNAPSHOT must be an archive of study revision 523eb3f, not a running checkout.
"""
import argparse
import collections
import hashlib
import json
import platform
import re
import subprocess
import sys
import tempfile
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('snapshot', type=Path)
p.add_argument('output', type=Path)
a = p.parse_args()
snapshot = a.snapshot.resolve()
evidence = snapshot / 'evidence/continuation-02'
sys.path.insert(0, str(snapshot / 'scripts'))
from continuation_runtime import Environment, parse, render
from continuation_evaluate import evaluate
from workload import write_workspace, source_hash


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def lines(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def tree(path):
    return {str(f.relative_to(path)): digest(f) for f in sorted(path.rglob('*')) if f.is_file() and '__pycache__' not in f.parts}


def stable(value):
    if isinstance(value, dict):
        return {k: stable(v) for k, v in value.items() if k != 'seconds'}
    if isinstance(value, list):
        return [stable(v) for v in value]
    if isinstance(value, str):
        value = re.sub(r'Ran (\d+) tests? in [\d.]+s', r'Ran \1 tests in TIME', value)
        return re.sub(r'File "[^"\n]*/tests/test_public.py"', 'File "WORKSPACE/tests/test_public.py"', value)
    return value


invalid = {'ok': False, 'error': 'Expected exactly one complete JSON action; nothing executed.'}
manifest = read(evidence / 'artifact-manifest.json')['files']
manifest_errors = [name for name, item in manifest.items()
                   if not (snapshot / name).is_file() or digest(snapshot / name) != item['sha256']
                   or (snapshot / name).stat().st_size != item['bytes']]
assert not manifest_errors, manifest_errors
report = {'reviewed_revision': '523eb3fb8aa56fed0ffdfe10f6b1f1cb3002ade6',
          'python': sys.version, 'platform': platform.platform(),
          'manifest': {'files_verified': len(manifest), 'errors': manifest_errors},
          'runs': {}, 'paired_checks': [], 'limitations': [
              'Published actions replayed; model generation, training and state isolation not rerun.',
              'Study Python 3.14.7; root replay Python 3.13.12. Elapsed seconds, unittest timing and absolute test traceback paths normalized.',
              'External checks reused from study after source inspection; root added one rename value-preservation probe.',
              'Token totals sum saved participant token fields, without retokenization.',
              'Fresh confirmation material not executed or used to select an intervention.']}
saved_evaluation = read(evidence / 'evaluation.json')
source_initial = {}
all_model = []
all_tools = []
all_summaries = []
replay_results = 0
with tempfile.TemporaryDirectory(prefix='construct-investigation-review-') as td:
    temporary = Path(td)
    for run in sorted((evidence / 'runs').iterdir()):
        if not (run / 'summary.json').exists():
            continue
        name = run.name
        task = next((t for t in ['dev-normalization', 'dev-execution', 'dev-filter-fresh'] if name.startswith(t)), 'dev-filter-fresh')
        saved_workspace = evidence / 'workspaces' / name
        workspace = temporary / name
        write_workspace(workspace, task, history=saved_workspace / 'history')
        assert (workspace / 'TASK.md').read_bytes() == (saved_workspace / 'TASK.md').read_bytes()
        assert tree(workspace / 'tests') == tree(saved_workspace / 'tests')
        env = Environment(workspace)
        events = lines(run / 'events.jsonl')
        provenance = next(e for e in events if e['kind'] == 'provenance')
        source_initial[name] = source_hash(workspace)
        assert source_initial[name] == provenance['initial_source_hash']
        transcript = ''
        pending = None
        models = []
        tools = []
        injected = 0
        for event in events:
            kind = event['kind']
            if kind == 'model':
                assert pending is None
                assert render((workspace / 'TASK.md').read_text(), transcript) == event['prompt'], (name, event['turn'], 'prompt')
                assert parse(event['raw']) == event['action']
                pending = event
                models.append(event)
            elif kind in ['tool', 'injected_prefix']:
                raw = event['raw'] if kind == 'injected_prefix' else pending['raw']
                action = event['action']
                assert parse(raw) == action
                actual = env.call(action) if action else invalid.copy()
                assert stable(actual) == stable(event['result']), (name, event.get('turn'), actual, event['result'])
                replay_results += 1
                transcript += '\nASSISTANT: ' + raw + '\nTOOL: ' + json.dumps(event['result'], sort_keys=True)
                if kind == 'injected_prefix':
                    injected += 1
                else:
                    assert pending['turn'] == event['turn'] and pending['action'] == action
                    tools.append(event)
                    pending = None
        assert pending is None
        summary = read(run / 'summary.json')
        assert summary['turns'] == len(models) and summary['tool_calls'] == env.calls
        assert source_hash(workspace) == summary['source_hash'] == digest(run / 'submitted.py') == digest(saved_workspace / 'etl_pipeline.py')
        evaluation = evaluate(workspace)
        assert stable(evaluation) == stable(saved_evaluation[name]), (name, 'evaluation mismatch')
        actions = collections.Counter((e['action'] or {}).get('action', 'invalid') for e in tools)
        probes = [e for e in tools if (e['action'] or {}).get('action') == 'probe']
        history_access = [e for e in tools if (e['action'] or {}).get('action') == 'history_search' or
                          ((e['action'] or {}).get('action') in ['read', 'search'] and
                           ('history' in (e['action'] or {}).get('path', '') or (e['action'] or {}).get('path') == '.'))]
        report['runs'][name] = {'score': evaluation['passed'], 'total': evaluation['total'],
                               'public_passed': evaluation['public']['returncode'] == 0,
                               'actions': dict(actions), 'injected_prefix_turns': injected,
                               'application_successful_probes': sum(bool(e['result'].get('application_ok')) for e in probes),
                               'passed_assertions': sum(e['result'].get('assertion_passed') is True for e in probes),
                               'failed_assertions': sum(e['result'].get('assertion_passed') is False for e in probes),
                               'history_accesses': len(history_access),
                               'source_sha256': summary['source_hash'], 'status': summary['status']}
        all_model += models
        all_tools += tools
        all_summaries.append(summary)
    for pair in read(evidence / 'analysis.json')['paired_state_checks']:
        left, right = pair['names']
        lw, rw = (evidence / 'workspaces' / name for name in (left, right))
        checks = {'names': [left, right], 'initial_source_equal': source_initial[left] == source_initial[right],
                  'full_history_equal': tree(lw / 'history') == tree(rw / 'history'),
                  'task_equal': digest(lw / 'TASK.md') == digest(rw / 'TASK.md'),
                  'public_tests_equal': tree(lw / 'tests') == tree(rw / 'tests')}
        assert checks == pair and all(v for k, v in checks.items() if k != 'names')
        report['paired_checks'].append(checks)

    # Execute the saved author correction, including both probes, in order.
    workspace = temporary / 'teacher'
    write_workspace(workspace, 'dev-filter-fresh')
    env = Environment(workspace)
    teacher = lines(evidence / 'correction/events.jsonl')
    for event in teacher:
        actual = env.call(event['action']) if event['action'] else invalid.copy()
        assert stable(actual) == stable(event['result']), ('teacher', event['turn'])
        replay_results += 1
    teacher_evaluation = evaluate(workspace)
    assert stable(teacher_evaluation) == stable(read(evidence / 'correction/evaluation.json'))
    assert source_hash(workspace) == digest(evidence / 'correction/workspace/etl_pipeline.py')
    report['teacher'] = {'events_replayed': len(teacher), 'score': teacher_evaluation['passed'],
                         'public_passed': teacher_evaluation['public']['returncode'] == 0}
    correction_rows = lines(evidence / 'correction/training.jsonl')
    conditional_first = next(e for e in lines(evidence / 'runs/conditional-correction-adapter/events.jsonl') if e['kind'] == 'model')
    assert conditional_first['prompt'] == correction_rows[2]['prompt']
    report['conditional_context'] = {'first_prompt_equals_taught_probe_prompt': True,
                                     'first_action': conditional_first['action'],
                                     'taught_action': json.loads(correction_rows[2]['target'])}

    workspace = temporary / 'bridge-target'
    write_workspace(workspace, 'dev-filter-fresh')
    env = Environment(workspace)
    bridge = read(evidence / 'bridge/executed-target.json')
    for event in bridge['prefix']:
        assert stable(env.call(event['action'])) == stable(event['result'])
        replay_results += 1
    assert stable(env.call(bridge['teacher_action'])) == stable(bridge['result'])
    replay_results += 1
    report['bridge_target'] = {'prefix_turns': len(bridge['prefix']), 'application_ok': bridge['result']['application_ok'],
                               'assertion_passed': bridge['result']['assertion_passed']}

    # New diagnostic of a visible unintended edit; not fresh learner evaluation.
    payload = {'pipeline': {'steps': [{'op': 'rename', 'from': 'amount', 'to': 'price'}]},
               'dataset': [{'amount': '  keep spaces  '}]}
    expected = {'status': 'ok', 'data': [{'price': '  keep spaces  '}], 'metrics': {'rows_in': 1, 'rows_out': 1}}
    report['additional_rename_preservation_probe'] = {'payload': payload, 'expected': expected, 'results': {}}
    for name in ['dev-normalization-base', 'dev-normalization-pilot-adapter']:
        result = Environment(temporary / name).call({'action': 'probe', 'payload': payload, 'expected': expected})
        report['additional_rename_preservation_probe']['results'][name] = {k: v for k, v in result.items() if k != 'seconds'}

training = [read(evidence / name / 'summary.json') for name in ['correction-adapter', 'bridge-adapter']]
for name, summary in zip(['correction-adapter', 'bridge-adapter'], training):
    steps = [e for e in lines(evidence / name / 'events.jsonl') if e['kind'] == 'train_step']
    assert len(steps) == summary['steps']
    assert [e['step'] for e in steps] == list(range(1, summary['steps'] + 1))
    assert (evidence / name / 'adapter.safetensors').stat().st_size == summary['adapter_bytes']
assert training[1]['initial_adapter_hash'] == training[0]['trained_adapter_hash']
report['training_costs'] = {'training_updates': sum(x['steps'] for x in training),
                          'training_rows': sum(x['rows'] for x in training),
                          'training_wall_seconds': sum(x['seconds'] for x in training),
                          'training_peak_mlx_bytes': max(x['peak_mlx_bytes'] for x in training),
                          'bridge_initial_hash_matches_correction_final': True}
for k, value in report['training_costs'].items():
    if k != 'bridge_initial_hash_matches_correction_final':
        assert abs(read(evidence / 'analysis.json')['costs'][k] - value) < 1e-6
for name, key in [('correction', 'source_events'), ('bridge', 'source')]:
    lineage = read(evidence / name / 'lineage.json')
    assert digest(snapshot / lineage[key]) == lineage['source_sha256']
bridge_row = lines(evidence / 'bridge/training.jsonl')[0]
source_turn = next(e for e in lines(evidence / 'runs/reacquisition-correction-adapter/events.jsonl')
                   if e['kind'] == 'model' and e['turn'] == 2)
assert bridge_row['prompt'] == source_turn['prompt']
assert bridge_row['target'] == correction_rows[2]['target']
assert len(correction_rows) == 7
source_events = lines(evidence / 'runs/dev-filter-fresh-pilot-adapter/events.jsonl')
for turn in [0, 1]:
    model = next(e for e in source_events if e['kind'] == 'model' and e['turn'] == turn)
    assert correction_rows[turn]['prompt'] == model['prompt']
    assert correction_rows[turn]['target'] == model['raw']
transcript = ''
task = (evidence / 'correction/workspace/TASK.md').read_text()
for i, event in enumerate(teacher):
    if i < 3:
        raw = event['raw']
    else:
        row = correction_rows[i - 1]
        assert row['prompt'] == render(task, transcript)
        raw = json.dumps(event['action'], separators=(',', ':'))
        assert row['target'] == raw
    transcript += '\nASSISTANT: ' + raw + '\nTOOL: ' + json.dumps(event['result'], sort_keys=True)
assert transcript == (evidence / 'correction/transcript.txt').read_text()
report['lineage'] = {'learner_prefix_targets': 2, 'authored_correction_targets': 5,
                     'authored_bridge_targets': 1, 'source_hashes_and_contexts_verified': True}
report['episode_costs'] = {'episodes': len(all_summaries), 'model_calls': len(all_model),
                         'prompt_tokens': sum(e['prompt_tokens'] for e in all_model),
                         'completion_tokens': sum(e['completion_tokens'] for e in all_model),
                         'episode_wall_seconds': sum(e['seconds'] for e in all_summaries),
                         'model_generation_seconds': sum(e['seconds'] for e in all_model),
                         'cap_hits': sum(e['completion_tokens'] >= 1024 for e in all_model)}
for k, v in report['episode_costs'].items():
    if k != 'cap_hits':
        author = read(evidence / 'analysis.json')['costs'][k]
        assert abs(author-v) < 1e-6
report['tool_results_replayed'] = replay_results
report['external_checks_replayed'] = len(all_summaries) * 18 + 18
report['public_suite_invocations_for_evaluation'] = len(all_summaries) + 1
report['additional_root_probes'] = 2
report['fresh_confirmation_status'] = read(evidence / 'fresh-freeze-status.json')['status']
assert report['fresh_confirmation_status'] == 'not evaluated'
a.output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'manifest': report['manifest'], 'tool_results_replayed': replay_results,
                  'scores': {k: v['score'] for k, v in report['runs'].items()},
                  'rename_preservation': {k: v['assertion_passed'] for k,v in report['additional_rename_preservation_probe']['results'].items()}}, indent=2))
