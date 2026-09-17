"""Inspect pinned SkillCraft source without importing or executing author code."""

import argparse
import ast
import hashlib
import json
from pathlib import Path
import subprocess


PIN = "0a9ba8808ba49bbc7bd40ad2e853896b8c3d4764"
FILES = [
    "README.md",
    "run.sh",
    "test_all_tasks.py",
    "utils/aux_tools/direct_exec.py",
    "utils/aux_tools/skill_cache.py",
    "utils/roles/task_agent.py",
    "utils/data_structures/task_config.py",
]


def function(source, name):
    return next(
        node for node in ast.walk(ast.parse(source))
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == name
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    revision = subprocess.check_output(
        ["git", "-C", str(args.repo), "rev-parse", "HEAD"], text=True
    ).strip()
    if revision != PIN:
        raise ValueError(f"Expected {PIN}, found {revision}")
    source = {path: (args.repo / path).read_text() for path in FILES}
    direct = source["utils/aux_tools/direct_exec.py"]
    skill = source["utils/aux_tools/skill_cache.py"]
    invoke = ast.unparse(function(direct, "on_exec_script_invoke"))
    modes = function(source["test_all_tasks.py"], "_build_eval_config_for_mode")
    mode_args = {}
    for branch in modes.body:
        if isinstance(branch, ast.If) and isinstance(branch.test, ast.Compare):
            name = ast.literal_eval(branch.test.comparators[0])
            call = branch.body[0].value
            mode_args[name] = {
                item.arg: ast.literal_eval(item.value)
                for item in call.keywords if isinstance(item.value, ast.Constant)
            }
    expected = {
        "base": (False, False),
        "skill": (True, False),
        "direct-exec": (False, True),
    }
    for mode, values in expected.items():
        assert (mode_args[mode]["enable_skill_cache"],
                mode_args[mode]["enable_direct_exec"]) == values
    checks = {
        "direct_uses_shared_tool_bridge":
            "from utils.aux_tools.skill_cache import ToolBridge, ToolCallQueue" in direct,
        "direct_executes_supplied_script": "exec(script_code, exec_namespace)" in invoke,
        "direct_logs_script_and_result": "_save_script_to_workspace(" in invoke,
        "direct_returns_debug_trace": "'full_traceback': tb" in invoke,
        "direct_omits_library_quality_check": "check_result_quality" not in direct,
        "library_checks_result_quality": "quality_info = check_result_quality(result)" in skill,
        "direct_loaded_as_agent_tool": "local_tools.extend(direct_exec_tools)" in source["utils/roles/task_agent.py"],
        "direct_prompt_requires_hardcoded_parameters":
            "Parameters are HARDCODED" in source["utils/data_structures/task_config.py"],
    }
    assert all(checks.values()), checks
    tracked = subprocess.check_output(
        ["git", "-C", str(args.repo), "ls-files"], text=True
    ).splitlines()
    result = {
        "repository": "https://github.com/shiqichen17/SkillCraft",
        "revision": revision,
        "source_sha256": {
            path: hashlib.sha256((args.repo / path).read_bytes()).hexdigest()
            for path in FILES
        },
        "mode_flags": mode_args,
        "static_checks": checks,
        "tracked_files": tracked,
        "limits": "Static source checks only; not the paper's verified execution revision. "
                  "No imports, dependencies, model calls, APIs or benchmark tasks executed. "
                  "No outcomes, actual repair behavior or lifetime costs reproduced.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"revision": revision, "checks": checks}, indent=2))


if __name__ == "__main__":
    main()
