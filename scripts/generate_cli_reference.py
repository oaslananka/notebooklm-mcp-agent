"""Write a minimal CLI reference page."""

from __future__ import annotations

from _repo_scan import ROOT


def main() -> int:
    target = ROOT / "docs" / "development" / "cli-reference.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        "\n".join(
            [
                "# CLI Reference",
                "",
                "`notebooklm-agent --version` prints package version metadata.",
                "",
                (
                    "`notebooklm-agent doctor` prints offline diagnostics without contacting "
                    "NotebookLM."
                ),
                "",
                "`notebooklm-agent stdio` starts the local MCP stdio transport.",
                "",
                "`notebooklm-agent serve --host 127.0.0.1 --port 8080` starts Streamable HTTP.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
