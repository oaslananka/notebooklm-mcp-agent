# ADR Index

Decision records live here when a non-obvious tradeoff affects supported runtime, security, dependency, release, or deployment behavior.

Current decisions:

- Streamable HTTP is the remote transport; SSE is not the primary transport.
- `notebooklm_mcp_agent` is the canonical import package.
- `nlm_mcp` remains only as a one-major-cycle compatibility shim.
