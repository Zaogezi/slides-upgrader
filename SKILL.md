---
name: slides-upgrader
description: Upgrade low-quality, outdated, or self-study-hostile STEM course materials from PPTX or PDF into improved self-study learning materials, then export PPTX, PDF, or both. Use when the user wants to improve lecture slides, course decks, handouts, or PDF slide exports for undergraduate STEM self-learning. This skill orchestrates content extraction, knowledge-graph completion, factual checking, testing, and quality review while delegating file editing, rendering, and export to whatever presentation/PDF capabilities are available in the agent environment.
---

# Slides Upgrader

## Role

Use this skill as the teaching-improvement layer for STEM courseware. Diagnose and restructure the learning experience, then rely on available file-format capabilities for implementation.

## Non-Negotiable Hard Gates

If any hard gate fails, stop the workflow and report the blocker. Do not produce or deliver a degraded PPTX/PDF as a substitute for passing the gate.

1. **Source Manifest Gate**: Step 2 must create `extracts/<task-slug>.source-manifest.json`. Every substantive source item must have a stable `id`, original wording or verbatim fragment, item type, source provenance, and extraction confidence.
2. **UTF-8 Encoding Gate**: All generated text artifacts must be written and read as UTF-8, including Markdown, JSON, CSV/TSV, SVG, HTML, logs, coverage reports, quality reports, and scratch notes that may be reused downstream. Do not use platform-default encodings, lossy replacement, GBK/ANSI fallbacks, or mojibake text in final artifacts. Any generated text artifact that cannot be decoded as UTF-8 or contains encoding-corruption markers is a blocker.
3. **Source Coverage Gate**: Every item in `extracts/<task-slug>.source-manifest.json` must appear in `assets/<task-slug>.knowledge-graph.md`, either in a normal graph field or in Unassigned Source Content. Topic-only capture is not enough; the item id and original wording or verbatim fragment must be present.
4. **Knowledge Graph Template Gate**: `assets/<task-slug>.knowledge-graph.md` and `assets/<task-slug>.knowledge-graph.completed.md` must retain the required template structure from `references/knowledge-graph-template.md`. They must include the chapter directory, chapter blocks, knowledge-point blocks, required knowledge-point subsections, and Unassigned Source Content table. Replacing the template with a brief outline, topic summary, page list, or ad hoc section such as "Lossless Source Items" is a blocker.
5. **Graph Preservation Gate**: Every source-derived item in `assets/<task-slug>.knowledge-graph.md` must survive into `assets/<task-slug>.knowledge-graph.completed.md`. Do not delete, merge away, summarize away, or paraphrase source items unless the original wording remains traceable with item id and provenance.
6. **Export Coverage Gate**: Every learner-facing item in `assets/<task-slug>.knowledge-graph.completed.md` must appear in the exported PPTX and/or PDF. Materialization may split, reorder within the approved learning flow, or re-render content, but it must not summarize multiple graph items into an untraceable substitute.
7. **Formula Gate**: Mathematical notation, including inline math inside sentences, must be exported through native equation objects, inline-equation-capable runs, or verified rendered formula/prose assets. Raw LaTeX, Unicode approximations, default text-box formulas, ordinary prose with text-like math substitutes, or placeholder equation strings are blocker failures.
8. **Diagram And Plot Gate**: Structural diagrams, mathematical schematics, charts, plots, and algorithm visualizations must be exported as verified visual objects generated through the approved route or retained as documented non-reconstructable source figures. A bare text box that merely describes the diagram, chart, axes, nodes, arrows, or visual relationship is not a substitute for the visual object and is a blocker.
9. **Code Gate**: PPTX code blocks must be single editable purpose-built code text boxes with monospace rich text runs when syntax highlighting is used. Screenshots, source crops, default/plain text boxes, token-level boxes, line-level boxes, or overlaid text fragments are blocker failures.
10. **Layout Gate**: Use the largest practical learner-facing text size and line spacing that fit without clipping or overlap. Split content across additional slides/pages before shrinking below the preset's preferred sizes. Preserving the original slide/page count is never a reason to overpack content.
11. **Visual Variety Gate**: PPTX outputs with six or more slides must use a deliberate mix of slide structures appropriate to the learning flow, such as chapter overview, concept introduction, definition and symbols, derivation, example walkthrough, interactive check, and chapter summary. A multi-slide deck dominated by one layout or one repeated visual template is a blocker unless the user explicitly requested a uniform template.
12. **Verification Gate**: No final delivery is allowed without render/preview evidence, automated template/content/style audits when available, UTF-8 validation for generated text artifacts, coverage review, and a quality report that records pass/revise/blocker status for every required gate.

