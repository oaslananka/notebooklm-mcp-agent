# Install

## Requirements

- Python `>=3.11,<3.15`
- `uv`, `pipx`, or `pip`
- A NotebookLM browser login state created by `notebooklm-agent login` or supplied through `NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_JSON`

## From PyPI

```bash
python -m pip install notebooklm-mcp-agent
notebooklm-agent --version
```

```powershell
python -m pip install notebooklm-mcp-agent
notebooklm-agent --version
```

## With uv Tool

```bash
uv tool install notebooklm-mcp-agent --with notebooklm-mcp-agent[browser]
notebooklm-agent login
notebooklm-agent stdio
```

```powershell
uv tool install notebooklm-mcp-agent --with notebooklm-mcp-agent[browser]
notebooklm-agent login
notebooklm-agent stdio
```

## From Source

```bash
git clone https://github.com/oaslananka/notebooklm-mcp-agent
cd notebooklm-mcp-agent
uv sync --locked --extra dev --extra browser
uv run notebooklm-agent doctor
```

```powershell
git clone https://github.com/oaslananka/notebooklm-mcp-agent
cd notebooklm-mcp-agent
uv sync --locked --extra dev --extra browser
uv run notebooklm-agent doctor
```
