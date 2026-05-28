# ADR Index

Decision records live here when a non-obvious tradeoff affects supported runtime, security, dependency, release, or deployment behavior.

Current decisions:

- Streamable HTTP is the remote transport; SSE is not the primary transport.
- `notebooklm_mcp_agent` is the canonical import package.
- `nlm_mcp` remains only as a one-major-cycle compatibility shim.
- Starlette >= 1.0.1 required (CVE-2026-48710) — [ADR 003](003-starlette-cve-pin.md)
- Branch protection enforced on main — [ADR 004](004-branch-protection.md)
- GitHub Actions concurrency groups for cancel-in-progress — [ADR 005](005-concurrency-groups.md)
- Ruff toolchain version tracking — [ADR 006](006-ruff-toolchain-update.md)
