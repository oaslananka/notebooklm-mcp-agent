# ADR 006: Ruff Toolchain Version Tracking

**Status**: Accepted  
**Date**: 2026-05-28  
**Driver**: Dev toolchain audit

## Context

Ruff is the project's Python linter and formatter, configured via `[tool.ruff]` in `pyproject.toml` and as a pre-commit hook. The pinned version `0.15.13` was one minor version behind latest (`0.15.14`).

## Decision

Update both pin locations in sync:

- `pyproject.toml` dev dependency: `ruff>=0.15.13` → `ruff>=0.15.14`
- `.pre-commit-config.yaml` hook rev: `v0.15.13` → `v0.15.14`
- Run `uv lock` to update lockfile

The `>=` specifier allows uv to resolve the latest compatible version (resolved to `0.15.15`).

## Consequences

- Positive: Linter/formatter runs latest minor release with latest bugfixes and rules
- Positive: Pre-commit hooks stay in sync with project environment
- Positive: Lockfile guarantees reproducible CI runs
- Negative: Minor release may include new lint rules that require code changes (acceptable — caught by CI)

## References

- `pyproject.toml` line 79
- `.pre-commit-config.yaml` lines 14-15
- Ruff changelog: https://github.com/astral-sh/ruff/releases
