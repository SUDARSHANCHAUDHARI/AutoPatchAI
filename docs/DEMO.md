# Demo

## Local CLI

```bash
python3 -m apps.api.app.cli \
  data/samples/package.json \
  data/samples/requirements.txt \
  data/samples/Dockerfile \
  --out-dir data/reports
```

Expected terminal output:

```text
Found 4 issue(s)
Planned 4 upgrade(s)
```

## Review Outputs

```bash
cat data/reports/risk-report.md
cat data/reports/pr-preview.md
cat data/reports/summary.json
```

## Docker CLI

```bash
docker compose run --rm api
```
