#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit generated text artifacts for strict UTF-8 decoding and mojibake."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_EXTENSIONS = {
    ".csv",
    ".css",
    ".html",
    ".json",
    ".log",
    ".md",
    ".svg",
    ".tsv",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}

# Keep these as ASCII escape sequences so this source file does not itself
# display as mojibake. The patterns match common UTF-8/GBK corruption markers.
MOJIBAKE_PATTERNS = [
    re.compile(pattern)
    for pattern in (
        r"\ufffd",
        r"\u9225[?\u6a9a]?|\u922d|\u922e|\u922b|\u9286",
        r"\b(?:\u8133|\u87fd|\u8796|\u87a4|\u5371|\u80c3|\u6e2d)\b",
        r"[\u951b\u942d\u9351\u701b\u7ecb\u8930\u7ddf]{4,}",
    )
]


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_stdout_utf8(text: str) -> None:
    sys.stdout.buffer.write(text.encode("utf-8"))


def iter_text_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(
                child
                for child in path.rglob("*")
                if child.is_file() and child.suffix.lower() in TEXT_EXTENSIONS
            )
        elif path.is_file():
            files.append(path)
    return sorted(set(files))


def audit_file(path: Path) -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    data = path.read_bytes()
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as error:
        return [("utf8-decode-blocker", f"{error.reason} at byte {error.start}")]

    for index, line in enumerate(text.splitlines(), start=1):
        if any(pattern.search(line) for pattern in MOJIBAKE_PATTERNS):
            findings.append(("mojibake-blocker", f"line {index}: {line.strip()[:160]}"))
            if len(findings) >= 10:
                findings.append(("mojibake-blocker", "additional mojibake lines omitted"))
                break
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit text artifacts for strict UTF-8 and mojibake.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--markdown-report", type=Path)
    args = parser.parse_args()

    files = iter_text_files(args.paths)
    rows: list[tuple[str, str, str]] = []
    for path in files:
        for kind, detail in audit_file(path):
            rows.append((str(path), kind, detail))

    status = "blocker" if rows else "pass"
    report_lines = [
        "# UTF-8 Artifact Audit",
        "",
        f"- Inputs: {', '.join(f'`{path}`' for path in args.paths)}",
        f"- Text files checked: {len(files)}",
        f"- Findings: {len(rows)}",
        f"- Status: {status}",
        "",
        "| File | Finding | Detail |",
        "| --- | --- | --- |",
    ]
    report_lines.extend(
        f"| `{markdown_escape(path)}` | {kind} | {markdown_escape(detail)} |"
        for path, kind, detail in rows
    )
    report = "\n".join(report_lines) + "\n"
    if args.markdown_report:
        args.markdown_report.write_text(report, encoding="utf-8")
    else:
        write_stdout_utf8(report)
    return 1 if rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
