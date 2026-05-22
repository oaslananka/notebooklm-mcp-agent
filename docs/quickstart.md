# Quickstart

## Local stdio

```bash
notebooklm-agent login
notebooklm-agent stdio
```

```powershell
notebooklm-agent login
notebooklm-agent stdio
```

Use this command from clients that launch a local MCP process.

## Loopback HTTP Development

```bash
NOTEBOOKLM_MCP_TRANSPORT=http NOTEBOOKLM_MCP_HTTP_HOST=127.0.0.1 notebooklm-agent serve --host 127.0.0.1
```

```powershell
$env:NOTEBOOKLM_MCP_TRANSPORT = "http"
$env:NOTEBOOKLM_MCP_HTTP_HOST = "127.0.0.1"
notebooklm-agent serve --host 127.0.0.1
```

## Remote HTTP

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
