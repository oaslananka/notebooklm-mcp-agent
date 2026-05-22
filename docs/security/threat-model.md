# Threat Model

NotebookLM MCP Agent has two trust zones: local stdio and remote Streamable HTTP.

Configuration variables covered by this model: `NOTEBOOKLM_MCP_TRANSPORT`, `NOTEBOOKLM_MCP_HTTP_HOST`, `NOTEBOOKLM_MCP_HTTP_PORT`, `NOTEBOOKLM_MCP_HTTP_PATH`, `NOTEBOOKLM_MCP_STATELESS_HTTP`, `NOTEBOOKLM_MCP_BASE_URL`, `NOTEBOOKLM_MCP_AUTH_MODE`, `NOTEBOOKLM_MCP_BEARER_TOKEN`, `NOTEBOOKLM_MCP_GITHUB_CLIENT_ID`, `NOTEBOOKLM_MCP_GITHUB_CLIENT_SECRET`, `NOTEBOOKLM_MCP_GITHUB_REDIRECT_PATH`, `NOTEBOOKLM_MCP_OAUTH_REQUIRED_SCOPES`, `NOTEBOOKLM_MCP_OAUTH_ALLOWED_USERS`, `NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_FILE`, `NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_JSON`, `NOTEBOOKLM_MCP_DATA_DIR`, `NOTEBOOKLM_MCP_SESSION_DB`, `NOTEBOOKLM_MCP_LOG_LEVEL`, `NOTEBOOKLM_MCP_LOG_FORMAT`, `NOTEBOOKLM_MCP_DESTRUCTIVE_REQUIRES_CONFIRM`, `NOTEBOOKLM_MCP_DEFAULT_POLL_INTERVAL_SEC`, and `NOTEBOOKLM_MCP_DEFAULT_POLL_TIMEOUT_SEC`.

## Controls

- Public HTTP requires `bearer` or `github-oauth`.
- `none` authentication is limited to stdio or loopback HTTP.
- Bearer credentials are accepted only from the `Authorization` header.
- GitHub OAuth requires an allowlist; the default allowlist is `oaslananka`.
- Invalid browser `Origin` headers are rejected with HTTP 403.
- NotebookLM auth files, inline auth JSON, OAuth secrets, cookies, and bearer values are secret material.
- Destructive tools require explicit confirmation.

## Upstream Limitation

This project uses `notebooklm-py`, an unofficial NotebookLM library. NotebookLM web APIs are not a public stability contract. A Google-side change can break authentication, source ingestion, chat, or artifact operations.
