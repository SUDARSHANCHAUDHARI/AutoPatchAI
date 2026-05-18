# Production Readiness

## Current Status

This repository has a working offline product MVP with deterministic dependency parsing, findings, upgrade planning, PR preview output, tests, and generated reports. It is portfolio-ready but not production complete yet.

## Required Before Public Release

- Add live vulnerability provider integrations behind testable boundaries.
- Add tests for malformed manifests and unsupported files.
- Validate all untrusted inputs.
- Add structured logging without leaking secrets.
- Document local setup and deployment.
- Review all sample data for sensitive content.
- Add authentication and authorization before handling private repositories.
- Run dependency and secret scans before release.
- Add audit logging for scan and PR actions.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
- Reports include severity, priority, validation guidance, and reviewer summaries.
