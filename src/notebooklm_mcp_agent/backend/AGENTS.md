# Backend Agent Map

## Responsibility

`backend/` owns NotebookLM client construction, retry behavior, exception mapping, task persistence, and normalization of upstream shapes.

## Allowed Imports

Backend may import `notebooklm_mcp_agent.config` and backend-local modules. It must not import tools, resources, OpenAPI, server, or CLI modules.

## Adding A New Item

Add a typed backend method, normalize upstream results at this boundary, and cover mapping branches with tests.

## Test Commands

```bash
uv run pytest tests/unit/test_backend_client.py tests/unit/test_backend_exceptions.py tests/unit/test_backend_tasks.py
```

## Conventions

Keep raw `Any` near upstream calls and return normalized structures to tools.
