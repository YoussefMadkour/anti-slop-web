# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses semantic versioning.
Rule IDs are stable across versions; retired rules are marked, never renumbered.

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
