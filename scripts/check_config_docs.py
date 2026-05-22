"""Verify implemented settings are documented in expected surfaces."""

from __future__ import annotations

from _repo_scan import ROOT, read_text, rel

ENV_VARS = [
    "NOTEBOOKLM_MCP_TRANSPORT",
    "NOTEBOOKLM_MCP_HTTP_HOST",
    "NOTEBOOKLM_MCP_HTTP_PORT",
    "NOTEBOOKLM_MCP_HTTP_PATH",
    "NOTEBOOKLM_MCP_STATELESS_HTTP",
    "NOTEBOOKLM_MCP_BASE_URL",
    "NOTEBOOKLM_MCP_AUTH_MODE",
    "NOTEBOOKLM_MCP_BEARER_TOKEN",
    "NOTEBOOKLM_MCP_GITHUB_CLIENT_ID",
    "NOTEBOOKLM_MCP_GITHUB_CLIENT_SECRET",
    "NOTEBOOKLM_MCP_GITHUB_REDIRECT_PATH",
    "NOTEBOOKLM_MCP_OAUTH_REQUIRED_SCOPES",
    "NOTEBOOKLM_MCP_OAUTH_ALLOWED_USERS",
    "NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_FILE",
    "NOTEBOOKLM_MCP_NOTEBOOKLM_AUTH_JSON",
    "NOTEBOOKLM_MCP_DATA_DIR",
    "NOTEBOOKLM_MCP_SESSION_DB",
    "NOTEBOOKLM_MCP_LOG_LEVEL",
    "NOTEBOOKLM_MCP_LOG_FORMAT",
    "NOTEBOOKLM_MCP_DESTRUCTIVE_REQUIRES_CONFIRM",
    "NOTEBOOKLM_MCP_DEFAULT_POLL_INTERVAL_SEC",
    "NOTEBOOKLM_MCP_DEFAULT_POLL_TIMEOUT_SEC",
]
DOCS = [
    ROOT / ".env.example",
    ROOT / "README.md",
    ROOT / "docs" / "configuration.md",
    ROOT / "docs" / "security" / "threat-model.md",
]
REMOVED = [
    "NOTEBOOKLM_MCP_TOKEN_QUERY_PARAM",
    "NOTEBOOKLM_MCP_REDIS_URL",
    "NOTEBOOKLM_MCP_ENCRYPTION_KEY",
    "NOTEBOOKLM_MCP_RATE_LIMIT_ENABLED",
    "NOTEBOOKLM_MCP_AUDIT_LOG_PATH",
]


def main() -> int:
    findings: list[str] = []
    for doc in DOCS:
        if not doc.exists():
            findings.append(f"{rel(doc)}: missing")
            continue
        text = read_text(doc)
        for env_var in ENV_VARS:
            if env_var not in text:
                findings.append(f"{rel(doc)}: missing {env_var}")
        for env_var in REMOVED:
            if env_var in text:
                findings.append(f"{rel(doc)}: removed setting still documented: {env_var}")
    settings_text = read_text(ROOT / "src" / "notebooklm_mcp_agent" / "config.py")
    for env_var in REMOVED:
        field_name = env_var.removeprefix("NOTEBOOKLM_MCP_").lower()
        if field_name in settings_text:
            findings.append(f"config.py: removed setting still implemented: {field_name}")
    if findings:
        print("Config documentation parity failed:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
