# anti-slop-web

**Design direction first. Anti-slop second. Reference knowledge third. Delivery gate last.**

A web-focused design reasoning system for AI coding agents. It helps agents build interfaces that
belong to their product, instead of the statistical average of every template they were trained on.

## The problem

Ask an agent for a landing page and you get the same page every time: indigo gradient, gradient
headline, a pill badge above it, two centered buttons, three identical icon cards, a "Trusted by"
bar of logos nobody supplied, glass navigation, and copy about elevating your workflow. Ask for a
dashboard and you get a sidebar, four stat cards with invented numbers and green deltas, one chart,
and one table, whatever the product does.

The common fix is a ban list. Ban lists go wrong in two ways. They ban good tools that happen to
be popular: Inter, centered heroes, bento grids, dark themes. And they install a new house style:
when every agent swaps Inter for the same "distinctive" font, that font becomes the new tell. They
also push agents toward strangeness, which costs users more than familiarity ever did.

This kit takes a different position:

> **A design technique is not bad because AI frequently uses it. It is bad when it appears
> without a product, content, brand, hierarchy, or usability reason.**
>
> **Do not make an interface strange merely to avoid looking AI-generated. Familiar conventions
> are often good UX. Novelty must have a reason.**

## What it is

- **Design direction.** A project `DESIGN.md`, four design dials, product archetype
  classification, and an optional signature element, settled before code is written.
- **Anti-slop guardrails.** Rule catalogs in one schema (Tell, Why, Default correction,
  Acceptable when, Scope, Severity). Every rule says when the pattern is legitimate, applies only
  to the archetypes where it matters, and can be waived for a recorded reason.
- **Reference knowledge.** Eleven reference files (layouts, typography, color, components,
  navigation, motion, dashboards, charts, tables, forms, design systems). They teach when a pattern
  fits, when it does not, the tradeoffs, accessibility concerns, and the usual AI misuse.
- **Delivery auditing.** Design, accessibility, and responsive audits, plus a compact delivery
  gate that never fails work on taste alone.

## What it is not

- **Not a theme.** It ships no colors, fonts, or components.
- **Not a component library.** Use whatever the project uses.
- **Not an anti-purple, anti-gradient rulebook.** Purple, gradients, glass, bento, dark themes, and
  Inter all pass when there is a reason. The defaults are what get flagged.
- **Not a substitute for real content or user research.** It refuses to invent testimonials,
  logos, and metrics, so someone still has to supply the real ones.

## Order of authority

Higher layers always override lower ones:

1. Product requirements (including the WCAG 2.2 AA floor)
2. Existing brand and project design direction
3. Usability and accessibility judgment
4. Content semantics
5. Anti-slop guardrails
6. Reference patterns
7. Decorative preferences

Accessibility minimums count as product requirements, so a brand decides *how* to meet them, never
*whether*. Above that floor, the brand outranks this kit. If the brand calls for something a rule
would flag, the agent follows the brand and records a waiver.

## How `DESIGN.md` works

`DESIGN.md` sits at the project root and is the source of truth for visual direction. The agent
creates it from [the template](skills/anti-slop-web/templates/DESIGN.md), or updates it if one
exists, and every screen is built against it. It covers product context and archetype, the four
dials with reasons, design intent ("should feel / should not feel"), the signature element,
palette roles, typography, layout, component language, motion, data visualization, required
states, project-specific bans, and **allowed exceptions**.

The allowed exceptions section is what keeps audits from becoming nagging. A decision recorded
there (for example "UI-08 default palette: brand guide v3 specifies indigo as primary") is marked
`WAIVED`, and later audits stop trying to "fix" it. P0 rules and WCAG A/AA failures cannot be
waived. Decisions that already match a rule's "Acceptable when" (a dark theme in a control room)
are recorded as PASS, not waived.

Agent-written direction is marked `Status: proposed` until the owner confirms it. Agents left to
choose a direction tend to fall back on their defaults, so the file says plainly that it is a
proposal.

## The four design dials

Each dial runs from 1 to 10, read in three bands (low 1-3, mid 4-6, high 7-10) so a reviewer can
check the build against what was declared.

| Dial | Measures |
|------|----------|
| **VARIANCE** | How much structural composition departs from strict symmetry and repetition |
| **MOTION** | How much purposeful animation and transition is appropriate |
| **DENSITY** | How much information and control is visible per unit of screen space |
| **CHARACTER** | How distinctive, expressive, branded, or recognizable the visual language should be |

Example settings (illustrations, not defaults):

| Product | VARIANCE | MOTION | DENSITY | CHARACTER |
|---------|---------:|-------:|--------:|----------:|
| Industrial operations dashboard | 3 | 1 | 9 | 5 |
| Luxury editorial | 8 | 4 | 2 | 9 |
| Bank admin console | 2 | 1 | 8 | 3 |
| Developer tool | 4 | 2 | 7 | 6 |

