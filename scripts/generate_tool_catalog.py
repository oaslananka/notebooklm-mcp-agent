"""Regenerate docs/tools/catalog.md from OpenAPI tool specs."""

from __future__ import annotations

from _repo_scan import ROOT

from notebooklm_mcp_agent.openapi import TOOL_SPECS


def main() -> int:
    target = ROOT / "docs" / "tools" / "catalog.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Tool Catalog",
        "",
        "| Tool | Group | Summary |",
        "|---|---|---|",
    ]
    for spec in TOOL_SPECS:
        lines.append(f"| `{spec.name}` | {spec.tag} | {spec.summary} |")
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
