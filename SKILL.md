---
name: slides-upgrader
description: Upgrade low-quality, outdated, or self-study-hostile STEM course materials from PPTX or PDF into improved self-study learning materials, then export PPTX, PDF, or both. Use when the user wants to improve lecture slides, course decks, handouts, or PDF slide exports for undergraduate STEM self-learning. This skill orchestrates content extraction, knowledge-graph completion, factual checking, testing, and quality review while delegating file editing, rendering, and export to whatever presentation/PDF capabilities are available in the agent environment.
---

# Slides Upgrader

## Role

Use this skill as the teaching-improvement layer for STEM courseware. Diagnose and restructure the learning experience, then rely on available file-format capabilities for implementation.

## Core Principles

- Treat the task as educational reconstruction, not cosmetic polishing.
- Preserve correct source content, useful diagrams, equations, examples, and instructor intent.
- During extraction, template filling, and reconstruction, do not freely rewrite or generate content. Preserve the source wording wherever it is usable.
- For PPTX output, do not use cropped source-slide images to reproduce text, mathematical formulas, or code. Reconstruct them with the required text, formula, and code export routes. Use cropped source images only for image-like source assets; regenerate schematic diagrams whenever the source provides enough structure to do so reliably.
- Fix self-study blockers: missing prerequisites, unexplained symbols, skipped reasoning, weak examples, poor sequencing, and exercises without guidance.
- Update or flag outdated claims, especially software versions, standards, APIs, datasets, benchmarks, laws, tools, and current practice.
- Prefer clear learning flow over slide count preservation when the source structure prevents self-study.
- Use the largest practical text size and line spacing that fit without clipping, overlap, or broken hierarchy. Prefer splitting dense content across additional slides/pages over shrinking learner-facing text.
- Visually verify every requested output before delivery.

## Environment Requirements

This skill does not ship a fixed runtime or package lockfile. The executing agent environment must provide the capabilities required by the selected input, output route, and source content:

- **Presentation/PPTX capability**: required for PPTX input or PPTX output. It must inspect, rebuild, preview/render, and export PPTX or equivalent deck files. For PPTX output that contains formulas, it must support native equation objects or verified rendered formula assets; formulas must not be exported as default text boxes containing raw LaTeX, plain Unicode approximations, or placeholder equation text. For PPTX output that contains code blocks, it must support purpose-built editable code text boxes with rich text runs so syntax highlighting can be applied inside one text box per code block; code must not be exported through default/plain text boxes.
- **PDF capability**: required for PDF input, PDF output, and final PDF render verification. It must extract text when possible, render pages to images, create or export PDFs, and support visual QA.
- **Research capability**: required only when the material contains time-sensitive, versioned, current-practice, or externally verifiable claims that must be checked or updated.
- **Formula rendering capability**: required when the material contains complex formulas or sentences/paragraphs with embedded mathematical expressions that cannot be reliably represented by the deck/PDF capability. Supported routes include MathJax, KaTeX, or LaTeX, with optional SVG/PNG conversion through tools such as `sharp` or `dvisvgm`. When a sentence or paragraph contains mathematical notation, render the whole sentence or paragraph through a route that supports inline math instead of leaving the mathematical expression as plain text inside a normal text run.
- **Structural diagram rendering capability**: required when the material contains trees, syntax trees, state machines, automata, flowcharts, dependency graphs, DAGs, or local knowledge-graph diagrams that must be generated or repaired. Supported routes include Graphviz, Mermaid, or equivalent graph renderers.
- **Code export capability**: required when the selected output contains code blocks. PPTX output must support purpose-built editable code text boxes with rich text runs; PDF output must preserve code-frame layout, monospace typography, syntax highlighting when used, indentation, and line breaks.
- **Programmatic SVG capability**: required when source-derived mathematical schematics, geometry sketches, set relations, vector mappings, or arrow relation diagrams must be generated or repaired.
- **Plotting capability**: required when source-derived data figures, function plots, heatmaps, matrices, algorithm visualizations, statistics charts, or experimental result plots must be generated or repaired. Supported routes include Python or JS plotting stacks.

