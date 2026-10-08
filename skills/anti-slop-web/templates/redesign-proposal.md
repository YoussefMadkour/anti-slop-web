# Redesign Proposal: <product or surface>

Status: proposed | approved | approved with changes
Author: <agent or person>, <date>
Scope: <which surfaces: whole product | marketing site | app shell | one flow>

Written in Redesign mode before any code changes. The owner approves, edits, or rejects each
section. Keep it short: a page or two. Detail belongs in `DESIGN.md` once approved.

## 1. Why redesign

<What is wrong with the current UI, in the owner's words where possible. Tie each point to
evidence: an audit finding, a user complaint, a business goal. "Looks dated" needs to be made
specific: which parts, compared with what.>

## 2. Baseline

Audit of the current UI (design, visual-system, accessibility, responsive):
- P0: <count and the important ones>
- HIGH: <count and the important ones>
- Visual-system inventory: <type sizes vs scale, raw colors, radii, component sources>

## 3. Keep

<Everything that stays: brand assets, voice, information architecture, flows users rely on,
components that work, content. Default is to keep; anything removed is listed in section 4
with a reason.>

## 4. Change

Direction:

| Dial | Now (as built) | Proposed | Reason |
|------|----------------|----------|--------|
| VARIANCE | | | |
| MOTION | | | |
| DENSITY | | | |
| CHARACTER | | | |

Signature element: <one sentence, or "restraint">
Palette: <keep | adjust (what) | new (why)>
Typography: <keep | new scale | new face (why)>
Removed: <element, reason>

## 5. Component library

Decision: <keep and re-tokenize | keep as-is | migrate from X to Y | adopt Y> because <reason>.
Effect components: <none | source and the pieces, each with its job>

| Current component | Proposed | Change |
|-------------------|----------|--------|
| <hand-rolled Button, 3 variants> | <library Button + project variants> | <replace; merge variants> |
| <MUI DatePicker> | <library DatePicker> | <replace to remove second library> |

## 6. Motion plan

Tier: <CSS | scroll-driven CSS | JS library (name) | canvas or WebGL>
Library: <none | name, and why CSS is not enough>

| Animation | Where | Job | Reduced-motion version |
|-----------|-------|-----|------------------------|
| <dialog enter and exit> | <all dialogs> | <state change> | <instant, fade only> |

## 7. Migration order

Each step ships on its own and leaves the product consistent.
1. Tokens: color, type, radius, spacing, motion (no visual change where values are equal)
2. Primitives: buttons, inputs, overlays, on the new tokens or library
3. Shell and navigation
4. Screens, highest traffic or highest pain first: <list>
5. Remove dead styles, old components, and unused dependencies

## 8. Risks and open questions

- <Risk: e.g. second library during migration; mitigation>
- <Question for the owner>

## 9. Approval

<Owner decision and any changes, recorded here before building starts.>
