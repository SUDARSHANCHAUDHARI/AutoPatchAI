# Architecture

AutoPatch AI is a defensive dependency review MVP. The current implementation is intentionally offline and deterministic so portfolio demos are repeatable.

## Flow

1. `dependency_parser.py` parses `package.json`, `requirements.txt`, and Dockerfile base images.
2. `vulnerability_scanner.py` applies an offline ruleset for known demo findings.
3. `upgrade_planner.py` creates prioritized upgrade actions.
4. `risk_summary.py` builds dashboard and reviewer summaries.
5. `ai_fix_explainer.py` generates a plain-English explanation boundary for future AI providers.
6. `github_pr_service.py` builds a PR preview without touching a live repository.

## Outputs

- dependency inventory JSON
- findings JSON
- upgrade plan JSON
- dashboard summary JSON
- Markdown risk report
- Markdown PR preview

## Boundary

The MVP does not call live vulnerability APIs, create GitHub branches, or apply dependency changes automatically. Those are future provider integrations.
