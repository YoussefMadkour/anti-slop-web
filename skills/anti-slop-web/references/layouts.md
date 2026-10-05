# Layouts

Page and app skeletons, composition patterns, and the CSS that makes them reflow. Load this
file when a task involves page structure, section composition, or an app shell. Everything
here is context, not a mandate: the brand, `DESIGN.md`, and the content override any pattern
below. Pick a layout because the content needs it, then check it against the VARIANCE dial.

Related: `navigation.md` (shells and menus), `dashboards.md` (widget grids), `typography.md`
(measure), responsive rules in `anti-slop-responsive`.

---

## Single column with a reading measure

**What:** One centered column constrained to a comfortable line length, with optional
breakout elements.
**Use when:**
- Prose dominates: articles, docs pages, changelogs, legal text, focused forms.
- The page has one job and one reading path.
**Avoid when:**
- Content is genuinely comparative or two-dimensional (tables, side-by-side plans).
- Wide screens leave the column feeling lost and nothing else belongs beside it (consider a sticky aside).
**Archetypes:** EDITORIAL, MARKETING (long-form), APPLICATION (settings, forms), DEVELOPER_TOOL (docs).
**Tradeoffs:**
- Excellent readability and simple responsive behavior.
- Low VARIANCE by nature; variety must come from type, imagery, and breakouts.
**Accessibility:**
- Keep the measure in `ch` or `rem` so it scales with zoom (RS-11).
- Center the column, not the paragraphs: left-aligned body text scans faster.
**Common AI misuse:** Full-width paragraphs on a 1440px canvas, or a centered column of
centered text for every section (UI-05).

```css
.prose { max-inline-size: 68ch; margin-inline: auto; padding-inline: 1rem; }
```

## Full-bleed and breakout grid

**What:** A three-track grid where content sits in the middle track and selected elements
span wider or edge to edge.
**Use when:**
- Long-form pages need occasional wide figures, maps, quotes, or color bands.
- You want rhythm breaks without changing the reading column.
**Avoid when:**
- Every element breaks out; the reading column disappears.
**Archetypes:** EDITORIAL, MARKETING, CREATIVE_EXPERIENCE.
**Tradeoffs:**
- Strong rhythm with one grid; slightly more CSS than a plain column.
**Accessibility:**
- Wide images still need alt text and captions (A11Y-15).
- Edge-to-edge text over images needs a contrast check on the worst area (A11Y-04).
**Common AI misuse:** A full-bleed gradient band between every section as the only variation (UI-05).

```css
.page {
  display: grid;
  grid-template-columns: 1fr min(68ch, 100% - 2rem) 1fr;
}
.page > * { grid-column: 2; }
.page > .wide { grid-column: 1 / -1; max-inline-size: 72rem; justify-self: center; width: 100%; }
.page > .bleed { grid-column: 1 / -1; }
```

## Split hero (text beside a visual)

**What:** Headline, supporting copy, and one primary action on one side; a real product
visual on the other. Ratios like 1.2fr / 1fr or 3fr / 2fr.
**Use when:**
- The product has something real to show: a screenshot, a photo, a demo, live data.
- The audience needs to read the claim and see the evidence together.
**Avoid when:**
- There is nothing real to show. A costume visual is worse than none (UI-22).
- The headline is long and needs the full width.
**Archetypes:** MARKETING, ECOMMERCE, DEVELOPER_TOOL (code beside copy).
**Tradeoffs:**
- Familiar and effective; also very common, so identity must come from content, type, and color.
- On small screens decide deliberately whether the visual goes first or second.
**Accessibility:**
- Source order should match reading order; reorder visually only with care (A11Y-19).
- The visual needs an alt text that states what it shows, not "dashboard screenshot".
**Common AI misuse:** Perspective-tilted fake dashboard with glow on the right side (UI-22),
two equal buttons under the copy (UI-06).

## Centered hero

**What:** Centered headline and action, often with a product shot or demo below.
**Use when:**
- The message is short and singular; the product shot below provides evidence.
- The brand system uses centered composition, or a symmetric layout fits low VARIANCE.
- Launch or announcement pages where one sentence carries the page.
**Avoid when:**
- It is chosen only because it is the default and nothing below it has real content (UI-02).
- Multi-line body copy would end up centered.
**Archetypes:** MARKETING, CREATIVE_EXPERIENCE, EDITORIAL (cover pages).
**Tradeoffs:**
- Calm and confident; easily reads as template when combined with eyebrow pill, two buttons,
  and gradient text (CL-01).
**Accessibility:**
- Same contrast checks if placed over imagery.
**Common AI misuse:** The full cluster: eyebrow badge, gradient headline, two equal CTAs,
aurora blobs (UI-18, UI-08, CL-01). The centered hero itself is not the problem.

