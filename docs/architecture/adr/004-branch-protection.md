# ADR 004: Branch Protection on main

**Status**: Accepted  
**Date**: 2026-05-28  
**Driver**: Security audit

## Context

The `main` branch had no branch protection applied. Any collaborator or automated agent could force-push, delete the branch, or merge unreviewed code directly. This represented a supply-chain and integrity risk for a published PyPI/GHCR package.

## Decision

Apply the following protection rules via `gh api PUT /repos/{owner}/{repo}/branches/main/protection`:

- Required pull request reviews: 1 approving review
- Require code owner reviews
- Required status checks: CI, Docs, CodeQL, Dependency Review, Security, Publish / build check
- Strict status check enforcement (up-to-date before merge)
- Require linear history
- Require conversation resolution
- Enforce for admins
- Disallow force pushes
- Disallow deletions

## Consequences

- Positive: No direct-to-main pushes — all changes go through PR review
- Positive: Required status checks prevent merging broken builds, security issues, or missing docs
- Positive: Linear history keeps the commit graph clean for release management
- Positive: Admins are also subject to protection (reduces bus-factor)
- Negative: Slight friction for hotfixes (must go through PR with simplified review)

## References

- `scripts/setup-branch-protection.ps1`
- `scripts/setup-branch-protection.sh`
- `docs/release/branch-protection.md`
