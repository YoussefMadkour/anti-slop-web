# Product Archetypes

Classify the interface before writing `DESIGN.md` (workflow step 3). The archetype tells you
three things: typical dial ranges, which rules to weigh heavily or lightly, and which
references to load.

Dial ranges below are **typical starting points, not defaults or limits**. Brand and product
requirements override them. Write a one-line reason for whatever you choose.

## Combining archetypes

Most products have one primary archetype per surface, and products often have several surfaces.
A developer tool usually has a `MARKETING` site with a `DEVELOPER_TOOL` secondary, and a
`DEVELOPER_TOOL` application with an `APPLICATION` secondary. Classify per surface and record
both in `DESIGN.md` §1. The primary archetype wins when the two disagree; the secondary adds
vocabulary (for example, monospace and dark themes become legitimate on the dev tool's
marketing site).

## How archetypes change the rules

- **Rule scope.** Each rule in `rules.md` and the specialist catalogs lists the archetypes it
  applies to fully. Outside its scope, flag a tell only if it clearly harms this product.
- **Conventions that look like slop but are not.** Each profile lists patterns that are
  legitimate in that archetype. Treat them as passing unless the content contradicts them.
- **Consistency versus variation.** Marketing and editorial work rewards compositional variety.
  Applications, dashboards, and operations software reward consistency: the same anatomy on every
  screen is a usability feature, not a template tell.

---

## MARKETING
**Job:** Explain a product and move a visitor to a specific next step.
**Typical dials:** VARIANCE 4-8, MOTION 2-6, DENSITY 2-4, CHARACTER 5-9.
**Prioritize:** A specific, honest value proposition; real proof; narrative order driven by the
audience's questions; one clear primary action per section.
**Legitimate here:** Hero sections, including centered ones; product screenshots; a logo bar of
real customers; pricing tables; FAQs built from real questions; expressive type and color.
**Weigh heavily:** UI-02, UI-03, UI-05, UI-08, UI-09, UI-22, IN-01 to IN-03, CP-01, CL-01.
**Weigh lightly:** UI-07.
**Load:** `layouts.md`, `typography.md`, `color.md`, `motion.md`; `anti-slop-copy`.

## APPLICATION
**Job:** Let signed-in users complete tasks repeatedly and efficiently (CRUD, settings, workflows,
collaboration).
**Typical dials:** VARIANCE 1-4, MOTION 1-3, DENSITY 4-7, CHARACTER 3-6.
**Prioritize:** Task flow, predictable navigation, every state designed, forms that forgive
errors, keyboard efficiency.
**Legitimate here:** Sidebar shells, consistent page anatomy, uniform lists and cards for uniform
objects, standard component-library controls, system fonts, Inter.
**Weigh heavily:** FN-01 to FN-05, UI-06, UI-07, UI-01 (novelty costs most here), A11Y rules.
**Weigh lightly:** UI-03, UI-05, UI-16, UI-17.
**Load:** `forms.md`, `components.md`, `navigation.md`; `anti-slop-a11y`.

## DASHBOARD
**Job:** Show the state of something at a glance and route attention to what needs action.
**Typical dials:** VARIANCE 2-5, MOTION 1-3, DENSITY 6-8, CHARACTER 3-6.
**Prioritize:** The one decision this screen supports; real numbers with named comparison
periods; scannability; honest empty and partial-data states.
**Legitimate here:** KPI rows (when the KPIs matter), grid layouts of same-type widgets, tabular
figures, muted chrome with color reserved for status and data, a bento overview when widgets
genuinely differ in importance.
**Weigh heavily:** UI-07, UI-24, UI-06, IN-02 (invented KPIs and deltas), FN-02, FN-03.
**Weigh lightly:** UI-03, UI-05, UI-17.
**Load:** `dashboards.md`, `charts.md`, `tables.md`.

## OPERATIONS
**Job:** Support people monitoring and controlling real systems or processes under time
pressure: logistics, manufacturing, support queues, incident response, fleet, trading desks.
**Typical dials:** VARIANCE 1-3, MOTION 1-2, DENSITY 7-10, CHARACTER 2-5.
**Prioritize:** Scanability, stable layout (nothing moves unless the world changed), status
encoding that survives color blindness and glare, exact values, alarm hierarchy, fast keyboard
paths, long-session comfort.
**Legitimate here:** Dense uniform tables and grids, strict symmetry, monospace or tabular
figures, dark themes for control rooms, high-contrast status colors, minimal animation, small
type at high density (still meeting contrast).
**Weigh heavily:** UI-01 (forced asymmetry or novelty is harmful), UI-19 (false indicators
are dangerous), FN-05, A11Y-08 (color-only status), A11Y-10.
**Weigh lightly:** UI-03, UI-05, UI-12, UI-16, UI-17. Do not apply marketing composition rules.
**Load:** `dashboards.md`, `tables.md`, `charts.md`.

