# Test Standards

Use this reference in workflow step 8 to test the upgraded material before final export and delivery. Test the completed knowledge graph, materialized output, selected-output verification, and required deliverables.

## Result Levels

- **Pass**: ready for delivery.
- **Revise**: usable, but should be fixed before delivery when practical.
- **Blocker**: do not deliver as final. Fix and re-test, or report the blocker.

## Test Inputs

Use these artifacts:

- `extracts/<task-slug>.source.md`
- `extracts/<task-slug>.source.json`
- `assets/<task-slug>.knowledge-graph.md`
- `assets/<task-slug>.knowledge-graph.completed.md`
- `assets/<task-slug>.knowledge-graph.changes.md` when present
- final rendered PDF pages when PDF output is requested
- PPTX preview/render evidence when PPTX output is requested
- PPTX object-model inspection evidence when PPTX output contains formulas and the available tooling supports document inspection
- PPTX object-model inspection evidence when PPTX output contains code blocks and the available tooling supports document inspection
- PPTX source-crop inventory or inspection notes when cropped source images are used
- formula and diagram render assets, contact sheets, or QA logs when formulas, structural diagrams, schematics, plots, or algorithm visualizations are generated or repaired
- quality report draft

## Source Fidelity Test

Pass:

- Source-derived content in the completed knowledge graph can be traced to extracted source content.
- Original wording is preserved where usable.
- Supplemental content is clearly labeled and does not replace source text without reason.
- The materialized PPTX/PDF faithfully restates all learner-facing content from `assets/<task-slug>.knowledge-graph.completed.md`, including verified corrections and labeled supplements.

Revise:

- Minor provenance gaps exist but the content is not misleading.
- Some source wording was lightly reformatted without clear notes.

Blocker:

- Content appears invented, untraceable, or materially different from the source without a recorded reason.
- Supplemental content is mixed into source-derived content without labels.
- The exported PPTX/PDF omits, summarizes away, selectively uses, or fabricates replacements for learner-facing content that appears in `assets/<task-slug>.knowledge-graph.completed.md`.

## Knowledge Graph Test

Pass:

- Required template sections are filled only where source or valid supplements support them.
- Blank fields remain blank when the source does not support completion and no completion rule applies.
- Step 4 and step 5 changes are recorded in the change log when applicable.

Revise:

- The graph is usable but has minor missing reasons, weak labels, or incomplete notes.

Blocker:

- The graph fills missing fields by invention.
- The graph omits required provenance for key concepts, formulas, examples, exercises, or claims.

## Source Coverage Test

This test checks lossless capture from source to knowledge graph. Walk through every substantive item in `extracts/<task-slug>.source.md` / `.json` and confirm each one is present in `assets/<task-slug>.knowledge-graph.md` and still present in `assets/<task-slug>.knowledge-graph.completed.md`. Compare item by item, not topic by topic — a topic heading is not capture; the underlying source wording or a verbatim fragment must appear with provenance.

Pass:

- Every substantive source item — titles, bullets, definitions, claims, explanations, examples, exercises, answers, formulas, code blocks, tables, figure/diagram specifications, speaker notes, captions — is placed in a chapter block, a knowledge-point field, a chapter summary, or the Unassigned Source Content section.
- Each captured item keeps its original wording (or a verbatim-quoted fragment) and provenance.
- Items moved out of Unassigned during completion are recorded in the change log with their destination.
- The completed graph contains no fewer source items than the step 3 graph.

Revise:

- One or more source items are captured only as a vague topic reference without the underlying wording, but the item is still traceable and can be recovered.
- An Unassigned entry was moved without a change-log note, but the destination is identifiable.

Blocker:

- A substantive source item recovered in step 2 has no home anywhere in the completed knowledge graph.
- Source wording was summarized away, merged out of existence, or replaced by a paraphrase without keeping a verbatim fragment and provenance.
- An Unassigned Source Content entry was deleted during completion without a recorded destination or reason.
- The completed graph dropped a source item that was present in the step 3 graph.

## Content Accuracy Test

Pass:

- Claims, formulas, definitions, diagrams, code, and examples are correct for the stated level.
- Assumptions and scope are visible.
- Time-sensitive claims are verified, updated, or clearly flagged.

Revise:

- Minor ambiguity, missing caveats, or unsupported claims remain.
- Examples are correct but do not show enough reasoning.

Blocker:

- Incorrect formulas, definitions, proofs, algorithms, units, labels, or conclusions.
- Outdated tooling or standards presented as current without warning.
- Contradictions between source-derived content and supplements.

## Self-Study Test

Pass:

