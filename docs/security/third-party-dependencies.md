# Third-Party Dependencies

Current source checks:

| Dependency | Selected range | Source checked | Reason |
|---|---:|---|---|
| Python | `>=3.11,<3.15` | Python release schedule | Covers 3.11 through current 3.14 maintenance. |
| `mcp` | `>=1.27.1,<2` | PyPI JSON and MCP Python SDK docs | Current stable SDK line. |
| `fastmcp` | `>=3.3.1,<4` | PyPI JSON and FastMCP docs | Current stable FastMCP line. |
| `opentelemetry-api` | `<1.42` resolver constraint | OpenTelemetry source and local warning-as-error test | Keeps FastMCP import warning-clean on Python 3.11 until upstream removes deprecated `SelectableGroups.values()` usage. |
| `notebooklm-py` | `>=0.4.1,<0.5` | PyPI JSON | Current stable upstream boundary. |
| `uv` | `0.11.15` in CI and Docker | uv GitHub releases and Docker image metadata | Current stable installer/container version. |
| GitHub Actions | SHA-pinned actions with Node24 or Docker metadata | Official action metadata | Avoids deprecated JavaScript action runtimes. |
| Bandit | `>=1.8` | PyCQA Bandit docs and local scan output | Full source scan runs without severity filtering. |
| Vulture | `>=2.14` | Vulture docs and local scan output | High-confidence dead-code scan is part of lint and CI. |
