# Claude Desktop

Use stdio for local Claude Desktop configuration.

```json
{
  "mcpServers": {
    "notebooklm-agent": {
      "command": "notebooklm-agent",
      "args": ["stdio"],
      "env": {
        "NOTEBOOKLM_MCP_LOG_LEVEL": "WARNING"
      }
    }
  }
}
```
