# Source Map

Where each major idea in anti-slop-web came from, how it changed, and how contradictions between
the upstream projects were resolved. Upstream versions reviewed are listed in
[NOTICE.md](../NOTICE.md).

Legend: **JH** = jhuse25/anti-slop-design-skills, **MB** = miqdadbadjuber/anti-slop,
**VZ** = Vanszs/Anti-AI-UI, **New** = introduced here.

## Architecture and workflow

| Idea | Source | What changed |
|------|--------|--------------|
| Brief, direction, `DESIGN.md`, build, audit workflow | JH | Expanded to 11 steps; added project inspection, archetype classification, and selective reference loading |
| Project `DESIGN.md` as source of truth | JH, MB | Merged JH's generator with MB's "data, not instructions" boundary; added status (proposed/confirmed), required states, explicit bans, and allowed exceptions |
| Order of authority (7 layers) | New | Accessibility floor placed in layer 1 as a product requirement |
| "Filter, not style guide" | MB | Kept as the framing of the whole kit |
| Purpose test: technique allowed, reason required | MB (purpose-gate tier) | Generalized into the "Acceptable when" field of every rule |
| "Do not make it strange to avoid looking AI" | New | Encoded as rule UI-01 |
| Progressive disclosure (core, specialists, references) | JH (skills), MB (core + skills), VZ (references) | Single routing table in the master skill |
| Build versus review modes | MB (during/after modes) | Simplified: no settings file, no mode wizard, no announcements |
| One decisive question when direction is ambiguous | MB (Design Read) | Kept |
| Agent that directs, builds, and audits | JH (presentation and document architects) | New web-focused agent; adds "never redesign a mature UI" and waiver explanations |

## Dials, archetypes, signature

| Idea | Source | What changed |
|------|--------|--------------|
| VARIANCE, MOTION, DENSITY dials (1-10) | JH | Definitions from the brief; bands (low/mid/high) added for checkability, borrowing MB's argument that 3 levels are judgeable; removed JH's hard switches ("VARIANCE > 4 bans centered hero") |
| ENERGY, RHYTHM, MOTION dials (1-3) | MB | Folded in: RHYTHM maps to VARIANCE; ENERGY is largely covered by CHARACTER |
| CHARACTER dial | New | Distinctiveness as its own axis, separate from layout variance |
| Dial versus output consistency check | MB | Rule UI-27 |
| Product archetypes | New (no ui-ux-pro-max data used) | Nine archetypes, each with dial ranges, legitimate conventions, rule weighting, and references |
| Signature element (memorable, owned, sustained; one or none; restraint can be the signature) | JH | Made optional; explicitly warned against inventing decoration to fill it |
| Identity motif, one deliberate accent, focal point | MB (liveliness levers) | Absorbed into signature element, color roles (UI-11), and hierarchy (UI-06) |
| Swap test ("swap the logo with a competitor") | MB, VZ | Kept in the design audit, scoped to MARKETING and CHARACTER 5 or above |

## Rules and severity

