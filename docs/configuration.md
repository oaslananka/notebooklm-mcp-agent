# Configuration

Settings are read from CLI flags, environment variables, and `.env`. Environment variables use the `NOTEBOOKLM_MCP_` prefix.

| Variable | Default | Notes |
|---|---|---|
| `NOTEBOOKLM_MCP_TRANSPORT` | `stdio` | `stdio` or `http`. |
| `NOTEBOOKLM_MCP_HTTP_HOST` | `0.0.0.0` | HTTP bind address. `none` auth requires loopback. |
| `NOTEBOOKLM_MCP_HTTP_PORT` | `8080` | HTTP port. |
| `NOTEBOOKLM_MCP_HTTP_PATH` | `/mcp` | Streamable HTTP MCP endpoint. |
| `NOTEBOOKLM_MCP_STATELESS_HTTP` | `true` | FastMCP stateless HTTP mode. |
| `NOTEBOOKLM_MCP_BASE_URL` | unset | Public URL for OpenAPI and OAuth redirects. |
| `NOTEBOOKLM_MCP_AUTH_MODE` | `none` | `none`, `bearer`, or `github-oauth`. |
| `NOTEBOOKLM_MCP_BEARER_TOKEN` | unset | Required for `bearer` HTTP auth. |
| `NOTEBOOKLM_MCP_GITHUB_CLIENT_ID` | unset | Required for GitHub OAuth. |
| `NOTEBOOKLM_MCP_GITHUB_CLIENT_SECRET` | unset | Required for GitHub OAuth; never log it. |
| `NOTEBOOKLM_MCP_GITHUB_REDIRECT_PATH` | `/auth/callback` | GitHub OAuth callback path. |
| `NOTEBOOKLM_MCP_OAUTH_REQUIRED_SCOPES` | `read:user,user:email` | GitHub scopes. |
| `NOTEBOOKLM_MCP_OAUTH_ALLOWED_USERS` | `oaslananka` | Required allowlist. Empty is invalid. |
| `NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_FILE` | `~/.config/notebooklm-agent/notebooklm_auth.json` | Browser login state path. |
| `NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_JSON` | unset | Inline NotebookLM storage JSON for managed secrets. |
| `NOTEBOOKLM_MCP_DATA_DIR` | `~/.local/share/notebooklm-agent` | Runtime task/session data. |
| `NOTEBOOKLM_MCP_SESSION_DB` | derived | SQLite URL; `{DATA_DIR}` is replaced at runtime. |
| `NOTEBOOKLM_MCP_LOG_LEVEL` | `INFO` | Python log level. |
| `NOTEBOOKLM_MCP_LOG_FORMAT` | `json` | `json` or `console`. |
| `NOTEBOOKLM_MCP_DESTRUCTIVE_REQUIRES_CONFIRM` | `true` | Destructive tools require `confirm=true`. |
| `NOTEBOOKLM_MCP_DEFAULT_POLL_INTERVAL_SEC` | `15` | Artifact/source polling interval. |
| `NOTEBOOKLM_MCP_DEFAULT_POLL_TIMEOUT_SEC` | `600` | Artifact/source polling timeout. |

Public HTTP with `NOTEBOOKLM_MCP_AUTH_MODE=none` fails at startup. Query-parameter bearer authentication is not supported; use `Authorization: Bearer`.