## Card grid (auto-fill)

**What:** A responsive grid of same-type items that reflows by available width, no breakpoints needed.
**Use when:**
- Items are genuinely equivalent: products, templates, integrations, team members, articles.
- Users compare or browse many items.
**Avoid when:**
- Items differ in importance (UI-03). Rank them instead.
- Only three items exist and a list or prose would read better.
**Archetypes:** ECOMMERCE, APPLICATION, DASHBOARD, EDITORIAL (indexes), DEVELOPER_TOOL (template galleries).
**Tradeoffs:**
- Scannable and robust; uniformity is the point, so it reads flat when used for persuasion.
**Accessibility:**
- Use a list (`<ul>`) for collections; make the card heading the link and expand its hit area
  rather than wrapping the whole card in nested interactive elements (A11Y-01).
**Common AI misuse:** Three icon cards with a title and blurb for features of unequal weight (UI-03).

```css
.grid { display: grid; gap: 1.5rem; grid-template-columns: repeat(auto-fill, minmax(min(18rem, 100%), 1fr)); }
```

The `min(18rem, 100%)` keeps a single column from overflowing on narrow screens (RS-01).

## Subgrid for aligned card internals

**What:** Cards in a row share row tracks so titles, bodies, and actions align across cards.
**Use when:**
- Comparison grids (plans, products) where misaligned prices or buttons hurt scanning.
**Avoid when:**
- Content is too variable to benefit, or cards stack on mobile anyway.
**Archetypes:** ECOMMERCE, MARKETING (pricing), APPLICATION.
**Tradeoffs:** Supported in all evergreen browsers; adds a little layout complexity.
**Accessibility:** No impact beyond normal card semantics.
**Common AI misuse:** Padding every card's text to equal length to fake alignment (UI-25).

```css
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr)); gap: 1.5rem; }
.card { display: grid; grid-row: span 3; grid-template-rows: subgrid; gap: 0.75rem; }
```

## Bento grid

**What:** A mosaic of cells of different sizes, usually with one dominant cell.
**Use when:**
- Content units genuinely differ in importance.
- Different media or data types benefit from different footprints (a video, a live number,
  a code sample, a quote).
- Visual hierarchy across a small set of items is useful (an overview screen, a launch page).
**Avoid when:**
- All units are equivalent: use a uniform grid or a list.
- The interface is dense and scanning consistency matters (OPERATIONS, most tables of widgets).
- The mosaic exists to look modern and the sizes are arbitrary.
**Archetypes:** MARKETING, DASHBOARD (overview), CREATIVE_EXPERIENCE. Rarely OPERATIONS.
**Tradeoffs:**
- High visual interest; sizes imply importance, so arbitrary sizes communicate false hierarchy.
- Needs a deliberate small-screen reading order.
**Accessibility:**
- DOM order must be the reading order; avoid `grid-auto-flow: dense` when it reorders
  content away from the source order (A11Y-19).
**Common AI misuse:** Using a bento grid simply because the model wants the page to look modern,
with the same icon, title, and blurb in every cell (UI-04).

## Masonry

**What:** Columns of variable-height items packed without row alignment.
**Use when:**
- Image galleries, mood boards, collections of quotes or notes with varied heights.
**Avoid when:**
- Order matters (chronology, ranking): masonry scrambles the reading sequence.
- Items need side-by-side comparison.
**Archetypes:** CREATIVE_EXPERIENCE, EDITORIAL, ECOMMERCE (lookbooks).
**Tradeoffs:**
- CSS `columns` works everywhere but orders top to bottom per column; native grid masonry is
  still progressive enhancement.
**Accessibility:**
- Column order changes tab order relative to visual rows; test keyboard paths (A11Y-02).
**Common AI misuse:** Masonry for testimonials that were invented (IN-01).

## Magazine and editorial index grid

**What:** One featured item spanning more space, with secondary items around it.
**Use when:**
- News, blogs, and content homes where editors set priority.
**Avoid when:**
- There is no real editorial priority; the "featured" item is arbitrary.
**Archetypes:** EDITORIAL, ECOMMERCE (campaigns), MARKETING (resource hubs).
**Tradeoffs:** Communicates priority well; requires curation to stay honest.
**Accessibility:** Headings per item, consistent link targets, captions on images.
**Common AI misuse:** Featured slot filled by whatever item came first in the data.

## Asymmetric splits

