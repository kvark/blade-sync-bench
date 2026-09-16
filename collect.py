#!/usr/bin/env python3
"""One-command JCGT collection over the blade / wgpu / bevy submodules."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BLADE = ROOT / "blade"
WGPU = ROOT / "wgpu"
BEVY = ROOT / "bevy"
COLLECT = BLADE / "paper" / "collect.py"


def main() -> int:
    missing = [p for p in (BLADE, WGPU, BEVY, COLLECT) if not p.exists()]
    if missing:
        names = ", ".join(str(p.relative_to(ROOT)) for p in missing)
        print(
            "missing submodules or collector "
            f"({names}). Run:\n  git submodule update --init --recursive",
            file=sys.stderr,
        )
        return 2
    command = [
        sys.executable,
        str(COLLECT),
        "--blade",
        str(BLADE),
        "--wgpu",
        str(WGPU),
        "--bevy",
        str(BEVY),
        *sys.argv[1:],
    ]
    return subprocess.call(command, cwd=str(BLADE))


if __name__ == "__main__":
    raise SystemExit(main())
