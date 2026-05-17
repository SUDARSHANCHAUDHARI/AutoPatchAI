# AutoPatch AI

**Goal:** AI-assisted dependency vulnerability fixer.

**MVP:** Upload package files, detect risky packages, and suggest safe upgrades.

## Core Features

- package.json scanner
- requirements.txt scanner
- Dockerfile scan
- CVE lookup
- AI upgrade explanation
- GitHub PR suggestion

## Suggested Stack

FastAPI, React, vulnerability data APIs, Docker.

## Status

Working CLI MVP.

## Quick Start

Scan the included dependency samples:

```bash
python3 -m apps.api.app.cli \
  data/samples/package.json \
  data/samples/requirements.txt \
  data/samples/Dockerfile \
  --out-dir data/reports
```

Run tests:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## MVP Capabilities

- Parses `package.json`, `requirements.txt`, and Dockerfile base images.
- Uses an offline vulnerability ruleset for repeatable demos.
- Flags vulnerable, unpinned, and `latest` dependency usage.
- Generates an upgrade plan and PR preview.

## Repository Status

This repository contains the production-ready foundation for the AutoPatch AI MVP. The current codebase is scaffolded and ready for focused implementation work.

## Production Foundation

- Private GitHub repository linked to `main`
- Initial MVP scaffold committed
- CI repository-health workflow
- Security policy
- Contribution guide
- Pull request and issue templates
- Production readiness checklist
- Safe ignore rules for local secrets and generated files
