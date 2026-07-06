#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit PPTX text coverage against a completed graph and detect one-template decks."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

SOURCE_ITEM_RE = re.compile(
    r"^\s*-\s*(?P<id>(?:p\d+|slide-[A-Za-z0-9_-]+|page-[A-Za-z0-9_-]+))\b.*?:\s*(?P<text>.+)$"
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", "", value).lower()


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_stdout_utf8(text: str) -> None:
    sys.stdout.buffer.write(text.encode("utf-8"))


def extract_pptx_text_and_layouts(path: Path) -> tuple[str, list[str], list[str]]:
    texts: list[str] = []
    slide_layouts: list[str] = []
    bg_signatures: list[str] = []
    with zipfile.ZipFile(path) as archive:
        slide_names = sorted(
            name
            for name in archive.namelist()
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )
        rel_cache: dict[str, ET.Element] = {}
        for slide_name in slide_names:
            root = ET.fromstring(archive.read(slide_name))
            texts.extend(node.text or "" for node in root.findall(".//a:t", NS))
            bg = root.find(".//p:bg", NS)
            bg_signatures.append(ET.tostring(bg, encoding="unicode") if bg is not None else "none")

            rel_name = slide_name.replace("ppt/slides/", "ppt/slides/_rels/") + ".rels"
            layout_target = "unknown"
            if rel_name in archive.namelist():
                rel_root = rel_cache.get(rel_name)
                if rel_root is None:
                    rel_root = ET.fromstring(archive.read(rel_name))
                    rel_cache[rel_name] = rel_root
                for rel in rel_root:
                    rel_type = rel.attrib.get("Type", "")
                    if rel_type.endswith("/slideLayout"):
                        layout_target = rel.attrib.get("Target", "unknown")
                        break
            slide_layouts.append(layout_target)
    return "\n".join(texts), slide_layouts, bg_signatures


def source_items_from_manifest(path: Path) -> list[tuple[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    raw_items = data.get("items", data) if isinstance(data, dict) else data
    if not isinstance(raw_items, list):
        raise ValueError("manifest must be a list or an object with an 'items' list")
    items: list[tuple[str, str]] = []
    for raw_item in raw_items:
        if not isinstance(raw_item, dict):
            continue
        item_id = raw_item.get("id")
        text = (
            raw_item.get("original_text")
            or raw_item.get("verbatim_fragment")
            or raw_item.get("text")
            or raw_item.get("content")
        )
        if isinstance(item_id, str) and isinstance(text, str) and text.strip():
            items.append((item_id, text.strip()))
    return items


def source_items_from_graph(path: Path) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = SOURCE_ITEM_RE.match(line)
        if match:
            text = re.sub(r"`+", "", match.group("text")).strip()
            if text:
                items.append((match.group("id"), text))
    return items


def fragment_present(fragment: str, deck_text: str) -> bool:
    normalized_fragment = normalize(fragment)
    normalized_deck = normalize(deck_text)
    if not normalized_fragment:
        return True
    if normalized_fragment in normalized_deck:
        return True
    tokens = [token for token in re.split(r"[\s,;:，。；：、()（）]+", fragment) if len(token) >= 4]
    if not tokens:
        return False
    hits = sum(1 for token in tokens if normalize(token) in normalized_deck)
    return hits / len(tokens) >= 0.7


def audit(
    graph: Path,
    pptx: Path,
    minimum_coverage: float,
    manifest: Path | None = None,
) -> tuple[list[tuple[str, str, str]], dict[str, str]]:
    deck_text, layouts, backgrounds = extract_pptx_text_and_layouts(pptx)
    items = source_items_from_manifest(manifest) if manifest else source_items_from_graph(graph)
    findings: list[tuple[str, str, str]] = []

    if not items:
        source = f"manifest {manifest}" if manifest else f"completed graph {graph}"
        findings.append(("coverage-blocker", "no source items could be extracted for coverage audit", source))
    else:
        missing: list[tuple[str, str]] = []
        for item_id, text in items:
            if not fragment_present(text[:220], deck_text):
                missing.append((item_id, text[:140]))
        coverage = 1 - (len(missing) / len(items))
        if coverage < minimum_coverage:
            findings.append(
                (
                    "coverage-blocker",
                    f"source-item text coverage {coverage:.0%} below required {minimum_coverage:.0%}",
                    f"{len(missing)} missing of {len(items)} items",
                )
            )
        for item_id, excerpt in missing[:30]:
            findings.append(("coverage-blocker", f"missing source item {item_id}", excerpt))
        if len(missing) > 30:
            findings.append(("coverage-blocker", "additional missing source items omitted from report", str(len(missing) - 30)))

    layout_counts = Counter(layouts)
    bg_counts = Counter(backgrounds)
    slide_count = len(layouts)
    if slide_count >= 6 and len(layout_counts) < 3:
        findings.append(("variety-blocker", "fewer than 3 slide layouts used in a multi-slide PPTX", str(dict(layout_counts))))
    if slide_count >= 6 and max(layout_counts.values(), default=0) / slide_count > 0.75:
        findings.append(("variety-blocker", "one slide layout dominates more than 75% of slides", str(dict(layout_counts))))
    if slide_count >= 6 and len(bg_counts) < 2:
        findings.append(("variety-revise", "all slides appear to use the same background signature", str(dict(bg_counts))))

    summary = {
        "slide_count": str(slide_count),
        "unique_layouts": str(len(layout_counts)),
        "unique_backgrounds": str(len(bg_counts)),
        "source_items_checked": str(len(items)),
    }
    return findings, summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit PPTX coverage and template/layout variety.")
    parser.add_argument("completed_graph", type=Path)
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--manifest", type=Path, help="Source manifest to use as the authoritative coverage checklist.")
    parser.add_argument("--minimum-coverage", type=float, default=0.95)
    parser.add_argument("--markdown-report", type=Path)
    args = parser.parse_args()

    findings, summary = audit(args.completed_graph, args.pptx, args.minimum_coverage, args.manifest)
    blocker_count = sum(1 for kind, _, _ in findings if kind.endswith("blocker"))
    status = "blocker" if blocker_count else ("revise" if findings else "pass")
    report_lines = [
        "# PPTX Coverage And Variety Audit",
        "",
        f"- Completed graph: `{args.completed_graph}`",
        f"- Source manifest: `{args.manifest}`" if args.manifest else "- Source manifest: not provided",
        f"- PPTX: `{args.pptx}`",
        f"- Slide count: {summary['slide_count']}",
        f"- Unique layouts: {summary['unique_layouts']}",
        f"- Unique backgrounds: {summary['unique_backgrounds']}",
        f"- Source items checked: {summary['source_items_checked']}",
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
    return 1 if blocker_count else 0


if __name__ == "__main__":
    raise SystemExit(main())
