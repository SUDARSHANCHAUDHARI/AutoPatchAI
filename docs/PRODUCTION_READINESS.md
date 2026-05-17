# Production Readiness

## Current Status

This repository has production foundation files and an MVP scaffold. The product implementation is not production complete yet.

## Required Before Public Release

- Implement the primary MVP workflow.
- Add automated tests for core detection logic.
- Validate all untrusted inputs.
- Add structured logging without leaking secrets.
- Document local setup and deployment.
- Review all sample data for sensitive content.
- Add authentication and authorization where user data or device data is handled.
- Run dependency and secret scans before release.

## Definition of Done

- CI passes on pull requests.
- README has setup, usage, and security notes.
- Sample data is safe to publish.
- Error paths are handled clearly.
- No secrets or local machine paths are committed.
