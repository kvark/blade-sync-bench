#!/usr/bin/env python3
"""One-command JCGT collection over the blade / wgpu / bevy submodules."""

from __future__ import annotations

import socket
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BLADE = ROOT / "blade"
WGPU = ROOT / "wgpu"
BEVY = ROOT / "bevy"
COLLECT = BLADE / "paper" / "collect.py"
RESULTS = ROOT / "results"


def user_passed_output(argv: list[str]) -> bool:
    return any(arg == "--output" or arg.startswith("--output=") for arg in argv)


def default_output() -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    host = socket.gethostname().split(".")[0]
    cleaned = "".join(c if c.isalnum() else "-" for c in host.lower())
    slug = "-".join(part for part in cleaned.split("-") if part) or "host"
    return RESULTS / f"{stamp}-{slug}"


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
    extra: list[str] = []
    if not user_passed_output(sys.argv[1:]):
        output = default_output()
        extra = ["--output", str(output)]
        print(f"Results: {output}", file=sys.stderr, flush=True)
        print(
            f"  validation → {output}-validation\n"
            f"  profile    → {output}-profile\n"
            f"  captures   → {output}-captures",
            file=sys.stderr,
            flush=True,
        )
    command = [
        sys.executable,
        str(COLLECT),
        "--blade",
        str(BLADE),
        "--wgpu",
        str(WGPU),
        "--bevy",
        str(BEVY),
        *extra,
        *sys.argv[1:],
    ]
    return subprocess.call(command, cwd=str(BLADE))


if __name__ == "__main__":
    raise SystemExit(main())
