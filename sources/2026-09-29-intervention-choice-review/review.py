"""Root offline review; no generation, fitting, or writes inside the study.
Usage: python review.py SNAPSHOT GIT_REPO OUTPUT.json
"""
import collections, copy, datetime, decimal, hashlib, json, platform, subprocess, sys
from pathlib import Path
root, repo, out = [Path(p).resolve() for p in sys.argv[1:]]
sys.path.insert(0,str(root/'src'))
import experiment as ex
from source_parser import extract
from repair_control import repair
load=lambda p:json.loads(p.read_text())
sha=lambda b:hashlib.sha256(b).hexdigest()
def git(*args):return subprocess.check_output(['git','-C',str(repo),*args])
def expected(case,interface):
    # Root implementation: integer string arithmetic, no treatment Decimal adapter.
    rows=[]
    for r in case['gold']['invoices']:
        digits={'JPY':0,'KWD':3}.get(r['currency'],2)
        whole,_,frac=r['amount'].partition('.')
        assert len(frac)<=digits
        units=int(whole)*10**digits+int(frac.ljust(digits,'0') or '0')
        if interface=='v1':rows.append({**{k:v for k,v in r.items() if k!='amount'},'amount_minor':units})
        else:
            date=None if r['due'] is None else dict(zip(['year','month','day'],map(int,r['due'].split('-'))))
            rows.append((r['id'],{'supplier':r['vendor'],'money':{'units':units,'currency':r['currency']},'deadline':date,'cancelled':r['status']=='cancelled','memo':r['memo']}))
    return {'invoices':rows} if interface=='v1' else {'invoices':dict(rows),'order':[r[0] for r in rows]}

hashes=load(root/'evidence/provenance/final-source-hashes.json')
for p,digest in hashes.items():assert sha((root/p).read_bytes())==digest,p
revisions=load(root/'evidence/provenance/revisions.json')
for cohort in ['development','acquisition','confirmation']:
    manifest=load(root/'evidence'/cohort/'manifest.json')
    assert sha(git('show',manifest['git_head']+':src/experiment.py'))==manifest['code_sha256']
    assert sha(git('show',manifest['git_head']+':protocols/phase1.md'))==manifest['protocol_sha256']
parser_manifest=load(root/'evidence/parser-confirmation/manifest.json')
assert sha(git('show',revisions['parser_freeze']+':protocols/followup.md'))==parser_manifest['protocol_sha256']
assert sha(git('show',revisions['parser_freeze']+':src/source_parser.py'))==parser_manifest['parser_sha256']
assert not git('ls-tree','-r','--name-only',revisions['parser_freeze'],'evidence/parser-confirmation').strip()
assert not git('ls-tree','-r','--name-only',revisions['policy_freeze'],'evidence/confirmation').strip()
assert git('show',revisions['policy_freeze']+':evidence/policy.json')==(root/'evidence/policy.json').read_bytes()

all_rows=[]; cohorts={};sources={};seen=set();failures=[]
for name,seed,size in [('development',110,2),('acquisition',220,4),('confirmation',330,6)]:
    data=load(root/'evidence'/name/'cases.json');assert data==ex.cases(seed,size)
    ids={r['id'] for c in data for r in c['gold']['invoices']};assert not seen&ids;seen |= ids
    cases={c['case_id']:c for c in data};sources.update(cases)
    for c in data:assert extract(c['source'])==c['gold']
    rows=ex.read_records(root/'evidence'/name/'outcomes.jsonl')
    for r in rows:
        case=cases[r['case_id']];target='canonical' if r['action']=='C' else r['interface']
        wanted={'model':ex.MODEL,'messages':[{'role':'system','content':ex.SEMANTICS},{'role':'user','content':ex.CONTRACTS[target]+'\n\nSOURCE:\n'+case['source']}],'temperature':0,'max_tokens':1000,'stream':False}
        assert r['request']==wanted
        assert r['group']==ex.visible_group(case['source'])
        assert r['response']['choices'][0]['finish_reason']=='stop'
        try:
            parsed=ex.parse(r['response']['choices'][0]['message'].get('content') or '')
            actual=ex.adapt(parsed,r['interface']) if r['action']=='C' else parsed
            assert actual==r['output'];assert ex.validate(actual,r['interface'])==r['valid']
            assert ex.diff(expected(case,r['interface']),actual)==r['differences']
        except (ValueError,TypeError,KeyError):
            assert 'error' in r and not r['success'];actual=None
        assert r['success']==(r['valid'] and actual==expected(case,r['interface']))
        if not r['success']:failures.append({'phase':name,'case_id':r['case_id'],'action':r['action'],'interface':r['interface'],'valid':r['valid'],'differences':r.get('differences'),'error':r.get('error')})
    assert ex.summarize(rows)==load(root/'evidence'/name/'summary.json')
    all_rows+=rows;cohorts[name]=rows