- The material has clear objectives or equivalent progression.
- Key concepts include prerequisites, definitions, reasoning steps, examples, and practice or reflection prompts where appropriate.
- Learners can study without relying on invisible instructor speech.

Revise:

- A learner can follow the main idea but must infer some transitions.
- Exercises exist but hints or answers are missing.

Blocker:

- The upgraded material still depends on missing oral explanation.
- Major concepts are only keywords, screenshots, or formulas with no usable explanation.

## Structure Test

Pass:

- Section order supports gradual learning.
- Advanced formulas, code, results, or applications appear after required definitions and assumptions.
- The output route specified by the user is followed.

Revise:

- Some sections should be split, merged, or reordered, but the material remains usable.

Blocker:

- Content appears in a random, circular, or misleading order.
- The output route differs from the user's specified route.

## Visual And Render Test

Pass:

- All required formula rendering, structural diagram rendering, and code export capabilities were preflighted before export when the material required them.
- The final PPTX/PDF has been compared against `assets/<task-slug>.knowledge-graph.completed.md`, and every learner-facing section, definition, claim, explanation, example, exercise, answer, formula, code block, diagram specification, table, correction, and labeled supplement is present.
- The requested output has been visually checked.
- PDF output has been rendered and checked when requested.
- PPTX output has preview/render evidence when requested.
- In PPTX output, cropped source-courseware images are used only for image-like assets or documented non-reconstructable schematic/figure exceptions.
- In PPTX output, text, mathematical formulas, mixed prose/math units, code, commands, and reconstructable tables are generated/rebuilt rather than cropped from the source courseware.
- Text, formulas, code, diagrams, charts, and tables are legible.
- Learner-facing text uses the largest practical font size and line spacing that fits without clipping, overlap, or hierarchy loss. Dense content is split or redesigned before text is shrunk.
- All mathematical formulas are rendered as readable native equations, verified equation renderings, or verified high-resolution formula images; no unintended raw LaTeX, broken Unicode math, placeholder equation text, default text-box formulas, or corrupted symbols remain.
- Sentences, bullets, captions, definitions, theorem statements, derivation steps, and paragraphs that contain inline mathematical expressions are rendered as coherent mixed prose/math units through an inline-math-capable route. Inline math is not left as plain text, Unicode approximation, raw LaTeX, or separate default text-box fragments inside otherwise ordinary prose.
- In PPTX output, mathematical formulas are native equation objects or verified rendered assets, not default PowerPoint text boxes or plain text placeholders.
- Structural diagrams are rendered through an appropriate graph route when needed, with readable node labels, edge labels, arrow direction, grouping, and non-ASCII text.
- Mathematical schematics, plots, charts, and algorithm visualizations preserve source-derived axes, scales, units, labels, legends, data values, geometry, and directionality.
- Schematic diagrams, structural diagrams, mathematical diagrams, and algorithm visuals are regenerated from source-derived structure whenever enough structure is available; retained source crops have a recorded reason.
- All code, shell commands, tracebacks, configuration snippets, and pseudocode appear inside visually distinct code frames with monospace typography and sufficient contrast.
- Code frames preserve semantic indentation, line breaks, string literals, operators, and comments; wrapping or splitting does not alter the code.
- In PPTX output, every code block is a single editable purpose-built PowerPoint code text box shape containing the complete code block.
- In PPTX output, code syntax highlighting is implemented with rich text runs inside that text box, not with screenshots, rasterized code, one text box per token, one text box per line, or overlaid text objects.
- In PPTX output, code text remains directly selectable, copyable, and editable in PowerPoint while preserving monospace typography, consistent background, border, padding, line spacing, and font size. Default/plain text boxes without code-frame styling and rich text runs do not pass.
- There is no accidental overlap, clipped text, unresolved placeholder, missing glyph, blank page, or unreadable contrast.
- Automated or mechanical checks have been run where the available tooling supports them.
- Each requested final file exists and is non-empty before visual review is marked complete.
- PDF render page count matches the intended output page/slide count when the PDF is created from slides or a page sequence.
- PPTX preview/render count matches the intended slide count when the route includes PPTX.

Revise:

- Minor alignment, spacing, or hierarchy issues remain but do not block reading.

Blocker:

