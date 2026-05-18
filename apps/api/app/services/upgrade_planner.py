"""Build upgrade plans."""

from __future__ import annotations


def plan_upgrades(findings: list[dict]) -> list[dict]:
    """Return upgrade actions."""
    plan = []
    for item in findings:
        severity = item.get("severity", "medium")
        plan.append(
            {
                "ecosystem": item["dependency"]["ecosystem"],
                "name": item["dependency"]["name"],
                "from": item["dependency"]["version"],
                "to": item["safe"],
                "reason": item["summary"],
                "source": item["dependency"]["source"],
                "severity": severity,
                "priority": "urgent" if severity == "high" else "normal",
                "confidence": "offline-rule-match" if item["cve"] != "UNPINNED" else "policy-check",
                "validation": "Run unit tests, dependency audit, and smoke checks before merging.",
            }
        )
    return sorted(plan, key=lambda item: (item["priority"] != "urgent", item["ecosystem"], item["name"]))
