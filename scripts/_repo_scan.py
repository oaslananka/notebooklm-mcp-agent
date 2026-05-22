"""Shared repository scanning helpers."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_PARTS = {
    ".git",
    ".codex-checkpoints",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
    "site",
}

SKIP_NAMES = {
    ".coverage",
    "AUTONOMOUS_BUILD.md",
    "audit-requirements.txt",
    "coverage.xml",
    "NEXT.md",
    "PROMPT.md",
    "uv.lock",
}

TEXT_SUFFIXES = {
    "",
    ".cfg",
    ".css",
    ".dockerignore",
    ".editorconfig",
    ".example",
    ".gitattributes",
    ".gitignore",
    ".html",
    ".ini",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}


def iter_text_files(root: Path = ROOT, *, extra_skip_names: Iterable[str] = ()) -> list[Path]:
    skip_names = SKIP_NAMES | set(extra_skip_names)
    paths: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if SKIP_PARTS.intersection(relative.parts):
            continue
        if path.name in skip_names:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"Dockerfile", "Makefile"}:
            paths.append(path)
    return sorted(paths)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def rel(path: Path, root: Path = ROOT) -> str:
    return path.relative_to(root).as_posix()
