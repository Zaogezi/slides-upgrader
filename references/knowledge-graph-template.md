# Knowledge Graph Template

Use this Markdown template after source extraction. Fill it with extracted courseware content first. If the source does not contain content for a field, leave the field blank.

Do not rewrite, paraphrase, normalize, or generate instructional text while filling this template from the source. Preserve original wording where usable. Add the source manifest item id and provenance for every filled item, such as slide number, page number, section title, speaker note, figure label, table label, or asset id.

## Lossless Source Capture

This step is lossless, not selective. Every substantive item recovered from the source in `extracts/<task-slug>.source.md` / `.json` — titles, bullets, definitions, claims, explanations, examples, exercises, answers, formulas, code blocks, tables, figure/diagram specifications, speaker notes, and captions — must be placed somewhere in this knowledge graph. Do not drop, summarize away, merge without trace, or silently skip source content because it is awkward, off-template, low quality, or seems redundant.

Reconcile source against graph item by item when you finish filling:

- Walk through each slide/page and each extracted item in `extracts/<task-slug>.source.md` / `.json`.
- Confirm each item has a home in the graph: a chapter block, a knowledge-point field, or the Unassigned Source Content section below.
- An item is considered captured only when its source manifest item id, original wording (or a verbatim-quoted fragment), and provenance appear in the graph. A topic heading without the underlying source text is not capture.
- A source item that does not fit an existing template field goes into the Unassigned Source Content section with provenance. It must not be omitted.
- If two source items overlap, keep both with provenance rather than discarding one, unless the duplication is verbatim re-publication of the same item at the same location.

Omission of recoverable source content is a blocker for this step, not a silent simplification.

## 1. Metadata

- Source file:
- Source format:
- Source language:
- Target language:
- Subject:
- Audience:
- User-specified output route:
- Markdown extract:
- JSON extract:
- Source manifest:
- Extraction uncertainty:
- Notes:

## 2. Chapter Directory

| Chapter id | Chapter title | Source location range | Main knowledge points | Prerequisite chapters or sections | Teaching requirements | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## 3. Chapters

Repeat this chapter block for every chapter or major source section.

### 3.x Chapter: `[chapter title]`

- Chapter id:
- Source location range:
- Original chapter / section title:
- Related figures / equations / code / tables:
- Source item ids:
- Provenance:

#### 3.x.1 Chapter Overview

- Motivation or use of this chapter:
  - Content:
  - Source item ids:
  - Provenance:
- Connection to the previous chapter or earlier material:
  - Content:
  - Provenance:
- Summary of main content:
  - Content:
  - Provenance:
- Teaching requirements:
  - Content:
  - Provenance:

#### 3.x.2 Knowledge Points

Repeat this knowledge-point block for every specific concept, theorem, method, model, algorithm, code pattern, experimental procedure, or problem type in the chapter.

##### 3.x.2.y Knowledge Point: `[knowledge point name]`

- Knowledge point id:
- Original heading or name:
- Source location range:
- Related figures / equations / code / tables:
- Provenance:

###### 3.x.2.y.1 Prerequisite Check

- Which existing knowledge does this knowledge point depend on?
  - Content:
  - Provenance:
- If the learner does not know it, which source content should they review? Fill only when this content exists in the source context.
  - Content:
  - Provenance:

###### 3.x.2.y.2 Knowledge-Point Introduction

- Limitation of the existing content:
  - Content:
  - Provenance:
- Problem this knowledge point solves:
  - Content:
  - Provenance:
- Connection to previous material:
  - Content:
  - Provenance:
- How the original problem is abstracted into a STEM problem:
  - Content:
  - Provenance:

###### 3.x.2.y.3 Concept And Formal Expression

- Rigorous definition:
  - Content:
  - Provenance:
- Symbol table / variable table:

| Symbol / variable | Meaning | Unit / type | Source item ids | Source wording | Provenance |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

- Mathematical formula / code:
  - Content:
  - Provenance:
- Natural-language explanation:
  - Content:
  - Provenance:

###### 3.x.2.y.4 Assumptions And Scope

- Conditions under which the conclusion holds:
  - Content:
  - Provenance:
- Model assumptions:
  - Content:
  - Provenance:
- Cases where this should not be used:
  - Content:
  - Provenance:
- Boundary cases:
  - Content:
  - Provenance:

###### 3.x.2.y.5 Intuition And Multiple Representations

