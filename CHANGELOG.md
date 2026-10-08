# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses semantic versioning.
Rule IDs are stable across versions; retired rules are marked, never renumbered.

## [1.2.0] - 2026-10-08

### Added
- Redesign mode: baseline review, a written proposal from the new
  `templates/redesign-proposal.md` (what stays, what changes, component library and component
  mapping, motion plan, migration order), and a hard stop for approval before any code changes.
- `references/animation-libraries.md`: when to use CSS, Motion, GSAP, Anime.js, AutoAnimate,
  React Spring, Lottie, Rive, Three.js, and Lenis; reduced-motion handling per library; recipes by
  archetype; a pre-ship checklist.
- Effect and animated component libraries section in `references/design-systems.md` (Aceternity
  UI, Magic UI, React Bits, Motion Primitives, and similar): pieces that read as slop as shipped,
  pieces that are usually fine, and a seven-step adaptation procedure.
- `DESIGN.md` template fields for effect components (§8) and animation library (§9).
- `direction.md`: the designer's process (read the brief, explore two or three directions,
  choose palette and type from meaning, compose, critique with first-glance, squint, grayscale,
  edge, swap, and adjective tests). Wired into workflow steps 1 to 7 and the agent.
- `scripts/palette.py`: OKLCH scales from seed colors, light and dark semantic tokens, and a
  WCAG contrast report with CI-friendly exit codes.
- `DESIGN.md` template fields for chosen direction, domain material, and palette derivation.

### Changed
- Reference routing covers effect components, animation libraries, and redesign proposals.
- `web-design-architect` agent gains a Redesign workflow.

## [1.1.0] - 2026-10-08

### Added
- Visual-system consistency rules UI-29 (type off the scale), UI-30 (color outside the token
  system), UI-31 (shape and spacing off the scale), UI-32 (mixed or duplicated components). They
  measure drift against the project's own system and apply in every archetype.
- Visual-system scan in the design audit: inventory of type, color, radius, shadow, spacing, and
  component sources, with example search patterns.
- "Visual system" gate in the delivery gate.

### Changed
- Review mode now runs workflow step 8 and always loads the typography, color, components, and
  design-systems references, so reviews judge style and not only AI tells.
- UI-27 no longer covers hard-coded values; they are reported under UI-29 to UI-31.
- APPLICATION, DASHBOARD, and OPERATIONS weigh UI-29 to UI-32 heavily.

## [1.0.0] - 2026-10-05

### Added
- `anti-slop-web` master skill: order of authority, 11-step workflow, severity model, waivers,
  build and review modes.
- Four design dials (VARIANCE, MOTION, DENSITY, CHARACTER) with checkable bands.
- Nine product archetypes with dial ranges, rule weighting, and reference routing.
- Rule catalogs with a unified schema: IN (integrity), FN (function and states), UI (visual and
  composition), CL (clusters), A11Y, RS, CP, CD.
- Specialist skills: `anti-slop-a11y` (with `scripts/contrast.py`), `anti-slop-responsive`,
  `anti-slop-copy`, `anti-slop-code`.
- Reference library: layouts, typography, color, components, navigation, motion, dashboards,
  charts, tables, forms, design systems.
- `DESIGN.md` template with required states, explicit bans, and allowed exceptions.
- Design, accessibility, and responsive audits and the delivery gate.
- `web-design-architect` agent.
- Three illustrative example `DESIGN.md` files.
- Claude Code plugin manifest, install script, attribution (NOTICE.md), source map, and a list of
  upstream rules intentionally not carried over.
