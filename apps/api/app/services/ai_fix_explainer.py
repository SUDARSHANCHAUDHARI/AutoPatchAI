"""Generate plain-English fix explanations."""

from __future__ import annotations


def explain_plan(plan: list[dict]) -> str:
    if not plan:
        return "No risky dependencies were detected."
    names = ", ".join(f"{item['name']} {item['from']} -> {item['to']}" for item in plan)
    return f"AutoPatch found {len(plan)} upgrade action(s): {names}. Apply upgrades, run tests, and review changelogs before merging."
