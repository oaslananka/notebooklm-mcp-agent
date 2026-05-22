# Tools Agent Map

## Responsibility

`tools/` owns MCP-visible tool registration, typed inputs, confirmation checks, and tool result shaping.

## Allowed Imports

Tools may import backend protocols, config, and tool-local helpers. Tools must not import CLI, server runtime, or OpenAPI builders.

## Adding A New Item

Add a Pydantic input model, register the tool, add OpenAPI metadata, update docs catalog, and add parity tests.

## Test Commands

```bash
uv run pytest tests/unit/test_tools_core.py tests/unit/test_tools_artifacts.py tests/unit/test_tools_language.py
uv run python scripts/check_tool_catalog.py
```

## Conventions

Destructive operations require explicit confirmation.
