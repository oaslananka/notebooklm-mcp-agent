# Architecture Principles

- Keep raw upstream `Any` at the backend boundary.
- Keep config independent from runtime wiring.
- Keep tools typed and confirmation-aware.
- Keep OpenAPI derived from the same catalog used by tests.
- Prefer small modules with explicit ownership over catch-all files.
