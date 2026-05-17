"""Parse dependency files."""

from __future__ import annotations

import json
from pathlib import Path


def parse_package_json(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
    return [{"ecosystem": "npm", "name": name, "version": version, "source": str(path)} for name, version in deps.items()]


def parse_requirements(path: Path) -> list[dict]:
    deps = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        name, sep, version = stripped.partition("==")
        deps.append({"ecosystem": "python", "name": name.strip(), "version": version.strip() if sep else "unpinned", "source": str(path)})
    return deps


def parse_dockerfile(path: Path) -> list[dict]:
    deps = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lower().startswith("from "):
            image = line.split()[1]
            name, _, version = image.partition(":")
            deps.append({"ecosystem": "docker", "name": name, "version": version or "latest", "source": str(path)})
    return deps


def parse_files(paths: list[Path]) -> list[dict]:
    deps = []
    for path in paths:
        lower = path.name.lower()
        if lower == "package.json":
            deps.extend(parse_package_json(path))
        elif lower == "requirements.txt":
            deps.extend(parse_requirements(path))
        elif "dockerfile" in lower:
            deps.extend(parse_dockerfile(path))
    return deps