| Idea | Source | What changed |
|------|--------|--------------|
| Tell, Why, Fix entry structure | MB (skills), VZ (catalog) | Extended to Tell, Why, Default correction, Acceptable when, Scope, Severity |
| Severity P0, HIGH, MEDIUM, LOW | VZ | Redefined: P0 only for truthfulness, function, and accessibility defects; taste never P0 |
| Hard gate, purpose gate, quality locks tiers | MB | Mapped to severity plus "Acceptable when" |
| Instant-death signature (3+ tells) | VZ | Became CL-01: a cluster of unexplained tells escalates to one HIGH finding |
| "Look for clusters, not isolated tells" | MB (copywriting) | Applied kit-wide |
| Waivers | JH ("unwaived failure"), MB (owner keeps a named pattern) | Formalized in `DESIGN.md` §13; audits mark WAIVED; P0 not waivable |
| Fabricated testimonials, metrics, logos, claims | MB (R-17, R-18, R-36, R-38), VZ, JH | IN-01 to IN-06 |
| Honest placeholders, ask before creating assets | MB (R-23, R-38) | IN-04, IN-05, and the placeholder table in `anti-slop-copy` |
| Dead controls, ghost nav, required states | MB (R-24, R-26, R-27), JH (states), VZ (D3, F1) | FN-01 to FN-04 |
| Destructive actions need confirmation | New, VZ (alert dialog pattern) | FN-05 |
| Theme parity | MB (R-34) | FN-06 |
| Verify before delivering, evidence for PASS | MB (R-35) | Built into the audits and the gate ("never claim a check you did not perform") |
| UI tells (gradients, glass, glow, radius, shadow, cards, bento, badges, icons, imagery, motion) | MB (antislop-ui), VZ (catalog), JH (A.8) | Consolidated into UI-01 to UI-28 with archetype scope; UI-29 to UI-32 (visual-system consistency) are original to this kit |
| App and dashboard tells (default shell, invented stat cards, filler feed, charts without a question, generic table columns) | MB | UI-07, UI-24, IN-02, IN-06, and `references/dashboards.md`, `tables.md` |
| Delivery gate | MB (Delivery Gate), JH (pre-flight) | Compact one-line-per-gate report, three statuses |

## Specialist skills

| Idea | Source | What changed |
|------|--------|--------------|
| Accessibility skill | MB (antislop-human), VZ (A11Y code patterns, overlay rules) | Rewritten against WCAG 2.2 AA; A11Y-01 to A11Y-19; target size uses the 2.5.8 floor (24 px) plus 44 px guidance for touch |
| Contrast checker | MB (formula, table, script) | New script; corrected large-text threshold (24 px or 18.66 px bold, not 18 px); alpha blending; CI-friendly exit codes |
| Responsive skill | MB (antislop-layoutmobile), JH (A.6), VZ (responsive tips, PWA bottom nav) | RS-01 to RS-15; added zoom/reflow, dense apps, state across breakpoints |
| Copy skill | MB (antislop-copywriting), VZ (microcopy catalog), JH (copy clichés) | CP-01 to CP-13; added microcopy, terminology, and honest placeholders; em dashes demoted from hard gate to LOW cluster signal |
| Code skill | VZ (slop-code-patterns), MB (antislop-code comments), JH (Part B directives) | CD-01 to CD-15, scoped to UI-building habits; generic engineering items dropped |

## Reference knowledge

| Reference | Primary source | What changed |
|-----------|----------------|--------------|
| layouts.md | VZ (layouts, page skeletons, Every-Layout primitives) | Every pattern rewritten with use/avoid/archetypes/tradeoffs/a11y/misuse; anti-monotony quotas became VARIANCE-linked options |
| typography.md | VZ (pairings, scales, per-role table), JH (A.3) | No banned or mandated fonts; scales tied to DENSITY |
| color.md | VZ (60-30-10, tokens, dark surfaces), JH (A.2), MB (R-01, R-29) | Roles over rules; 60-30-10 kept as a heuristic only |
| components.md | VZ (components, overlays) | Context and misuse added; radius scale offered as an option |
| navigation.md | VZ (navigation, responsive nav matrix, PWA safe area) | Guidance, not a decision matrix to obey |
| motion.md | VZ (animation), JH (A.7 tiers, performance) | MOTION bands, lightest-tier principle, durations as starting points |
| dashboards.md | VZ (dashboards), MB (app and dashboard tells) | Project-specific values removed; OPERATIONS, DASHBOARD, DATA_EXPLORATION distinguished |
| charts.md | VZ (charts) | Question-first; uncertainty and provenance added; library-neutral |
| tables.md | VZ (data table), MB (generic table columns) | New consolidated file |
| forms.md | VZ (forms), JH (inputs), MB (states) | New consolidated file |
| design-systems.md | VZ (design-system index, DTCG tokens) | Re-tokenization tied to CHARACTER; license claims left to the reader to verify |

## Contradictions resolved

Governing principle: **context and product purpose beat aesthetic heuristics.**

