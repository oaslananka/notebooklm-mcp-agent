# Auth Agent Map

## Responsibility

`auth/` owns HTTP bearer validation, GitHub OAuth flow, session storage, and origin checks.

## Allowed Imports

Auth may import `notebooklm_mcp_agent.config` and auth-local modules. It must not import tools or backend behavior except through explicit validation helpers.

## Adding A New Item

Add tests for valid, invalid, and missing credential cases. Do not log bearer values, OAuth codes, cookies, client secrets, or PKCE verifiers.

## Test Commands

```bash
uv run pytest tests/unit/test_auth.py tests/unit/test_oauth.py
```

## Conventions

Public HTTP must fail closed. `auth_mode=none` is only for stdio or loopback HTTP.
