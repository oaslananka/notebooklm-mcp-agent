"""NotebookLM backend adapter package."""

from notebooklm_mcp_agent.backend.client import NotebookLMBackend
from notebooklm_mcp_agent.backend.exceptions import BackendError

__all__ = ["BackendError", "NotebookLMBackend"]
