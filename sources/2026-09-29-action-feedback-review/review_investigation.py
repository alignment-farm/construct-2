"""Offline root review of EGI 9380a56. No model calls or adapter loading.
Usage: python review_investigation.py SNAPSHOT OUT.json
The snapshot must be an extracted archive of the reviewed commit.
"""
import collections
import hashlib
import json
import platform
import shutil
import sys
import tempfile
from pathlib import Path

root = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
r = root / 'evidence/autonomy-03'
load = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
events = lambda p: [json.loads(line) for line in p.read_text().splitlines()]
manifest = load(r / 'artifact-manifest.json')['files']
for name, item in manifest.items():
    assert sha(root / name) == item['sha256'], name
    assert (root / name).stat().st_size == item['bytes'], name
sys.path.insert(0, str(root / 'scripts'))
from continuation_evaluate import evaluate
from autonomy_confirmation import grade, cases
from autonomy_tools import Environment, initial_messages, TOOLS

assert cases() == load(r / 'confirmation-freeze.json')['cases']
assert sha(root / 'scripts/autonomy_confirmation.py') == load(r / 'confirmation-freeze.json')['script_sha256']
original = load(r / 'evaluation.json')
confirmation = load(r / 'confirmation-evaluation.json')
assert original.keys() == confirmation.keys()
programs = {}
with tempfile.TemporaryDirectory(prefix='construct-root-review-') as directory:
    temporary = Path(directory)
    for name in original:
        w = temporary / name
        shutil.copytree(r / 'workspaces' / name, w)
        a, b = evaluate(w), grade(w)
        for actual, saved in [(a, original[name]), (b, confirmation[name])]:
            for k in ['passed', 'total', 'complete']:
                assert actual[k] == saved[k], (name, k)
            assert [c['passed'] for c in actual['cases']] == [c['passed'] for c in saved['cases']], name
        assert a['public']['returncode'] == original[name]['public']['returncode']
        programs[name] = dict(development=a['passed'], confirmation=b['passed'], public_returncode=a['public']['returncode'])
    joint = {}
    freeze = load(r / 'joint-freeze.json')
    for name in ['joint-acquisition-learned', 'joint-acquisition-ordinary4', 'joint-acquisition-ordinary27']:
        es = events(r / 'runs' / name / 'events.jsonl')
        provenance = es[0]
        msg = provenance['initial_messages'][1]['content']
        source = msg.split('CURRENT SOURCE (etl_pipeline.py):\n', 1)[1].split('\n\nHISTORY INDEX:', 1)[0]
        assert hashlib.sha256(source.encode()).hexdigest() == freeze['source_sha256']
        w = temporary / (name + '-actions')
        shutil.copytree(r / 'workspaces' / name, w)
        (w / 'etl_pipeline.py').write_text(source)
        for filename, digest in freeze['history'].items():
            data = (r / 'complete-history' / filename).read_bytes()
            assert hashlib.sha256(data).hexdigest() == digest
            target = w / 'history' / filename
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(data)
        assert initial_messages(w) == provenance['initial_messages']
        assert provenance['tool_schemas'] == TOOLS
        env = Environment(w)
        counts = collections.Counter()
        verification = []
        for event in es:
            if event['kind'] != 'tool':
                continue
            action, saved = event['action'], event['result']
            actual = env.call(action)
            counts[action['action']] += 1
            # Timings and Python's diagnostic formatting vary with interpreter.
            for key in saved.keys() - {'seconds', 'stderr'}:
                assert actual.get(key) == saved[key], (name, event['turn'], key)
            if action['action'] in ['probe', 'replay', 'test', 'edit', 'restore', 'done']:
                verification.append(dict(turn=event['turn'], action=action, passed=actual.get('assertion_passed'), returncode=actual.get('returncode'), ok=actual.get('ok')))
        assert sha(w / 'etl_pipeline.py') == sha(r / 'runs' / name / 'submitted.py')
        joint[name] = dict(replayed_tool_calls=sum(counts.values()), actions=dict(counts), final_source_matches=True, verification=verification)

costs = load(r / 'costs.json')
for row in costs['episodes']:
    es = events(r / 'runs' / row['name'] / 'events.jsonl')
    models = [e for e in es if e['kind'] == 'model']
    assert len(models) == row['model_calls']
    assert sum(e.get('prompt_tokens') or 0 for e in models) == row['prompt_tokens']
    assert sum(e.get('completion_tokens') or 0 for e in models) == row['generated_tokens']
    assert es[-1]['elapsed'] == row['elapsed_seconds']
for row in costs['training_attempts']:
    es = events(r / row['name'] / 'events.jsonl')
    assert sum(e['kind'] == 'train_step' for e in es) == row['recorded_updates']
rows = events(r / 'acquisition/training.jsonl')
assert len(rows) == 23
for row in rows:
    if row['origin'] == 'investigator correction':
        task, index = row['id'].rsplit('-teacher-', 1)
        origin = events(r / 'acquisition' / task / 'events.jsonl')
        action = [e['action'] for e in origin if e.get('turn') is None][int(index)]
    else:
        origin = events(root / row['source_event'])
        action = next(e['action'] for e in origin if e['kind'] == 'tool' and e['turn'] == row['turn'])
    function = row['assistant']['tool_calls'][0]['function']
    assert function['name'] == action['action']
    assert function['arguments'] == {k:v for k,v in action.items() if k != 'action'}
for lineage in load(r / 'acquisition/lineage.json'):
    for turn in lineage['masked_source_edit_turns']:
        assert not any(row['id'] == f"{lineage['task']}-learner-{turn}" for row in rows)
paired = [events(r / 'runs' / name / 'events.jsonl') for name in ['joint-acquisition-learned', 'joint-acquisition-ordinary4']]
assert paired[0][0]['initial_messages'] == paired[1][0]['initial_messages']
a, b = [[e for e in es if e['kind'] == 'tool'] for es in paired]
divergence = next(i for i,(x,y) in enumerate(zip(a,b)) if (x['action'],x['result']) != (y['action'],y['result']))
assert divergence == 2
result = dict(revision='9380a564e104dbd766702a823a125f21ab55696a', python=platform.python_version(), manifest_files=len(manifest), programs=programs, joint=joint,
    training_targets=dict(collections.Counter(row['origin'] for row in rows)), lineage_actions_verified=len(rows), first_divergent_action_one_based=divergence+1,
    cost_episodes_verified=len(costs['episodes']), recorded_updates=costs['recorded_updates'], saved_updates=46,
    conservative_serial_heavy_seconds=costs['conservative_serial_heavy_seconds'], model_calls=0,
    limits='Replay validates archived actions, outputs and lineage, not model generation, adapter loading, training reproducibility, timestamps or unseen transfer.')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['joint', 'programs']}, indent=2))
