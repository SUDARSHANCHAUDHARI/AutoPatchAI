"""CLI for AutoPatch AI MVP."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from apps.api.app.services.ai_fix_explainer import explain_plan
from apps.api.app.services.dependency_parser import parse_files
from apps.api.app.services.github_pr_service import build_pr_preview
from apps.api.app.services.upgrade_planner import plan_upgrades
from apps.api.app.services.vulnerability_scanner import scan_vulnerabilities


def main() -> None:
    parser = argparse.ArgumentParser(description="AutoPatch AI dependency scanner")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("data/reports"))
    args = parser.parse_args()
    deps = parse_files(args.files)
    findings = scan_vulnerabilities(deps)
    plan = plan_upgrades(findings)
    explanation = explain_plan(plan)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, payload in {"dependencies": deps, "findings": findings, "upgrade_plan": plan}.items():
        (args.out_dir / f"{name}.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (args.out_dir / "pr-preview.md").write_text(build_pr_preview(plan, explanation), encoding="utf-8")
    print(f"Found {len(findings)} issue(s)")
    print(f"Planned {len(plan)} upgrade(s)")


if __name__ == "__main__":
    main()