## Archetype classification

Before writing `DESIGN.md`, the agent classifies each surface into a primary archetype, plus an
optional secondary one: `MARKETING`, `APPLICATION`, `DASHBOARD`, `OPERATIONS`, `EDITORIAL`,
`ECOMMERCE`, `DEVELOPER_TOOL`, `CREATIVE_EXPERIENCE`, `DATA_EXPLORATION`.

The archetype sets typical dial ranges, decides which rules weigh heavily or lightly, and selects
references. Marketing-page rules are not applied to an operations console: there, uniform dense
tables, strict symmetry, and dark themes are often right, and forced asymmetry is a defect.
Profiles: [`archetypes.md`](skills/anti-slop-web/archetypes.md).

## Same system, three products

**1. A SaaS marketing page** for an invoicing tool. `MARKETING`, dials around 6 / 4 / 3 / 7.
The agent inventories real content before choosing sections. Rules UI-02 (template skeleton) and
UI-03 (uniform feature cards) apply in full: the flagship feature gets a full-width section with
a real screenshot, and the rest become a list. There is no testimonials section until the owner
supplies real quotes (IN-01), and no "10,000+ teams" figure (IN-02). Expressive type and one
owned signature are expected. Loads `layouts.md`, `typography.md`, `color.md`, `motion.md`, and
the copy skill.

**2. An industrial operations dashboard** for a packaging line. `OPERATIONS` + `DASHBOARD`, dials
3 / 1 / 9 / 5. Uniform dense tables and identical sensor tiles pass, because consistency speeds
up scanning. A dark control-room theme is in scope rather than a tell. Forced asymmetry would
fail UI-01. The rules that bite hardest are color-only status (A11Y-08, raised to P0 here),
indicators that mark nothing (UI-19), unlabeled stale data (FN-02), and destructive controls
without a confirmation (FN-05). The signature is a status language that combines shape, color,
and text. No entrance animations. Loads `dashboards.md`, `tables.md`, and `charts.md`.

**3. A developer tool**: a CLI plus a web console. `DEVELOPER_TOOL` + `APPLICATION`, dials
4 / 2 / 7 / 6. Monospace, a dark theme, a command palette, and dense layouts are legitimate. The
marketing site may use monospace headings (in scope for the archetype, so UI-17 passes), but a fake terminal
animation fails UI-22: it must show a real, runnable command. Performance and security claims
need evidence (IN-03). Loads `navigation.md`, `tables.md`, and `typography.md`.

Filled-in `DESIGN.md` files for all three are in [`examples/`](examples/). They illustrate the
reasoning and are not presets to copy.

## Example workflow

```
You:    Build the pricing page for our scheduling app.

Agent:  Reads DESIGN.md (confirmed; MARKETING secondary for the site; dials 5/3/3/6;
        signature: the week-strip calendar motif). Reads the existing pricing data in
        lib/plans.ts: two paid tiers plus free.
        Loads layouts.md and the copy skill.
        Builds three columns because there are three real tiers. Highlights none, because
        no tier is the most popular by data. Comparison table below for the 14 differences.
        CTA labels: "Start free", "Start 14-day trial", "Talk to sales".
        Audit: UI-25 PASS (tiers from real data); IN-02 PASS (no invented "most popular").
        a11y: comparison table uses th scope; toggle exposes aria-pressed.
        Responsive: comparison table becomes priority columns plus "show all" below 700 px.

        Delivery Gate
        Design direction: PASS (5/3/3/6; week-strip motif in the plan headers)
        Content integrity: PASS (all prices from lib/plans.ts)
        ...
        Final status: SHIP
```

## Installation

### Claude Code plugin

From a clone or a published copy of this repository:

```
/plugin marketplace add YoussefMadkour/anti-slop-web      # or a local path: ./anti-slop-web
/plugin install anti-slop-web@anti-slop-web
```

This installs five skills (`anti-slop-web`, `anti-slop-a11y`, `anti-slop-responsive`,
`anti-slop-copy`, `anti-slop-code`) and the `web-design-architect` agent.

### Install script

```bash
git clone https://github.com/YoussefMadkour/anti-slop-web.git
cd anti-slop-web
./install.sh                        # into ~/.claude
CLAUDE_HOME=./.claude ./install.sh  # or into a project's .claude directory
```

Skills appear in new sessions. Restart Claude Code to dispatch the agent. Optionally paste
[`docs/claude-md-snippet.md`](docs/claude-md-snippet.md) into your project's `CLAUDE.md`.

### Other coding agents

Every skill is a plain `SKILL.md` file with YAML front matter, so any agent that can read files can
use them (Codex, Cursor, Windsurf, Copilot, Gemini CLI, or a raw API call).

