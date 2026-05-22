"""Verify OpenAPI paths and operation IDs match the tool spec list."""

from __future__ import annotations

import sys

from _repo_scan import ROOT

sys.path.insert(0, str(ROOT / "src"))

from notebooklm_mcp_agent import openapi


def main() -> int:
    findings: list[str] = []
    paths = openapi.OPENAPI_SCHEMA["paths"]
    for spec in openapi.TOOL_SPECS:
        path = f"/tools/{spec.name}"
        if path not in paths:
            findings.append(f"missing OpenAPI path for {spec.name}")
            continue
        operation_id = paths[path]["post"].get("operationId")
        expected = spec.name.replace(".", "_")
        if operation_id != expected:
            findings.append(f"{spec.name}: operationId {operation_id!r} != {expected!r}")
    extra = sorted(set(paths) - {f"/tools/{spec.name}" for spec in openapi.TOOL_SPECS})
    findings.extend(f"unexpected OpenAPI path {path}" for path in extra)
    if findings:
        print("OpenAPI parity failed:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
