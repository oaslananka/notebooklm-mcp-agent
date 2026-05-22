"""Verify release metadata is internally consistent without publishing."""

from __future__ import annotations

import os
import re
import subprocess
import tempfile
import tomllib
import venv
from pathlib import Path

from _repo_scan import ROOT, read_text


def main() -> int:
    findings: list[str] = []
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    version = project["version"]
    if version != "1.0.0":
        findings.append("initial release version must be 1.0.0")
    init_text = read_text(ROOT / "src" / "notebooklm_mcp_agent" / "__init__.py")
    if f'__version__ = "{version}"' not in init_text:
        findings.append("__init__.__version__ must match pyproject")
    changelog = read_text(ROOT / "CHANGELOG.md")
    if not re.search(r"## \[?1\.0\.0\]?", changelog):
        findings.append("CHANGELOG.md must contain a 1.0.0 entry")
    findings.extend(_verify_dist_artifacts(version))
    if findings:
        print("Release readiness check failed:")
        print("\n".join(f"- {finding}" for finding in findings))
        return 1
    return 0


def _verify_dist_artifacts(version: str) -> list[str]:
    findings: list[str] = []
    dist_dir = ROOT / "dist"
    wheel = dist_dir / f"notebooklm_mcp_agent-{version}-py3-none-any.whl"
    sdist = dist_dir / f"notebooklm_mcp_agent-{version}.tar.gz"
    sbom = dist_dir / "notebooklm-mcp-agent.sbom.json"
    for path in (wheel, sdist, sbom):
        if not path.exists():
            findings.append(f"missing release artifact: {path.relative_to(ROOT)}")
    if not wheel.exists():
        return findings
    findings.extend(_smoke_install_wheel(wheel, version))
    return findings


def _smoke_install_wheel(wheel: Path, version: str) -> list[str]:
    findings: list[str] = []
    with tempfile.TemporaryDirectory(prefix="notebooklm-agent-release-") as temp_dir:
        venv_dir = Path(temp_dir) / "venv"
        venv.EnvBuilder(with_pip=True).create(venv_dir)
        bin_dir = "Scripts" if os.name == "nt" else "bin"
        python = venv_dir / bin_dir / ("python.exe" if os.name == "nt" else "python")
        commands = [
            [
                str(python),
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                str(wheel),
            ],
            [str(python), "-m", "notebooklm_mcp_agent", "--version"],
            [str(python), "-m", "notebooklm_mcp_agent", "doctor", "--offline"],
            [
                str(python),
                "-c",
                (
                    "import importlib.metadata as m; "
                    "assert m.version('notebooklm-mcp-agent') == "
                    f"{version!r}"
                ),
            ],
        ]
        for command in commands:
            result = subprocess.run(  # noqa: S603
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            output = f"{result.stdout}\n{result.stderr}"
            if result.returncode != 0:
                findings.append(
                    f"release smoke command failed ({' '.join(command[:3])}): {output.strip()}"
                )
                continue
            lowered = output.casefold()
            if "warning" in lowered or "deprecat" in lowered:
                findings.append(f"release smoke command emitted warning ({' '.join(command[:3])})")
        version_result = subprocess.run(  # noqa: S603
            [str(python), "-m", "notebooklm_mcp_agent", "--version"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if f"notebooklm-agent {version}" not in version_result.stdout:
            findings.append("installed CLI --version output did not include expected version")
    return findings


if __name__ == "__main__":
    raise SystemExit(main())