Formula, structural diagram, code export, SVG, and plotting tools are conditional requirements. Do not require all of them for every task; preflight only the routes needed by the source and completed knowledge graph. If a needed formula, structural diagram, or code export capability is unavailable, the agent must stop before export/materialization. If the environment permits installing dependencies, request approval and install the corresponding environment; otherwise ask the user to install the missing capability and do not produce a degraded export.

## Capability Discovery

Before editing files or updating factual claims, search or inspect the agent environment for:

- A presentation or slide-deck capability that can inspect, edit, rebuild, render, and export PPTX or equivalent deck files.
- A PDF capability that can read, extract, render pages, create PDFs, and visually verify final output.
- Formula and diagram rendering capabilities needed by the material, selected from `references/math-diagram-rendering.md`: MathJax, KaTeX, LaTeX, Graphviz, Mermaid, SVG generation, or Python/JS plotting.
- A web search, browser, documentation, retrieval, or citation-capable research tool for time-sensitive or externally verifiable claims.

Run a capability preflight before source extraction or materialization. Record the results in the quality report or scratch notes:

- **PDF tools**: verify that text extraction can run and that at least one PDF render path can produce page images. For Poppler, try paths in this order: bundled runtime `bin` wrapper, bundled runtime `native/poppler/bin`, bundled runtime `native/poppler/Library/bin`, then system `PATH`.
- **Presentation tools**: verify that the presentation/deck capability can create or inspect a trivial deck and render at least one slide preview before relying on it for final output.
- **PPTX export**: verify that the chosen authoring/export route can write a non-empty `.pptx` under the intended output directory or scratch directory.
- **PPTX formula export**: when PPTX output contains formulas or mixed prose/math sentences, verify that the chosen authoring route can create native equation objects, inline equation runs, or place verified rendered formula/prose assets. Do not use default text boxes, raw LaTeX, plain Unicode approximations, or placeholder equation strings as a fallback. Do not split a sentence into plain text plus a text-like formula substitute when the sentence contains mathematical notation.
- **PPTX code export**: when PPTX output contains code, verify that the chosen authoring route can create a purpose-built single editable code text box per code block with monospace rich text runs for syntax highlighting. Do not use default/plain text boxes, screenshots, or one text box per token as a fallback.
- **PDF export/render**: verify that the chosen PDF creation route can write a non-empty `.pdf` and render it back to page images.
- **Formula and diagram rendering**: when the source or completed graph contains complex formulas, structural diagrams, mathematical schematics, plots, or algorithm visualizations, read `references/math-diagram-rendering.md` and verify the relevant renderer with a small sample before relying on it.
- **Missing formula/structure/code environment**: if formula rendering, structural diagram rendering, or code export capability is required but unavailable, stop before export. Install the missing dependency only when the execution environment allows it and user approval has been granted; otherwise report the exact missing item and ask the user to install it. Do not continue by converting formulas or code to default text boxes, screenshots, raw syntax, or unverified approximations.
- **Research tools**: when freshness checking is needed, verify that the research capability can reach authoritative sources before changing time-sensitive claims.
- If a wrapper command fails but an underlying binary exists in a known runtime path, use the working binary and record the fallback path instead of treating the capability as missing.

If any required capability is unavailable, refuse to export the task. Tell the user which capability is missing and direct them to the installation guide:
`INSTALLATION_GUIDE_URL_TBD`

## Capability Routing

- First, discover the available file-handling capabilities by searching installed skills for presentation/PPTX/PowerPoint/slide-deck support and PDF reading/rendering/export support.
- Read `references/file-in-adapters.md` for format-specific source parsing, `references/file-out-adapters.md` for materialization/export/verification, and `references/math-diagram-rendering.md` when formulas or diagrams must be generated or repaired.
- Use format-specific tools only at the I/O boundaries: source inspection/extraction, PPTX materialization when needed, PDF export, and selected-output verification.
- Use formula, diagram, SVG, and plotting tools only as rendering routes for source-derived or verified supplemental content; do not use them to invent new facts, labels, equations, graph edges, or data.
- Use the same teaching diagnosis, self-study reconstruction, factual review, and test standards regardless of whether the source was PPTX or PDF.
- For time-sensitive or factual claims that require cross check, use the discovered web-searching capability.

## Artifact Paths

Use stable task-specific filenames. Derive `<task-slug>` from the source filename or user request.

