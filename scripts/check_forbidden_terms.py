"""Fail when repository content contains banned platform or hype terms."""

from __future__ import annotations

import re

from _repo_scan import ROOT, iter_text_files, read_text, rel

FORBIDDEN_PATTERNS = [
    "notebooklm" + r"-mcp-" + "pro",
    "notebooklm" + r"_mcp_" + "pro",
    "nlm" + r"-mcp-" + "pro",
    r"\bdop" + r"pler\b",
    r"\bgit" + r"lab\b",
    r"git" + r"lab\.com",
    r"\baz" + "u" + r"re\b",
    r"az" + "u" + r"re\.com",
    r"az" + "u" + "rewebsites",
    r"mir" + r"ror[-_ ]?publish",
    r"\bmir" + r"ror\b",
    r"\brail" + r"way\b",
    r"fly\.io",
    r"fly\.toml",
    r"\bkuber" + r"netes\b",
    r"\bk8s\b",
    r"\bself-" + r"hosted\b",
    r"\bprepare-" + r"workspace\b",
    r"best in " + "class",
    r"world-" + "class",
    r"industry-" + "leading",
    r"cutting-" + "edge",
    r"state of the " + "art",
    r"\bper" + r"fect\b",
    r"\bflaw" + r"less\b",
    r"100% as " + "hype",
    r"principal " + "developer",
    r"principle " + "developer",
    r"professional " + "grade",
    r"enterprise " + "grade",
    r"production " + "grade",
    r"production-" + "grade",
    r"robust " + "solution",
    r"powerful " + "tool",
    r"\bamaz" + r"ing\b",
    r"\bun" + r"leash\b",
    r"\bsuper" + r"charge\b",
    r"\brevol" + r"utionize\b",
    r"\bsky" + r"rocket\b",
    r"\bdel" + r"ight\b",
    r"as you can " + "see",
    r"needless to " + "say",
    r"without further " + "ado",
    r"in " + "conclusion",
    r"for " + "everyone",
    r"trusted by " + "thousands",
    "Generated " + "by",
    "AI-" + "generated",
    "Co-" + "authored-by: " + "Claude",
    "Co-" + "authored-by: " + "GPT",
    "Co-" + "authored-by: " + "Codex",
]


def main() -> int:
    findings: list[str] = []
    patterns = [re.compile(pattern, re.IGNORECASE) for pattern in FORBIDDEN_PATTERNS]
    for path in iter_text_files(ROOT, extra_skip_names={"check_forbidden_terms.py"}):
        for line_number, line in enumerate(read_text(path).splitlines(), start=1):
            for pattern in patterns:
                if pattern.search(line):
                    findings.append(f"{rel(path)}:{line_number}: {pattern.pattern}")
    if findings:
        print("Forbidden terms found:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
