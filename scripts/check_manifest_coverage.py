#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check that every source-manifest item id appears in target text files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_items(manifest_path: Path) -> list[dict[str, Any]]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and isinstance(data.get("items"), list):
        items = data["items"]
    else:
        raise ValueError("manifest must be a list or an object with an 'items' list")

    normalized: list[dict[str, Any]] = []
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} is not an object")
        item_id = item.get("id")
        if not item_id or not isinstance(item_id, str):
            raise ValueError(f"item {index} is missing string field 'id'")
        normalized.append(item)
    return normalized


def parse_target(value: str) -> tuple[str, Path]:
    if "=" in value:
        label, path = value.split("=", 1)
        label = label.strip()
        if not label:
            raise argparse.ArgumentTypeError("target label cannot be empty")
        return label, Path(path)
    path = Path(value)
    return path.stem, path


def first_fragment(item: dict[str, Any]) -> str:
    for key in ("original_text", "verbatim_fragment", "text", "content"):
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            text = " ".join(value.split())
            return text[:90] + ("..." if len(text) > 90 else "")
    return ""


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_stdout_utf8(text: str) -> None:
    sys.stdout.buffer.write(text.encode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify that every manifest item id appears in each target file."
    )
    parser.add_argument("manifest", type=Path)
    parser.add_argument(
        "targets",
        nargs="+",
        type=parse_target,
        help="Target file path, or label=path. Example: step3=assets/x.knowledge-graph.md",
    )
    parser.add_argument(
        "--markdown-report",
        type=Path,
        help="Optional path for a Markdown coverage table.",
    )
    args = parser.parse_args()

    items = load_items(args.manifest)
    target_texts = {
        label: path.read_text(encoding="utf-8")
        for label, path in args.targets
    }

    rows: list[tuple[str, str, str, str, dict[str, str], str]] = []
    missing: list[tuple[str, str]] = []
    for item in items:
        item_id = item["id"]
        item_type = str(item.get("item_type", item.get("type", "")))
        source_location = str(item.get("source_location", item.get("provenance", "")))
        target_statuses = {
            label: "present" if item_id in text else "missing-blocker"
            for label, text in target_texts.items()
        }
        for label, status in target_statuses.items():
            if status != "present":
                missing.append((item_id, label))
        overall = "present" if all(status == "present" for status in target_statuses.values()) else "missing-blocker"
        rows.append((item_id, item_type, source_location, first_fragment(item), target_statuses, overall))

    target_labels = [label for label, _ in args.targets]
    target_summary = ", ".join(f"{label}=`{path}`" for label, path in args.targets)
    status = "pass" if not missing else "blocker"
    columns = ["Source item id", "Type", "Source location", "Original wording / fragment"]
    columns.extend(f"{label} status" for label in target_labels)
    columns.append("Status")

    report_lines = [
        "# Source To Graph Coverage",
        "",
        f"- Manifest: `{args.manifest}`",
        f"- Targets: {target_summary}",
        f"- Total items: {len(items)}",
        f"- Missing items: {len(missing)}",
        f"- Status: {status}",
        "",
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for item_id, item_type, source_location, fragment, target_statuses, overall in rows:
        values = [
            item_id,
            item_type,
            source_location,
            fragment,
            *(target_statuses[label] for label in target_labels),
            overall,
        ]
        report_lines.append("| " + " | ".join(markdown_escape(value) for value in values) + " |")
    if missing:
        report_lines.extend(["", "## Blockers", ""])
        report_lines.extend(f"- `{item_id}` missing from `{label}`" for item_id, label in missing)

    report = "\n".join(report_lines) + "\n"
    if args.markdown_report:
        args.markdown_report.write_text(report, encoding="utf-8")
    else:
        write_stdout_utf8(report)

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
