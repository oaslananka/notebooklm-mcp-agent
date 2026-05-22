"""Verify canonical project identity and URL references."""

from __future__ import annotations

import re

from _repo_scan import ROOT, iter_text_files, read_text, rel

PROJECT_URL_PATTERN = re.compile(
    r"https://(?:github\.com/oaslananka|oaslananka\.github\.io|pypi\.org/project|ghcr\.io/oaslananka)/[^\s)\]\"']+"
)
ALLOWED_PREFIXES = (
    "https://github.com/oaslananka/notebooklm-mcp-agent",
    "https://oaslananka.github.io/notebooklm-mcp-agent/",
    "https://pypi.org/project/notebooklm-mcp-agent/",
    "https://ghcr.io/oaslananka/notebooklm-mcp-agent",
)
FORBIDDEN_IDENTITY = (
    "notebooklm" + "-mcp-" + "pro",
    "notebooklm" + "_mcp_" + "pro",
    "nlm" + "-mcp-" + "pro",
)


def main() -> int:
    findings: list[str] = []
    for path in iter_text_files(ROOT, extra_skip_names={"check_owner_refs.py"}):
        text = read_text(path)
        for term in FORBIDDEN_IDENTITY:
            if term.casefold() in text.casefold():
                findings.append(f"{rel(path)}: forbidden identity reference: {term}")
        for match in PROJECT_URL_PATTERN.finditer(text):
            url = match.group(0).rstrip(".,")
            if _allowed_external_url(url):
                continue
            findings.append(f"{rel(path)}: non-canonical project URL: {url}")
    if findings:
        print("Owner reference check failed:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    return 0


def _allowed_external_url(url: str) -> bool:
    return url.startswith(ALLOWED_PREFIXES) or url.startswith("https://github.com/login/oauth/")


if __name__ == "__main__":
    raise SystemExit(main())
