# OpenAPI Agent Map

## Responsibility

This directory is reserved for future OpenAPI decomposition. The current implementation lives in `src/notebooklm_mcp_agent/openapi.py`.

## Allowed Imports

OpenAPI code may import tool models and catalog metadata. It must not import CLI or runtime server wiring.

## Adding A New Item

Move code from `openapi.py` only with tests and updated generation scripts.

## Test Commands

```bash
uv run pytest tests/unit/test_openapi.py
uv run python scripts/check_openapi_parity.py
```

## Conventions

Keep operation IDs deterministic and based on canonical tool names.
