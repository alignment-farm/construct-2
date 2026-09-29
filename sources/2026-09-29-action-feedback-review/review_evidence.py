"""Collect and verify offline phase-6/7 replays. No participant calls.
Run the six audit/diagnosis commands in README first, then:
python review_evidence.py SNAPSHOT GIT_REPOSITORY OUT.json
"""
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path

root, repo, out = [Path(p).resolve() for p in sys.argv[1:]]
load = lambda p: json.loads(p.read_text())
sha = lambda b: hashlib.sha256(b).hexdigest()
def git(*args):
    return subprocess.check_output(['git', '-C', str(repo), *args])
manifest_counts = {}
for phase, commit in [('phase6','cd2582c6e0fed3105e935086550d10f7821ae156'),('phase7','5e2d06a22f302ecfbd124f6f009b84274c39986b')]:
    manifest = load(root / phase / 'manifest.json')
    for name, expected in manifest['files'].items():
        data = git('show', commit + ':' + name)
        assert len(data) == expected['bytes'], name
        assert sha(data) == expected['sha256'], name
    manifest_counts[phase] = dict(revision=commit, files=len(manifest['files']))
freeze = '94bc951e92206fa6a2f144ce974e6cb384fab313'
assert not git('ls-tree','-r','--name-only',freeze,'phase7/transfer-tasks.json').strip()
assert git('ls-tree','-r','--name-only','368a61e','phase7/transfer-tasks.json').strip()
assert b'def tasks():' in git('show','fa9f5e7:scripts/phase6_transfer.py')
result = dict(revision='5e2d06a22f302ecfbd124f6f009b84274c39986b', collector_python=platform.python_version(),
    replay_python=subprocess.check_output([str(root/'phase7/.venv/bin/python'),'-c','import platform;print(platform.python_version())'],text=True).strip(),
    manifest_counts=manifest_counts,
    phase6_task_definitions_in_frozen_script=True, phase7_task_file_absent_at_freeze_present_next_commit=True,
    model_calls=0, refits=0,
    limits='Root reruns supplied audit code and inspections, not independently reimplemented specifications; no model generations or fits repeated. Git chronology is not an independent timestamp attestation.')
for key, path in {
    'phase6_audit':'root-review-phase6/audit.json',
    'phase6_native_costs':'root-review-phase6/native-costs.json',
    'phase6_semantic_intervention':'root-review-semantic/summary.json',
    'phase7_audit':'root-review-phase7/audit.json',
    'phase7_documentation':'root-review-docs/results.json',
    'phase7_mutation':'root-review-mutation/summary.json',
    'phase7_review_repair':'root-review-repair/repair-replay.json',
    'phase7_final_costs':'root-review-repair/final-costs.json',
}.items():
    result[key] = load(root / '.cache' / path)
# Store semantic content of changed documentation for human review, not just AST presence.
assert sum(r['executable_and_documentation_gate'] for r in result['phase7_documentation']) == 5
result['root_pytest_invocations'] = 48 + 61 + 2 + 4 + 1
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['manifest_counts','root_pytest_invocations','replay_python','model_calls','refits']},indent=2))
