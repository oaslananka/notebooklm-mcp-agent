"""Write the generated OpenAPI schema snapshot."""

from __future__ import annotations

import json

from _repo_scan import ROOT

from notebooklm_mcp_agent.openapi import OPENAPI_SCHEMA


def main() -> int:
    target = ROOT / "docs" / "tools" / "openapi.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(OPENAPI_SCHEMA, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
