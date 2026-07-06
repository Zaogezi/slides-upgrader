# -*- coding: utf-8 -*-
"""Flag likely formulas or visual-object placeholders inside ordinary PPTX text boxes."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
}

MATH_PATTERNS = [
    re.compile(r"\\(?:frac|sum|int|lim|sqrt|alpha|beta|gamma|theta|lambda|mu|sigma|Delta|Omega)\b"),
    re.compile(r"\$[^$]+\$"),
    re.compile(r"\b[a-zA-Z]\s*[_^]\s*[\w{]"),
    re.compile(r"[∑∫√∞≈≠≤≥×÷→↦∈∉⊂⊆∪∩∀∃]"),
    re.compile(r"\b(?:lim|argmax|argmin|max|min)\s*[_{]"),
]

VISUAL_PLACEHOLDER_PATTERNS = [
    re.compile(r"\b(?:diagram|graph|chart|plot|flowchart|automaton|state machine)\s*:", re.I),
    re.compile(r"\b(?:x-axis|y-axis|node|edge|arrow|transition|legend|data points?)\b", re.I),
]


def text_of(shape: ET.Element) -> str:
    return "".join(node.text or "" for node in shape.findall(".//a:t", NS)).strip()


def has_math_object(shape: ET.Element) -> bool:
    return shape.find(".//m:oMath", NS) is not None or shape.find(".//m:oMathPara", NS) is not None


def looks_like_formula(text: str) -> bool:
    return any(pattern.search(text) for pattern in MATH_PATTERNS)


def looks_like_visual_placeholder(text: str) -> bool:
    return any(pattern.search(text) for pattern in VISUAL_PLACEHOLDER_PATTERNS)


def markdown_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def write_stdout_utf8(text: str) -> None:
    sys.stdout.buffer.write(text.encode("utf-8"))


def slide_number(path: str) -> str:
    match = re.search(r"slide(\d+)\.xml$", path)
    return match.group(1) if match else path


def audit_pptx(path: Path) -> list[tuple[str, str, str, str]]:
    findings: list[tuple[str, str, str, str]] = []
    with zipfile.ZipFile(path) as archive:
        slide_names = sorted(
            name for name in archive.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
        for slide_name in slide_names:
            root = ET.fromstring(archive.read(slide_name))
            for index, shape in enumerate(root.findall(".//p:sp", NS), start=1):
                text = text_of(shape)
                if not text:
                    continue
                if looks_like_formula(text) and not has_math_object(shape):
                    findings.append((slide_number(slide_name), str(index), "formula-textbox-blocker", text[:120]))
                elif looks_like_visual_placeholder(text):
                    findings.append((slide_number(slide_name), str(index), "possible-visual-placeholder", text[:120]))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit a PPTX for likely formulas or visual placeholders in ordinary text boxes."
    )
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--markdown-report", type=Path)
    args = parser.parse_args()

    findings = audit_pptx(args.pptx)
    blocker_count = sum(1 for _, _, kind, _ in findings if kind.endswith("blocker"))
    report_lines = [
        "# PPTX STEM Textbox Audit",
        "",
        f"- PPTX: `{args.pptx}`",
        f"- Findings: {len(findings)}",
        f"- Blockers: {blocker_count}",
        f"- Status: {'blocker' if blocker_count else 'pass'}",
        "",
        "| Slide | Shape index | Finding | Text excerpt |",
        "| --- | --- | --- | --- |",
    ]
    report_lines.extend(
        f"| {slide} | {shape} | {kind} | {markdown_escape(excerpt)} |"
        for slide, shape, kind, excerpt in findings
    )
    report = "\n".join(report_lines) + "\n"
    if args.markdown_report:
        args.markdown_report.write_text(report, encoding="utf-8")
    else:
        write_stdout_utf8(report)
    return 1 if blocker_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
