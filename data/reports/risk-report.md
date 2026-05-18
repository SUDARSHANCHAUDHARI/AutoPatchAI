# AutoPatch AI Risk Report

- Dependencies scanned: 4
- Findings: 4
- Planned upgrades: 4
- High severity: 2
- Medium severity: 2

## Priority Queue

### 1. lodash

- Ecosystem: npm
- Severity: high
- Priority: urgent
- Upgrade: `4.17.20` -> `4.17.21`
- Source: `data/samples/package.json`
- Confidence: offline-rule-match
- Validation: Run unit tests, dependency audit, and smoke checks before merging.
- Reason: lodash should be upgraded to 4.17.21.

### 2. django

- Ecosystem: python
- Severity: high
- Priority: urgent
- Upgrade: `3.2.0` -> `4.2.11`
- Source: `data/samples/requirements.txt`
- Confidence: offline-rule-match
- Validation: Run unit tests, dependency audit, and smoke checks before merging.
- Reason: django should be upgraded to 4.2.11.

### 3. python

- Ecosystem: docker
- Severity: medium
- Priority: normal
- Upgrade: `latest` -> `3.12-slim`
- Source: `data/samples/Dockerfile`
- Confidence: offline-rule-match
- Validation: Run unit tests, dependency audit, and smoke checks before merging.
- Reason: python should be upgraded to 3.12-slim.

### 4. requests

- Ecosystem: python
- Severity: medium
- Priority: normal
- Upgrade: `unpinned` -> `pin-reviewed-version`
- Source: `data/samples/requirements.txt`
- Confidence: policy-check
- Validation: Run unit tests, dependency audit, and smoke checks before merging.
- Reason: requests is unpinned.
