# ChatGPT

Expose Streamable HTTP with `NOTEBOOKLM_MCP_AUTH_MODE=bearer` or `github-oauth`, then use `/openapi.json` for action schema discovery.

Required public settings:

```text
NOTEBOOKLM_MCP_TRANSPORT=http
NOTEBOOKLM_MCP_AUTH_MODE=bearer
NOTEBOOKLM_MCP_BEARER_TOKEN=<managed secret>
NOTEBOOKLM_MCP_BASE_URL=https://your-server.example.com
```
