"""Tests for AutoPatch AI MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from apps.api.app.services.dependency_parser import parse_files
from apps.api.app.services.risk_summary import build_markdown_report, summarize_findings
from apps.api.app.services.upgrade_planner import plan_upgrades
from apps.api.app.services.vulnerability_scanner import scan_vulnerabilities


ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / "data/samples/package.json", ROOT / "data/samples/requirements.txt", ROOT / "data/samples/Dockerfile"]


class AutoPatchTests(unittest.TestCase):
    def test_detects_and_plans_upgrades(self) -> None:
        findings = scan_vulnerabilities(parse_files(FILES))
        plan = plan_upgrades(findings)
        names = {item["name"] for item in plan}
        self.assertIn("lodash", names)
        self.assertIn("django", names)
        self.assertIn("requests", names)
        self.assertIn("python", names)
        self.assertEqual("urgent", plan[0]["priority"])
        self.assertIn("validation", plan[0])

    def test_cli_writes_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, "-m", "apps.api.app.cli", *map(str, FILES), "--out-dir", tmp], cwd=ROOT, check=True, capture_output=True, text=True)
            plan = json.loads(Path(tmp, "upgrade_plan.json").read_text(encoding="utf-8"))
            summary = json.loads(Path(tmp, "summary.json").read_text(encoding="utf-8"))
            risk_report = Path(tmp, "risk-report.md").read_text(encoding="utf-8")
            self.assertIn("Planned", result.stdout)
            self.assertGreaterEqual(len(plan), 4)
            self.assertEqual(2, summary["high_severity"])
            self.assertIn("AutoPatch AI Risk Report", risk_report)

    def test_builds_dashboard_summary(self) -> None:
        deps = parse_files(FILES)
        findings = scan_vulnerabilities(deps)
        plan = plan_upgrades(findings)
        summary = summarize_findings(deps, findings, plan)
        report = build_markdown_report(summary, plan)

        self.assertEqual(4, summary["dependencies_scanned"])
        self.assertEqual(4, summary["planned_upgrades"])
        self.assertIn("Priority Queue", report)


if __name__ == "__main__":
    unittest.main()
