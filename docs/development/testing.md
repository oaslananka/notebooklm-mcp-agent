# Testing

Run the full local quality gate before handing off a change:

```bash
task verify
```

```powershell
task verify
```

The default offline test suite is:

```bash
task test
```

```powershell
task test
```

`task lint` runs Ruff, formatting checks, repository hygiene scripts, OpenAPI/tool catalog parity, architecture checks, and a high-confidence Vulture dead-code scan. `task security` runs `pip-audit`, a full Bandit source scan, the repository secret-pattern check, and `gitleaks`.

Live NotebookLM tests are marked `e2e` and require explicit environment opt-in.
