"""Compatibility shim for the legacy ``nlm_mcp`` import package."""

from __future__ import annotations

import warnings

from notebooklm_mcp_agent import __author__, __license__, __version__

warnings.warn(
    "The nlm_mcp import path is deprecated; use notebooklm_mcp_agent instead.",
    DeprecationWarning,
    stacklevel=2,
)

__all__ = ["__author__", "__license__", "__version__"]
