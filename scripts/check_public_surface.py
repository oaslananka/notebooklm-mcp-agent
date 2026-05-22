"""Verify public package, import, and CLI metadata."""

from __future__ import annotations

import importlib
import sys
import tomllib

from _repo_scan import ROOT

sys.path.insert(0, str(ROOT / "src"))


def main() -> int:
    findings: list[str] = []
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = data["project"]
    if project["name"] != "notebooklm-mcp-agent":
        findings.append("project.name must be notebooklm-mcp-agent")
    if project["version"] != "1.0.0":
        findings.append("project.version must be 1.0.0")
    if project["requires-python"] != ">=3.11,<3.15":
        findings.append("requires-python must be >=3.11,<3.15")
    scripts = project.get("scripts", {})
    if scripts.get("notebooklm-agent") != "notebooklm_mcp_agent.cli:app":
        findings.append("notebooklm-agent script must point at notebooklm_mcp_agent.cli:app")
    package = importlib.import_module("notebooklm_mcp_agent")
    if getattr(package, "__version__", "") != project["version"]:
        findings.append("package __version__ must match pyproject version")
    try:
        importlib.import_module("nlm_mcp")
    except Exception as exc:  # pragma: no cover - script diagnostics
        findings.append(f"legacy nlm_mcp shim must import: {exc}")
    if findings:
        print("Public surface check failed:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
