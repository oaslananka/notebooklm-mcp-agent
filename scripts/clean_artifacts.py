"""Remove local generated artifacts inside the repository."""

from __future__ import annotations

import shutil

from _repo_scan import ROOT

SKIP_DIRS = {".git", ".venv", "venv", "env"}
NAMES = {
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "audit-requirements.txt",
    "build",
    "dist",
    "htmlcov",
    "site",
}


def main() -> int:
    for path in sorted(ROOT.rglob("*"), key=lambda item: len(item.parts), reverse=True):
        if SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            continue
        if path.name in NAMES:
            if path.is_dir():
                shutil.rmtree(path)
            elif path.is_file():
                path.unlink()
        elif path.suffix == ".pyc" and path.is_file():
            path.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
