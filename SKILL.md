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
- Fix self-study blockers: missing prerequisites, unexplained symbols, skipped reasoning, weak examples, poor sequencing, and exercises without guidance.
- Update or flag outdated claims, especially software versions, standards, APIs, datasets, benchmarks, laws, tools, and current practice.
- Prefer clear learning flow over slide count preservation when the source structure prevents self-study.
- Visually verify every requested output before delivery.

## Capability Discovery

Before editing files or updating factual claims, search or inspect the agent environment for:

- A presentation or slide-deck capability that can inspect, edit, rebuild, render, and export PPTX or equivalent deck files.
- A PDF capability that can read, extract, render pages, create PDFs, and visually verify final output.
- A subagent or delegation capability for source extraction and output materialization.
- A web search, browser, documentation, retrieval, or citation-capable research tool for time-sensitive or externally verifiable claims.

If any required capability is unavailable, refuse to execute the task. Tell the user which capability is missing and direct them to the installation guide:
`INSTALLATION_GUIDE_URL_TBD`

## Capability Routing

- First, discover the available file-handling capabilities by searching installed skills for presentation/PPTX/PowerPoint/slide-deck support and PDF reading/rendering/export support.
- Read `references/file-in-adapters.md` for format-specific source parsing and `references/file-out-adapters.md` for materialization, export, and selected-output verification.
- Use format-specific tools only at the I/O boundaries: source inspection/extraction, PPTX materialization when needed, PDF export, and selected-output verification.
- Use the same teaching diagnosis, self-study reconstruction, factual review, and test standards regardless of whether the source was PPTX or PDF.
- For time-sensitive or factual claims that require cross check, use the discovered web-searching capability.

## Artifact Paths

Use stable task-specific filenames. Derive `<task-slug>` from the source filename or user request.

- `extracts/<task-slug>.source.md`: extracted source content in Markdown, preserving original wording and page/slide provenance.
- `extracts/<task-slug>.source.json`: extracted source content in structured JSON, preserving original wording, assets, provenance, and extraction confidence.
- `assets/<task-slug>.knowledge-graph.md`: knowledge graph template filled only with source-derived content.
- `assets/<task-slug>.knowledge-graph.completed.md`: knowledge graph after rule-based completion and freshness checking.
- `assets/style-presets/default.json`: default teaching-courseware visual preset for output materialization and visual/export checks.
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
2. **Parse, inspect, and export source extracts**: read `references/file-in-adapters.md`, then use the discovered capability appropriate to the input format. Export the original source content to both `extracts/<task-slug>.source.md` and `extracts/<task-slug>.source.json`. Include page/slide provenance, extracted assets, and extraction confidence. Do not rewrite, summarize, or normalize source text; preserve original wording whenever possible.
3. **Fill the knowledge graph template from extracts**: read `extracts/<task-slug>.source.md`, `extracts/<task-slug>.source.json`, and `references/knowledge-graph-template.md`. Place source-derived content into the template and export `assets/<task-slug>.knowledge-graph.md`. If the source file has no content for a template field, leave that field blank. Do not invent, paraphrase, or smooth the source text; keep original wording and provenance.
4. **Complete blank template fields**: read `assets/<task-slug>.knowledge-graph.md` and `references/completion-rules.md`. Complete only the blank fields needed for self-study quality, then export `assets/<task-slug>.knowledge-graph.completed.md`. Do not freely rewrite or generate text. Prefer source wording, and for supplemental content selectively use verified search results or authoritative references when required. Label supplemental content separately from source-derived content.
5. **Check freshness and correctness in the completed graph**: read `assets/<task-slug>.knowledge-graph.completed.md` and `references/outdated-content-checking.md`. If the task requires updating or correcting time-sensitive claims, verify them with authoritative sources through the discovered research capability; if that capability is unavailable, refuse the task and direct the user to the installation guide. Export the checked result back to `assets/<task-slug>.knowledge-graph.completed.md`, preserving source-derived text and labeling verified supplements.
6. **Materialize the upgraded material**: read `references/file-out-adapters.md` and `assets/style-presets/default.json`, then start the required output subagent(s) for the user-specified output route. Use `assets/<task-slug>.knowledge-graph.completed.md` as the content source of truth and provide the style preset as the default visual guidance when the source style is unusable, incomplete, or not requested for preservation. Do not invent facts, examples, explanations, exercises, citations, or visual labels during materialization. Preserve original course phrasing unless a completion rule or verified update requires a clearly labeled supplement.
7. **Export and verify selected outputs**: require the output subagent to export the user-specified PPTX and/or PDF and apply the relevant checks from `assets/style-presets/default.json`. For PDF output, require render verification with the discovered PDF capability. For PPTX output, require preview/render or equivalent visual verification with the discovered presentation/deck capability. Inspect or review the subagent's verification output for clipping, overlap, unreadable formulas, missing glyphs, poor contrast, blank pages/slides, broken images, inconsistent numbering, unresolved placeholders, and violations of the default preset's accessibility/export checks.
8. **Test the upgraded material**: read `references/test-standards.md`, then test the completed knowledge graph, materialized output, selected-output verification, and required deliverables. Record test results in a quality report. Do not deliver if any blocker-level test fails.
9. **Iterate if tests fail**: fix content, provenance, materialization, or layout issues through the appropriate underlying capability, then re-export, re-render, and re-test. Do not deliver an output that fails testing unless the failure is explicitly reported as a blocker.
10. **Export final files to `exports/`**: create `exports/<task-slug>/` and place the requested PPTX and/or verified PDF, quality report, and final `assets/<task-slug>.knowledge-graph.completed.md` copy there. Do not deliver from scratch or temporary locations.
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
- Steps 6-10, materialization and export: read `references/file-out-adapters.md` and `assets/style-presets/default.json`. The adapter defines output route execution, PPTX creation, PDF creation, selected-output verification, and `exports/<task-slug>/` deliverables; the style preset defines default teaching-courseware visual guidance and export checks.
- Step 8, test: read `references/test-standards.md` before approving delivery or writing the final quality report.