**What:** Unequal column ratios (60/40, 70/30) and offset alignment to create rhythm.
**Use when:**
- VARIANCE is mid to high and sections have different jobs.
- One side is clearly primary (prose) and the other supporting (figure, aside).
**Avoid when:**
- VARIANCE is low, or the product is dense and scanning consistency matters (UI-01).
- Asymmetry is added to meet a quota. There is no required number of asymmetric moments.
**Archetypes:** MARKETING, EDITORIAL, CREATIVE_EXPERIENCE.
**Tradeoffs:** Adds energy; alternating left/right forever becomes its own monotony.
**Accessibility:** Keep source order logical when visually swapping sides.
**Common AI misuse:** Endless image-left, text-right alternation as the only structural idea (UI-05).

## Scroll-sticky feature section

**What:** A visual pinned on one side while explanatory steps scroll on the other.
**Use when:**
- A sequence of features maps onto one evolving visual (a product UI changing state).
**Avoid when:**
- The visual does not change meaningfully per step.
- MOTION is low and the effect becomes the only motion on the page.
**Archetypes:** MARKETING, DEVELOPER_TOOL, CREATIVE_EXPERIENCE.
**Tradeoffs:** Engaging on desktop; on small screens show the visual inline per step instead.
**Accessibility:**
- Each step's visual must be available without scrolling tricks; inline images on mobile and
  for reduced motion (A11Y-10).
**Common AI misuse:** Pinning a static image while text scrolls past, adding length without information.

## Sidebar app shell

**What:** Persistent navigation sidebar beside a scrolling content area, often with a top bar.
**Use when:**
- An application has several top-level sections that users switch between often.
- Navigation depth is 5 to 20 items, possibly grouped.
**Avoid when:**
- The product has two or three sections (a top nav is lighter).
- Marketing sites that are not applications.
**Archetypes:** APPLICATION, DASHBOARD, OPERATIONS, DEVELOPER_TOOL, DATA_EXPLORATION.
**Tradeoffs:**
- Strong, well-understood convention. The shell is rarely the problem; what fills it is (UI-07).
- Costs horizontal space; plan a rail or drawer for narrower widths (RS-05).
**Accessibility:**
- `<nav aria-label>` landmark, `aria-current="page"` on the active item (A11Y-14, A11Y-17).
- Independent scroll regions must be keyboard scrollable.
**Common AI misuse:** Sidebar, four stat cards, chart, and table before anyone named the screen's job (UI-07).

```css
.shell { display: grid; grid-template-columns: 16rem 1fr; grid-template-rows: 3.5rem 1fr; block-size: 100dvh; }
.shell > aside { grid-row: 1 / -1; overflow-y: auto; }
.shell > main { overflow-y: auto; }
```

## Docs three-column (holy grail)

**What:** Navigation tree, content, and an "on this page" table of contents.
**Use when:**
- Documentation, knowledge bases, specifications with long pages.
**Avoid when:**
- Pages are short; the TOC duplicates two headings.
**Archetypes:** DEVELOPER_TOOL, EDITORIAL, APPLICATION (help centers).
**Tradeoffs:** Very efficient on wide screens; the TOC column usually disappears first as width shrinks.
**Accessibility:**
- Two navigation landmarks need distinct labels ("Documentation", "On this page").
- A skip link to content helps keyboard users past a long tree (see `navigation.md`).
**Common AI misuse:** Three columns on a marketing page with nothing to navigate.

## Sticky aside

**What:** A secondary column (TOC, summary, buy box, filters) that sticks while main content scrolls.
**Use when:**
- The aside stays relevant throughout scrolling: checkout summary, product buy box, article TOC.
**Avoid when:**
- The aside is taller than the viewport and becomes unreachable (RS-02).
**Archetypes:** ECOMMERCE, EDITORIAL, DEVELOPER_TOOL, APPLICATION.
**Tradeoffs:** Keeps context visible; needs a max height with its own scroll.
**Accessibility:** Content in the aside must remain reachable at 200% zoom (RS-11).
**Common AI misuse:** Sticky elements stacked until they cover half the screen on small viewports (RS-14).

## Z and F scanning patterns

**What:** Eye-tracking descriptions of how people scan sparse pages (Z) and text-heavy pages (F).
**Use when:**
- As a diagnostic: is the key information where scanning naturally lands (top-left,
  left-aligned headings, front-loaded words)?
**Avoid when:**
- Treated as a layout recipe. They describe behavior on weakly structured pages; strong
  hierarchy changes how people scan.
**Archetypes:** MARKETING (Z), EDITORIAL and DATA_EXPLORATION (F).
**Tradeoffs:** Useful heuristics, not laws.
**Accessibility:** Front-loaded headings and link text also help screen-reader users who scan by headings and links.
**Common AI misuse:** Citing the F-pattern to justify a template.

---

## Section rhythm and variety

Variety between sections is a VARIANCE decision, not a quota. Options, roughly in order of
how much they change:

