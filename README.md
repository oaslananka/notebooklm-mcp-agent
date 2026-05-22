# NotebookLM MCP Agent

NotebookLM MCP Agent is a Python MCP server and CLI for NotebookLM workflows.

Status: `1.0.0` release-ready bootstrap. Publishing is owner-triggered only.

## Install

```bash
python -m pip install notebooklm-mcp-agent
notebooklm-agent --version
```

```powershell
python -m pip install notebooklm-mcp-agent
notebooklm-agent --version
```

## Quickstart

Local stdio:

```bash
notebooklm-agent login
notebooklm-agent stdio
```

```powershell
notebooklm-agent login
notebooklm-agent stdio
```

Loopback HTTP:

```bash
NOTEBOOKLM_MCP_TRANSPORT=http NOTEBOOKLM_MCP_HTTP_HOST=127.0.0.1 notebooklm-agent serve --host 127.0.0.1
```

```powershell
$env:NOTEBOOKLM_MCP_TRANSPORT = "http"
$env:NOTEBOOKLM_MCP_HTTP_HOST = "127.0.0.1"
notebooklm-agent serve --host 127.0.0.1
```

Remote HTTP with bearer authentication:

```bash
export NOTEBOOKLM_MCP_TRANSPORT=http
export NOTEBOOKLM_MCP_AUTH_MODE=bearer
export NOTEBOOKLM_MCP_BEARER_TOKEN="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
export NOTEBOOKLM_MCP_BASE_URL=https://your-server.example.com
notebooklm-agent serve --host 0.0.0.0 --port 8080
```

```powershell
$env:NOTEBOOKLM_MCP_TRANSPORT = "http"
$env:NOTEBOOKLM_MCP_AUTH_MODE = "bearer"
$env:NOTEBOOKLM_MCP_BEARER_TOKEN = python -c "import secrets; print(secrets.token_urlsafe(32))"
$env:NOTEBOOKLM_MCP_BASE_URL = "https://your-server.example.com"
notebooklm-agent serve --host 0.0.0.0 --port 8080
```

## Client Setup

- Stdio clients launch `notebooklm-agent stdio`.
- Streamable HTTP clients connect to `NOTEBOOKLM_MCP_BASE_URL` plus `NOTEBOOKLM_MCP_HTTP_PATH`.
- OpenAPI clients use `/openapi.json`.

## Auth Modes

- `none`: allowed only for stdio or loopback HTTP.
- `bearer`: requires `Authorization: Bearer` and `NOTEBOOKLM_MCP_BEARER_TOKEN`.
- `github-oauth`: requires GitHub OAuth credentials and `NOTEBOOKLM_MCP_OAUTH_ALLOWED_USERS`.

## Configuration

Supported settings: `NOTEBOOKLM_MCP_TRANSPORT`, `NOTEBOOKLM_MCP_HTTP_HOST`, `NOTEBOOKLM_MCP_HTTP_PORT`, `NOTEBOOKLM_MCP_HTTP_PATH`, `NOTEBOOKLM_MCP_STATELESS_HTTP`, `NOTEBOOKLM_MCP_BASE_URL`, `NOTEBOOKLM_MCP_AUTH_MODE`, `NOTEBOOKLM_MCP_BEARER_TOKEN`, `NOTEBOOKLM_MCP_GITHUB_CLIENT_ID`, `NOTEBOOKLM_MCP_GITHUB_CLIENT_SECRET`, `NOTEBOOKLM_MCP_GITHUB_REDIRECT_PATH`, `NOTEBOOKLM_MCP_OAUTH_REQUIRED_SCOPES`, `NOTEBOOKLM_MCP_OAUTH_ALLOWED_USERS`, `NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_FILE`, `NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_JSON`, `NOTEBOOKLM_MCP_DATA_DIR`, `NOTEBOOKLM_MCP_SESSION_DB`, `NOTEBOOKLM_MCP_LOG_LEVEL`, `NOTEBOOKLM_MCP_LOG_FORMAT`, `NOTEBOOKLM_MCP_DESTRUCTIVE_REQUIRES_CONFIRM`, `NOTEBOOKLM_MCP_DEFAULT_POLL_INTERVAL_SEC`, and `NOTEBOOKLM_MCP_DEFAULT_POLL_TIMEOUT_SEC`.

See the canonical docs site: <https://oaslananka.github.io/notebooklm-mcp-agent/>.

## NotebookLM Limitation

This project uses `notebooklm-py`, an unofficial NotebookLM library. NotebookLM web APIs are not a public stability contract. A Google-side change can break authentication, source ingestion, chat, or artifact operations. The server validates its own MCP/OpenAPI behavior, but it cannot guarantee upstream NotebookLM API stability.

The project is not official Google software and is not affiliated with, endorsed by, or certified by Google.

## Security Defaults

- Public HTTP without auth fails at startup.
- Query-parameter bearer authentication is not accepted.
- Invalid browser `Origin` headers return HTTP 403.
- GitHub OAuth requires an allowlist; examples use `oaslananka`.
- Destructive NotebookLM operations require explicit confirmation.
- Secret material belongs in environment or secret stores, not repository files.

## Development

```bash
uv sync --locked --extra dev --extra browser
task verify
```

```powershell
uv sync --locked --extra dev --extra browser
task verify
```

## License

MIT. See [LICENSE](LICENSE).
