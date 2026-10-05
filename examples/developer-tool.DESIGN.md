# Product Design Direction

<!-- Fictional example. Illustrates reasoning; do not copy values as a preset. -->

Status: confirmed
Owner: Tracewell (fictional) design and developer relations
Last updated: 2026-07-18
Sources inspected: Existing CLI output styles, docs site, console prototype, brand mark (a single
vertical bar glyph), user interviews with on-call engineers.

## 1. Product context

Product: Tracewell (fictional), a request tracing tool: an SDK, a CLI, and a web console that
shows how a request moved through services and where time was spent.
Audience: Backend and platform engineers, often on call, often reading traces during an incident.
Primary tasks: Find the slow or failing span in a trace; compare a trace with a healthy baseline;
copy IDs and commands into a terminal.
Environment: Laptops and large monitors, often late at night, alongside a terminal and an editor.
Device priority: Desktop first; console read-only on tablets; marketing site fully responsive.
Archetype: DEVELOPER_TOOL (+ APPLICATION for the console; the marketing site is MARKETING +
DEVELOPER_TOOL)

## 2. Design dials

VARIANCE: 4 | The console is consistent; the marketing site varies sections to show different
artifacts (code, trace, CLI).
MOTION: 2 | Motion only for expanding spans and panel transitions that preserve context.
DENSITY: 7 | Traces have hundreds of spans; engineers want them visible with timings.
CHARACTER: 6 | Developers recognize the tool from its trace view in screenshots and docs; the rest
stays quiet.

## 3. Design intent

The interface should feel:
- Fast and precise, like a good profiler
- Honest about timings and sampling
- At home next to a terminal and editor

The interface should NOT feel:
- Like a generic AI startup page with glowing gradients
- Decorative or cute
- Slow to get to the data

## 4. Signature element

Signature: The waterfall bar: each span drawn as a thin bar on a shared time axis, with the
critical path in the brand amber and everything else in gray. It is the real trace rendering,
used as the hero image on the marketing site (from a real public demo service), in the docs, and in
the console.
Layer: data
Why it belongs to this product: It is the product's core output; the critical-path highlight is
what the tool computes that others do not show by default.
Sustained in: console trace view, docs diagrams, marketing hero, CLI output (ASCII version in the
same amber), status page.

## 5. Palette

Primary: Path amber #E8A33D | critical path, primary actions, focus ring
Neutral: cool grays from #0E1013 (page, dark) to #F3F4F6 (page, light)
Accent: none beyond amber
Semantic colors: error #F2665C, warning #E8C34A, success #5CC08A | span status only
Data colors: spans gray #5B6470 by default; services colored only when the user enables "color by
service" (Okabe-Ito based categorical set)
Theme behavior: follows system preference; dark is the default when no preference is set because
most usage is alongside dark terminals
Contrast verified: text #E5E7EB on #0E1013 15.38:1; amber #E8A33D on #0E1013 8.83:1; amber on light
#F3F4F6 requires darker #9A6110 for text (4.66:1) (computed with contrast.py)

## 6. Typography

Display: Inter Tight semibold | compact for dense headings; chosen for numeric clarity
Body: Inter | familiar to the audience, excellent at small sizes
Mono: JetBrains Mono | IDs, durations, code, CLI examples, and marketing section headings
Hierarchy: 1.2 scale from 14px in the console; 1.25 from 16px on the marketing site
Measure: 70ch for docs prose
Numerals: tabular figures for all durations
Loading: self-hosted, variable fonts, subsets

## 7. Layout principles

App shell: console uses sidebar (projects, services, saved searches) plus a top bar with search
Grid: console is panel-based (trace list, waterfall, span detail); marketing site 12 columns
Content widths: docs 70ch with sticky table of contents; console full width
Density strategy: compact rows, collapsible span groups, detail in a side panel
Navigation: command palette (Cmd or Ctrl K) for traces, services, and actions
Responsive collapse: console panels become a single panel with back navigation below 900px;
waterfall scrolls horizontally inside a focusable region

## 8. Component language

Radius: 4px controls, 6px panels
Borders: 1px gray; panels separated by borders and surface tone
Shadows: menus, popovers, and the command palette only
Cards: docs examples only
Inputs: search with query syntax highlighting; labels above in forms
Tables: trace list with sortable duration, status, service, and timestamp columns
Buttons: primary amber, secondary outlined, icon-only buttons with names
Menus: keyboard navigable, shortcuts shown
Modals: command palette and destructive confirmations (delete saved search)
Component library: Radix Primitives re-tokenized

## 9. Motion

Purpose: preserve context when expanding spans and switching panels
Timing: 150ms ease-out
Allowed animation: span group expand and collapse; side panel slide
Ambient animation: none
Reduced-motion behavior: instant expand and panel swap
Implementation tier: CSS

## 10. Data visualization

Chart language: waterfall (signature), latency histograms, percentile lines
Color encoding: critical path amber, other spans gray, errors red with an error icon
Labels: durations on spans wider than 40px; otherwise in detail panel and accessible table
Tooltips: span name, service, duration, start offset; never the only access
Comparison: baseline trace overlay as a dashed outline
Uncertainty: sampled traces labeled with sampling rate; histograms state sample size
Provenance: trace ID, ingestion time, and SDK version on every trace

## 11. Required states

Loading: trace list skeleton matching row height; waterfall shows a labeled progress bar for large
traces
Empty: first project shows install steps with the real SDK snippet; search with no results shows
the query and suggests widening the time range
Error: ingestion errors show the failing SDK version and a docs link
Partial data: missing spans marked "Span not received (possible sampling or dropped data)"
Offline: console shows last loaded data with a banner
Permission denied: project hidden; direct links explain how to request access
Success: copy buttons confirm "Copied" via a live region
Disabled: actions explain why in a tooltip and in text

## 12. Explicit project bans

- No fake terminal windows with typed animations on the marketing site; CLI examples are real
  commands with real output, copyable (UI-22).
- No performance claims ("10x faster") without a published, reproducible benchmark (IN-03).
- No customer logos until approved ones are supplied (IN-01).

## 13. Allowed exceptions

- UI-08 Default AI palette: WAIVED for the docs syntax theme only. Code samples in the docs use
  the editor theme most of our users already run, which includes violet keywords; the rest of
  the palette is amber and grays. Recorded by design lead, 2026-07-18.
- UI-17 Typographic costume: PASS, no waiver needed. Monospace marketing headings are in scope
  for DEVELOPER_TOOL; they mirror the CLI and trace output that are the product's identity.
- UI-12 Unearned dark theme: no waiver needed. Dark default is in scope for DEVELOPER_TOOL and the
  system preference is respected.