- Geometric intuition:
  - Content:
  - Provenance:
- Physical meaning, for mathematical or physical topics:
  - Content:
  - Provenance:
- Code meaning, for computer science topics:
  - Content:
  - Provenance:
- Analogy, only when a fitting analogy exists:
  - Content:
  - Provenance:

###### 3.x.2.y.6 Derivation / Algorithm / Modeling Process

- Intuitive derivation:
  - Content:
  - Provenance:
- Core derivation:
  - Content:
  - Provenance:
- Complete derivation:
  - Content:
  - Provenance:
- Algorithm flow:
  - Content:
  - Provenance:
- Modeling steps:
  - Content:
  - Provenance:

###### 3.x.2.y.7 Examples And Counterexamples

- Standard example:
  - Content:
  - Provenance:
- Counterexample:
  - Content:
  - Provenance:
- Boundary example:
  - Content:
  - Provenance:

###### 3.x.2.y.8 Interactive Checks

For every interaction, include a clear answer and explanation when available.

- Concept judgment:
  - Prompt:
  - Answer:
  - Explanation:
  - Provenance:
- Small calculation:
  - Prompt:
  - Answer:
  - Explanation:
  - Provenance:
- Code reading, for computer science topics:
  - Prompt:
  - Answer:
  - Explanation:
  - Provenance:
- Phenomenon explanation, when applicable:
  - Prompt:
  - Answer:
  - Explanation:
  - Provenance:

###### 3.x.2.y.9 Worked Problems And Detailed Analysis

Repeat this block for every worked example or exercise selected for detailed treatment.

- Problem:
  - Content:
  - Provenance:
- Problem recognition:
  - Content:
  - Provenance:
- Solution idea:
  - Content:
  - Provenance:
- Formula / code steps:
  - Content:
  - Provenance:
- Natural-language explanation:
  - Content:
  - Provenance:
- Unit / dimension / result check, when needed:
  - Content:
  - Provenance:
- Common mistakes:
  - Content:
  - Provenance:

###### 3.x.2.y.11 Method Summary

- General steps for this type of problem:
  - Content:
  - Provenance:
- Applicable problem types:
  - Content:
  - Provenance:
- Common errors:
  - Content:
  - Provenance:
- Comparison with other methods:
  - Content:
  - Provenance:

###### 3.x.2.y.12 Extended Content

- Necessary extension:
  - Content:
  - Provenance:
- Interest extension:
  - Content:
  - Provenance:
- Connection to later courses:
  - Content:
  - Provenance:
- Practical application:
  - Content:
  - Provenance:

#### 3.x.3 Chapter Summary

- Main conclusions of this chapter:
  - Content:
  - Provenance:
- Knowledge structure of this chapter:
  - Content:
  - Provenance:
- Connections among knowledge points:
  - Content:
  - Provenance:
- Typical problem-solving methods:
  - Content:
  - Provenance:
- Common mistakes and cautions:
  - Content:
  - Provenance:
- Connection to later chapters or later courses:
  - Content:
  - Provenance:

## 4. Unassigned Source Content

Use this section as the lossless catch-all so that no recoverable source item is dropped during graph construction. Add one entry per source item that does not fit any chapter, knowledge-point, or chapter-summary field above. Do not leave this section as the only home for an item when a proper field exists; first try to place the item in the closest knowledge-point field, then fall back here.

| Entry id | Source item id | Original source wording (or verbatim fragment) | Source location | Asset type | Why it is unassigned | Intended reuse | Provenance |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

- Entry id: stable local id, e.g. `U1`, `U2`.
- Source item id: stable id from `extracts/<task-slug>.source-manifest.json`.
- Original source wording: verbatim text, formula, code, table fragment, figure caption, or speaker-note text. Quote the source; do not paraphrase.
- Source location: slide number, page number, or section title.
- Asset type: text, formula, code, table, figure/diagram specification, speaker note, caption, or other.
- Why it is unassigned: e.g. no matching knowledge point, marginal note, aside, transition slide, appendix-style remark, or source artifact that does not map to a template field.
- Intended reuse: how this item should be carried downstream — keep verbatim in output, attach to a knowledge point during completion, or flag for user review.
- Provenance: same provenance rules as the rest of the graph.

Completion rules in `references/completion-rules.md` may later move an item from here into a knowledge-point field, but never delete an entry without recording where it was moved or why it was discarded.
