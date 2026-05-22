# Architecture Overview

Runtime flow:

```text
MCP client -> stdio or Streamable HTTP -> auth middleware -> FastMCP registry -> typed tools -> backend adapter -> notebooklm-py
```

Boundaries:

- `config.py` owns settings parsing and startup validation.
- `auth/` owns HTTP bearer and GitHub OAuth checks.
- `backend/` owns NotebookLM client calls and normalization.
- `tools/` owns MCP tool inputs and outputs.
- `openapi.py` owns OpenAPI operation metadata.
- `cli.py` wires command execution and HTTP routes.