1. Vendor the repository into the project, for example at `.agents/anti-slop-web/`.
2. Point the agent's instruction file (`AGENTS.md`, `.cursorrules`, `GEMINI.md`) at
   `skills/anti-slop-web/SKILL.md`, using the snippet in `docs/claude-md-snippet.md`.
3. The master skill tells the agent which other files to read and when. All paths are relative
   to the skill folders.

## Token budget

The master skill is about 1,700 words and loads on every UI task. The other files load only
when needed:

| Layer | Loads when | Size |
|-------|-----------|------|
| `anti-slop-web/SKILL.md` | Every web UI task | about 1,700 words |
| `archetypes.md`, `templates/DESIGN.md` | Setting direction | about 1,200 and 1,100 words |
| Specialist skills | Their concern is in play | about 1,600 to 2,400 words each |
| One to four reference files | The task needs them | about 1,200 to 2,900 words each |
| `rules.md` and audits | Auditing before delivery | about 4,700 words, plus 400 to 700 per audit |

A dashboard task typically loads the master skill, `dashboards.md`, `charts.md`, and `tables.md`.
It does not load the marketing references or the copy skill unless copy is being written.

## Repository structure

```
anti-slop-web/
├── README.md
├── LICENSE
├── NOTICE.md                       upstream attribution and licenses
├── CHANGELOG.md
├── install.sh
├── .claude-plugin/                 plugin.json, marketplace.json
├── skills/
│   ├── anti-slop-web/              master skill (always loaded)
│   │   ├── SKILL.md
│   │   ├── archetypes.md
│   │   ├── rules.md                IN, FN, UI, CL rules
│   │   ├── templates/DESIGN.md
│   │   ├── references/             layouts, typography, color, components, navigation, motion,
│   │   │                           dashboards, charts, tables, forms, design-systems
│   │   └── audits/                 design, accessibility, responsive, delivery gate
│   ├── anti-slop-a11y/             A11Y rules + scripts/contrast.py
│   ├── anti-slop-responsive/       RS rules
│   ├── anti-slop-copy/             CP rules
│   └── anti-slop-code/             CD rules
├── agents/
│   └── web-design-architect.md
├── examples/                       three illustrative DESIGN.md files
└── docs/
    ├── source-map.md               which idea came from which upstream project
    ├── not-carried-over.md         upstream rules deliberately dropped, with reasons
    └── claude-md-snippet.md
```

The shared `references/`, `audits/`, and `templates/` folders live inside the master skill
rather than at the repository root. A skill folder copied on its own (by `install.sh` or by a
plugin manager) then keeps every relative link intact, and the specialist skills reach them as
siblings (`../anti-slop-web/...`).

## Rule catalogs at a glance

| Prefix | Lives in | Covers |
|--------|----------|--------|
| IN | `anti-slop-web/rules.md` | Integrity: fabricated proof, metrics, claims, disguised placeholders |
| FN | `anti-slop-web/rules.md` | Function: dead controls, missing states, form feedback, destructive actions, theme parity |
| UI | `anti-slop-web/rules.md` | Visual and composition tells, each scoped by archetype |
| CL | `anti-slop-web/rules.md` | Cluster escalation |
| A11Y | `anti-slop-a11y/SKILL.md` | WCAG 2.2 AA-oriented accessibility rules |
| RS | `anti-slop-responsive/SKILL.md` | Responsive, touch, zoom, and reflow |
| CP | `anti-slop-copy/SKILL.md` | Copy and microcopy |
| CD | `anti-slop-code/SKILL.md` | Implementation habits of AI agents building UI |

Severity: **P0** blocks shipping and cannot be waived (truthfulness, function, accessibility).
**HIGH** must be fixed or waived with a reason. **MEDIUM** is fixed when cheap. **LOW** is a note.
Any WCAG 2.2 A/AA failure blocks shipping whatever its label. Taste alone never fails delivery.

## Attribution

anti-slop-web consolidates and rewrites ideas from three MIT-licensed projects:
[jhuse25/anti-slop-design-skills](https://github.com/jhuse25/anti-slop-design-skills) (workflow,
`DESIGN.md`, dials, signature element),
[miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) (filter philosophy,
purpose-gated rules, delivery gate, specialist concerns), and
[Vanszs/Anti-AI-UI](https://github.com/Vanszs/Anti-AI-UI) (reference library, severity scale).
See [NOTICE.md](NOTICE.md) for licenses, [docs/source-map.md](docs/source-map.md) for what came
from where, and [docs/not-carried-over.md](docs/not-carried-over.md) for what was left out and why.

## License

MIT. See [LICENSE](LICENSE). Upstream notices are in [NOTICE.md](NOTICE.md).
