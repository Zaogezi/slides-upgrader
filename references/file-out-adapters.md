# File Output Adapters

Use this reference for output-side workflow requirements and final deliverable contracts. Do not duplicate deck authoring, PDF generation, rendering, or export internals already owned by available presentation/deck or PDF skills.

## Boundary Principle

After the shared workflow produces `assets/<task-slug>.knowledge-graph.completed.md`, materialize the selected output route directly through the available presentation/deck and/or PDF capabilities. The workflow provides:

- User-specified output route.
- `assets/<task-slug>.knowledge-graph.completed.md`.
- `assets/<task-slug>.knowledge-graph.changes.md` when present.
- `extracts/<task-slug>.source.md` and `.json` when source provenance is needed.
- `assets/style-presets/default.json` as the default teaching-courseware visual preset.
- `references/math-diagram-rendering.md` as the route matrix and QA contract for complex formulas, structural diagrams, mathematical schematics, plots, and algorithm visualizations.
- `exports/<task-slug>/` as the final output directory.

The workflow must not create unsupported content during materialization. Use the completed knowledge graph as the content source of truth and complete content manifest. The selected PPTX and/or PDF output must faithfully restate every learner-facing item in `assets/<task-slug>.knowledge-graph.completed.md`, including verified corrections and labeled supplements. Do not selectively omit sections, examples, formulas, code blocks, diagrams, tables, exercises, answers, caveats, or source attributions because they are dense or inconvenient to lay out. Split slides/pages, continue content across multiple frames, or simplify decoration instead of dropping content. The style preset guides layout, typography, accessibility, STEM content rendering, and export checks when the source style is unusable, incomplete, or not requested for preservation.

When the material contains complex formulas or diagrams, use `references/math-diagram-rendering.md` to select the rendering route. Formula, diagram, SVG, and plotting tools may render source-derived or verified supplemental content, but must not invent equations, labels, graph edges, data values, or visual claims. When the material contains formulas, structural diagrams, or code and the required rendering/export environment is missing, stop before export. Install the missing environment only when permitted and approved; otherwise ask the user to install it. Do not produce a degraded output by replacing formulas, structural diagrams, or code with default text boxes, raw syntax, screenshots, or unverified approximations.

For PPTX output, cropped images from the original courseware are allowed only for image-like source assets such as photos, scans of physical objects, screenshots where the screenshot itself is the teaching object, or complex source figures that cannot be reconstructed reliably from available source information. Do not use cropped source-slide images to reproduce text, mathematical formulas, mixed prose/math sentences, code, commands, tables that can be rebuilt, or editable content. Reconstruct those items through the appropriate text, formula, code, table, or diagram route. For schematic diagrams, structural diagrams, mathematical diagrams, and algorithm visuals, prefer regenerating them from source-derived structure over cropping the original slide; use a crop only when the source does not provide enough structure to regenerate faithfully or reconstruction would risk changing meaning, and record the reason in the quality report.

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
6. references/math-diagram-rendering.md when the material includes complex formulas, structural diagrams, schematics, plots, or algorithm visualizations

Required output directory:
exports/<task-slug>/

