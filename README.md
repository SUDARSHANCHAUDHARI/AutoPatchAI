# AutoPatch AI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](#requirements)
[![Status](https://img.shields.io/badge/status-MVP-green)](#status)
[![Security](https://img.shields.io/badge/security-defensive%20lab-purple)](#safe-use)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Dependency vulnerability scanner and upgrade planner. Scans `package.json`, `requirements.txt`, and `Dockerfile` base images, flags risky pins, and produces an upgrade plan with PR preview output.

---

## Overview

AutoPatch AI is a defensive analysis tool that audits dependency manifests for known vulnerabilities, unpinned versions, and `latest` tag usage. It generates a structured upgrade plan with priority, severity, and confidence metadata, plus a reviewer-friendly risk report and PR preview ready for handoff.

The current MVP is a Python CLI. A FastAPI + React web dashboard is scaffolded under `apps/` for future development.

## Features

- Scans `package.json`, `requirements.txt`, and Dockerfile base images
- Offline vulnerability ruleset for repeatable demos
- Flags vulnerable, unpinned, and `latest` dependency usage
- Generates an upgrade plan with priority, severity, and confidence
- Produces a reviewer-friendly risk report and PR preview
- Outputs structured JSON for events, findings, plan, and summary

## Requirements

- Python 3.10 or newer
- Linux, macOS, or Windows
- No third-party Python packages (standard library only)
- Optional: Docker for the demo container

## Installation

```bash
git clone https://github.com/SUDARSHANCHAUDHARI/AutoPatchAI.git
cd AutoPatchAI
pip install .
```

This registers the `auto-patch-ai` CLI command.

To run without installing:

```bash
python3 main.py --help
```

## Usage

Scan the included dependency samples:

```bash
python3 main.py \
  data/samples/package.json \
  data/samples/requirements.txt \
  data/samples/Dockerfile \
  --out-dir data/reports
```

Generated outputs in `data/reports/`:

- `dependencies.json` — parsed dependency inventory
- `findings.json` — flagged vulnerabilities and risky pins
- `upgrade_plan.json` — prioritized upgrade actions
- `summary.json` — counts and severity breakdown
- `risk-report.md` — reviewer-friendly Markdown risk report
- `pr-preview.md` — PR-style preview of suggested changes

## Project Structure

```
AutoPatchAI/
├── apps/
│   ├── api/        FastAPI app scaffold (planned)
│   └── web/        React/Next.js app scaffold (planned)
├── data/
│   ├── samples/    Safe sample manifests
│   └── reports/    Example generated output
├── docker/         Dockerfile + compose support
├── docs/           Architecture, security, demo notes
├── scripts/        Setup, seed, and run helpers
├── tests/          Unit and integration tests
├── main.py         CLI entrypoint
├── pyproject.toml  Package metadata
└── LICENSE
```

## Testing

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## Docker Demo

```bash
docker compose run --rm api
```

## Safe Use

This project is defensive and analysis-focused. Use only on manifests, repositories, and lab environments you own or have explicit written permission to assess. The included sample manifests are synthetic and safe for public demo use.

## Status

Working Python CLI MVP. Web dashboard scaffold present but not yet implemented.

## Roadmap

- Real OSV / NVD integration behind an offline-friendly provider boundary
- `package-lock.json` and `poetry.lock` support
- Breaking-change risk checks
- GitHub App flow for draft PR creation
- Web dashboard for upload, findings, and PR preview

## License

Released under the [MIT License](LICENSE). You are free to use, modify, and distribute this software with attribution.

## Author

**Sudarshan Chaudhari** — [SudarshanTechLabs](https://github.com/SUDARSHANCHAUDHARI)
Bangkok, Thailand

For inquiries: open an issue on [GitHub](https://github.com/SUDARSHANCHAUDHARI/AutoPatchAI/issues).
