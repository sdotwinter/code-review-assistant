from __future__ import annotations

import argparse
from pathlib import Path

from reporter import print_findings, print_json, print_summary
from review_engine import review_path


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="code-review-assistant",
        description="Rule-based pre-review scanner for Python/JS/TS projects.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_scan = sub.add_parser("scan", help="Scan a folder and print findings")
    p_scan.add_argument("path", nargs="?", default=".")

    p_summary = sub.add_parser("summary", help="Scan a folder and print summary")
    p_summary.add_argument("path", nargs="?", default=".")

    p_suggest = sub.add_parser("suggest", help="Scan and output JSON findings")
    p_suggest.add_argument("path", nargs="?", default=".")

    args = parser.parse_args(argv)
    root = Path(args.path).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Error: path not found or not a directory: {root}")
        return 2

    findings = [f.to_dict() for f in review_path(root)]

    if args.command == "scan":
        print_findings(findings)
    elif args.command == "summary":
        print_summary(findings)
    elif args.command == "suggest":
        print_json(findings)

    return 0
