# File Output Adapters

Use this reference for output-side workflow requirements and final deliverable contracts. Do not duplicate deck authoring, PDF generation, rendering, or export internals already owned by available presentation/deck or PDF skills.

## Boundary Principle

After the shared workflow produces `assets/<task-slug>.knowledge-graph.completed.md`, materialize the selected output route directly through the available presentation/deck and/or PDF capabilities. The workflow provides:

- User-specified output route.
- `assets/<task-slug>.knowledge-graph.completed.md`.
- `assets/<task-slug>.knowledge-graph.changes.md` when present.
- `extracts/<task-slug>.source.md` and `.json` when source provenance is needed.
- `assets/style-presets/default.json` as the default teaching-courseware visual preset.
- `exports/<task-slug>/` as the final output directory.

The workflow must not create unsupported content during materialization. Use the completed knowledge graph as the content source of truth. The style preset guides layout, typography, accessibility, STEM content rendering, and export checks when the source style is unusable, incomplete, or not requested for preservation.

## Valid Output Routes

Do not choose the output route silently. If the user has not specified the route, ask before materialization.

- **Output PPTX**: use the presentation/deck capability and require PPTX visual verification.
- **Output PDF**: use the PDF capability unless PDF creation must go through a presentation/deck workflow; require PDF render verification.
- **Output PPTX and PDF**: use the presentation/deck capability and require both PPTX visual verification and PDF render verification.

## Workflow Requirement Selection

Apply exactly one of these workflow requirement sets:

- Use **Workflow Requirements: PPTX/PPTX+PDF Output** when the user selected `output PPTX` or `output PPTX and PDF`.
- Use **Workflow Requirements: Direct PDF Output** when the user selected `output PDF` and the PDF can be created directly from the completed knowledge graph.
- If the user selected `output PDF` but PDF creation must go through a presentation workflow, use **Workflow Requirements: PPTX/PPTX+PDF Output** with `output PDF` as the route and return only the PDF deliverable.

Resolve all placeholders before materialization. Do not weaken the constraints about source fidelity or non-fabrication.

## Workflow Requirements: PPTX/PPTX+PDF Output

Use these requirements when the route requires PPTX output, with or without PDF output.

```text
Use the available presentation/deck skill or capability to materialize upgraded courseware from the completed knowledge graph.

Task slug:
<task-slug>

User-specified output route:
<output-route>

Required input files:
1. assets/<task-slug>.knowledge-graph.completed.md
2. assets/<task-slug>.knowledge-graph.changes.md, if present
3. extracts/<task-slug>.source.md
4. extracts/<task-slug>.source.json
5. assets/style-presets/default.json

Required output directory:
exports/<task-slug>/

Requirements:
- Use assets/<task-slug>.knowledge-graph.completed.md as the content source of truth.
- Use assets/style-presets/default.json as the default visual guidance for slide structure, typography, color, callouts, formulas, code, figures, accessibility, and export checks.
- Preserve the user's requested style and usable source visual identity when specified; otherwise apply the default style preset to improve readability and self-study usability.
- Do not invent facts, examples, explanations, exercises, citations, or visual labels.
- Preserve original course phrasing wherever usable.
- Use only source-derived content and clearly labeled supplements from the completed knowledge graph.
- Keep process notes out of visible learner-facing slides/pages.
- Render every mathematical formula as a legible formula object, equation rendering, or verified high-resolution formula image. Do not leave raw LaTeX, broken Unicode math, placeholder equation text, or unverified screenshots in learner-facing output unless the source itself is explicitly teaching raw syntax.
- Place every code fragment, shell command, traceback, configuration snippet, or pseudocode block inside a visually distinct code frame with monospace typography, sufficient contrast, preserved indentation, and wrapping or line splitting that does not change semantics.
- Create a PPTX file only when the route includes PPTX.
- Export a final PDF only when the route includes PDF.
- Visually verify the PPTX using the available presentation/deck capability.
- When PDF is requested, use the available PDF capability or supported export path to render-verify the final PDF.
- During verification, inspect every slide/page containing formulas or code at full size. Formula and code defects are blocker-level issues unless explicitly marked as unresolved source-quality limitations in the quality report.
- Include the relevant export checks from assets/style-presets/default.json in verification.
- Record visual/export issues and fixes in the quality report.
- If required deck or PDF capabilities are unavailable, report the missing capability and do not fabricate output.

Record before leaving materialization:
- PPTX path, if produced.
- PDF path, if produced.
- Verification summary.
- Quality report path.
- Any blocker that must be preserved downstream.
```