| Lever | Low VARIANCE (1-3) | Mid (4-6) | High (7-10) |
|-------|--------------------|-----------|-------------|
| Section anatomy | Repeated deliberately | Varies by section job | Varies strongly, composed per section |
| Container width | One or two widths | Prose, standard, wide | Freely mixed including bleeds |
| Vertical spacing | Consistent scale steps | Larger steps around key sections | Dramatic contrast |
| Alignment | Shared axis | Mostly shared, some offsets | Offset and asymmetric |
| Rhythm breaks | Rare | Every few sections when content provides one | Frequent, content-driven |

Useful heuristics, all optional:
- Let each section's job pick its anatomy: proof wants a quote or case, comparison wants a
  table, process wants a sequence, a single capability wants a demo.
- One dominant element per section makes hierarchy obvious (UI-06).
- Tighter spacing inside a group than between groups (UI-15).
- A rhythm break (full-bleed image, data band, large quote) helps only if it carries content.

Low VARIANCE with uniform sections is a valid decision for docs, changelogs, and
institutional sites. Record it in `DESIGN.md` so audits do not flag it (UI-05).

## Intrinsic layout primitives

Compose layouts that adapt without many media queries.

| Primitive | Purpose | Core idea |
|-----------|---------|-----------|
| Stack | Vertical spacing between siblings | `display: flex; flex-direction: column; gap: var(--space)` |
| Cluster | Wrapping inline groups (tags, actions) | `display: flex; flex-wrap: wrap; gap: var(--space)` |
| Center | Constrained, centered measure | `max-inline-size: var(--measure); margin-inline: auto` |
| Sidebar | Main plus narrow aside that wraps when cramped | container `display: flex; flex-wrap: wrap`; aside `flex-basis: 16rem; flex-grow: 1`; main `flex-basis: 0; flex-grow: 999; min-inline-size: 50%` |
| Switcher | Row of items that becomes a column below a threshold | `flex-basis: calc((var(--threshold) - 100%) * 999)` |
| Grid | Auto-fill responsive grid | `repeat(auto-fill, minmax(min(var(--min), 100%), 1fr))` |
| Frame | Media at a fixed aspect ratio | `aspect-ratio: 16 / 9; object-fit: cover` |
| Reel | Horizontal scrolling strip | `display: flex; overflow-x: auto` with scroll snap |

A reel is intentional horizontal scroll inside a region; it must not cause the page itself to
scroll sideways (RS-01) and needs visible affordance plus keyboard access (A11Y-02).

## Container queries

**What:** Components respond to the width of their container instead of the viewport.
**Use when:**
- The same component lives in a sidebar, a main column, and a modal.
- Dashboards where widget width depends on the grid, not the screen.
**Avoid when:**
- Page-level layout that genuinely depends on the viewport.
**Archetypes:** APPLICATION, DASHBOARD, ECOMMERCE, DATA_EXPLORATION.
**Tradeoffs:** Supported in evergreen browsers; requires declaring containment on the parent.
**Accessibility:** Combined with rem-based thresholds, components reflow correctly under zoom (RS-11).
**Common AI misuse:** Device-width media queries inside components that move between slots (RS-15).

```css
.widget-slot { container-type: inline-size; }
@container (min-width: 32rem) {
  .widget { display: grid; grid-template-columns: 2fr 3fr; }
}
```

## Breakpoints

Place breakpoints where the content breaks: a line gets too long, a card too narrow, a
table unreadable. Then test at common widths (roughly 320, 375, 768, 1024, 1280, 1440 and
the gaps between). Device lists are test points, not design inputs (RS-15). Plan at least one
intermediate state between phone and desktop when the content needs it (RS-05). Express
breakpoints in `em` or `rem` so they respond to user font size.

## Viewport height units

**What:** `svh` (small: browser UI shown), `lvh` (large: UI hidden), `dvh` (dynamic, updates).
**Use when:**
- An app shell or a deliberately full-screen section needs to fit the visible viewport on mobile.
**Avoid when:**
- Sections that should size to their content; most sections should.
**Archetypes:** APPLICATION (shells), CREATIVE_EXPERIENCE, MARKETING (an intentional full-height hero).
**Tradeoffs:**
- `100vh` on mobile includes hidden browser chrome and overflows (RS-14).
- `dvh` can cause layout changes while the browser UI animates; `svh` is stable for above-the-fold content.
**Accessibility:** Full-height sections must not trap content below the fold at zoom (RS-11).
**Common AI misuse:** `h-screen` on every hero with only a headline in it.

```css
.hero { min-block-size: 100vh; min-block-size: 100svh; }
.app  { block-size: 100vh; block-size: 100dvh; }
```
