"""Offline Response.json branch probe; no HTTP requests or model calls.

Run in uv with an explicitly pinned Requests source revision and simplejson.
This checks one reported implementation defect, not whole-task agent behavior.
"""
import ast
import hashlib
import importlib.metadata
import inspect
import json
from pathlib import Path
import platform
import sys
import textwrap

import requests

ROOT = Path(__file__).resolve().parents[2]
label = sys.argv[1]
reference = ROOT / '.cache/evidence-acquisition/requests' / label / 'requests/models.py'
tree = ast.parse(reference.read_text())
response = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'Response')
reference_fn = next(n for n in response.body if isinstance(n, ast.FunctionDef) and n.name == 'json')
actual_fn = ast.parse(textwrap.dedent(inspect.getsource(requests.Response.json))).body[0]
# Parsing a dedented method also dedents its docstring; normalize only that text.
assert ast.get_docstring(reference_fn) == ast.get_docstring(actual_fn)
reference_fn.body[0].value.value = ast.get_docstring(reference_fn)
actual_fn.body[0].value.value = ast.get_docstring(actual_fn)
assert ast.dump(reference_fn) == ast.dump(actual_fn), 'Installed method differs from pinned source'

cases = [
    ('invalid-explicit-utf8', b'not json', 'utf-8', False),
    ('invalid-inferred-utf8', b'not json', None, False),
    ('invalid-inferred-utf16', '{"a"="b"'.encode('utf-16'), None, False),
    ('invalid-short', b'x', None, False),
    ('valid-explicit-utf8', b'{"a": 1}', 'utf-8', True),
    ('valid-inferred-utf8', b'{"a": 1}', None, True),
    ('valid-inferred-utf16', '{"a": 1}'.encode('utf-16'), None, True),
]
outcomes = []
for name, content, encoding, valid in cases:
    r = requests.Response()
    r._content = content
    r.encoding = encoding
    try:
        result = r.json()
        record = {'case': name, 'result': result, 'contract_met': valid and result == {'a': 1}}
    except Exception as exc:
        record = {'case': name, 'exception': type(exc).__module__ + '.' + type(exc).__name__,
                  'contract_met': not valid and isinstance(exc, requests.exceptions.JSONDecodeError),
                  'catchable_as_request_exception': isinstance(exc, requests.exceptions.RequestException),
                  'catchable_as_backend_json_error': isinstance(exc, requests.compat.JSONDecodeError)}
    outcomes.append(record)

print(json.dumps({'scope': 'Deterministic offline Response.json component probe; no agent results',
                  'source_label': label, 'python': platform.python_version(),
                  'dependencies': {d.metadata['Name']: d.version for d in importlib.metadata.distributions()},
                  'requests_direct_url': json.loads(importlib.metadata.distribution('requests').read_text('direct_url.json') or 'null'),
                  'method_ast_matches_pinned_source': True,
                  'reference_sha256': hashlib.sha256(reference.read_bytes()).hexdigest(),
                  'outcomes': outcomes}, indent=2))
