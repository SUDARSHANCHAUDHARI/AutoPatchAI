"""Build dashboard-ready AutoPatch summaries."""

from __future__ import annotations


def summarize_findings(dependencies: list[dict], findings: list[dict], plan: list[dict]) -> dict[str, object]:
    severity_counts: dict[str, int] = {}
    ecosystem_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for finding in findings:
        severity = finding.get("severity", "medium")
        dependency = finding["dependency"]
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
        ecosystem = dependency["ecosystem"]
        source = dependency["source"]
        ecosystem_counts[ecosystem] = ecosystem_counts.get(ecosystem, 0) + 1
        source_counts[source] = source_counts.get(source, 0) + 1

    return {
        "dependencies_scanned": len(dependencies),
        "findings": len(findings),
        "planned_upgrades": len(plan),
        "high_severity": severity_counts.get("high", 0),
        "medium_severity": severity_counts.get("medium", 0),
        "severity_counts": severity_counts,
        "ecosystem_counts": ecosystem_counts,
        "source_counts": source_counts,
        "top_priority": plan[0] if plan else None,
    }


def build_markdown_report(summary: dict[str, object], plan: list[dict]) -> str:
    lines = [
        "# AutoPatch AI Risk Report",
        "",
        f"- Dependencies scanned: {summary['dependencies_scanned']}",
        f"- Findings: {summary['findings']}",
        f"- Planned upgrades: {summary['planned_upgrades']}",
        f"- High severity: {summary['high_severity']}",
        f"- Medium severity: {summary['medium_severity']}",
        "",
        "## Priority Queue",
        "",
    ]
    if not plan:
        lines.append("No upgrade actions are required.")
    for index, item in enumerate(plan, start=1):
        lines.extend(
            [
                f"### {index}. {item['name']}",
                "",
                f"- Ecosystem: {item['ecosystem']}",
                f"- Severity: {item['severity']}",
                f"- Priority: {item['priority']}",
                f"- Upgrade: `{item['from']}` -> `{item['to']}`",
                f"- Source: `{item['source']}`",
                f"- Confidence: {item['confidence']}",
                f"- Validation: {item['validation']}",
                f"- Reason: {item['reason']}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"
