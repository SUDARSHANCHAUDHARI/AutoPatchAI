"""Build PR preview text."""

from __future__ import annotations


def build_pr_preview(plan: list[dict], explanation: str) -> str:
    lines = ["# AutoPatch AI Upgrade PR", "", explanation, "", "## Changes", ""]
    for item in plan:
        lines.append(f"- `{item['name']}`: `{item['from']}` -> `{item['to']}` in `{item['source']}`")
    return "\n".join(lines) + "\n"
