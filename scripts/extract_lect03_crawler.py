from __future__ import annotations

import json
import re
from pathlib import Path

import pdfplumber


ROOT = Path(r"D:\Skills\slides-upgrader")
SOURCE = Path(r"C:\Users\zaoge\Downloads\lect03_crawler-模板.pdf")
TASK_SLUG = "lect03_crawler"


def clean_text(text: str) -> str:
    text = (
        text.replace("\uf06e", "-")
        .replace("\uf070", "-")
        .replace("\uf0d8", "-")
        .replace("— —", " - ")
        .replace("——", " - ")
    )
    text = re.sub(r"(?<=[A-Za-z])\s+(?=[A-Za-z])", "", text)
    text = re.sub(r"(?<=[0-9])\s+(?=[0-9])", "", text)
    text = re.sub(r"(?<=[A-Za-z])\s+(?=[0-9])", "", text)
    text = re.sub(r"(?<=[0-9])\s+(?=[A-Za-z])", "", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[\u4e00-\u9fff])", "", text)
    text = re.sub(r"(?<=[\u4e00-\u9fff])\s+(?=[A-Za-z0-9_./:#<>=\'\"-])", "", text)
    text = re.sub(r"(?<=[A-Za-z0-9_./:#<>=\'\"-])\s+(?=[\u4e00-\u9fff])", "", text)
    replacements = {
        "BeautifulSoup": "Beautiful Soup",
        "findall": "find_all",
        "gettext": "get_text",
        "nextsibling": "next_sibling",
        "previoussibling": "previous_sibling",
        "NavigableString": "Navigable String",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\s*\|\s*", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    extracts_dir = ROOT / "extracts"
    extracts_dir.mkdir(exist_ok=True)

    pages = []
    with pdfplumber.open(str(SOURCE)) as pdf:
        for page_number, page in enumerate(pdf.pages, 1):
            raw = (page.extract_text(x_tolerance=1, y_tolerance=3) or "").strip()
            pages.append(
                {
                    "page": page_number,
                    "raw_text": raw,
                    "clean_text": clean_text(raw),
                    "width": page.width,
                    "height": page.height,
                    "extraction_confidence": "high" if raw else "low",
                    "asset_descriptions": [
                        "PowerPoint slide-export page; rendered preview stored under work/lect03_crawler/source_preview."
                    ],
                }
            )

    md_lines = [
        "# Source Extract: lect03_crawler",
        "",
        f"- Source file: {SOURCE}",
        "- Source format: slide-export PDF",
        "- Pages: 45",
        "- Source language: Chinese with Python/HTML code",
        "- Target language: Chinese",
        "- Extraction confidence: high for text; PowerPoint tracking introduced extra spaces, cleaned copy preserves wording for downstream use.",
        "",
    ]
    for page in pages:
        md_lines.extend(
            [
                f"## Page {page['page']}",
                "",
                page["clean_text"] or "[No extractable text]",
                "",
            ]
        )

    (extracts_dir / f"{TASK_SLUG}.source.md").write_text("\n".join(md_lines), encoding="utf-8")
    (extracts_dir / f"{TASK_SLUG}.source.json").write_text(
        json.dumps(
            {
                "source_file": str(SOURCE),
                "task_slug": TASK_SLUG,
                "source_format": "slide-export PDF",
                "page_count": len(pages),
                "source_language": "Chinese with Python/HTML code",
                "target_language": "Chinese",
                "pages": pages,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(extracts_dir / f"{TASK_SLUG}.source.md")
    print(extracts_dir / f"{TASK_SLUG}.source.json")


if __name__ == "__main__":
    main()