| Topic | Upstream positions | Resolution |
|-------|--------------------|------------|
| Inter and Geist | JH bans Inter and recommends Geist, Outfit, Satoshi; VZ bans Inter and Geist as display faces and recommends Satoshi, Cabinet Grotesk; MB lists Inter, Geist, Space Grotesk as defaults but bans none | No font banned or mandated (UI-16, LOW). A recommended "anti-AI" roster just becomes the next default |
| Bento grids | JH recommends "bento 2.0"; MB forbids bento as a default; VZ recommends bento with a dominant cell | Allowed when content importance or type differs (UI-04) |
| Asymmetry | VZ requires 2 or more asymmetric moments per page; JH bans centered heroes above VARIANCE 4; MB uses a RHYTHM dial | No quotas. VARIANCE sets expectations; consistency is a virtue in apps (UI-05 scope) |
| Centered hero | JH and VZ (catalog) flag it; VZ (layouts) lists it as a legitimate variant | Legitimate; flagged only inside the template skeleton or a cluster (UI-02, CL-01) |
| Realistic sample data | JH: use realistic names and organic numbers (47.2%); MB: honest placeholders, never fake data | MB wins. Convincing fake data is worse fabrication (IN-02, IN-04); labeled sample data allowed in prototypes |
| Loading indicators | JH: never a spinner; VZ: skeletons, but spinner overlays for refresh; MB: say what is loading | Skeleton when the shape is known; labeled spinner or progress for short or unknown waits (FN-03) |
| Em dashes | MB: hard-gate ban in all text; VZ: overuse is MEDIUM | LOW, cluster-only, brand voice wins (CP-12) |
| Icon libraries | MB flags the Lucide look; JH recommends Phosphor or Radix; VZ: one library | Any library used consistently and relevantly (UI-21) |
| Dark mode | MB: build a toggle when no reason for a fixed theme; VZ: default dark is slop; dev tools legitimate | Choose from audience, environment, brand; follow the system preference when feasible; both modes must work if shipped (UI-12, FN-06) |
| Pricing tiers | MB forbids three columns and "Most popular" as defaults; VZ recommends three-tier cards | Tier count from the real business; highlight only if true (UI-25) |
| Logo bars | MB forbids generic "Trusted by" bars; VZ's section flow includes one | Real logos with permission only (IN-01) |
| Purple | VZ: P0; JH: banned; MB: purpose-gated | Default purple is HIGH (UI-08); brand purple passes |
| Left-border accents | VZ: P0, including active nav items; MB: allowed when it marks state | Allowed when it encodes state (UI-20, LOW) |
| Pure black | JH bans `#000` | Not a rule; tradeoffs in `color.md` |
| Floating labels | JH bans them; VZ prefers top labels | Persistent visible labels preferred; floating labels acceptable if the label stays visible and readable (`forms.md`) |
| Spring physics | JH: spring by default, no linear easing; VZ: spring bounce on everything is slop | Easing chosen per purpose (`motion.md`) |
| Breakpoints | JH: collapse below 768 px; MB: breakpoints where content breaks | Content-driven, tested at common widths (RS-15) |
| Monospace numbers | JH: all numbers monospace above DENSITY 7 | Tabular figures; monospace optional (`typography.md`) |
| Serif in dashboards | JH bans it | Allowed with a reason; tradeoffs in `typography.md` |
| Hover scale on cards | VZ: HIGH | Motion rules cover purpose (UI-23); layout-shifting hover is CD-10 |
| KPI deltas | VZ: every KPI shows a delta; MB: only with a real comparison | Only with a real, named comparison period (IN-02) |
| "At least one real number per feature section" | VZ (M13) | Dropped: it pressures agents to invent numbers. Specificity comes from mechanism and real data |
| Motion maximum of 400 ms | VZ | Starting point for UI feedback; narrative motion at high MOTION may be longer (`motion.md`) |
| Custom cursors | JH bans them | Allowed in CREATIVE_EXPERIENCE when the task still works (UI-01) |
| Storytelling section order | VZ recommends the canonical flow; MB flags the monotonous template | Conventional order is fine when every section has real content (UI-02) |
