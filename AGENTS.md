# Agent Operating Map

## What This Repository Is

NotebookLM MCP Agent is a Python MCP server and CLI for NotebookLM workflows. It exposes local stdio and Streamable HTTP transports, with bearer and GitHub OAuth authentication for remote HTTP.

## Setup

```bash
uv sync --locked --extra dev --extra browser
```

```powershell
uv sync --locked --extra dev --extra browser
```

Use `Taskfile.yml` as the canonical command surface. `Makefile` is only a wrapper around `task`.

## Build And Test

Required local gates before commits:

```bash
task lint
task typecheck
task test
task docs
task security
task gc
task verify:release
```

```powershell
task lint
task typecheck
task test
task docs
task security
task gc
task verify:release
```

## Repository Layout

- `src/notebooklm_mcp_agent/`: canonical Python package.
- `src/nlm_mcp/`: deprecated import shim only.
- `tests/`: offline unit and integration tests by default.
- `docs/`: MkDocs source content.
- `scripts/`: cross-platform verification and generation scripts.
- `.github/workflows/`: hosted GitHub Actions gates.
- `deploy/`: Dockerfile and Docker Compose.

## Conventions

- Use Python `>=3.11,<3.15`.
- Use `uv` for lock and environment management.
- Use Conventional Commits.
- Keep public identity set to `oaslananka/notebooklm-mcp-agent`.
- Keep CLI examples on `notebooklm-agent`.
- Keep environment variables on the `NOTEBOOKLM_MCP_` prefix.
- Do not commit private operator files such as `PROMPT.md`, `AUTONOMOUS_BUILD.md`, `AGENT_ORDERS*.md`, or `NEXT.md`.

## Architectural Rules

- `config.py` owns settings parsing and startup validation.
- `backend/` owns NotebookLM client integration and normalization.
- `auth/` owns HTTP bearer and GitHub OAuth handling.
- `tools/` owns MCP tool input and output behavior.
- `openapi.py` owns OpenAPI operation metadata.
- `cli.py` wires command execution and HTTP routes.
- Avoid circular imports and cross-layer imports not allowed by `scripts/check_architecture.py`.

## Where Decisions Live

Use `docs/architecture/adr/` for non-obvious runtime, dependency, security, release, or deployment decisions.

## Common Tasks

- Regenerate catalog: `task catalog`
- Verify owner hygiene: `task verify:owner`
- Build docs: `task docs`
- Build release artifacts without publishing: `task verify:release`
- Clean local outputs: `task clean`

## Non-Negotiable Cleanup Checks

These must return zero findings before handoff:

```bash
python scripts/check_owner_refs.py
python scripts/check_forbidden_terms.py
python scripts/check_no_secrets.py
python scripts/check_config_docs.py
python scripts/check_public_surface.py
python scripts/check_tool_catalog.py
python scripts/check_openapi_parity.py
python scripts/check_architecture.py
```
