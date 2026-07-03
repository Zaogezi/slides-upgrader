# Outdated Content Checking

Use this reference when course material may contain obsolete facts, versions, standards, datasets, APIs, software commands, benchmarks, laws, or current-practice claims.

## Claims That Need Verification

Verify or flag claims involving:

- Software versions, package APIs, commands, installation steps, or screenshots.
- Hardware specs, performance benchmarks, pricing, or availability.
- Standards, protocols, laws, regulations, policies, or accreditation requirements.
- Dataset names, URLs, access methods, licenses, or leaderboard results.
- "Current", "latest", "state of the art", "widely used", or "recent" claims.
- Tool recommendations that could cost the learner time or money.
- Facts about organizations, people, products, or services.

Usually stable and lower priority:

- Core mathematical definitions and theorems.
- Classical physics laws within their stated assumptions.
- Established algorithms and data structures.
- Historical facts that are not being framed as current.

## Source Preference

Prefer sources in this order:

1. Official documentation, standards bodies, maintainers, publishers, or institutional pages.
2. Peer-reviewed papers, textbooks, or authoritative technical references.
3. Reputable vendor or project release notes for versioned tools.
4. Secondary tutorials only when primary sources are unavailable or too sparse.

Do not treat old course slides, unsourced blogs, or forum snippets as authoritative for current claims.

## Verification Notes

When changing or flagging content, record:

- Original claim.
- Updated claim or uncertainty.
- Source used, if available.
- Publication date, release date, or access date when relevant.
- Whether the update affects examples, commands, screenshots, or exercises.

Keep notes short enough for the final quality report.

## Rewrite Rules

- Do not modernize stable concepts just to make the deck feel newer.
- Do not silently replace a course's chosen toolchain if the original may be required by the instructor.
- When a version matters, write the version explicitly.
- When multiple versions are common, label examples by version or give a compatibility note.
- If a task requires updating, correcting, or modernizing a time-sensitive claim but no research capability is available, refuse the task and direct the user to the installation guide in `SKILL.md`.
- If research is available but a specific claim cannot be resolved from authoritative sources, mark it as "needs review" instead of inventing certainty.

## Visual Update Rules

For outdated screenshots or UI workflows:

- Prefer replacing with current, source-backed steps.
- If exact UI cannot be verified, use conceptual steps rather than fake screenshots.
- Keep old screenshots only when the course explicitly studies legacy tools.

## Final Report Items

Include in the delivery report:

- Claims updated.
- Claims flagged as uncertain.
- Sources used for current claims.
- Any old examples left unchanged because they are part of the course context.