- The agent exported PPTX/PDF after detecting that required formula rendering, structural diagram rendering, or code export capability was missing.
- Missing formula, structural diagram, or code export capability was bypassed by using raw syntax, default text boxes, screenshots, simplified redraws, or unverified approximations.
- Any PPTX cropped source-slide image is used to reproduce rebuildable text, mathematical formulas, mixed prose/math, code, commands, or tables.
- A reconstructable schematic, structural diagram, mathematical diagram, or algorithm visual is left as a cropped source-slide image without a documented source-quality reason.
- Clipped text, overlapping objects, unreadable fonts, broken glyphs, blurred figures, missing pages, or low-contrast content.
- Learner-facing text is unnecessarily small or tightly spaced when the content could have been split across slides/pages or laid out with more available space.
- The output preserves the original slide/page count by compressing text, reducing line spacing, or overpacking content in a way that harms readability.
- Any learner-facing item from `assets/<task-slug>.knowledge-graph.completed.md` is missing, replaced by a summary, selectively omitted, or materially changed during PPTX/PDF export without a recorded verified correction.
- Any mathematical formula is raw when it should be rendered, visually corrupted, clipped, missing symbols, too small to read, or exported as a default text box/plain text placeholder.
- Any sentence, bullet, caption, definition, theorem statement, derivation step, or paragraph containing mathematical notation is exported as ordinary prose with the mathematical expression represented by plain text, Unicode approximation, raw LaTeX, or a separate default text box instead of a coherent inline-math rendering unit.
- Inline math appears with mismatched baseline, broken spacing, incorrect punctuation placement, split sentence fragments, or inconsistent typography that changes readability or meaning.
- Any structural diagram has missing labels, reversed arrows, clipped nodes, broken non-ASCII text, misleading layout, or unreadable small text.
- Any plot, chart, schematic, or algorithm visualization changes source-derived data, labels, axes, units, directionality, or visual meaning without a recorded verified correction.
- Any code-like content is presented as ordinary prose when it should be in a code frame, or the code frame changes indentation, line breaks, commands, strings, or operators in a way that can mislead learners.
- Screenshots replace text where editable reconstruction was required and feasible.
- Cropped source-courseware images replace text, formulas, code, or reconstructable diagrams where generated reconstruction was required and feasible.
- Any PPTX code block is exported as a default/plain text box, rasterized, split across token-level or line-level text boxes, built from multiple overlaid text objects, lacks editable/selectable code text, or simulates highlighting outside the text box's rich text runs.
- Any PPTX code frame shows character drift, token misalignment, line-height jumps, text overflow, overlap, or PDF export offset caused by fragmented code objects.

## Automated Visual QA Checklist

Run this checklist before final delivery whenever the capability exists:

- **PPTX existence**: requested `.pptx` exists under `exports/<task-slug>/` and has non-zero file size.
- **PPTX render evidence**: final PPTX has rendered slide previews, a montage/contact sheet, or equivalent deck preview evidence.
- **PPTX slide count**: preview/render count equals the intended final slide count.
- **PPTX layout check**: available overflow/overlap tests report no blocker-level issues, or every warning is visually inspected and resolved or documented.
- **Text size and spacing review**: inspect text-bearing full-size previews/pages. Confirm font sizes and line spacing are as large as practical for the layout, and any dense content was split/redesigned before shrinking text.
- **Completed Markdown coverage review**: compare the final PPTX/PDF against `assets/<task-slug>.knowledge-graph.completed.md`. Confirm all learner-facing Markdown items are present in the export and that no unsupported content was invented during materialization.
- **PPTX source-crop review**: inspect every cropped source-courseware image. Confirm it is image-like source content or a documented non-reconstructable figure/schematic exception, and confirm no crop is being used for rebuildable text, formulas, mixed prose/math, code, commands, or tables.
- **Required renderer/export preflight**: confirm formula rendering, structural diagram rendering, and code export routes were checked before export whenever the material required them. If any required route was missing, export must have stopped and the quality report must name the missing environment and installation action/user request.
- **PDF existence**: requested `.pdf` exists under `exports/<task-slug>/` and has non-zero file size.
- **PDF render evidence**: final PDF is rendered back to page images.
- **PDF page count**: rendered PDF page count equals the intended final page count.
- **PDF nonblank check**: rendered PDF pages are not blank.
- **Formula render review**: inspect every formula-bearing and mixed prose/math full-size preview/page. Confirm formulas and inline math are rendered, complete, not clipped, symbol-correct, readable at final export size, aligned with surrounding prose, and not default text-box formulas.
- **Mixed prose/math unit review**: inspect every sentence, bullet, caption, definition, theorem statement, derivation step, or paragraph with inline mathematical notation. Confirm the whole unit uses an inline-math-capable rendering route and is not split into ordinary prose plus text-like formula substitutes.
- **PPTX formula object review**: when PPTX output contains formulas, inspect the PPTX structure or equivalent document model. Confirm formulas are native equation objects or verified rendered assets, not default text boxes, raw LaTeX, plain Unicode approximations, or placeholders.
- **Diagram render review**: inspect every diagram-bearing full-size preview/page. Confirm structural diagrams, schematics, plots, and charts are complete, correctly labeled, directionally correct, unclipped, and readable at final export size.
- **Code frame review**: inspect every code-bearing full-size preview/page. Confirm code is inside a distinct code frame, uses monospace typography, preserves indentation and line breaks, and has readable contrast.
- **PPTX editable code review**: when PPTX output contains code, inspect the PPTX structure or equivalent document model. Confirm each code block is one purpose-built editable code text box shape, contains the full code text, uses internal rich text runs for syntax highlighting, and is not a default/plain text box, screenshot, or group of token/line text boxes.
- **Legibility review**: inspect full-size previews or a readable contact sheet for clipping, overlap, missing glyphs, unreadable formulas/code, poor contrast, broken images, and unresolved placeholders.
- **Evidence retention**: keep render previews, contact sheets, layout reports, or test logs under `exports/<task-slug>/qa/` or another clearly named verification folder.

