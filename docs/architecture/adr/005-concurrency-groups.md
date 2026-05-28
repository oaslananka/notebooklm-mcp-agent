# ADR 005: GitHub Actions Concurrency Groups

**Status**: Accepted  
**Date**: 2026-05-28  
**Driver**: CI efficiency audit

## Context

Multiple workflow runs on the same branch/PR could execute concurrently, wasting CI minutes and causing race conditions on deployment artifacts. Each workflow used different concurrency patterns, some with none at all.

## Decision

Apply a standard concurrency group pattern to all CI/test/lint/docs workflows:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true
```

Key design choices:

- **Workflow name prefix** (`github.workflow`): isolates groups across different workflows so they don't cancel each other
- **PR number fallback** (`github.event.pull_request.number || github.ref`): uses PR number for PR events, falls back to branch ref for push/merge events
- **cancel-in-progress: true** for all CI/test workflows: newer runs cancel older in-progress ones on the same branch
- **Deploy-safe publish.yml**: uses `cancel-in-progress: ${{ github.event_name == 'pull_request' }}` — only PR-triggered runs cancel; release and workflow_dispatch runs serialize safely
- **Scheduled/release workflows untouched**: scorecard.yml (schedule) and release-please.yml (release_event) keep `cancel-in-progress: false`

## Consequences

- Positive: CI minutes saved — old runs cancelled when new commits push
- Positive: Deploy safety preserved — release runs never cancelled
- Positive: Cross-workflow isolation — ci.yml and security.yml don't interrupt each other
- Positive: predictable, audit-friendly pattern across all workflows
- Negative: When two pushes happen in quick succession, the first run's results are lost (acceptable tradeoff)

## References

- `.github/workflows/ci.yml`
- `.github/workflows/security.yml`
- `.github/workflows/codeql.yml`
- `.github/workflows/docs.yml`
- `.github/workflows/dependency-review.yml`
- `.github/workflows/publish.yml`