- `extracts/<task-slug>.source.md`: extracted source content in Markdown, preserving original wording and page/slide provenance.
- `extracts/<task-slug>.source.json`: extracted source content in structured JSON, preserving original wording, assets, provenance, and extraction confidence.
- `assets/<task-slug>.knowledge-graph.md`: knowledge graph template filled only with source-derived content.
- `assets/<task-slug>.knowledge-graph.completed.md`: knowledge graph after rule-based completion and freshness checking.
- `assets/style-presets/default.json`: default teaching-courseware visual preset for output materialization and visual/export checks.
- `exports/<task-slug>/qa/`: retained render evidence, contact sheets, generated formula/diagram assets, and visual QA logs.
- `exports/<task-slug>/`: final deliverables, including requested PPTX and/or verified PDF, quality report, and relevant final knowledge graph.

## Prerequisite Information

Before rewriting, establish the following information:

- **Format**: infer from the file extension and source inspection. Classify as PPTX, text-based PDF, scanned PDF, mixed PDF, slide-export PDF, handout PDF, or unknown.
- **Subject**: infer from the material itself. Classify as mathematics, physics, engineering, computer science, lab course, or another STEM area.
- **Target language**: infer from the request or source language; ask the user if the desired language is ambiguous.
- **Style preservation**: infer from the request; ask whether to preserve the original visual style only if it affects the output route or effort.
- **Output route**: ask the user to specify one route before materialization:
  - output PPTX
  - output PDF
  - output PPTX and PDF

- If the user has not specified some information, pause before executing and ask for details. Make sure all of the given information before execution 

## Workflow

1. **Establish prerequisite information**: infer format and subject from the source, infer target language and style preservation when possible, and obtain the user-specified output route before materialization. Ask user for uncertain information. Establish all the required information.
2. **Parse, inspect, and export source extracts**: read `references/file-in-adapters.md`, then use the discovered capability appropriate to the input format. Export the original source content to both `extracts/<task-slug>.source.md` and `extracts/<task-slug>.source.json`. Include page/slide provenance, extracted assets, extraction confidence, and any normalization/cleaning confidence. Do not rewrite, summarize, or pedagogically upgrade source text. When extraction artifacts such as PDF spacing, broken line joins, or OCR noise make the wording unreadable, preserve raw text in JSON and add a separately labeled normalized text field for downstream use.
3. **Fill the knowledge graph template from extracts**: read `extracts/<task-slug>.source.md`, `extracts/<task-slug>.source.json`, and `references/knowledge-graph-template.md`. Place source-derived content into the template and export `assets/<task-slug>.knowledge-graph.md`. If the source file has no content for a template field, leave that field blank. Do not invent, paraphrase, or smooth the source text; keep original wording and provenance.
4. **Complete blank template fields**: read `assets/<task-slug>.knowledge-graph.md` and `references/completion-rules.md`. Complete only the blank fields needed for self-study quality, then export `assets/<task-slug>.knowledge-graph.completed.md`. Do not freely rewrite or generate text. Prefer source wording, and for supplemental content selectively use verified search results or authoritative references when required. Label supplemental content separately from source-derived content.
5. **Check freshness and correctness in the completed graph**: read `assets/<task-slug>.knowledge-graph.completed.md` and `references/outdated-content-checking.md`. If the task requires updating or correcting time-sensitive claims, verify them with authoritative sources through the discovered research capability; if that capability is unavailable, refuse the task and direct the user to the installation guide. Export the checked result back to `assets/<task-slug>.knowledge-graph.completed.md`, preserving source-derived text and labeling verified supplements.
6. **Materialize the upgraded material**: read `references/file-out-adapters.md`, `references/math-diagram-rendering.md` when formula or diagram rendering is needed, and `assets/style-presets/default.json`, then use the required file-handling capability for the user-specified output route. Use `assets/<task-slug>.knowledge-graph.completed.md` as the content source of truth and provide the style preset as the default visual guidance when the source style is unusable, incomplete, or not requested for preservation. Render complex formulas, mixed prose/math sentences or paragraphs, structural diagrams, schematics, and plots through the route matrix in `references/math-diagram-rendering.md`, and export code through the required code route for the selected output format. For PPTX output, crop the original source only for image-like assets; reconstruct text, formulas, and code, and prefer generated/recreated schematic diagrams over source crops when source structure is sufficient. Do not invent facts, examples, explanations, exercises, citations, equations, data, graph edges, or visual labels during materialization. If the required formula, structural diagram, or code export environment is missing, stop materialization; install it only with permission when possible, otherwise ask the user to install it. Preserve original course phrasing unless a completion rule or verified update requires a clearly labeled supplement.
7. **Export and verify selected outputs**: export the user-specified PPTX and/or PDF through the selected file-handling capability and apply the relevant checks from `assets/style-presets/default.json` and `references/math-diagram-rendering.md`. For PDF output, require render verification with the discovered PDF capability. For PPTX output, require preview/render or equivalent visual verification with the discovered presentation/deck capability. Inspect or review the verification output for clipping, overlap, unreadable formulas, missing glyphs, poor contrast, blank pages/slides, broken images, inconsistent numbering, unresolved placeholders, formulas exported as default text boxes or raw syntax, broken diagram labels, reversed diagram arrows, corrupted plots, default/plain PPTX text boxes used for code blocks, non-editable PPTX code blocks, token-by-token code text boxes, code syntax highlighting simulated through multiple text objects, and violations of the default preset's accessibility/export checks. Also run the automated checks in `references/test-standards.md`: non-empty requested files, preview/render page counts, PDF page count matching the intended deck/page count, formula/diagram full-size review, PPTX formula object/rendered-asset review, PPTX editable code text-box review, and required final artifacts under `exports/<task-slug>/`.
8. **Test the upgraded material**: read `references/test-standards.md`, then test the completed knowledge graph, materialized output, selected-output verification, and required deliverables. Record test results, preflight results, render evidence, and final checklist status in a quality report. Do not deliver if any blocker-level test fails.
9. **Iterate if tests fail**: fix content, provenance, materialization, or layout issues through the appropriate underlying capability, then re-export, re-render, and re-test. Do not deliver an output that fails testing unless the failure is explicitly reported as a blocker.
10. **Export final files to `exports/`**: create `exports/<task-slug>/` and place the requested PPTX and/or verified PDF, quality report, final `assets/<task-slug>.knowledge-graph.completed.md` copy, and change/freshness logs when present. Before delivery, complete the final deliverable checklist in `references/test-standards.md`. Do not deliver from scratch or temporary locations.
11. **Deliver with a concise report**: provide the requested PPTX and/or PDF paths under `exports/<task-slug>/`, the major learning improvements, and any factual claims that were changed, sourced, or left uncertain.