## Core Principles

- During extraction, template filling, and reconstruction, do not freely rewrite or generate content. Preserve the source wording wherever it is usable.
- Treat source extraction and knowledge-graph construction as lossless content capture. Every learner-facing item recovered from the source — definitions, claims, explanations, examples, exercises, answers, formulas, code blocks, tables, figure/diagram specifications, speaker notes, captions, and any other substantive content — must appear somewhere in `assets/<task-slug>.knowledge-graph.md` and survive into `assets/<task-slug>.knowledge-graph.completed.md`. Do not drop, summarize away, or silently skip source content because it is awkward, off-template, or low quality. If a source item does not fit an existing template field, record it under the closest knowledge point or in the explicit Unassigned Source Content section with provenance, rather than omitting it.
- Treat `assets/<task-slug>.knowledge-graph.completed.md` as a complete content manifest for export. PPTX and PDF outputs must faithfully restate every learner-facing item in that corrected Markdown, including supplements and verified corrections, without selective omission, summarization, or newly invented substitute content.
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

## Encoding Requirements

Use UTF-8 for every generated text artifact and script-created report. In Python, use explicit `encoding="utf-8"` for `read_text`, `write_text`, `open`, JSON reads/writes, CSV/TSV reads/writes, and subprocess-captured text that is saved for reuse. In PowerShell, use UTF-8 output encodings when writing generated text files. Never rely on Windows ANSI, GBK, or locale defaults for Markdown, JSON, CSV/TSV, SVG, HTML, or log artifacts.

Preserve source text in its intended language, but do not preserve mojibake. If extraction produces garbled text such as replacement characters or UTF-8/GBK corruption markers, keep the raw extraction separately when available, add a normalized UTF-8 field only after review, and mark the item as an extraction/encoding uncertainty. Do not let corrupted text become learner-facing content or a passing knowledge graph.

## Capability Discovery

Before editing files or updating factual claims, search or inspect the agent environment for:

- A presentation or slide-deck capability that can inspect, edit, rebuild, render, and export PPTX or equivalent deck files.
- A PDF capability that can read, extract, render pages, create PDFs, and visually verify final output.
- Formula and diagram rendering capabilities only after the source or completed graph confirms formulas, diagrams, schematics, plots, or algorithm visualizations. Do not read `references/math-diagram-rendering.md` during general discovery.
- A web search, browser, documentation, retrieval, or citation-capable research tool for time-sensitive or externally verifiable claims.

Run a capability preflight before source extraction or materialization. Record the results in the quality report or scratch notes:

- **PDF tools**: verify that text extraction can run and that at least one PDF render path can produce page images. For Poppler, try paths in this order: bundled runtime `bin` wrapper, bundled runtime `native/poppler/bin`, bundled runtime `native/poppler/Library/bin`, then system `PATH`.
- **Presentation tools**: verify that the presentation/deck capability can create or inspect a trivial deck and render at least one slide preview before relying on it for final output.
- **PPTX export**: verify that the chosen authoring/export route can write a non-empty `.pptx` under the intended output directory or scratch directory.
- **PPTX formula export**: when PPTX output contains formulas or mixed prose/math sentences, verify that the chosen authoring route can create native equation objects, inline equation runs, or place verified rendered formula/prose assets. Do not use default text boxes, raw LaTeX, plain Unicode approximations, or placeholder equation strings as a fallback. Do not split a sentence into plain text plus a text-like formula substitute when the sentence contains mathematical notation.
- **PPTX code export**: when PPTX output contains code, verify that the chosen authoring route can create a purpose-built single editable code text box per code block with monospace rich text runs for syntax highlighting. Do not use default/plain text boxes, screenshots, or one text box per token as a fallback.
- **PDF export/render**: verify that the chosen PDF creation route can write a non-empty `.pdf` and render it back to page images.
- **Formula and diagram rendering**: first classify whether the source or completed graph contains complex formulas, structural diagrams, mathematical schematics, plots, or algorithm visualizations. Only when such content is confirmed, read `references/math-diagram-rendering.md` and verify the relevant renderer with a small sample before relying on it.
- **Missing formula/structure/code environment**: if formula rendering, structural diagram rendering, or code export capability is required but unavailable, stop before export. Install the missing dependency only when the execution environment allows it and user approval has been granted; otherwise report the exact missing item and ask the user to install it. Do not continue by converting formulas or code to default text boxes, screenshots, raw syntax, or unverified approximations.
- **Research tools**: when freshness checking is needed, verify that the research capability can reach authoritative sources before changing time-sensitive claims.
- If a wrapper command fails but an underlying binary exists in a known runtime path, use the working binary and record the fallback path instead of treating the capability as missing.

