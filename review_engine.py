from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List


@dataclass
class Finding:
    rule_id: str
    severity: str
    file: str
    line: int
    message: str

    def to_dict(self) -> dict:
        return asdict(self)


SUPPORTED_EXT = {".py", ".js", ".ts"}


def discover_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part.startswith(".") for part in path.parts):
            continue
        if "node_modules" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() in SUPPORTED_EXT:
            yield path


def review_path(root: Path) -> List[Finding]:
    findings: List[Finding] = []
    for file in discover_files(root):
        findings.extend(review_file(file, root))
    return findings


def review_file(file_path: Path, root: Path) -> List[Finding]:
    findings: List[Finding] = []
    try:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return findings

    rel = str(file_path.relative_to(root))

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        if "TODO" in stripped or "FIXME" in stripped:
            findings.append(Finding("todo-fixme", "low", rel, i, "Contains TODO/FIXME marker"))

        if "print(" in stripped or "console.log(" in stripped:
            findings.append(Finding("debug-output", "medium", rel, i, "Debug output found in code"))

        if stripped.startswith("except:"):
            findings.append(Finding("bare-except", "high", rel, i, "Bare except detected; catch specific exceptions"))

        if len(line) > 120:
            findings.append(Finding("long-line", "low", rel, i, "Line exceeds 120 characters"))

    return findings
