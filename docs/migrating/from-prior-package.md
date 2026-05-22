# Migration From The Prior Package

The canonical repository is `oaslananka/notebooklm-mcp-agent`.

Use:

- PyPI package: `notebooklm-mcp-agent`
- Python import: `notebooklm_mcp_agent`
- CLI: `notebooklm-agent`
- Image: `ghcr.io/oaslananka/notebooklm-mcp-agent`

The legacy `nlm_mcp` Python import remains as a compatibility shim for one major cycle. New code should import `notebooklm_mcp_agent`.
