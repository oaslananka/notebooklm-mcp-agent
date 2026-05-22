# Docs Agent Map

## Responsibility

The `docs/` tree explains supported installation, configuration, security, architecture, client setup, tools, and release workflow.

## Allowed Imports

Docs may reference public package names, CLI commands, and generated catalog files. Do not document unsupported platforms or private operator files.

## Adding A Page

Add the page under the closest existing section, wire it into `mkdocs.yml`, and run:

```bash
uv run mkdocs build --strict
uv run python scripts/check_docs_commands.py
```

## Conventions

Keep examples runnable on Linux/macOS and Windows PowerShell when shell behavior differs. Keep secret values as placeholders.
