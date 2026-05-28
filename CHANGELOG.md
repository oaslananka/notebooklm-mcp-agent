# Changelog

## 1.0.0 (2026-05-28)


### Bug Fixes

* resolve CVE-2026-48710, update deps, add branch protection, concurrency groups, ADR docs ([ac10eb6](https://github.com/oaslananka/notebooklm-mcp-agent/commit/ac10eb6e7911a7106ffdc2deb3b88007384e5d49))

## 1.0.0 - 2026-05-19

Initial public release preparation for `notebooklm-mcp-agent`.

### Added

- Canonical package metadata for `notebooklm-mcp-agent`.
- Canonical Python package `notebooklm_mcp_agent`.
- CLI executable `notebooklm-agent`.
- MCP stdio transport and Streamable HTTP transport.
- Bearer and GitHub OAuth authentication for remote HTTP.
- Startup rejection for public HTTP with `auth_mode=none`.
- OpenAPI 3.1 schema generation for HTTP clients.
- Tool catalog coverage for notebook, source, chat, research, artifact, language, compatibility, and admin tools.
- Dockerfile and Docker Compose files for owner-operated deployments.
- CI, docs, CodeQL, dependency review, security, Scorecard, Release Please, and publish build-check workflows.

### Changed

- Project identity now points only to `oaslananka/notebooklm-mcp-agent`.
- `NOTEBOOKLM_MCP_` is the configuration environment prefix.

### Security

- Query-parameter bearer authentication is removed.
- GitHub OAuth requires a non-empty allowlist.
- Invalid browser `Origin` headers return HTTP 403.