If any required capability is unavailable, refuse to export the task. Tell the user which capability is missing and direct them to the installation guide:
`INSTALLATION_GUIDE_URL_TBD`

## Capability Routing

- First, discover the available file-handling capabilities by searching installed skills for presentation/PPTX/PowerPoint/slide-deck support and PDF reading/rendering/export support.
- Do not read any reference file until its gate condition is true. At each workflow step, select only the reference required by that step, and do not preload later-step references for convenience.
- Read `references/file-in-adapters.md` only when source extraction begins, `references/file-out-adapters.md` only after the output route is known and materialization begins, and `references/math-diagram-rendering.md` only when formulas, diagrams, schematics, plots, or algorithm visualizations must be generated, repaired, or verified.
- Use format-specific tools only at the I/O boundaries: source inspection/extraction, PPTX materialization when needed, PDF export, and selected-output verification.
- Use formula, diagram, SVG, and plotting tools only as rendering routes for source-derived or verified supplemental content; do not use them to invent new facts, labels, equations, graph edges, or data.
- Use the same teaching diagnosis, self-study reconstruction, factual review, and test standards regardless of whether the source was PPTX or PDF.
- For time-sensitive or factual claims that require cross check, use the discovered web-searching capability.

## Artifact Paths

Use stable task-specific filenames. Derive `<task-slug>` from the source filename or user request.

