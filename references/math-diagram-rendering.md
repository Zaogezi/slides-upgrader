# Math And Diagram Rendering

Use this reference during capability preflight, output materialization, and visual QA whenever the source or completed knowledge graph contains complex formulas, structural diagrams, mathematical diagrams, data figures, algorithm visualizations, or source figures that must be reconstructed.

## Boundary Principle

Rendering tools support learner-facing output, but they must not become a source of new facts. Use only source-derived content and clearly labeled supplements from the completed knowledge graph. Preserve original notation, labels, graph direction, data values, and visual meaning unless the completed graph records a verified correction.

Prefer native equation, editable, or vector output when the final route supports it. Use raster images only when the target format cannot preserve the visual reliably, and render at high enough resolution for the final PPTX/PDF size. Mathematical formulas must not be exported as default text boxes containing raw LaTeX, plain Unicode approximations, or placeholder equation text. If prose contains inline mathematical notation, preserve the surrounding sentence or paragraph as the rendering unit instead of rendering only the mathematical token separately.

## Rendering Route Matrix

| Content type | Preferred tool route | Required environment | Best for | Do not use for |
|---|---|---|---|---|
| Complex mathematical formulas | MathJax, KaTeX, or LaTeX rendering | Node.js with `mathjax-full` or `katex`; or TeX Live / MiKTeX; optional `sharp` or `dvisvgm` for image conversion | Matrices, fractions, integrals, sums, limits, piecewise functions, derivation chains, optimization objectives, probability formulas | Structural diagrams, flowcharts, data plots |
| Structural diagrams | Graphviz or Mermaid rendering | Graphviz `dot`; or Node.js with `@viz-js/viz`; Mermaid may use `@mermaid-js/mermaid-cli` and Chromium | Trees, syntax trees, state machines, automata, flowcharts, dependency graphs, DAGs, local knowledge-graph structure | High-precision mathematical formulas, complex geometry diagrams |
| Mathematical schematic diagrams | Hand-authored SVG or programmatic SVG | Basic SVG generation through Node.js or Python; optional `sharp`, CairoSVG, Inkscape, or browser-based PNG conversion | Commutative diagrams, coordinate sketches, vector-space mappings, set relations, simple geometry, arrow relation diagrams, concept schematics | Large data plots, complex formula layout |
| Data and algorithm visualizations | Python or JS plotting | Python with Pillow, matplotlib, or networkx; or Node.js with Canvas, SVG, or D3; optional `reportlab`, `python-pptx`, or `sharp` | Function plots, heatmaps, matrix visualization, statistical charts, algorithm process diagrams, batch exercise figures, experimental result plots | Single pure formulas, Office-editable equations |

## Capability Preflight

Before materialization, inspect the completed knowledge graph and extracted source for formula-bearing and diagram-bearing items. Run only the checks relevant to the material:

- **Formula rendering**: verify at least one usable route can render a sample display equation with fractions, superscripts/subscripts, and a Greek symbol to SVG or high-resolution PNG. Record the tool, command, output format, and fallback path.
- **Structural diagram rendering**: verify Graphviz, Mermaid, or equivalent can render a small directed graph to SVG or PNG. Record whether the route supports labels, multiline text, and non-ASCII characters.
- **Programmatic SVG**: verify the chosen runtime can write valid SVG and, when raster output is needed, convert it to PNG without clipping.
- **Plotting route**: verify the chosen Python or JS plotting stack can create a non-empty PNG or SVG for a minimal chart when data figures or algorithm visualizations are required.

If the material contains complex formulas, structural diagrams, schematics, plots, or algorithm visualizations and no suitable route from the matrix is available, treat the missing renderer as a required capability blocker for final output. Stop export before materialization. If the execution environment allows dependency installation, request approval and install the corresponding renderer; otherwise ask the user to install it. Do not replace formulas or diagrams with raw syntax, default text boxes, screenshots, simplified redraws, or unverified approximations.

## Formula Rendering Requirements

- Preserve source notation, variable names, ordering, equation numbering, and referenced labels.
- Use MathJax, KaTeX, or LaTeX for display formulas that include matrices, aligned derivations, cases, roots, sums, integrals, limits, probability notation, optimization objectives, or dense symbolic expressions.
- For inline math inside a sentence, bullet, caption, theorem statement, definition, or paragraph, render the whole sentence or paragraph through an inline-math-capable route. Preserve the original prose, spacing, punctuation, and mathematical baseline alignment. Do not keep prose in ordinary text while substituting the math expression with plain text, Unicode approximations, raw LaTeX, or a separate default text box.
- Use SVG where possible for crisp PPTX/PDF export. If raster output is required, render with transparent or matching background and enough pixel density to remain readable at final size.
- Keep the formula text or source LaTeX in a sidecar note, metadata field, or quality-report appendix when practical so later maintainers can regenerate the visual.
- Do not leave learner-facing raw LaTeX unless the lesson is explicitly teaching LaTeX or formula syntax.
- For PPTX output, do not use default PowerPoint text boxes for formulas. Use native equation objects when available; otherwise place verified SVG or high-resolution PNG assets generated from MathJax, KaTeX, or LaTeX.
- Visually inspect every formula-bearing and mixed prose/math final page or slide at full size. Check for missing glyphs, clipped ascenders/descenders, collapsed fractions, incorrect line breaks, low contrast, unreadable scaling, baseline mismatch between prose and inline math, and sentences split into incompatible text/formula fragments.

## Structural Diagram Requirements

- Use Graphviz or Mermaid for trees, syntax trees, state machines, automata, flowcharts, dependency graphs, DAGs, and local knowledge-graph diagrams.
- Preserve source node labels, edge labels, directionality, grouping, and any semantic color or shape meaning. If the source is ambiguous, record the uncertainty rather than inventing missing labels.
- Use SVG where possible. If converting to PNG, ensure the exported image has adequate resolution and no clipped labels or arrowheads.
- Avoid using formula renderers for structural diagrams. Embed formulas inside diagram labels only when the chosen graph route can preserve them legibly; otherwise render the formula separately and compose the layout through the deck/PDF capability.
- Visually inspect every diagram-bearing final page or slide at full size. Check for missing labels, reversed arrows, edge crossings that obscure meaning, clipped nodes, broken non-ASCII text, and unreadable small text.

## Mathematical Schematic And Plot Requirements

- Use programmatic SVG for concept schematics, coordinate sketches, vector-space mappings, set relations, simple geometry, and arrow relation diagrams when a source figure is missing or unusable but the completed graph provides enough source-derived structure.
- Use Python or JS plotting for function plots, heatmaps, matrices, statistics charts, algorithm process visuals, or experimental result figures.
- Keep axes, scales, units, legends, labels, and data values traceable to the source or completed graph.
- Do not smooth, interpolate, extrapolate, or cosmetically alter data in ways that change interpretation unless the completed graph records a verified correction.

## Evidence And Reporting

Save generated formula and diagram assets under `exports/<task-slug>/qa/` or a clearly named asset subfolder when they are part of the final output. The quality report must include:

- Rendering routes used for formulas, structural diagrams, schematics, and plots.
- Preflight results and fallback paths.
- Asset paths for generated SVG/PNG/PDF intermediates when retained.
- Full-size visual review result for every formula-bearing and diagram-bearing page or slide.
- Any unresolved source-quality limitation or renderer limitation.
