# Changelog

Notable changes to this repository. Dates are ISO 8601.

## Unreleased

### Added

- Thirteen guides in `docs/` covering prompting, AI Fluency and evaluation, Projects and Skills, artifacts, connectors and MCP, Enterprise Search, Research, Claude Code, other Claude tools, security and privacy, tool selection, and troubleshooting.
- Seven original exercises in `exercises/`, with synthetic data in `examples/`.
- Annotated official links and a verification log in `resources/`.
- `scripts/validate.py` with unit tests, and a GitHub Actions workflow that runs them.
- MIT license for code, CC BY 4.0 for written content, and a notice describing scope.

### Changed

- Validator now rejects links that resolve outside the repository (a root-relative link such as `/etc/hosts` previously passed) and rejects em dashes in authored prose.
- Added a Troubleshooting pointer to Getting started, and reworded the exercise 4 premise so it makes no unsupported claim.
- Verified Claude for Microsoft 365 against Anthropic's product page and replaced the unverified-product caveat.
- Documented the Anthropic Trademark Guidelines and the residual naming risk in `NOTICE.md`.
- Added the maintainer's course completion badge link to the README.

Content reviewed against official sources on 2026-11-20.
