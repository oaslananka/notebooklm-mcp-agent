"""Generate SHA256 checksums for files in a directory."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    target_dir = Path(args[0] if args else "dist")
    if not target_dir.exists():
        print(f"{target_dir} does not exist")
        return 1
    checksum_file = target_dir / "SHA256SUMS"
    lines: list[str] = []
    for path in sorted(target_dir.iterdir()):
        if not path.is_file() or path.name == checksum_file.name:
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.name}")
    checksum_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
