# Package Agent Map

## Responsibility

This package contains the canonical runtime implementation.

## Allowed Imports

Top-level modules may import internal layers only when there is no narrower owner. Prefer placing behavior in the layer-specific package.

## Adding A New Item

Add implementation in the narrowest package, add tests, then expose through `server.create_server()` or `cli.py` only when needed.

## Test Commands

```bash
uv run pytest tests
uv run python scripts/check_architecture.py
```

## Conventions

Keep public imports intentional and update `scripts/check_public_surface.py` when the public surface changes.
