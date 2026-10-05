# Not Carried Over

Upstream rules and features deliberately left out of anti-slop-web, with reasons. Most were
dropped because they were absolute where context should decide, because they would create a new
house style, or because they belong to a different medium.

Legend: **JH** = jhuse25/anti-slop-design-skills, **MB** = miqdadbadjuber/anti-slop,
**VZ** = Vanszs/Anti-AI-UI.

## Absolute aesthetic bans

| Upstream rule | Source | Why not carried |
|---------------|--------|-----------------|
| Ban Inter in premium or creative contexts; use Geist, Outfit, Cabinet Grotesk, or Satoshi | JH | Bans a strong, well-made face and swaps in a new default roster. Typeface needs a reason, not a blacklist |
| Display font must not be Inter or Geist | VZ | Same reason; dense applications often want exactly these faces |
| Never pure `#000000` | JH | A tradeoff (halation, OLED, brand), not a defect |
| Accent saturation below 80 percent; one accent maximum | JH | Many brands are legitimately saturated or multi-color; color roles (UI-11) carry the useful part |
| No serif in dashboards or software UI | JH | Editorial dashboards and some brands use serifs well |
| No custom cursors | JH | Legitimate in creative experiences |
| No floating labels | JH | Guidance in `forms.md` instead; a floating label that stays visible is acceptable |
| Never a circular spinner | JH | Spinners suit short or unknown-shape waits |
| Spring physics by default, no linear easing | JH | Becomes a new default motion signature; easing should follow purpose |
| VARIANCE above 4 bans centered heroes | JH | Mechanical coupling; a centered hero can be right at any VARIANCE |
| DENSITY above 7 bans cards and forces monospace numbers | JH | Tabular figures solve the alignment problem; cards can be right in dense UIs |
| Purple or indigo accent and gradient text are P0 | VZ | Taste is never P0 here; default purple is HIGH, brand purple passes |
| Left-border accents are P0, including active nav | VZ | Left-edge indicators are a legitimate state encoding |
| Em dash forbidden in any text (hard gate) | MB | Punctuation is not a product failure; demoted to a LOW cluster signal |
| Bento grids, three pricing columns, logo bars, four-column footers forbidden as layouts | MB | Content decides; these are flagged only when unjustified |
| `hover:scale-105` is HIGH | VZ | Covered by purpose (UI-23) and layout shift (CD-10) |
| Glassmorphism banned on cards, uniform glass banned, dose cap of 1 to 2 elements | VZ, MB | Kept as reasoning in UI-09 rather than numeric caps |

## Mandatory quotas and formulas

| Upstream rule | Source | Why not carried |
|---------------|--------|-----------------|
| At least 2 deliberate asymmetric moments per page | VZ | A quota forces asymmetry where consistency serves users; VARIANCE expresses intent instead |
| Always use 60-30-10 | VZ | Kept as a heuristic in `color.md` |
| Always use an 8 px spacing system | VZ | One valid option among several scales |
| Distinctive display font required | VZ | Low-CHARACTER products should not be forced into display type |
| Max 3 weights, max 2 families | VZ | Reasonable defaults, kept as guidance |
| Vary section padding with prescribed values (hero py-32, features py-16) | VZ | Prescribes a look; rhythm guidance kept in `layouts.md` |
| Never repeat the same section anatomy consecutively; break rhythm every 2 to 3 sections | VZ | Marketing heuristics that are wrong for applications; tied to VARIANCE now |
| At least one real number per feature section | VZ | Pressures agents to invent numbers |
| Every KPI shows a delta and comparison | VZ | Encourages invented deltas; deltas only with real comparisons |
| Round KPIs aggressively (12.4K) | VZ | Operations and finance often need exact values; depends on the task |
| Never exceed 400 ms; animate at most 30 percent of elements | VZ | Useful starting points, not limits; kept as guidance |
| Build a light/dark toggle whenever there is no reason for a fixed theme | MB | Scope creep for many tasks; recommend following the system preference when feasible |
| Required liveliness: identity motif, one accent, focal point on every screen | MB | Folded into the optional signature element and hierarchy rules; forcing liveliness on a bank console is wrong |
| Signature element mandatory | JH | Made optional; restraint is often correct |

## Recommended stand-ins that create a new default

| Upstream recommendation | Source | Why not carried |
|-------------------------|--------|-----------------|
| "Creative arsenal": magnetic buttons, spotlight-border cards, kinetic type, bento 2.0, sticky scroll stacks | JH | A catalog of effects is exactly what the signature element rule warns against |
| `picsum.photos` random images as placeholders | JH | Random photos disguise missing content; labeled placeholders instead |
| Realistic contextual names and "organic" numbers like 47.2% | JH | Makes fabricated data more convincing; contradicts IN-02 and IN-04 |
| Specific premium font lists and pairings as defaults | JH, VZ | Kept only as labeled illustrations in `typography.md`, if at all |
| Hard-coded project values (a teal brand color, Indonesian copy, one school product) | VZ | Project-specific; would leak one product's identity into every project |
| Linear, Vercel, Stripe page skeletons as templates | VZ | Learning their conventions is fine; copying their skeletons is UI-26 |

## Process and tooling

| Upstream feature | Source | Why not carried |
|------------------|--------|-----------------|
| First-run install wizard, settings file for "during/after" mode, mandatory mode announcements | MB | Process overhead that every session pays; build and review modes are simpler |
| "Draft without direction" with forced ENERGY 1 / RHYTHM 1 / MOTION 1 dials | MB | Replaced with a proposed `DESIGN.md` derived from inspection plus one decisive question |
| Audit files written to `anti-slop/audit-NNN-date.md` | MB | Left to the user; findings are reported in the conversation by default |
| Multi-agent plugin doors (Codex, Cursor, Kimi, Cline, Pi, OMP), npx installer, MCP contrast server | MB | Out of scope for a first release; plain `SKILL.md` files work in any agent |
| `ui-ux-pro-max` CSV databases and BM25 search scripts | VZ (third-party, NextLevelBuilder) | Third-party material with its own provenance; its style database recommends patterns this kit treats as context-dependent (for example "if data heavy, add glassmorphism") |
| Decks and documents skills, presentation and document agents | JH | This kit is web-focused |
| Generic engineering items: tests for every feature, i18n extraction, ESLint configs, folder structure, TypeScript strictness | VZ | Not specific to AI-built UI; the project's own standards govern these |
| Magic numbers, barrel exports, project structure tells | VZ | General code quality; only z-index, `!important`, and specificity spam kept (CD-15) |
| Kiro steering format and "Creative Freedom" footer on every file | VZ | Format-specific; the authority order already says references are not ceilings |
| Model-switching advice ("use your most design-capable model for direction") | JH | Tool- and vendor-specific |
