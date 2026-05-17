"""Build upgrade plans."""

from __future__ import annotations


def plan_upgrades(findings: list[dict]) -> list[dict]:
    """Return upgrade actions."""
    return [
        {
            "ecosystem": item["dependency"]["ecosystem"],
            "name": item["dependency"]["name"],
            "from": item["dependency"]["version"],
            "to": item["safe"],
            "reason": item["summary"],
            "source": item["dependency"]["source"],
        }
        for item in findings
    ]
