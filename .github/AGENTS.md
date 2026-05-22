# GitHub Agent Map

## Responsibility

`.github/` owns issue templates, CODEOWNERS, Dependabot, and GitHub Actions workflows.

## Allowed Imports

Not applicable.

## Adding A New Item

Use hosted runners, top-level `contents: read`, job-level permissions only where required, timeouts on every job, and SHA-pinned actions whose metadata has no deprecated JavaScript runtime.

## Test Commands

```bash
uv run zizmor --min-severity medium .github/workflows
actionlint .github/workflows/*.yml
```

## Conventions

Do not add publish-on-push behavior. Publishing remains owner-triggered.
