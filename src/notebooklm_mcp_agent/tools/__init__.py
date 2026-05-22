"""Tool registration package for NotebookLM MCP."""

from notebooklm_mcp_agent.tools.admin import HealthOutput, VersionOutput, register_admin_tools
from notebooklm_mcp_agent.tools.artifacts import register_artifact_tools
from notebooklm_mcp_agent.tools.chat import register_chat_tools
from notebooklm_mcp_agent.tools.compat import register_compat_tools
from notebooklm_mcp_agent.tools.language import register_language_tools
from notebooklm_mcp_agent.tools.notebooks import register_notebook_tools
from notebooklm_mcp_agent.tools.research import register_research_tools
from notebooklm_mcp_agent.tools.sources import register_source_tools

__all__ = [
    "HealthOutput",
    "VersionOutput",
    "register_admin_tools",
    "register_artifact_tools",
    "register_chat_tools",
    "register_compat_tools",
    "register_language_tools",
    "register_notebook_tools",
    "register_research_tools",
    "register_source_tools",
]
