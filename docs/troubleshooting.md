# Troubleshooting

| Symptom | Check |
|---|---|
| HTTP server exits at startup | Public HTTP needs `NOTEBOOKLM_MCP_AUTH_MODE=bearer` or `github-oauth`. |
| Browser client receives 403 | Check the `Origin` header and `NOTEBOOKLM_MCP_BASE_URL`. |
| OAuth login rejected | Confirm `NOTEBOOKLM_MCP_OAUTH_ALLOWED_USERS` includes the GitHub login. |
| NotebookLM calls fail | Re-run `notebooklm-agent login` and replace the configured auth file. |
