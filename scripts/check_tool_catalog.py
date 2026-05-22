"""Verify generated tool catalog contains every OpenAPI tool spec."""

from __future__ import annotations

import sys

from _repo_scan import ROOT, read_text

sys.path.insert(0, str(ROOT / "src"))

from notebooklm_mcp_agent import openapi


def main() -> int:
    catalog = ROOT / "docs" / "tools" / "catalog.md"
    if not catalog.exists():
        print("docs/tools/catalog.md is missing")
        return 1
    text = read_text(catalog)
    missing = [spec.name for spec in openapi.TOOL_SPECS if spec.name not in text]
    if missing:
        print("Tool catalog is missing entries:")
        print("\n".join(f"- {name}" for name in missing))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
