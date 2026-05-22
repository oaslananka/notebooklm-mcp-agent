# Branch Protection

Target default branch rules:

- Pull request required after initial bootstrap.
- Required PR checks: `CI`, `Docs`, `CodeQL`, `Dependency Review`, `Security`, and `Publish / build check`.
- Main-only release readiness workflows that must stay green after merge: `OpenSSF Scorecard` and `Release Please`.
- Conversation resolution required.
- Force pushes disabled.
- Branch deletion disabled.
- Linear history preferred when owner workflow supports it.

Setup helpers:

```bash
scripts/setup-branch-protection.sh oaslananka/notebooklm-mcp-agent main
```

```powershell
scripts/setup-branch-protection.ps1 -Repo oaslananka/notebooklm-mcp-agent -Branch main
```
