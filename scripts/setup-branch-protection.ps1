param(
  [string]$Repo = "oaslananka/notebooklm-mcp-agent",
  [string]$Branch = "main"
)

$body = @{
  required_status_checks = @{
    strict = $true
    contexts = @(
      "CI",
      "Docs",
      "CodeQL",
      "Dependency Review",
      "Security",
      "Publish / build check"
    )
  }
  enforce_admins = $true
  required_pull_request_reviews = @{
    required_approving_review_count = 1
    require_code_owner_reviews = $true
  }
  restrictions = $null
  required_linear_history = $true
  required_conversation_resolution = $true
  allow_force_pushes = $false
  allow_deletions = $false
} | ConvertTo-Json -Depth 5 -Compress

$body | gh api "repos/$Repo/branches/$Branch/protection" --method PUT --input -
