# AutoPatch AI

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-product%20polish-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

AI-assisted dependency vulnerability fixer that scans package files and produces safe upgrade plans.

- **Portfolio group:** Product-style SaaS project
- **Status:** Product polish implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/AutoPatchAI
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/AutoPatchAI`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic dependency analysis, upgrade planning, PR preview output, dashboard-ready summary JSON, and product-style risk reports.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

## Core Features

- package.json scanner
- requirements.txt scanner
- Dockerfile scan
- CVE lookup
- AI upgrade explanation
- GitHub PR suggestion
- severity and priority scoring
- dashboard summary JSON
- risk report for reviewers

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

Generated outputs:

- `data/reports/dependencies.json`
- `data/reports/findings.json`
- `data/reports/upgrade_plan.json`
- `data/reports/summary.json`
- `data/reports/risk-report.md`
- `data/reports/pr-preview.md`

## Docker Demo

```bash
docker compose run --rm api
```

## Product Polish Capabilities

- Parses `package.json`, `requirements.txt`, and Dockerfile base images.
- Uses an offline vulnerability ruleset for repeatable demos.
- Flags vulnerable, unpinned, and `latest` dependency usage.
- Generates an upgrade plan and PR preview.
- Adds priority, confidence, severity, and validation metadata to upgrade actions.
- Generates reviewer-friendly risk and PR reports.

## Roadmap

- Add real OSV/NVD integration behind an offline-friendly provider boundary
- Add package-lock and poetry.lock support
- Add breaking-change risk checks
- Add GitHub App flow for draft PR creation
- Add web dashboard for upload, findings, and PR preview