- `extracts/<task-slug>.source.md`: extracted source content in Markdown, preserving original wording and page/slide provenance.
- `extracts/<task-slug>.source.json`: extracted source content in structured JSON, preserving original wording, assets, provenance, and extraction confidence.
- `extracts/<task-slug>.source-manifest.json`: lossless source item manifest used for coverage checks. Each substantive item must have `id`, `source_location`, `item_type`, `original_text` or `verbatim_fragment`, `asset_ref` when applicable, and `extraction_confidence`.
- `assets/<task-slug>.knowledge-graph.md`: knowledge graph template filled only with source-derived content.
- `assets/<task-slug>.knowledge-graph.completed.md`: knowledge graph after rule-based completion and freshness checking.
- `assets/<task-slug>.rendering-inventory.md`: formula, mixed prose/math, structural diagram, schematic, chart, plot, and algorithm-visualization inventory with required render route, export form, evidence path, and blocker status.
- `assets/<task-slug>.coverage.source-to-graph.md`: source manifest to knowledge graph coverage table and blocker list, produced before completion.
- `assets/<task-slug>.coverage.graph-to-export.md`: completed graph to final export coverage table and blocker list, produced before delivery.
- `assets/<task-slug>.encoding-audit.md`: UTF-8 and mojibake audit for generated text artifacts.
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
2. **Parse, inspect, and export source extracts**: when source extraction actually begins, read `references/file-in-adapters.md`, then use the discovered capability appropriate to the input format. Export the original source content to `extracts/<task-slug>.source.md`, `extracts/<task-slug>.source.json`, and `extracts/<task-slug>.source-manifest.json` as UTF-8. Include page/slide provenance, extracted assets, extraction confidence, and any normalization/cleaning confidence. Do not rewrite, summarize, or pedagogically upgrade source text. When extraction artifacts such as PDF spacing, broken line joins, OCR noise, or encoding corruption make the wording unreadable, preserve raw extraction separately and add a separately labeled normalized UTF-8 text field for downstream use. Pass the Source Manifest Gate and UTF-8 Encoding Gate before continuing.
3. **Fill the knowledge graph template from extracts**: read `extracts/<task-slug>.source.md`, `extracts/<task-slug>.source.json`, `extracts/<task-slug>.source-manifest.json`, and `references/knowledge-graph-template.md`. Place source-derived content into the template and export `assets/<task-slug>.knowledge-graph.md`. If the source file has no content for a template field, leave the field blank rather than deleting the field or collapsing the template. Do not invent, paraphrase, or smooth the source text; keep original wording, source item id, and provenance. Treat this step as lossless: every substantive source item recovered in step 2 — every title, bullet, definition, claim, explanation, example, exercise, answer, formula, code block, table, figure/diagram specification, speaker note, and caption — must be mapped into the graph. Reconcile source against graph item by item. Any source item that does not fit an existing knowledge-point field goes into the Unassigned Source Content section with provenance instead of being dropped. A source item is considered omitted until its manifest id and original wording or verbatim fragment are explicitly placed in the graph; omission is a blocker, not a silent simplification. When Python is available, run `scripts/audit_knowledge_graph_template.py assets/<task-slug>.knowledge-graph.md --markdown-report assets/<task-slug>.knowledge-graph.template-audit.md` and fix any blocker before continuing. After step 4 creates the completed graph, run `scripts/check_manifest_coverage.py extracts/<task-slug>.source-manifest.json step3=assets/<task-slug>.knowledge-graph.md completed=assets/<task-slug>.knowledge-graph.completed.md --markdown-report assets/<task-slug>.coverage.source-to-graph.md` when Python is available. Pass the Source Coverage Gate and Knowledge Graph Template Gate before continuing beyond coverage review.
4. **Complete blank template fields**: read `assets/<task-slug>.knowledge-graph.md` and `references/completion-rules.md`. Complete only the blank fields needed for self-study quality, then export `assets/<task-slug>.knowledge-graph.completed.md`. Keep the same template structure; completion may fill or move content but must not replace the template with a compact outline, chapter summary, or source-item list. Do not freely rewrite or generate text. Prefer source wording, and for supplemental content selectively use verified search results or authoritative references when required. Label supplemental content separately from source-derived content. Preserve source item ids during completion; if a source item is moved, record its old location, new location, and reason in the change log. Run the source-to-graph coverage command from step 3, then run `scripts/audit_knowledge_graph_template.py assets/<task-slug>.knowledge-graph.completed.md --markdown-report assets/<task-slug>.knowledge-graph.completed.template-audit.md` when Python is available. Fix missing ids and template blockers before continuing. Pass the Knowledge Graph Template Gate and Graph Preservation Gate before continuing.
5. **Check freshness and correctness in the completed graph**: read `assets/<task-slug>.knowledge-graph.completed.md` and `references/outdated-content-checking.md`. If the task requires updating or correcting time-sensitive claims, verify them with authoritative sources through the discovered research capability; if that capability is unavailable, refuse the task and direct the user to the installation guide. Export the checked result back to `assets/<task-slug>.knowledge-graph.completed.md`, preserving source-derived text and labeling verified supplements.
6. **Materialize the upgraded material**: after the user-specified output route is known and materialization begins, read `references/file-out-adapters.md` and `assets/style-presets/default.json`. Read `references/math-diagram-rendering.md` only if the completed graph or selected output requires formula, diagram, schematic, plot, algorithm-visualization, or code rendering guidance. Use the required file-handling capability for the user-specified output route. Use `assets/<task-slug>.knowledge-graph.completed.md` as the content source of truth and complete content manifest, and provide the style preset as the default visual guidance when the source style is unusable, incomplete, or not requested for preservation. Materialization is not summarization: the exported PPTX and/or PDF must restate every learner-facing definition, claim, explanation, example, exercise, answer, formula, code block, diagram specification, table, correction, and labeled supplement from the completed Markdown. Layout may split, reorder within the approved learning flow, or re-render formulas/diagrams/code, but it must not omit content, replace content with a summary, silently merge away details, or add unsupported content. Before creating final slides/pages, create `assets/<task-slug>.rendering-inventory.md` for every formula, mixed prose/math unit, structural diagram, schematic, chart, plot, and algorithm visualization in the completed graph. Maintain a graph-item-to-export-location table while materializing, then save it as `assets/<task-slug>.coverage.graph-to-export.md`. For PPTX, choose multiple slide structures from the style preset's preferred slide types and match them to the learning function of each section; do not reuse one visual template across the whole deck unless the user explicitly requests uniformity. Render complex formulas, mixed prose/math sentences or paragraphs, structural diagrams, schematics, and plots through the route matrix in `references/math-diagram-rendering.md` only after that reference's gate is true, and export code through the required code route for the selected output format. For PPTX output, crop the original source only for image-like assets; reconstruct text, formulas, and code, and prefer generated/recreated schematic diagrams over source crops when source structure is sufficient. Do not replace formulas, diagrams, charts, plots, schematics, or algorithm visuals with bare text boxes that describe what should have been rendered. Do not invent facts, examples, explanations, exercises, citations, equations, data, graph edges, or visual labels during materialization. If the required formula, structural diagram, schematic, plotting, or code export environment is missing, stop materialization; install it only with permission when possible, otherwise ask the user to install it. Preserve original course phrasing unless a completion rule or verified update requires a clearly labeled supplement. Pass the Formula Gate, Diagram And Plot Gate, Code Gate, Layout Gate, and Visual Variety Gate before export verification.
7. **Export and verify selected outputs**: export the user-specified PPTX and/or PDF through the selected file-handling capability and apply the relevant checks from `assets/style-presets/default.json`. Apply checks from `references/math-diagram-rendering.md` only if that reference was opened because its gate condition was true. For PDF output, require render verification with the discovered PDF capability. For PPTX output, require preview/render or equivalent visual verification with the discovered presentation/deck capability. Inspect or review the verification output for clipping, overlap, unreadable formulas, missing glyphs, poor contrast, blank pages/slides, broken images, inconsistent numbering, unresolved placeholders, formulas exported as default text boxes or raw syntax, broken diagram labels, reversed diagram arrows, corrupted plots, default/plain PPTX text boxes used for code blocks, non-editable PPTX code blocks, token-by-token code text boxes, code syntax highlighting simulated through multiple text objects, insufficient slide-structure variety, and violations of the default preset's accessibility/export checks. When Python and direct file access are available for PPTX output, run `scripts/audit_pptx_coverage_and_variety.py assets/<task-slug>.knowledge-graph.completed.md exports/<task-slug>/<output>.pptx --manifest extracts/<task-slug>.source-manifest.json --markdown-report exports/<task-slug>/qa/pptx-coverage-and-variety-audit.md`; treat coverage and variety blockers as blocker-level failures. Preserve verification evidence for step 8, including non-empty requested files, preview/render page counts, PDF page count when applicable, formula/diagram full-size review when applicable, PPTX formula object/rendered-asset review when applicable, PPTX editable code text-box review when applicable, PPTX coverage/variety audit when applicable, and required final artifacts under `exports/<task-slug>/`.
8. **Test the upgraded material**: read `references/test-standards.md`, then test the completed knowledge graph, materialized output, selected-output verification, and required deliverables. Run the Knowledge Graph Template Test and Source Coverage Test to confirm every substantive source item from `extracts/<task-slug>.source.md` / `.json` / `.source-manifest.json` was captured into `assets/<task-slug>.knowledge-graph.completed.md` and that nothing was dropped or summarized away during graph construction or completion. Run or manually reproduce the manifest coverage check for both the step 3 graph and completed graph. Run `scripts/audit_utf8_artifacts.py extracts assets exports/<task-slug> --markdown-report assets/<task-slug>.encoding-audit.md` when Python is available, and fix any UTF-8 or mojibake blocker before delivery. Review `assets/<task-slug>.coverage.graph-to-export.md` and the PPTX coverage/variety audit against the final render/preview evidence to pass the Export Coverage and Visual Variety gates. Record test results, preflight results, render evidence, coverage tables, automated audit paths, hard-gate status, and final checklist status in a quality report. Do not deliver if any blocker-level test or hard gate fails.
9. **Iterate if tests fail**: fix content, provenance, materialization, or layout issues through the appropriate underlying capability, then re-export, re-render, and re-test. Do not deliver an output that fails testing unless the failure is explicitly reported as a blocker.
10. **Export final files to `exports/`**: create `exports/<task-slug>/` and place the requested PPTX and/or verified PDF, quality report, final `assets/<task-slug>.knowledge-graph.completed.md` copy, and change/freshness logs when present. Before delivery, complete the final deliverable checklist in `references/test-standards.md`. Do not deliver from scratch or temporary locations.
11. **Deliver with a concise report**: provide the requested PPTX and/or PDF paths under `exports/<task-slug>/`, the major learning improvements, and any factual claims that were changed, sourced, or left uncertain.

