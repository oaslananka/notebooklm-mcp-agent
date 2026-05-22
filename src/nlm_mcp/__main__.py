"""Compatibility entrypoint for ``python -m nlm_mcp``."""

from __future__ import annotations

from notebooklm_mcp_agent.cli import app

if __name__ == "__main__":
    app()
