"""Audit the inspected InSCIt development release and pinned cache hashes.

Run with uv run --no-project python sources/2026-09-28-evidence-acquisition/audit_assets.py.
Use --fetch to reconstruct immutable public source files missing from the cache.
Mutable GitHub API snapshots are not reconstructed by this script.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
args = argparse.ArgumentParser(description=__doc__)
args.add_argument('--fetch', action='store_true')
options = args.parse_args()
records = json.loads((HERE / 'retrieval.json').read_text())
verified = []
for item in records:
    immutable = item['url'].startswith('https://raw.githubusercontent.com/')
    if not immutable or item['status'] != 200:
        continue
    path = ROOT / item['path']
    if not path.exists() and options.fetch:
        request = urllib.request.Request(item['url'], headers={'User-Agent': item['user_agent']})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read(item['bytes'] + 1)
        assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256']
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    data = path.read_bytes()
    assert len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256'], path
    verified.append(item['path'])

data = json.loads((ROOT / '.cache/evidence-acquisition/inscit/data/dev.json').read_text())
counts = collections.Counter()
types = collections.Counter()
mixed = []
for key, conversation in sorted(data.items()):
    turns = conversation['turns']
    for index, turn in enumerate(turns):
        counts['turns'] += 1
        counts[f"references_{len(turn['labels'])}"] += 1
        types.update(label['responseType'] for label in turn['labels'])
        if len({label['responseType'] for label in turn['labels']}) > 1:
            mixed.append({'conversation': key, 'turn': index + 1})
        assert len(turn['context']) == 2 * index + 1
        assert len(turn['prevEvidence']) == index
        if index + 1 < len(turns):
            next_context = turns[index + 1]['context']
            assert next_context[:len(turn['context'])] == turn['context']
            assert next_context[len(turn['context'])] in [label['response'] for label in turn['labels']]
            counts['recorded_continuations'] += 1

selected = []
for key, index in [('food_level1_dial28', 4), ('food_level1_dial28', 5), ('food_level1_dial33', 2)]:
    turn = data[key]['turns'][index - 1]
    selected.append({'conversation': key, 'turn': index,
                     'record_sha256': hashlib.sha256(json.dumps(turn, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
                     'reference_types': [label['responseType'] for label in turn['labels']],
                     'reference_evidence_ids': [[e['passage_id'] for e in label['evidence']] for label in turn['labels']]})
print(json.dumps({'scope': 'Descriptive artifact audit, not agent outcomes or a causal action comparison',
                  'inscit_revision': '2319fb85932b9528a13417223ffc6fc629ae8087',
                  'verified_immutable_files': len(verified),
                  'conversations': len(data), 'counts': counts, 'reference_type_counts': types,
                  'mixed_response_type_turns': len(mixed), 'selected_records': selected}, indent=2))