## EDITORIAL
**Job:** Be read: articles, publications, documentation, long-form storytelling.
**Typical dials:** VARIANCE 3-8, MOTION 1-4, DENSITY 2-5, CHARACTER 5-9.
**Prioritize:** Reading comfort (measure, leading, contrast), typographic hierarchy, navigable
structure, images that carry information.
**Legitimate here:** Serif body text, single-column layouts, centered measure, generous
whitespace, full-bleed images, magazine grids for indexes.
**Weigh heavily:** UI-05 (for index pages), UI-22, CP rules.
**Weigh lightly:** UI-07.
**Load:** `typography.md`, `layouts.md`; `anti-slop-copy`.

## ECOMMERCE
**Job:** Help shoppers find, evaluate, and buy products with confidence.
**Typical dials:** VARIANCE 2-6, MOTION 1-4, DENSITY 4-7, CHARACTER 4-8.
**Prioritize:** Product imagery, price and availability clarity, filtering, trustworthy checkout,
real reviews, fast pages on mobile.
**Legitimate here:** Uniform product grids, standard cart and checkout patterns (novelty in
checkout costs money), sticky add-to-cart on mobile, review stars from real reviews.
**Weigh heavily:** IN-01 (fake reviews), FN-04, FN-05, UI-01 in checkout, RS rules.
**Weigh lightly:** UI-03 on listing pages.
**Load:** `layouts.md`, `forms.md`, `components.md`, `navigation.md`.

## DEVELOPER_TOOL
**Job:** Serve developers: APIs, SDKs, CLIs, infrastructure consoles, IDE-like tools, docs.
**Typical dials:** VARIANCE 2-5, MOTION 1-3, DENSITY 6-8, CHARACTER 4-7.
**Prioritize:** Copyable, runnable code; accurate technical detail; keyboard-first interaction;
dense information with clear hierarchy; fast search.
**Legitimate here:** Monospace type, dark themes, terminal and code-block visuals (when real and
runnable), technical iconography, command palettes, dense layouts, syntax-highlight palettes.
**Weigh heavily:** IN-03 (performance and security claims), UI-22 (fake terminals), CP-01.
**Weigh lightly:** UI-12, UI-17, UI-16.
**Load:** `navigation.md`, `tables.md`, `typography.md`; for the marketing site also `layouts.md`.

## CREATIVE_EXPERIENCE
**Job:** Deliver an experience where the form is part of the message: portfolios, campaigns,
launches, art, interactive stories, games.
**Typical dials:** VARIANCE 6-10, MOTION 5-10, DENSITY 1-4, CHARACTER 8-10.
**Prioritize:** A strong owned idea executed with rigor; performance budget for heavy media;
accessible fallbacks (reduced motion, keyboard path, readable text alternative).
**Legitimate here:** Unconventional navigation, scroll-driven narratives, WebGL, custom cursors,
experimental type, full-screen motion, as long as the core content stays reachable.
**Weigh heavily:** A11Y-10 (motion safety), RS-02 (content reachable on small screens),
UI-27 (the concept must be sustained), performance.
**Weigh lightly:** UI-01 (novelty is the point, but the task must still work), UI-23.
**Load:** `motion.md`, `typography.md`, `layouts.md`.

## DATA_EXPLORATION
**Job:** Let analysts and curious users ask their own questions of data: BI tools, research
portals, public data sites, notebooks, query builders.
**Typical dials:** VARIANCE 1-4, MOTION 1-3, DENSITY 6-9, CHARACTER 2-5.
**Prioritize:** Hierarchy, comparison, provenance (source, freshness, method), filtering and
drill-down, legibility of labels and numbers, honest uncertainty, export.
**Legitimate here:** Dense tables, small multiples, linked filters, many controls on screen,
muted chrome so data carries color.
**Weigh heavily:** UI-24, IN-02, A11Y-18 (chart alternatives), A11Y-11, FN-02 (partial data).
**Weigh lightly:** UI-03, UI-05.
**Load:** `charts.md`, `tables.md`, `dashboards.md`.

---

## The four example profiles

These are illustrations of reasoning, not presets.

| Product | VARIANCE | MOTION | DENSITY | CHARACTER | Reasoning |
|---------|---------:|-------:|--------:|----------:|-----------|
| Industrial operations dashboard | 3 | 1 | 9 | 5 | Operators scan for anomalies across shifts; stable layout and dense exact values matter; a recognizable status language aids training |
| Luxury editorial | 8 | 4 | 2 | 9 | The brand is the product; composition and type carry identity; content is sparse and image-led |
| Bank admin console | 2 | 1 | 8 | 3 | Correctness, auditability, and staff familiarity beat expression; follow the bank's design system |
| Developer tool | 4 | 2 | 7 | 6 | Dense and keyboard-driven, with an identity developers recognize in docs, CLI, and console alike |
