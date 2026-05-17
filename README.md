# AutoPatch AI

[![Python](https://img.shields.io/badge/Python-3.12-blue)](#) [![Status](https://img.shields.io/badge/status-MVP-green)](#) [![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#)

AI-assisted dependency vulnerability fixer that scans package files and produces safe upgrade plans.

- **Portfolio group:** Product-style SaaS project
- **Status:** MVP implemented, tested, committed, and pushed to GitHub
- **GitHub:** https://github.com/SUDARSHANCHAUDHARI/AutoPatchAI
- **Local path:** `/Users/screencloudsudarshan/SUDARSHAN_CODE/sudarshan_repos/CyberSecurity/AutoPatchAI`

## MVP Snapshot

This repository includes a working MVP with safe sample data, deterministic detection or analysis logic, local tests, and generated output reports where relevant. It is ready for README/demo polish or deeper product work.

## Safe Use

This project is defensive and analysis-focused. Use only with logs, systems, repositories, and lab environments you own or have permission to assess.

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

## Roadmap

- Polish sample output screenshots or terminal demos
- Add architecture diagram and deeper implementation notes
- Expand test coverage around edge cases
- Add Docker or local demo workflow where useful
- Prepare `v0.1.0-mvp` release notes
