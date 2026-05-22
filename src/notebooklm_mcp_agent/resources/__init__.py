"""NotebookLM MCP resource registration."""

from notebooklm_mcp_agent.resources.artifact import register_artifact_resources
from notebooklm_mcp_agent.resources.notebook import register_core_resources

__all__ = ["register_artifact_resources", "register_core_resources"]