policy=load(root/'evidence/policy.json');acq=cohorts['acquisition']
counts={g:{a:{'success':sum(r['success'] for r in acq if r['group']==g and r['action']==a),'n':sum(r['group']==g and r['action']==a for r in acq)} for a in ['D','C']} for g in ex.GROUPS}
choice={g:max(['D','C'],key=lambda a:counts[g][a]['success']/counts[g][a]['n']) for g in counts}
assert policy['counts']==counts and policy['choice']==choice and policy['global_choice']=='C'
assert policy['eligible_outcomes_sha256']==sha((root/'evidence/acquisition/outcomes.jsonl').read_bytes())
assert load(root/'evidence/confirmation/manifest.json')['policy_sha256']==sha((root/'evidence/policy.json').read_bytes())

def policies(rows):
    pairs={}
    for r in rows:pairs.setdefault(r['case_id'],{})[r['action']]=r
    result={}
    for name in ['fixed_D','fixed_C','inherited_category','inherited_global','current_source','schema_aware_reuse','validator_fallback','oracle']:
        charged=[];decisions=[]
        for cid,pair in pairs.items():
            group=ex.visible_group(sources[cid]['source']);interface=pair['D']['interface']
            if name=='fixed_D':a='D'
            elif name in ['fixed_C','inherited_global','schema_aware_reuse']:a='C'
            elif name=='inherited_category':a=choice[group]
            elif name=='current_source':a='D' if group=='plain' else 'C'
            elif name=='validator_fallback':
                a='D' if pair['D']['valid'] else 'C'
                if a=='C':charged.append(pair['D'])
            else:a='D' if pair['D']['success'] else 'C'
            charged.append(pair[a]);decisions.append({'case_id':cid,'interface':interface,'action':a,'success':pair[a]['success']})
        result[name]={'n':len(decisions),'success':sum(x['success'] for x in decisions),'valid':sum(pairs[x['case_id']][x['action']]['valid'] for x in decisions),'requests':len(charged),'prompt_tokens':sum(r['response']['usage']['prompt_tokens'] for r in charged),'completion_tokens':sum(r['response']['usage']['completion_tokens'] for r in charged),'decisions':decisions,'oracle_not_deployable':name=='oracle'}
    return result
raw=policies(cohorts['confirmation']);assert raw==load(root/'evidence/confirmation/policies.json')
patched=[]
for original,saved in zip(cohorts['confirmation'],ex.read_records(root/'evidence/confirmation/repaired-outcomes.jsonl'),strict=True):
    r=copy.deepcopy(original);c=sources[r['case_id']];actual=repair(c['source'],r.get('output'),r['interface'])
    r.update(output=actual,valid=ex.validate(actual,r['interface']),differences=ex.diff(expected(c,r['interface']),actual))
    r['success']=r['valid'] and not r['differences']
    for k in ['output','valid','differences','success']:assert r[k]==saved[k]
    patched.append(r)
repaired=policies(patched);assert repaired==load(root/'evidence/confirmation/repaired-policies.json')
parser_replays={}
for name in ['parser-development','parser-confirmation']:
    data=load(root/'evidence'/name/'cases.json');rows=load(root/'evidence'/name/'outcomes.json');by_id={c['case_id']:c for c in data}
    if name=='parser-confirmation':
        assert data==ex.cases(440,6)
        assert not seen&{r['id'] for c in data for r in c['gold']['invoices']}
    for c in data:assert extract(c['source'])==c['gold']
    for row in rows:
        c=by_id[row['case_id']];actual=ex.adapt(extract(c['source']),row['interface'])
        assert actual==expected(c,row['interface'])==row['output'];assert row['success']
    parser_replays[name]={'source_cases':len(data),'complete':len(rows)}
costs=load(root/'evidence/costs.json')
for name,rows in cohorts.items():
    check={'requests':len(rows),'complete_success':sum(r['success'] for r in rows),'failed_complete_tasks':sum(not r['success'] for r in rows),'structurally_valid':sum(r['valid'] for r in rows),'prompt_tokens':sum(r['response']['usage']['prompt_tokens'] for r in rows),'completion_tokens':sum(r['response']['usage']['completion_tokens'] for r in rows),'request_seconds':sum(r['request_seconds'] for r in rows),'adapter_seconds':sum(r.get('adapter_seconds',0) for r in rows)}
    assert check==costs[name]
for report in [raw,repaired]:
    for value in report.values():value.pop('decisions')
result={'revision':'cb25d5c64bd64859e0e9abbcfc41f0e8f44762df','python':platform.python_version(),'source_hashes_verified':len(hashes),'raw_response_replays':len(all_rows),'shared_repair_replays':len(patched),'parser_replays':parser_replays,'policy_counts':counts,'policy_choice':choice,'raw_policies':raw,'repaired_policies':repaired,'failures':failures,'participant_prompt_tokens':sum(r['response']['usage']['prompt_tokens'] for r in all_rows),'participant_completion_tokens':sum(r['response']['usage']['completion_tokens'] for r in all_rows),'chronology_and_manifest_checks':'passed; follow-up protocol hash checked at historical freeze','new_model_calls':0,'limits':'Saved generation outputs replayed; no regeneration, new cases, causal interface-transfer estimate, natural-language coverage or total engineering-cost estimate.'}
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['raw_policies','repaired_policies','failures','policy_counts']},indent=2))
