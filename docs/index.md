# NotebookLM MCP Agent

NotebookLM MCP Agent is a Python MCP server and CLI for NotebookLM workflows.

It exposes local stdio transport for desktop MCP clients and Streamable HTTP for remote clients. Remote HTTP supports `bearer` and `github-oauth` authentication. `auth_mode=none` is limited to stdio or loopback HTTP development.

This project uses `notebooklm-py`, an unofficial NotebookLM library. NotebookLM web APIs are not a public stability contract. A Google-side change can break authentication, source ingestion, chat, or artifact operations. The server validates its own MCP and OpenAPI behavior, but it cannot guarantee upstream NotebookLM API stability.

## Quick Links

- [Install](install.md)
- [Quickstart](quickstart.md)
- [Configuration](configuration.md)
- [Tools](tools/index.md)
- [Security threat model](security/threat-model.md)
- [Release process](release/process.md)