## Workflow Requirements: Direct PDF Output

Use these requirements when the route is output PDF and the PDF can be created directly from the completed knowledge graph.

```text
Use the available PDF skill or capability to create a verified PDF from the completed knowledge graph.

Task slug:
<task-slug>

User-specified output route:
output PDF

Required input files:
1. assets/<task-slug>.knowledge-graph.completed.md
2. assets/<task-slug>.knowledge-graph.changes.md, if present
3. extracts/<task-slug>.source.md
4. extracts/<task-slug>.source.json
5. assets/style-presets/default.json

Required output directory:
exports/<task-slug>/

Requirements:
- Use assets/<task-slug>.knowledge-graph.completed.md as the content source of truth.
- Use assets/style-presets/default.json as the default visual guidance for page structure, typography, color, callouts, formulas, code, figures, accessibility, and PDF export checks.
- Preserve the user's requested style and usable source visual identity when specified; otherwise apply the default style preset to improve readability and self-study usability.
- Do not invent facts, examples, explanations, exercises, citations, or visual labels.
- Preserve original course phrasing wherever usable.
- Use only source-derived content and clearly labeled supplements from the completed knowledge graph.
- Render every mathematical formula as a legible formula object, equation rendering, or verified high-resolution formula image. Do not leave raw LaTeX, broken Unicode math, placeholder equation text, or unverified screenshots in learner-facing output unless the source itself is explicitly teaching raw syntax.
- Place every code fragment, shell command, traceback, configuration snippet, or pseudocode block inside a visually distinct code frame with monospace typography, sufficient contrast, preserved indentation, and wrapping or line splitting that does not change semantics.
- Create the final PDF under exports/<task-slug>/.
- Render-verify the final PDF using the available PDF capability.
- During verification, inspect every page containing formulas or code at full size. Formula and code defects are blocker-level issues unless explicitly marked as unresolved source-quality limitations in the quality report.
- Include the relevant export checks from assets/style-presets/default.json in verification.
- Record visual/export issues and fixes in the quality report.
- If required PDF creation or render verification is unavailable, report the missing capability and do not fabricate output.

Record before leaving materialization:
- PDF path.
- Render verification summary.
- Quality report path.
- Any blocker that must be preserved downstream.
```

## Output Checks

After materialization, check that:

- Required files are under `exports/<task-slug>/`.
- The PPTX path exists and is non-empty when the route includes PPTX.
- The PPTX has preview/render evidence when the route includes PPTX.
- The PDF path exists and is non-empty when the route includes PDF.
- The PDF has render verification evidence when the route includes PDF.
- PDF render page count matches the intended output page/slide count when the PDF was exported from a deck or page sequence.
- Formula-bearing pages/slides have full-size render evidence showing formulas are not raw, clipped, corrupted, or unreadable.
- Code-bearing pages/slides have full-size render evidence showing code appears inside code frames and preserves indentation, line breaks, and readable contrast.
- The quality report exists.
- The quality report includes capability preflight results, visual/export checks, and final checklist status.
- The quality report states whether `assets/style-presets/default.json` was applied, partially applied, or overridden by source/user style requirements.
- `assets/<task-slug>.knowledge-graph.completed.md` is copied to `exports/<task-slug>/`.
- `assets/<task-slug>.knowledge-graph.changes.md` is copied to `exports/<task-slug>/` when present.
- Any freshness/checking log created during step 5 is copied to `exports/<task-slug>/`.

If a required deliverable is missing, rerun or repair the appropriate output workflow through the underlying file capability instead of fabricating it.

## Missing Capability Policy

Refuse the task and direct the user to the installation guide in `SKILL.md` when a required capability is missing, including:

- PPTX output without a presentation/deck capability.
- PDF output or PDF render verification without a PDF capability.
- Required file-handling capability for the selected output route is unavailable.

## Deliverables

Write final deliverables under `exports/<task-slug>/`, then return:

- PPTX path when produced.
- Verified PDF path when produced.
- Final completed knowledge graph copy.
- Knowledge graph change log copy when present.
- Freshness/checking log copy when present.
- Quality report covering output route, render verification, learning upgrades, factual updates, and unresolved uncertainties.
