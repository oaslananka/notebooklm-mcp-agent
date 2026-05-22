#!/usr/bin/env bash
set -euo pipefail

repo="${1:-oaslananka/notebooklm-mcp-agent}"
branch="${2:-main}"

cat <<'JSON' | gh api "repos/${repo}/branches/${branch}/protection" --method PUT --input -
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "CI",
      "Docs",
      "CodeQL",
      "Dependency Review",
      "Security",
      "Publish / build check"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "required_approving_review_count": 1,
    "require_code_owner_reviews": true
  },
  "restrictions": null,
  "required_linear_history": true,
  "required_conversation_resolution": true,
  "allow_force_pushes": false,
  "allow_deletions": false
}
JSON
