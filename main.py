"""CLI entrypoint for AutoPatch AI."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from apps.api.app.cli import main

if __name__ == "__main__":
    main()
