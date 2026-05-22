# Contributing

## Setup

```bash
uv sync --locked --extra dev --extra browser
task verify
```

```powershell
uv sync --locked --extra dev --extra browser
task verify
```

## Workflow

- Use Conventional Commits.
- Keep each change scoped to one behavior or hardening area.
- Add tests for behavior changes.
- Update docs when public behavior, configuration, security posture, or release flow changes.
- Do not commit secrets, browser auth state, local caches, build output, or private operator files.

## Local Gates

Run:

```bash
task lint
task typecheck
task test
task docs
task security
task gc
```

Pull requests must keep the canonical identity set to `oaslananka/notebooklm-mcp-agent`.
