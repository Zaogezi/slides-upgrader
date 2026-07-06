#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit completed knowledge graphs for template conformance and mojibake."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "## 1. Metadata",
    "## 2. Chapter Directory",
    "## 3. Chapters",
    "## 4. Unassigned Source Content",
]

REQUIRED_KP_SUBHEADINGS = [
    "Prerequisite Check",
    "Knowledge-Point Introduction",
    "Concept And Formal Expression",
    "Assumptions And Scope",
    "Intuition And Multiple Representations",
    "Derivation / Algorithm / Modeling Process",
    "Examples And Counterexamples",
    "Interactive Checks",
    "Worked Problems And Detailed Analysis",
    "Method Summary",
]

# Keep these as ASCII escape sequences so this source file does not itself
# display as mojibake. The patterns match common UTF-8/GBK corruption markers.
MOJIBAKE_PATTERNS = [
    re.compile(pattern)
    for pattern in (
        r"[\u9286\u9225\u922d][\w\u4e00-\u9fa5]{0,8}",
        r"[\u951b\u942d\u9351\u701b\u7ecb\u8930\u7ddf]{2,}",
        r"\b(?:\u8133|\u87fd|\u8796|\u87a4|\u5371|\u80c3|\u6e2d|\u922b|\u922d|\u922e)\b",
        r"\ufffd",
    )
]


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_stdout_utf8(text: str) -> None:
    sys.stdout.buffer.write(text.encode("utf-8"))


def line_number(text: str, needle: str) -> int:
    index = text.find(needle)
    if index < 0:
        return 0
    return text[:index].count("\n") + 1


def find_mojibake_lines(lines: list[str]) -> list[tuple[int, str]]:
    findings: list[tuple[int, str]] = []
    for index, line in enumerate(lines, start=1):
        if any(pattern.search(line) for pattern in MOJIBAKE_PATTERNS):
            findings.append((index, line.strip()[:160]))
    return findings


def audit(path: Path) -> list[tuple[str, str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        return [("encoding-blocker", f"UTF-8 decode failed at byte {error.start}", error.reason)]
    lines = text.splitlines()
    findings: list[tuple[str, str, str]] = []

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            findings.append(("template-blocker", "missing required heading", heading))

    if "## 4. Lossless Source Items" in text:
        findings.append(
            (
                "template-blocker",
                "non-template section used instead of required graph fields",
                "## 4. Lossless Source Items",
            )
        )

    chapter_count = len(re.findall(r"^###\s+3\.\S*\s+Chapter:", text, flags=re.MULTILINE))
    kp_count = len(re.findall(r"^#####\s+3\.\S*\s+Knowledge Point:", text, flags=re.MULTILINE))
    if chapter_count == 0:
        findings.append(("template-blocker", "no template chapter blocks found", "### 3.x Chapter"))
    if kp_count == 0:
        findings.append(("template-blocker", "no template knowledge-point blocks found", "##### 3.x.2.y Knowledge Point"))

    for subheading in REQUIRED_KP_SUBHEADINGS:
        if subheading not in text:
            findings.append(("template-blocker", "missing required knowledge-point subsection", subheading))

    chapter_directory_header = (
        "| Chapter id | Chapter title | Source location range | Main knowledge points | "
        "Prerequisite chapters or sections | Teaching requirements | Notes |"
    )
    if chapter_directory_header not in text:
        findings.append(("template-blocker", "chapter directory does not match template columns", "Chapter Directory table"))

    unassigned_header = (
        "| Entry id | Source item id | Original source wording (or verbatim fragment) | "
        "Source location | Asset type | Why it is unassigned | Intended reuse | Provenance |"
    )
    if unassigned_header not in text:
        findings.append(("template-blocker", "unassigned source content table is missing or malformed", "Unassigned Source Content table"))

    mojibake = find_mojibake_lines(lines)
    for index, excerpt in mojibake[:25]:
        findings.append(("encoding-blocker", f"possible mojibake at line {index}", excerpt))
    if len(mojibake) > 25:
        findings.append(("encoding-blocker", "additional mojibake lines omitted from report", str(len(mojibake) - 25)))

    source_ids = set(re.findall(r"\b(?:p|slide-|page-)[A-Za-z0-9_-]+\b", text))
    if len(source_ids) < 2:
        findings.append(("provenance-blocker", "too few source item ids visible for a completed graph", str(len(source_ids))))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a completed knowledge graph against the required template.")
    parser.add_argument("knowledge_graph", type=Path)
    parser.add_argument("--markdown-report", type=Path)
    args = parser.parse_args()

    findings = audit(args.knowledge_graph)
    status = "blocker" if findings else "pass"
    report_lines = [
        "# Knowledge Graph Template Audit",
        "",
        f"- Knowledge graph: `{args.knowledge_graph}`",
        f"- Findings: {len(findings)}",
        f"- Status: {status}",
        "",
        "| Finding | Detail | Evidence |",
        "| --- | --- | --- |",
    ]
    report_lines.extend(
        f"| {kind} | {markdown_escape(detail)} | {markdown_escape(evidence)} |"
        for kind, detail, evidence in findings
    )
    report = "\n".join(report_lines) + "\n"
    if args.markdown_report:
        args.markdown_report.write_text(report, encoding="utf-8")
    else:
        write_stdout_utf8(report)
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
