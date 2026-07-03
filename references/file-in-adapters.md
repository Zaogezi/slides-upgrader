# File Input Adapters

Use this reference for input-side subagent delegation and extract output contracts. Do not duplicate parsing internals already owned by available presentation/deck or PDF skills.

## Boundary Principle

PPTX and PDF differ only in which subagent prompt and capability receive the extraction task. The main workflow needs the same outputs in both cases:

- `extracts/<task-slug>.source.md`
- `extracts/<task-slug>.source.json`
- Original wording preserved where possible.
- Page/slide provenance for every extracted item.
- Asset descriptions, uncertainty notes, and extraction confidence.

After source content is recovered, return to the shared workflow in `SKILL.md` for knowledge-graph completion, factual checking, testing, and quality review.

## PPTX Input Adapter

For `.pptx` sources or equivalent presentation source files, start a subagent and instruct it to use the available presentation/deck skill or capability. The main agent should not duplicate PPTX inspection, rendering, layout parsing, notes extraction, or asset extraction rules that are already owned by the presentation/deck capability.

The main agent is responsible only for:

- Providing the deck path, `<task-slug>`, and output paths.
- Requiring source-faithful extraction with slide-level provenance.
- Receiving the generated `extracts/<task-slug>.source.md` and `extracts/<task-slug>.source.json`.
- Checking that both files exist and match the required output contract.

Use this prompt for the subagent:

```text
Use the available presentation/deck skill or capability to inspect and extract the source deck below.

Source deck:
<absolute-source-deck-path>

Task slug:
<task-slug>

Required outputs:
1. extracts/<task-slug>.source.md
2. extracts/<task-slug>.source.json

Requirements:
- Preserve the deck's original wording wherever extraction quality allows.
- Do not improve, rewrite, summarize, or pedagogically upgrade the content.
- Include slide-level provenance for extracted titles, visible text, speaker notes, figures, equations, tables, code, charts, and embedded assets.
- Render or visually inspect slides as needed using the presentation/deck skill or capability.
- Record extraction confidence and any inaccessible objects, missing fonts, broken layouts, ambiguous equations, unreadable screenshots, or visually important content.
- In the JSON output, preserve structured fields for source location, original text, notes, asset descriptions, layout/template observations, extraction confidence, and uncertainty notes.
- In the Markdown output, make the extracted content readable for downstream knowledge-graph template filling.
- If the presentation/deck skill or capability cannot complete extraction or render verification, report the missing capability or source-quality blocker instead of inventing content.

Return only:
- The paths of the two created extract files.
- A concise extraction summary.
- Any blocker or uncertainty that the main agent must preserve downstream.
```

## PDF Input Adapter

For `.pdf` sources, start a subagent and instruct it to use the available PDF skill/capability. The main agent should not duplicate PDF parsing, OCR, rendering, or extraction rules that are already owned by the PDF skill.

The main agent is responsible only for:

- Providing the PDF path, `<task-slug>`, and output paths.
- Requiring source-faithful extraction with provenance.
- Receiving the generated `extracts/<task-slug>.source.md` and `extracts/<task-slug>.source.json`.
- Checking that both files exist and match the required output contract.

Use this prompt for the subagent:

```text
Use the available PDF skill/capability to inspect and extract the PDF source below.

Source PDF:
<absolute-source-pdf-path>

Task slug:
<task-slug>

Required outputs:
1. extracts/<task-slug>.source.md
2. extracts/<task-slug>.source.json

Requirements:
- Preserve the PDF's original wording wherever extraction quality allows.
- Do not improve, rewrite, summarize, or pedagogically upgrade the content.
- Include page-level provenance for extracted text, figures, equations, tables, code, headings, and notes.
- Render or visually inspect pages as needed using the PDF skill/capability.
- Record extraction confidence and any unreadable, ambiguous, missing, scanned, OCR-sensitive, or visually important content.
- In the JSON output, preserve structured fields for source location, original text, asset descriptions, extraction confidence, and uncertainty notes.
- In the Markdown output, make the extracted content readable for downstream knowledge-graph template filling.
- If the PDF skill/capability cannot complete extraction or render verification, report the missing capability or source-quality blocker instead of inventing content.

Return only:
- The paths of the two created extract files.
- A concise extraction summary.
- Any blocker or uncertainty that the main agent must preserve downstream.
```

## Source Quality Blockers

Report a content blocker, without pretending the task is complete, when source quality prevents reliable reconstruction:

- Scans are too low-resolution to recover important text.
- Equations or diagrams cannot be interpreted confidently.
- Critical source pages are missing, corrupted, or out of order.
- OCR changes technical symbols, code, formulas, or units in a way that cannot be resolved.

When blocked by source quality rather than missing capability, state exactly what input is needed.

## Handoff Notes

Before leaving the input phase, export both required extract files:

- `extracts/<task-slug>.source.md`
- `extracts/<task-slug>.source.json`

Both files must preserve original wording and source provenance. The Markdown file should be readable for template filling. The JSON file should be structured enough for reliable cross-reference.

Keep concise notes covering:

- Source format and classification.
- Extracted outline or section map.
- Important source assets to preserve.
- Extraction uncertainties.
- Recommended output route candidates for `references/file-out-adapters.md`.
