"""Independent finite-task rescoring of the pinned maintenance publication."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import subprocess

PIN = 'be7a508bfea002baceec72f32f7f9d6f73f7861a'


def answer(c, version):
    waived = (version >= 1 and (c['channel'], c['priority']) == ('copper', 'fast')) or (
        version >= 2 and (c['channel'], c['priority']) == ('violet', 'slow'))
    if not (c['certified'] or waived):
        return f"FAIL SKIP SKIP {c['stock']} HELD"
    return 'PASS RESERVE SHIP 0 SENT' if c['stock'] else 'PASS SKIP SKIP 0 WAIT'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--study', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    assert subprocess.check_output(['git', '-C', str(a.study), 'rev-parse', 'HEAD'], text=True).strip() == PIN
    hashes = {}

    def read(rel):
        b = (a.study / rel).read_bytes()
        hashes[rel] = hashlib.sha256(b).hexdigest()
        return b

    analysis = json.loads(read('evidence/final-analysis.json'))
    checked = 0
    endpoints = []
    tie = {}
    for run in analysis['acquisitions'] + analysis['runs']:
        source = run.get('source_run', run.get('run'))
        rows = [json.loads(l) for l in read(source + '/responses.jsonl').splitlines()]
        for row in rows:
            assert (row['raw'].strip() == answer(row['case'], row['version'])) == row['scores']['complete']
            checked += 1
        if run.get('design', {}).get('phase') != 'assessment':
            continue
        grouped = defaultdict(list)
        for row in rows:
            grouped[row['state'], row['panel']].append(row)
        for e in run['endpoints']:
            state = e['history'] + ('-start' if e['support'] == 'none' else '--' + e['support'])
            rs = grouped[state, 'final']
            assert len(rs) == 192
            final_ids = {r['case']['entity'] for r in rs}
            panel_ids = {r['case']['entity'] for r in rows if r['panel'] in ('validation', 'prefix', 'pre')}
            assert not final_ids & panel_ids
            complete = sum(r['raw'].strip() == answer(r['case'], 2) for r in rs)
            assert complete == e['complete']
            endpoints.append({'seed': run['design']['seed'], 'history': e['history'],
                              'support': e['support'], 'complete': complete})
            if run['design']['seed'] == 701 and e['history'] == 'novel' and e['support'] != 'none':
                def obligations(panel):
                    result = {}
                    for group in ('new', 'earlier', 'ineligible'):
                        selected = [r for r in panel if
                                    (answer(r['case'], 1) != answer(r['case'], 2) if group == 'new' else
                                     answer(r['case'], 0) != answer(r['case'], 1) if group == 'earlier' else
                                     answer(r['case'], 2).startswith('FAIL'))]
                        result[group] = {'correct': sum(r['raw'].strip() == answer(r['case'], 2) for r in selected),
                                         'n': len(selected)}
                    result['complete'] = sum(r['raw'].strip() == answer(r['case'], 2) for r in panel)
                    return result
                tie[e['support']] = {'final': obligations(rs), 'validation': obligations(grouped[state, 'validation'])}
    frozen = read('evidence/frozen-predictors-v1.json')
    assert frozen == subprocess.check_output(['git', '-C', str(a.study), 'show', '735f941:evidence/frozen-predictors-v1.json'])
    pred = json.loads(frozen)['prefix']
    ranges = {arm: sorted([v['intercept'], v['intercept'] + v['slope']]) for arm, v in pred.items()}
    assert ranges['bridged'][0] > ranges['novel'][1]
    table = {}
    evidence = json.loads(read('evidence/explicit-v1/evidence.json'))
    for r in evidence:
        c = r['case']
        assert r['label'] == answer(c, r['version'])
        key = '|'.join(str(c[k]) for k in ('channel', 'priority', 'certified', 'stock'))
        table[key] = r['label']
    assert table == json.loads(read('evidence/explicit-v1/table.json'))
    explicit = json.loads(read('evidence/explicit-v1/responses.json'))
    for r in explicit:
        key = '|'.join(str(r['case'][k]) for k in ('channel', 'priority', 'certified', 'stock'))
        assert r['raw'] == table[key] == answer(r['case'], 2)
    out = {'reviewed_revision': PIN, 'source_sha256': hashes, 'rescored_model_responses': checked,
           'assessment_endpoints': endpoints, '701_novel_history_tie': tie,
           'prefix_prediction_ranges': ranges, 'prefix_always_bridged': True,
           'frozen_predictors_match_preassessment_commit': True,
           'explicit_evidence_labels_checked': len(evidence), 'explicit_keys': len(table),
           'explicit_complete': len(explicit),
           'limits': 'Checks saved text and data, not model generation, tokenizer, gradients or optimizer restoration.'}
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'source_sha256'}, indent=2))


if __name__ == '__main__':
    main()
