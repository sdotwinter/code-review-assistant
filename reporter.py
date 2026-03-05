from __future__ import annotations

import json
from collections import Counter
from typing import Iterable


def print_findings(findings: Iterable[dict]) -> None:
    rows = list(findings)
    if not rows:
        print("✅ No findings")
        return

    print("rule_id        severity  location                      message")
    print("-" * 75)
    for f in rows:
        location = f"{f['file']}:{f['line']}"
        print(f"{f['rule_id'][:13]:13} {f['severity'][:8]:8} {location[:28]:28} {f['message']}")


def print_summary(findings: Iterable[dict]) -> None:
    rows = list(findings)
    if not rows:
        print("No findings in this scan.")
        return

    sev = Counter(f["severity"] for f in rows)
    rules = Counter(f["rule_id"] for f in rows)

    print(f"Total findings: {len(rows)}")
    print(f"By severity: high={sev.get('high',0)} medium={sev.get('medium',0)} low={sev.get('low',0)}")
    print("Top rules:")
    for name, count in rules.most_common(5):
        print(f"- {name}: {count}")


def print_json(findings: Iterable[dict]) -> None:
    print(json.dumps(list(findings), indent=2))
