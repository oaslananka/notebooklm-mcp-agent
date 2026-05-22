"""Lightweight secret and local-artifact guard."""

from __future__ import annotations

import re

from _repo_scan import ROOT, iter_text_files, read_text, rel

FORBIDDEN_FILENAMES = {
    ".env",
    "auth.json",
    "credentials.json",
    "storage_state.json",
    "notebooklm_auth.json",
    "cookies.json",
}
FORBIDDEN_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".kubeconfig"}
SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "site",
    "dist",
    "build",
}
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----"),
    re.compile(r"Authorization:\s*Bearer\s+[A-Za-z0-9._~+/=-]{16,}", re.IGNORECASE),
    re.compile(
        r"(?m)^\s*(?:access_token|refresh_token|client_secret|password)\s*=\s*"
        r"['\"]?[A-Za-z0-9._~+/=-]{20,}['\"]?\s*$",
        re.IGNORECASE,
    ),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
]


def main() -> int:
    findings: list[str] = []
    for path in ROOT.rglob("*"):
        if SKIP_DIRS.intersection(path.parts) or not path.is_file():
            continue
        if path.name in FORBIDDEN_FILENAMES and path.name != ".env.example":
            findings.append(f"{rel(path)}: forbidden local secret-bearing file")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(f"{rel(path)}: forbidden secret-bearing suffix")
    for path in iter_text_files(ROOT, extra_skip_names={"check_no_secrets.py", ".env.example"}):
        text = read_text(path)
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(f"{rel(path)}: secret-shaped content matched {pattern.pattern}")
    if findings:
        print("Secret check failed:")
        print("\n".join(f"- {finding}" for finding in sorted(findings)))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