Requirements:
- Use assets/<task-slug>.knowledge-graph.completed.md as the content source of truth.
- Treat assets/<task-slug>.knowledge-graph.completed.md as the complete learner-facing content manifest. Every exported slide/page must be traceable to it, and every learner-facing item in it must appear in the PPTX/PDF unless explicitly marked as process-only metadata.
- Use assets/style-presets/default.json as the default visual guidance for slide structure, typography, color, callouts, formulas, code, figures, accessibility, and export checks.
- Use references/math-diagram-rendering.md to select formula, structure-diagram, schematic, and plot rendering routes when needed.
- Before materialization, preflight every required formula rendering, structural diagram rendering, and code export route. If any required route is unavailable, stop export immediately. If the execution environment allows dependency installation, request approval and install the corresponding toolchain; otherwise ask the user to install the missing environment and do not generate a partial or degraded PPTX/PDF.
- Preserve the user's requested style and usable source visual identity when specified; otherwise apply the default style preset to improve readability and self-study usability.
- Source-image cropping policy for PPTX output: use crops only for image-like assets. Rebuild text, mathematical formulas, mixed prose/math units, code, and reconstructable tables as generated PPTX content. Prefer generated/recreated schematics and structural diagrams over source crops whenever source-derived structure is sufficient.
- Text sizing policy: use the largest practical font size and line spacing for learner-facing text that fits the slide/page safely. When content is dense, split it across additional slides/pages, reduce nonessential decoration, or simplify layout before reducing font size or line spacing. Do not compress text merely to preserve the original slide count.
- Do not invent facts, examples, explanations, exercises, citations, or visual labels.
- Do not summarize, abbreviate, silently merge away, or selectively skip content from the completed Markdown. If the content does not fit, add slides/pages or restructure the layout while preserving all learner-facing details.
- Preserve original course phrasing wherever usable.
- Use only source-derived content and clearly labeled supplements from the completed knowledge graph.
- Keep process notes out of visible learner-facing slides/pages.
- Render every mathematical formula as a legible native equation object, verified equation rendering, or verified high-resolution formula image. Do not leave raw LaTeX, broken Unicode math, placeholder equation text, default text-box formulas, or unverified screenshots in learner-facing output unless the source itself is explicitly teaching raw syntax.
- When a sentence, bullet, caption, definition, theorem statement, derivation step, or paragraph contains mathematical notation, treat the whole sentence or paragraph as a mixed prose/math rendering unit. Use an inline-math-capable route such as native equation runs, MathJax, KaTeX, or LaTeX-rendered SVG/PNG for that unit. Do not export the prose as ordinary text while representing the embedded mathematical expression as plain text, Unicode approximation, raw LaTeX, or a separate default text box.
- For PPTX output, formulas must not be exported through default PowerPoint text boxes or plain text placeholders. Use native equation objects when the presentation capability supports them; otherwise use verified SVG or high-resolution PNG formula assets generated through the approved formula route.
- Render complex formulas through MathJax, KaTeX, or LaTeX when the deck/PDF capability cannot create reliable native equation objects.
- Render structural diagrams through Graphviz, Mermaid, or an equivalent graph renderer when the content is a tree, syntax tree, automaton, state machine, flowchart, dependency graph, DAG, or local knowledge graph.
- Render mathematical schematics through hand-authored or programmatic SVG when the source-derived structure is precise enough to reconstruct.
- Render data figures and algorithm visualizations through Python or JS plotting when the completed graph provides the data, labels, and intended visual relationship.
- Preserve original notation, node labels, edge labels, directionality, axes, scales, units, legends, and data values. If any item is ambiguous, mark it unresolved in the quality report rather than inventing it.
- Place every code fragment, shell command, traceback, configuration snippet, or pseudocode block inside a purpose-built code frame with monospace typography, sufficient contrast, preserved indentation, and wrapping or line splitting that does not change semantics.
- For PPTX output, each code block must be one editable PowerPoint text box shape containing the complete code block. The code text must be selectable, copyable, and editable in PowerPoint.
- Apply syntax highlighting inside that single text box through rich text runs. Use run-level color for keywords, functions, strings, comments, literals, and normal text when highlighting is available.
- Do not use default/plain text boxes, screenshots, rasterized code, separate text boxes per token, separate text boxes per line, or multiple overlaid text objects to simulate syntax highlighting in PPTX.
- Use a monospace font such as `Consolas`, `Cascadia Mono`, or `Courier New`, with consistent background color, border, padding, line spacing, and font size for code frames.
- Create a PPTX file only when the route includes PPTX.
- Export a final PDF only when the route includes PDF.
- Visually verify the PPTX using the available presentation/deck capability.
- When PDF is requested, use the available PDF capability or supported export path to render-verify the final PDF.
- During verification, inspect every slide/page containing formulas, mixed prose/math sentences, diagrams, plots, schematics, or code at full size. Confirm learner-facing text uses the largest practical font size and line spacing for its container and that dense slides were split or redesigned instead of being compressed into small, tight text. Compare the final PPTX/PDF against `assets/<task-slug>.knowledge-graph.completed.md` and confirm every learner-facing item in the completed Markdown is represented in the exported material without fabricated replacement content. For PPTX output with formulas, inspect the PPTX object structure or equivalent document model and confirm formulas and mixed prose/math units are native equation-capable objects/runs or verified rendered assets, not default text boxes, split plain-text fragments, or raw syntax. For PPTX output with code, inspect the PPTX object structure or equivalent document model and confirm each code block is a purpose-built single editable text box with internal rich text runs, not a default/plain text box or a collection of token text boxes. Formula, diagram, plot, schematic, code, and content coverage defects are blocker-level issues unless explicitly marked as unresolved source-quality limitations in the quality report.
- During PPTX verification, inspect every crop from source courseware and classify it as allowed image-like content or a documented exception for a non-reconstructable schematic/figure. Any crop containing rebuildable text, formulas, mixed prose/math, code, commands, or tables is a blocker.
- Include the relevant export checks from assets/style-presets/default.json in verification.
- Retain formula and diagram render evidence, generated assets, contact sheets, or review logs under `exports/<task-slug>/qa/` when possible.
- Record visual/export issues and fixes in the quality report.
- If required deck, PDF, formula rendering, structural diagram rendering, or code export capabilities are unavailable, report the missing capability and do not fabricate output or use source crops as a substitute for rebuildable text/formula/code.