## Output Requirements

- Always deliver the user-requested PPTX and/or PDF under `exports/<task-slug>/`.
- When the route includes PPTX, export a `.pptx` file under `exports/<task-slug>/`.
- When the route includes PDF, export a render-verified `.pdf` file under `exports/<task-slug>/`.
- Include a short quality report covering learning-structure improvements, factual updates, and remaining uncertainties.
- Include a Reference Access Log in the quality report, listing every reference file opened, the workflow step, the gate condition that made it necessary, and the output it governed.
- Include a Hard Gate Status section in the quality report, listing Source Manifest, UTF-8 Encoding, Source Coverage, Knowledge Graph Template, Graph Preservation, Export Coverage, Formula, Diagram And Plot, Code, Layout, Visual Variety, and Verification gates as pass, revise, or blocker. Any blocker means do not deliver final PPTX/PDF.
- Include a content coverage statement confirming that every learner-facing item from `assets/<task-slug>.knowledge-graph.completed.md` appears in the exported PPTX and/or PDF, or mark the output as blocked until omissions are fixed.
- Include a graph-to-export coverage table path, usually `assets/<task-slug>.coverage.graph-to-export.md`, confirming that every learner-facing completed graph item maps to a final export location.
- Include a source capture statement confirming that every substantive item recovered from the source in `extracts/<task-slug>.source.md` / `.json` / `.source-manifest.json` was placed into `assets/<task-slug>.knowledge-graph.md` and survives in `.completed.md`, or list the specific source item ids not yet captured as a blocker.
- Include a source-to-graph coverage table path, usually `assets/<task-slug>.coverage.source-to-graph.md`.
- Include UTF-8 artifact audit path, usually `assets/<task-slug>.encoding-audit.md`, and confirm that generated text artifacts decode as UTF-8 without mojibake blockers.
- Include knowledge graph template audit paths for the step 3 and completed graphs, and include PPTX coverage/variety audit path when PPTX output is produced.
- Keep generated scratch notes separate from final learner-facing material.