## Deliverables Test

Pass:

- Final files are under `exports/<task-slug>/`.
- Requested PPTX is present when the route includes PPTX.
- Verified PDF is present when the route includes PDF.
- Quality report is present.
- Final completed knowledge graph is present.
- Change log is present when step 4 or step 5 modified the step 3 knowledge graph.
- Any freshness/checking log created during step 5 is present.
- Final checklist status is recorded in the quality report.

Blocker:

- Requested PDF is missing or not render-verified.
- Requested PPTX is missing or lacks visual verification evidence.
- Final deliverables are only in scratch, temporary, or intermediate locations.

## Final Deliverable Checklist

Before delivery, explicitly verify and record the result of each required item:

- `exports/<task-slug>/` exists.
- Requested PPTX exists under `exports/<task-slug>/` and is non-empty.
- Requested PDF exists under `exports/<task-slug>/` and is non-empty.
- PDF render evidence exists when PDF is requested.
- PDF rendered page count equals intended final page count when page count is knowable.
- PPTX preview/render evidence exists when PPTX is requested.
- PPTX preview/render slide count equals intended final slide count when slide count is knowable.
- `quality-report.md` or equivalent quality report exists under `exports/<task-slug>/`.
- `assets/<task-slug>.knowledge-graph.completed.md` has been copied under `exports/<task-slug>/`.
- `assets/<task-slug>.knowledge-graph.changes.md` has been copied under `exports/<task-slug>/` when step 4 or step 5 made changes.
- Any freshness/checking log has been copied under `exports/<task-slug>/` when created.
- The quality report states pass, revise, or blocker and lists any unresolved revise/blocker issues.

## Quality Report Requirements

The quality report must include:

- Test result: pass, revise, or blocker.
- Output route used.
- PPTX path when requested.
- PDF path when requested.
- Capability preflight results or any fallback paths used.
- Missing formula, structural diagram, or code export environments, including whether the agent installed them with approval or stopped and asked the user to install them.
- Visual QA evidence paths and page/slide counts.
- Text size and spacing review result, including any dense slides/pages split to preserve large readable text.
- Completed Markdown coverage review result, including confirmation that all learner-facing items from `assets/<task-slug>.knowledge-graph.completed.md` appear in the exported PPTX/PDF, or a blocker list of missing/changed items.
- Source capture review result, including the Source Coverage Test outcome and confirmation that every substantive item recovered from `extracts/<task-slug>.source.md` / `.json` is present in `assets/<task-slug>.knowledge-graph.completed.md` with original wording and provenance, or a blocker list of source items not yet captured.
- PPTX source-crop review result, including every retained crop's purpose and any documented exception for a diagram or schematic that could not be regenerated safely.
- Formula render review result, including any formula-bearing and mixed prose/math pages/slides checked, plus PPTX object-model evidence that formulas and inline-math units are native equation-capable objects/runs or verified rendered assets rather than default text boxes when PPTX output contains formulas.
- Diagram render review result, including any diagram-bearing, schematic-bearing, plot-bearing, or chart-bearing pages/slides checked.
- Formula and diagram rendering routes used, including preflight results and fallback paths.
- Code frame review result, including any code-bearing pages/slides checked, plus PPTX object-model evidence for editable single-text-box rich text code blocks when PPTX output contains code.
- Final deliverable checklist status.
- Major learning improvements.
- Factual claims changed, sourced, flagged, or left uncertain.
- Any blocker or revise-level issues intentionally left unresolved.