Record before leaving materialization:
- PPTX path, if produced.
- PDF path, if produced.
- Verification summary.
- Formula and diagram rendering routes used, if any.
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
6. references/math-diagram-rendering.md when the material includes complex formulas, structural diagrams, schematics, plots, or algorithm visualizations

Required output directory:
exports/<task-slug>/

Requirements:
- Use assets/<task-slug>.knowledge-graph.completed.md as the content source of truth.
- Treat assets/<task-slug>.knowledge-graph.completed.md as the complete learner-facing content manifest. Every exported page must be traceable to it, and every learner-facing item in it must appear in the PDF unless explicitly marked as process-only metadata.
- Use assets/style-presets/default.json as the default visual guidance for page structure, typography, color, callouts, formulas, code, figures, accessibility, and PDF export checks.
- Use references/math-diagram-rendering.md to select formula, structure-diagram, schematic, and plot rendering routes when needed.
- Before materialization, preflight every required formula rendering, structural diagram rendering, and code export route. If any required route is unavailable, stop export immediately. If the execution environment allows dependency installation, request approval and install the corresponding toolchain; otherwise ask the user to install the missing environment and do not generate a partial or degraded PDF.
- Preserve the user's requested style and usable source visual identity when specified; otherwise apply the default style preset to improve readability and self-study usability.
- Use the largest practical font size and line spacing for learner-facing text that fits the page safely. Split dense content across additional pages before shrinking text or tightening line spacing.
- Do not invent facts, examples, explanations, exercises, citations, or visual labels.
- Do not summarize, abbreviate, silently merge away, or selectively skip content from the completed Markdown. If the content does not fit, add pages or restructure the layout while preserving all learner-facing details.
- Preserve original course phrasing wherever usable.
- Use only source-derived content and clearly labeled supplements from the completed knowledge graph.
- Render every mathematical formula as a legible formula object, verified equation rendering, or verified high-resolution formula image. Do not leave raw LaTeX, broken Unicode math, placeholder equation text, default text-box formulas, or unverified screenshots in learner-facing output unless the source itself is explicitly teaching raw syntax.
- When a sentence, bullet, caption, definition, theorem statement, derivation step, or paragraph contains mathematical notation, treat the whole sentence or paragraph as a mixed prose/math rendering unit. Use an inline-math-capable route such as native equation runs, MathJax, KaTeX, or LaTeX-rendered SVG/PNG for that unit. Do not export the prose as ordinary text while representing the embedded mathematical expression as plain text, Unicode approximation, raw LaTeX, or a separate default text box.
- Render complex formulas through MathJax, KaTeX, or LaTeX when the PDF capability cannot create reliable native equation objects.
- Render structural diagrams through Graphviz, Mermaid, or an equivalent graph renderer when the content is a tree, syntax tree, automaton, state machine, flowchart, dependency graph, DAG, or local knowledge graph.
- Render mathematical schematics through hand-authored or programmatic SVG when the source-derived structure is precise enough to reconstruct.
- Render data figures and algorithm visualizations through Python or JS plotting when the completed graph provides the data, labels, and intended visual relationship.
- Preserve original notation, node labels, edge labels, directionality, axes, scales, units, legends, and data values. If any item is ambiguous, mark it unresolved in the quality report rather than inventing it.
- Place every code fragment, shell command, traceback, configuration snippet, or pseudocode block inside a visually distinct code frame with monospace typography, sufficient contrast, preserved indentation, and wrapping or line splitting that does not change semantics.
- Create the final PDF under exports/<task-slug>/.
- Render-verify the final PDF using the available PDF capability.
- During verification, inspect every page containing formulas, diagrams, plots, schematics, or code at full size. Compare the final PDF against `assets/<task-slug>.knowledge-graph.completed.md` and confirm every learner-facing item in the completed Markdown is represented in the exported material without fabricated replacement content. Formula, diagram, plot, schematic, code, and content coverage defects are blocker-level issues unless explicitly marked as unresolved source-quality limitations in the quality report.
- Include the relevant export checks from assets/style-presets/default.json in verification.
- Retain formula and diagram render evidence, generated assets, contact sheets, or review logs under `exports/<task-slug>/qa/` when possible.
- Record visual/export issues and fixes in the quality report.
- If required PDF creation, render verification, formula rendering, structural diagram rendering, or code export capability is unavailable, report the missing capability and do not fabricate output.

