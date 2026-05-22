# Release Process

1. Run `task verify` and `task verify:release`.
2. Merge the Release Please pull request after required checks pass.
3. Owner creates or approves the release event.
4. `Publish` builds wheel, sdist, SBOM, checksums, and container image.
5. PyPI publishing uses trusted publishing; GHCR publishing uses the repository token.

Do not create tags or publish artifacts without an explicit owner release command.
