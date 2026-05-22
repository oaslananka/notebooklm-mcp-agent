"""Smoke-check documentation command examples for removed names."""

from __future__ import annotations

from _repo_scan import ROOT, iter_text_files, read_text, rel

REMOVED_COMMANDS = (
    "nlm-" + "mcp ",
    "notebooklm" + "-mcp-" + "pro",
    "NLM" + "_MCP_",
)


def main() -> int:
    findings: list[str] = []
    for path in iter_text_files(ROOT / "docs"):
        text = read_text(path)
        for command in REMOVED_COMMANDS:
            if command in text:
                findings.append(f"{rel(path)}: removed command/config reference {command}")
    if findings:
        print("Documentation command check failed:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
