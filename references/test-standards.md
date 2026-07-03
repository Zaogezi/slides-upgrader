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
- There is no accidental overlap, clipped text, unresolved placeholder, missing glyph, blank page, or unreadable contrast.

Revise:

- Minor alignment, spacing, or hierarchy issues remain but do not block reading.

Blocker:

- Clipped text, overlapping objects, unreadable fonts, broken glyphs, blurred figures, missing pages, or low-contrast content.
- Screenshots replace text where editable reconstruction was required and feasible.

## Deliverables Test

Pass:

- Final files are under `exports/<task-slug>/`.
- Requested PPTX is present when the route includes PPTX.
- Verified PDF is present when the route includes PDF.
- Quality report is present.
- Final completed knowledge graph is present.
- Change log is present when step 4 or step 5 modified the step 3 knowledge graph.

Blocker:

- Requested PDF is missing or not render-verified.
- Requested PPTX is missing or lacks visual verification evidence.
- Final deliverables are only in scratch, temporary, or intermediate locations.

## Quality Report Requirements

The quality report must include:

- Test result: pass, revise, or blocker.
- Output route used.
- PPTX path when requested.
- PDF path when requested.
- Major learning improvements.
- Factual claims changed, sourced, flagged, or left uncertain.
- Any blocker or revise-level issues intentionally left unresolved.