## Reference Access Protocol

Read references in workflow order. Do not load all references by default. Before opening any reference, answer:

1. Which workflow step is active now?
2. What gate condition makes this reference necessary now?
3. What output, decision, or check will this reference directly govern?

If the answer is unclear, do not read the reference yet. If a reference is not selected, do not open it, summarize it, preload it, or ask another agent to read it.

Record every opened reference in the quality report:

| Step | Reference opened | Gate condition | Used for |
| --- | --- | --- | --- |
| 2 | `references/file-in-adapters.md` | Source extraction has started | Source extract contract |

## Reference Gates

| Gate condition | Read | Do not read yet |
| --- | --- | --- |
| Step 2 source extraction has started for a PPTX or PDF source | `references/file-in-adapters.md` | Output, testing, completion, and math/diagram references |
| Step 3 knowledge graph construction has started from existing source extracts | `references/knowledge-graph-template.md` | Completion, output, testing, and math/diagram references |
| Step 4 blank-field completion has started from `assets/<task-slug>.knowledge-graph.md` | `references/completion-rules.md` | Output and testing references |
| Step 5 detects time-sensitive, versioned, current-practice, or externally verifiable claims that need checking | `references/outdated-content-checking.md` | This reference when no such claims are present |
| Step 6 materialization has started and the user-specified output route is known | `references/file-out-adapters.md` and `assets/style-presets/default.json` | Output references before route selection |
| Step 6 or 7 confirms complex formulas, mixed prose/math, structural diagrams, schematics, plots, algorithm visualizations, or route-specific code rendering questions | `references/math-diagram-rendering.md` | This reference for plain text-only material or before such content is confirmed |
| Step 8 final testing, delivery approval, or quality report writing has started | `references/test-standards.md` | Testing reference before materialized outputs or verification evidence exist |
