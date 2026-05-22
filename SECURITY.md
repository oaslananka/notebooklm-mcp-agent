# Security Policy

## Supported Versions

The first supported release line is `1.x`.

## Reporting

Report vulnerabilities through GitHub private vulnerability reporting when available:

<https://github.com/oaslananka/notebooklm-mcp-agent/security/advisories/new>

Do not include secrets in issues, pull requests, or discussions.

## Security Model

- Stdio inherits local caller permissions.
- Public HTTP requires `bearer` or `github-oauth`.
- `auth_mode=none` is limited to stdio or loopback HTTP.
- GitHub OAuth requires a non-empty allowlist.
- NotebookLM browser auth files and inline auth JSON are secret material.
- Destructive tools require explicit confirmation.

See `docs/security/threat-model.md` for the detailed model.
