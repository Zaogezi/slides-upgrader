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
- PPTX object-model inspection evidence when PPTX output contains code blocks and the available tooling supports document inspection
- formula and diagram render assets, contact sheets, or QA logs when formulas, structural diagrams, schematics, plots, or algorithm visualizations are generated or repaired
- quality report draft

## Source Fidelity Test

Pass:

- Source-derived content in the completed knowledge graph can be traced to extracted source content.
- Original wording is preserved where usable.
- Supplemental content is clearly labeled and does not replace source text without reason.

Revise:

- Minor provenance gaps exist but the content is not misleading.
- Some source wording was lightly reformatted without clear notes.

Blocker:

- Content appears invented, untraceable, or materially different from the source without a recorded reason.
- Supplemental content is mixed into source-derived content without labels.

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

- The requested output has been visually checked.
- PDF output has been rendered and checked when requested.
- PPTX output has preview/render evidence when requested.
- Text, formulas, code, diagrams, charts, and tables are legible.
- All mathematical formulas are rendered as readable equations or verified high-resolution formula images; no unintended raw LaTeX, broken Unicode math, placeholder equation text, or corrupted symbols remain.
- Structural diagrams are rendered through an appropriate graph route when needed, with readable node labels, edge labels, arrow direction, grouping, and non-ASCII text.
- Mathematical schematics, plots, charts, and algorithm visualizations preserve source-derived axes, scales, units, labels, legends, data values, geometry, and directionality.
- All code, shell commands, tracebacks, configuration snippets, and pseudocode appear inside visually distinct code frames with monospace typography and sufficient contrast.
- Code frames preserve semantic indentation, line breaks, string literals, operators, and comments; wrapping or splitting does not alter the code.
- In PPTX output, every code block is a single editable PowerPoint text box shape containing the complete code block.
- In PPTX output, code syntax highlighting is implemented with rich text runs inside that text box, not with screenshots, rasterized code, one text box per token, one text box per line, or overlaid text objects.
- In PPTX output, code text remains directly selectable, copyable, and editable in PowerPoint while preserving monospace typography, consistent background, border, padding, line spacing, and font size.
- There is no accidental overlap, clipped text, unresolved placeholder, missing glyph, blank page, or unreadable contrast.
- Automated or mechanical checks have been run where the available tooling supports them.
- Each requested final file exists and is non-empty before visual review is marked complete.
- PDF render page count matches the intended output page/slide count when the PDF is created from slides or a page sequence.
- PPTX preview/render count matches the intended slide count when the route includes PPTX.

Revise:

- Minor alignment, spacing, or hierarchy issues remain but do not block reading.

Blocker:

- Clipped text, overlapping objects, unreadable fonts, broken glyphs, blurred figures, missing pages, or low-contrast content.
- Any mathematical formula is raw when it should be rendered, visually corrupted, clipped, missing symbols, or too small to read.
- Any structural diagram has missing labels, reversed arrows, clipped nodes, broken non-ASCII text, misleading layout, or unreadable small text.
- Any plot, chart, schematic, or algorithm visualization changes source-derived data, labels, axes, units, directionality, or visual meaning without a recorded verified correction.
- Any code-like content is presented as ordinary prose when it should be in a code frame, or the code frame changes indentation, line breaks, commands, strings, or operators in a way that can mislead learners.
- Screenshots replace text where editable reconstruction was required and feasible.
- Any PPTX code block is rasterized, split across token-level or line-level text boxes, built from multiple overlaid text objects, lacks editable/selectable code text, or simulates highlighting outside the text box's rich text runs.
- Any PPTX code frame shows character drift, token misalignment, line-height jumps, text overflow, overlap, or PDF export offset caused by fragmented code objects.

## Automated Visual QA Checklist

Run this checklist before final delivery whenever the capability exists:

- **PPTX existence**: requested `.pptx` exists under `exports/<task-slug>/` and has non-zero file size.
- **PPTX render evidence**: final PPTX has rendered slide previews, a montage/contact sheet, or equivalent deck preview evidence.
- **PPTX slide count**: preview/render count equals the intended final slide count.
- **PPTX layout check**: available overflow/overlap tests report no blocker-level issues, or every warning is visually inspected and resolved or documented.
- **PDF existence**: requested `.pdf` exists under `exports/<task-slug>/` and has non-zero file size.
- **PDF render evidence**: final PDF is rendered back to page images.
- **PDF page count**: rendered PDF page count equals the intended final page count.
- **PDF nonblank check**: rendered PDF pages are not blank.
- **Formula render review**: inspect every formula-bearing full-size preview/page. Confirm formulas are rendered, complete, not clipped, symbol-correct, and readable at final export size.
- **Diagram render review**: inspect every diagram-bearing full-size preview/page. Confirm structural diagrams, schematics, plots, and charts are complete, correctly labeled, directionally correct, unclipped, and readable at final export size.
- **Code frame review**: inspect every code-bearing full-size preview/page. Confirm code is inside a distinct code frame, uses monospace typography, preserves indentation and line breaks, and has readable contrast.
- **PPTX editable code review**: when PPTX output contains code, inspect the PPTX structure or equivalent document model. Confirm each code block is one editable text box shape, contains the full code text, uses internal rich text runs for syntax highlighting, and is not a screenshot or a group of token/line text boxes.
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
- Visual QA evidence paths and page/slide counts.
- Formula render review result, including any formula-bearing pages/slides checked.
- Diagram render review result, including any diagram-bearing, schematic-bearing, plot-bearing, or chart-bearing pages/slides checked.
- Formula and diagram rendering routes used, including preflight results and fallback paths.
- Code frame review result, including any code-bearing pages/slides checked, plus PPTX object-model evidence for editable single-text-box rich text code blocks when PPTX output contains code.
- Final deliverable checklist status.
- Major learning improvements.
- Factual claims changed, sourced, flagged, or left uncertain.
- Any blocker or revise-level issues intentionally left unresolved.