## Output Requirements

- Always deliver the user-requested PPTX and/or PDF under `exports/<task-slug>/`.
- When the route includes PPTX, export a `.pptx` file under `exports/<task-slug>/`.
- When the route includes PDF, export a render-verified `.pdf` file under `exports/<task-slug>/`.
- Include a short quality report covering learning-structure improvements, factual updates, and remaining uncertainties.
- Keep generated scratch notes separate from final learner-facing material.

## Reference Map

Read references in workflow order. Do not load all references by default.

- Step 2, source extraction: read `references/file-in-adapters.md`. It defines PPTX/PDF input parsing, source rendering, extraction confidence, and the required `extracts/<task-slug>.source.md` / `.json` outputs.
- Step 3, knowledge graph construction: read `references/knowledge-graph-template.md`. It defines the Markdown template exported to `assets/<task-slug>.knowledge-graph.md`.
- Step 4, blank-field completion: read `references/completion-rules.md`. It defines when and how to fill missing fields while preserving source wording and labeling supplements.
- Step 5, freshness checking: read `references/outdated-content-checking.md` when the knowledge graph contains time-sensitive, versioned, current-practice, or externally verifiable claims.
- Steps 6-10, materialization and export: read `references/file-out-adapters.md`, `references/math-diagram-rendering.md` when formulas or diagrams need generation or repair, and `assets/style-presets/default.json`. The adapters define output route execution, PPTX creation, PDF creation, formula/diagram rendering, selected-output verification, and `exports/<task-slug>/` deliverables; the style preset defines default teaching-courseware visual guidance and export checks.
- Step 8, test: read `references/test-standards.md` before approving delivery or writing the final quality report.