Record before leaving materialization:
- PDF path.
- Render verification summary.
- Formula and diagram rendering routes used, if any.
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
- Text-bearing pages/slides have full-size render evidence showing learner-facing text uses generous readable font sizes and line spacing, with no avoidable small/tight text caused by preserving slide count or overpacking content.
- Exported PPTX/PDF content has been checked against `assets/<task-slug>.knowledge-graph.completed.md`; every learner-facing item in the completed Markdown is present, and no slide/page introduces unsupported substitute content.
- Formula-bearing and mixed prose/math pages/slides have full-size render evidence showing formulas and inline mathematical expressions are not raw, clipped, corrupted, unreadable, exported through default text boxes, or split away from their sentence/paragraph rendering unit.
- PPTX formula-bearing slides have object-model evidence, when the route includes PPTX and tooling supports inspection, showing formulas are native equation objects or verified rendered formula assets rather than default text boxes.
- PPTX output contains no cropped source-slide images used as substitutes for rebuildable text, formulas, mixed prose/math, code, commands, or tables.
- PPTX schematic, structural-diagram, mathematical-diagram, and algorithm-visual slides use regenerated assets whenever source-derived structure is sufficient; any retained source crop has a quality-report reason.
- Diagram-bearing pages/slides have full-size render evidence showing diagrams are complete, directionally correct, labeled, unclipped, and readable.
- Plot-bearing pages/slides have full-size render evidence showing axes, labels, legends, units, and data values are readable and traceable.
- Code-bearing pages/slides have full-size render evidence showing code appears inside code frames and preserves indentation, line breaks, and readable contrast.
- PPTX code-bearing slides have object-model evidence, when the route includes PPTX, showing each code block is one purpose-built editable code text box shape with complete code text and internal rich text runs for syntax highlighting, not a default/plain text box.
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
- PPTX output containing formulas when the presentation/deck capability cannot create native equation objects or place verified rendered formula assets without default text-box formulas.
- PPTX output containing code when the presentation/deck capability cannot create editable single-text-box code frames with rich text runs.
- PPTX output that can only preserve text, formulas, mixed prose/math, or code by cropping source-slide images.
- PDF output or PDF render verification without a PDF capability.
- Required file-handling capability for the selected output route is unavailable.
- Formula or diagram rendering is required by the material and no suitable route from `references/math-diagram-rendering.md` is available.
- Structural diagram rendering is required by the material and Graphviz, Mermaid, or an equivalent verified route is unavailable.
- Code export is required by the material and the selected output route cannot preserve the required code-frame semantics and verification evidence.

When one of these missing capabilities is detected, stop export and either install the missing environment with user approval, if allowed by the execution environment, or ask the user to install it. Do not continue with raw syntax, screenshots, default text boxes, simplified diagrams, or any other degraded substitute.

## Deliverables

Write final deliverables under `exports/<task-slug>/`, then return:

- PPTX path when produced.
- Verified PDF path when produced.
- Final completed knowledge graph copy.
- Knowledge graph change log copy when present.
- Freshness/checking log copy when present.
- Quality report covering output route, render verification, formula/diagram rendering routes, learning upgrades, factual updates, and unresolved uncertainties.
