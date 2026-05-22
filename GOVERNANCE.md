# Governance

NotebookLM MCP Agent is maintained by `oaslananka`.

## Maintainer Responsibilities

- Review security-sensitive changes.
- Keep release and publish workflows owner-controlled.
- Keep CI and security gates required on protected branches.
- Keep public docs aligned with implemented behavior.

## Decision Records

Non-obvious runtime, security, release, dependency, and deployment decisions belong in `docs/architecture/adr/`.

## Release Control

Publishing to PyPI or GHCR requires an explicit owner action through the release process. Build and dry-run checks may run on pull requests and default-branch pushes.
