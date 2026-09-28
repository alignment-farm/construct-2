"""Root aggregation and raw-response regrading; no model calls or study writes.

Use a snapshot of evidence-set-memory at 8ac9b69 with the hash-verified
phase-2 partitions restored by scripts/phase2_assets.py --rebuild-cache.
This reproduces the published annotation metric, not semantic correctness.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import string


def read(path):
    return json.loads(path.read_text())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    return ' '.join(re.sub(r'\b(a|an|the)\b', ' ', text).split())


def f1(gold, actual):
    g, a = normalized(gold).split(), normalized(actual).split()
    common = sum((Counter(g) & Counter(a)).values())
    return (2 * common / (len(g) + len(a))) if g and a else int(g == a)


def answer_from_raw(raw):
    text = raw['response']['choices'][0]['message']['content'].split('</think>')[-1].strip()
    if text.startswith('```'):
        text = text.split('\n', 1)[1].rsplit('```', 1)[0]
    found = []
    for m in re.finditer('{', text):
        try:
            obj, _ = json.JSONDecoder().raw_decode(text[m.start():])
        except ValueError:
            continue
        if isinstance(obj, dict) and isinstance(obj.get('answer'), str) and isinstance(obj.get('citations'), list):
            found.append(obj)
    if not found or any(type(x) is not int for x in found[-1]['citations']):
        return {'answer': '', 'citations': [], 'parse_error': True}
    return found[-1]


def grade(answer, label, selected):
    alternatives = [label['answer'], *label['aliases']]
    em = int(any(normalized(g) == normalized(answer['answer']) for g in alternatives))
    gold, citations = set(label['supports']), set(answer['citations'])
    return dict(answer_em=em, answer_f1=max(f1(g, answer['answer']) for g in alternatives),
                citations_complete=gold <= citations, citations_valid=citations <= set(selected),
                complete=int(em and gold <= citations <= set(selected)),
                retrieved_complete=gold <= set(selected))


def check_grade(actual, expected):
    for key, value in actual.items():
        assert abs(value - expected[key]) < 1e-12, (key, value, expected[key])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists(), 'Choose a new report path'
    root = args.study
    report = {'reviewed_revision': '8ac9b694a32e53e5941912b65e2c8881ce0d7c4b'}
    manifest = read(root/'phase5/manifest.json')['files']
    assert all(sha(root/p) == v['sha256'] and (root/p).stat().st_size == v['bytes'] for p, v in manifest.items())
    report['phase5_manifest_files_verified'] = len(manifest)
    for split in ('train', 'development', 'confirmation'):
        m = read(root/f'phase2/data/{split}-manifest.json')
        for kind in ('inputs', 'labels'):
            assert sha(root/f'.cache/phase2/partitions/{split}-{kind}.json') == m[f'{kind}_sha256']
    report['phase2_partition_hashes_verified'] = 6
    labels = {x['id']: x for x in read(root/'.cache/phase2/partitions/confirmation-labels.json')}
    selection = read(root/'phase2/runs/confirmation-selection/outcomes.json')
    aggregates = {}
    for row in selection:
        complete = int(set(labels[row['id']]['supports']) <= set(row['selected']))
        assert complete == row['complete']
        arm = aggregates.setdefault(row['arm'], dict(n=0, annotated_support_complete=0, energy_optimal=0))
        arm['n'] += 1
        arm['annotated_support_complete'] += complete
        arm['energy_optimal'] += int(abs(row['score_gap']) < 1e-6)
    report['phase2_selection'] = aggregates
    folder = root/'phase2/runs/confirmation-reader'
    rows = read(folder/'outcomes.json')
    calls = {p.name.removesuffix('-response.json'): read(p) for p in folder.glob('*-response.json')}
    raw_answers = {k: answer_from_raw(v) for k, v in calls.items()}
    all_rows = {r['id']: r for r in rows if r['arm'] == 'all'}
    qa = {}
    for row in rows:
        answer = raw_answers[row['request_hash']]
        assert answer == row['answer']
        request = read(folder/f"{row['request_hash']}-request.json")
        assert hashlib.sha256(json.dumps(request, sort_keys=True).encode()).hexdigest() == row['request_hash']
        prompt = json.loads(request['messages'][1]['content'])
        assert sorted(p['idx'] for p in prompt['paragraphs']) == row['selected']
        before = grade(answer, labels[row['id']], row['selected'])
        check_grade(before, row)
        needs_repair = (not answer['answer'].strip() or bool(answer.get('parse_error'))
                        or not set(answer['citations']) <= set(row['selected']))
        assert row['fallback'] == (needs_repair and row['arm'] != 'all')
        replacement = all_rows[row['id']]
        final = raw_answers[replacement['request_hash']] if needs_repair else answer
        after = grade(final, labels[row['id']], replacement['selected'] if needs_repair else row['selected'])
        check_grade(after, row['after_fallback'])
        group = qa.setdefault(row['arm'], dict(n=0, retrieved=0, em=0, complete=0, after_fallback=0))
        group['n'] += 1
        for key, field in [('retrieved','retrieved_complete'), ('em','answer_em'), ('complete','complete')]:
            group[key] += before[field]
        group['after_fallback'] += after['complete']
    report['phase2_original_qa'] = qa
    report['phase2_original_qa_mapped_rows'] = len(rows)
    report['phase2_original_qa_unique_calls'] = len(calls)
    report['phase2_original_qa_usage'] = {k: sum(v['response']['usage'][k] for v in calls.values())
                                           for k in ('prompt_tokens','completion_tokens')}
    total = Counter()
    for path in (root/'phase2/runs').rglob('*-response.json'):
        raw = read(path)
        total['requests'] += 1
        for key in ('prompt_tokens','completion_tokens'):
            total[key] += raw['response']['usage'][key]
    report['phase2_all_saved_physical_calls'] = dict(total)
    phase5 = {}
    for row in read(root/'phase5/runs/confirmation/outcomes.json'):
        group = phase5.setdefault(row['method'], Counter())
        group.update(episodes=1, before=row['first_complete'], after=row['final_complete'],
                     cache_hits=row['cache_hit'], repairs=bool(row['repair']), bytes=row['delivery_bytes'],
                     native_executions=row['executions'])
        if not row['cache_hit']:
            group['uncached'] += 1
            group['uncached_complete'] += row['first_complete']
            group[row['transfer_regime'] + '_complete'] += row['first_complete']
    report['phase5_confirmation_aggregation'] = {k: dict(v) for k,v in phase5.items()}
    report['interpretation_limit'] = 'Reproduced annotation scores do not certify source-grounded answers. No new reader inference or new experimental samples.'
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True)+'\n')
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
