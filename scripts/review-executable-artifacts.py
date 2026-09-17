"""Static inventory of pinned public artifacts; never imports or runs their code."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cache', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    pins = {'agent-workflow-memory': '8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1',
            'SkillWeaver': 'f2a63d65d0f6ff46ac30e817cede8797f8f25b97'}
    hashes, inventories = {}, {}
    for name, pin in pins.items():
        repo = args.cache / name
        assert subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip() == pin
        files = subprocess.check_output(['git', '-C', str(repo), 'ls-files'], text=True).splitlines()
        inventories[name] = files
        hashes[name] = {file: hashlib.sha256((repo / file).read_bytes()).hexdigest()
                        for file in files if Path(file).suffix in ('.py', '.md', '.json', '.txt')}

    awm = args.cache / 'agent-workflow-memory'
    source = (awm / 'mind2web/run_mind2web.py').read_text()
    tree = ast.parse(source)
    action_branch = next(n for n in ast.walk(tree) if isinstance(n, ast.If)
                         and ast.unparse(n.test) == "args.mode == 'action'")
    assert len(action_branch.body) == 1 and isinstance(action_branch.body[0], ast.Raise)
    assert ast.unparse(action_branch.body[0].exc) == 'NotImplementedError'
    assert not (awm / 'mind2web/data/workflow/code.py').exists()

    sw = args.cache / 'SkillWeaver'
    libraries = []
    for file in sorted(sw.glob('skillnet/**/*_code.py')):
        fns = [n for n in ast.parse(file.read_text()).body
               if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        libraries.append({'file': str(file.relative_to(sw)), 'functions': len(fns),
                          'with_docstring': sum(ast.get_docstring(n) is not None for n in fns),
                          'metadata_present': file.with_name(file.name.replace('_code.py', '_metadata.json')).exists(),
                          'functions_with_css_selector_calls': sum(any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr in ('locator', 'query_selector', 'query_selector_all') for n in ast.walk(fn)) for fn in fns)})
    assert len(libraries) == 5 and not any(x['metadata_present'] for x in libraries)
    prompt_tree = ast.parse((sw / 'skillweaver/create_skill_library_prompt.py').read_text())
    function = next(n for n in prompt_tree.body if isinstance(n, ast.AsyncFunctionDef))
    first_branch = next(n for n in function.body if isinstance(n, ast.If))
    assert 'prod' in ast.unparse(first_branch.test)
    assert ast.unparse(first_branch.body[0]) == 'return await knowledge_base.retrieve(task_string, lm)'
    kb_tree = ast.parse((sw / 'skillweaver/knowledge_base/knowledge_base.py').read_text())
    retrieve = next(n for n in ast.walk(kb_tree) if isinstance(n, ast.AsyncFunctionDef) and n.name == 'retrieve')
    assert 'format_function_as_pretty_string(function)' in ast.unparse(retrieve)
    assert 'as_reference_only' not in ast.unparse(retrieve)
    check = (sw / 'skillweaver/sanity_check_code.py').read_text()
    assert '".locator(" in code or ".query_selector" in code' in check
    out = {'revisions': pins, 'tracked_files': inventories, 'source_sha256': hashes,
           'awm_action_branch_raises': True, 'awm_workflow_code_module_absent': True,
           'skillweaver_libraries': libraries,
           'skillweaver_webarena_tasks': len(json.loads((sw / 'skillweaver/evaluation/test_cases/test.webarena.raw.json').read_text())),
           'skillweaver_prod_retrieval_ignores_reference_flag': True,
           'skillweaver_generated_code_rejects_css_selector_calls': True,
           'limits': 'Static source/artifact checks only. No dependency setup, browser execution, model call, task success reproduction or acquisition cost measurement.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('source_sha256', 'tracked_files')}, indent=2))


if __name__ == '__main__':
    main()
