"""Tests for AutoPatch AI MVP."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from apps.api.app.services.dependency_parser import parse_files
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

    def test_cli_writes_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, "-m", "apps.api.app.cli", *map(str, FILES), "--out-dir", tmp], cwd=ROOT, check=True, capture_output=True, text=True)
            plan = json.loads(Path(tmp, "upgrade_plan.json").read_text(encoding="utf-8"))
            self.assertIn("Planned", result.stdout)
            self.assertGreaterEqual(len(plan), 4)


if __name__ == "__main__":
    unittest.main()
