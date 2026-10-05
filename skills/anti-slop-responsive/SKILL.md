---
name: anti-slop-responsive
description: "Responsive and mobile specialist for web UI built or reviewed by AI agents: mobile-first behavior, reflow, horizontal overflow, typography scaling, touch targets, tables and charts on small screens, navigation collapse, dense applications across widths, viewport-unit traps, and state preservation across breakpoints. Load with anti-slop-web for any layout work."
license: MIT
---

# Anti-Slop Responsive

A small-screen layout is a different layout, not the desktop layout at a smaller size. AI agents
tend to design one wide state, then add a media query that stacks everything below one
breakpoint. The result overflows, hides content, keeps desktop-scale spacing, and breaks the
middle widths nobody checked.

The rules below use the kit schema and apply to every archetype unless noted. Run the procedure
in `../anti-slop-web/audits/responsive-audit.md`.

## Principles

- **Mobile-first by default, priority-first always.** Start from the narrowest supported width
  and add layout as space allows. For dense desktop-first tools (OPERATIONS, DATA_EXPLORATION),
  decide what the small-screen version is for: often a focused subset (monitor, approve, look up)
  rather than every desktop control.
- **Breakpoints follow content.** Place a breakpoint where the content stops working (a column
  becomes unreadably narrow, a row of controls wraps badly), not at a device width. Then test at
  common widths (320, 375, 768, 1024, 1280, 1440+) and by dragging through the whole range.
- **Intrinsic before explicit.** `minmax()`, `auto-fit`, `flex-wrap`, `clamp()`, and container
  queries handle most reflow without breakpoints. See `../anti-slop-web/references/layouts.md`.
- **Responsive includes zoom.** A layout that works at 320 CSS px also works for desktop users
  zoomed to 400 percent (WCAG 1.4.10).

---

### RS-01: Horizontal overflow
**Tell:** The page scrolls sideways at 320 px or at any width in between: a fixed-width element,
a long URL or token, an unwrapped code block, a wide table or image, negative margins, `100vw`
elements next to a vertical scrollbar.
**Why:** Users cannot see the edge of the page, content is cut off, and every vertical swipe drifts.
**Default correction:** Find the widest element (`document.documentElement.scrollWidth` versus
`clientWidth`, or outline everything in dev tools). Contain it: `max-width: 100%` on media,
`overflow-wrap: anywhere` for long strings, `min-width: 0` on grid and flex children, scroll
containers for code and tables.
**Acceptable when:** Deliberate horizontal scroll inside a labeled container (a carousel, a code
block, a wide table region). The page itself never scrolls sideways.
**Severity:** P0 when the page scrolls horizontally or content is cut off at supported widths.
MEDIUM for a few pixels of stray overflow with no lost content.

### RS-02: Content unreachable on small screens
**Tell:** Information or actions hidden with `display: none` below a breakpoint with no
alternative; `overflow: hidden` clipping text or controls; sticky elements covering content;
"desktop only" features that are also needed on mobile.
**Why:** Users on phones lose the information or cannot complete the task.
**Default correction:** Move, collapse, or progressively disclose content instead of deleting it.
If a feature genuinely cannot work on small screens, say so and offer the nearest alternative.
**Acceptable when:** Decorative elements removed on small screens. A documented, deliberate
scope decision (in `DESIGN.md` §7) that a workflow is desktop-only, with a clear message.
**Severity:** P0.

### RS-03: Broken touch or mobile interaction
**Tell:** Hover-only menus, reveals, and tooltips; drag-only interactions; a navigation that cannot
be opened or closed on touch; the on-screen keyboard covering the focused input; fixed bottom bars
covering the last items or the submit button; double-tap zoom required to hit a control.
**Why:** The interaction does not exist for touch users, or the task cannot be completed.
**Default correction:** Every hover interaction gets a tap equivalent; every drag gets a button or
menu alternative. Scroll focused inputs into view and reserve space for fixed bars with
`scroll-padding` and safe-area insets. Test with touch emulation and, where possible, a real device.
**Acceptable when:** Never for primary tasks.
**Severity:** P0.

### RS-04: Squeezed desktop
**Tell:** The narrow layout is the desktop layout shrunk: multi-column rows that never stack,
sidebars that stay open and crush the content, desktop navigation rows that wrap into two lines.
**Why:** Nothing was designed for the small state; everything is cramped and collides.
**Default correction:** Design the narrow state deliberately: what stacks, what collapses into a
menu or drawer, what reorders, what is disclosed on demand.
**Acceptable when:** The product explicitly does not support small screens (a documented decision
for an internal desktop tool), and it shows a clear message instead of a broken layout.
**Severity:** HIGH.

### RS-05: Missing intermediate widths
**Tell:** Two states only: a phone stack and a wide grid. Between about 600 and 1100 px the phone
stack stretches absurdly wide or the wide grid is crammed.
**Why:** Tablets, split-screen windows, and small laptops live in that band.
**Default correction:** Let content define as many states as it needs, often three: one column,
two columns, full grid. Intrinsic grids (`repeat(auto-fit, minmax(18rem, 1fr))`) often remove the
need for extra breakpoints.
**Acceptable when:** Content that genuinely has two states (a single article column).
**Severity:** MEDIUM.

### RS-06: Desktop-scale sizing on small screens
**Tell:** Desktop section padding (96 to 160 px), hero heights, headline sizes, and gaps carried
unchanged to phones; full-viewport sections that push all content below the fold.
**Why:** The page scrolls through empty space and oversized type.
**Default correction:** A smaller spacing and type register on narrow screens; `clamp()` for
section spacing; size sections to content unless full height is the point.
**Acceptable when:** CREATIVE_EXPERIENCE pieces where a full-screen moment is the design, with
content still reachable.
**Severity:** MEDIUM.

### RS-07: Touch ergonomics
**Tell:** Targets that meet the 24 px floor (A11Y-12) but sit flush against each other; primary
actions in hard-to-reach corners on phones; destructive actions adjacent to frequent ones.
**Why:** Mis-taps, especially one-handed and on the move.
**Default correction:** About 44 px hit areas for primary touch controls; spacing between adjacent
targets; primary mobile actions within thumb reach (bottom area) where the pattern supports it;
destructive actions separated.
**Acceptable when:** Dense desktop-first tools on touch laptops may keep compact targets with spacing.
**Severity:** MEDIUM.

### RS-08: Tables without a small-screen strategy
**Tell:** Wide tables that overflow the page, shrink to unreadable text, or drop columns silently.
**Why:** Tabular data is often the main content in apps and dashboards.
**Default correction:** Choose per table: a focusable, labeled horizontal scroll region with a
sticky first column; priority columns with the rest available on demand; or a stacked card or
definition-list layout per row when rows are read one at a time. See
`../anti-slop-web/references/tables.md`.
**Acceptable when:** The table fits at the narrowest supported width.
**Scope:** Any page containing a data table.
**Severity:** HIGH when data becomes unreadable or unreachable, otherwise MEDIUM.

### RS-09: Charts unreadable on small screens
**Tell:** Charts squeezed to the viewport with overlapping labels, unreadable ticks, legends that
take half the height, and hover-only tooltips.
**Why:** The chart stops answering its question.
**Default correction:** Reduce tick density, abbreviate labels, move legends below or label lines
directly, switch to horizontal bars for long category names, show the key value as text, allow
tap to inspect, or let wide time series scroll inside a labeled container.
**Acceptable when:** The product documents that small screens are unsupported (RS-04).
**Scope:** Any page containing a chart.
**Severity:** MEDIUM.

### RS-10: Dense application without a priority strategy
**Tell:** A dense desktop tool reflowed to one long column containing every panel and toolbar; or
the opposite, a dense desktop tool that adopts phone-style spacing at desktop widths and wastes
the screen.
**Why:** DENSITY should change with the medium, guided by what users do on each.
**Default correction:** Decide the small-screen job (monitor, triage, approve) and surface that
first; collapse secondary panels into drawers or tabs. On wide screens, use the space: multi-pane
layouts, more columns, persistent filters.
**Acceptable when:** The product is explicitly desktop-only (see RS-04).
**Scope:** APPLICATION, DASHBOARD, OPERATIONS, DATA_EXPLORATION, DEVELOPER_TOOL.
**Severity:** MEDIUM.

### RS-11: Reflow and zoom failure
**Tell:** At 200 percent text zoom text is clipped or overlaps; at 400 percent page zoom (320 CSS px
wide) content requires two-dimensional scrolling; fixed-height containers cut off enlarged text.
**Why:** Low-vision users zoom. WCAG 1.4.4 and 1.4.10 require that this works.
**Default correction:** Avoid fixed heights on text containers; use `min-height`; size type in rem;
test at 200 and 400 percent.
**Acceptable when:** Content that genuinely needs two dimensions (maps, large data tables, diagrams).
**Severity:** HIGH.

### RS-12: Fluid type without zoom safety
**Tell:** Font sizes in pure `vw` units, or `clamp()` with a `vw`-only preferred value, so text
does not grow with browser zoom; minimum sizes below 16 px for body text on phones.
**Why:** Zoom stops working for text, and small body text strains reading.
**Default correction:** Combine rem and vw in the preferred value
(`clamp(1rem, 0.9rem + 0.5vw, 1.25rem)`); keep body text at about 16 px or more on small screens;
verify at 200 percent zoom.
**Acceptable when:** Display text in CREATIVE_EXPERIENCE work, if body text remains zoomable.
**Severity:** MEDIUM.

### RS-13: State lost across breakpoints
**Tell:** Resizing or rotating the device resets form input, closes or desynchronizes the
navigation drawer, loses scroll position, or swaps a component for a different one that does not
share state (desktop table and mobile cards with separate selection).
**Why:** Rotation and window resizing are normal. Losing work punishes users for them.
**Default correction:** Prefer one component that changes presentation over two components that
swap. Keep state above the layout switch. Close transient overlays predictably when their trigger
disappears.
**Acceptable when:** Purely presentational differences.
**Severity:** MEDIUM. HIGH if user input is lost.

### RS-14: Viewport-unit and fixed-bar traps
**Tell:** `height: 100vh` sections that overflow behind mobile browser chrome; `position: fixed`
bottom bars that ignore safe areas and sit under the iOS home indicator in standalone mode; sticky
headers taking a large share of a short viewport.
**Why:** Content is hidden behind browser and device chrome.
**Default correction:** `min-height: 100dvh` (with a `100vh` fallback) or `svh` for above-the-fold
sizing; safe-area insets (`env(safe-area-inset-bottom)`, with `viewport-fit=cover`); compact sticky
chrome that shrinks or hides on scroll when space is tight.
**Acceptable when:** The product documents that small screens are unsupported (RS-04).
**Severity:** MEDIUM.

### RS-15: Device-list breakpoints
**Tell:** Breakpoints at exact device widths (375, 414, 390) chosen because "that is the iPhone",
with layouts that break between them.
**Why:** Devices change every year; content breaks where it breaks.
**Default correction:** Set breakpoints where content fails; test at common widths as samples.
**Acceptable when:** A framework's default breakpoint scale used consistently, with layouts
verified between steps.
**Severity:** LOW.

---

## Responsive checklist (quick)

- [ ] No horizontal page scroll from 320 px upward; nothing clipped (RS-01, RS-02)
- [ ] Every interaction works with touch alone; keyboard never hides the focused input (RS-03)
- [ ] Narrow, middle, and wide states are each designed (RS-04, RS-05)
- [ ] Spacing and type scale down deliberately; body text about 16 px or more (RS-06, RS-12)
- [ ] Primary touch targets about 44 px with spacing (RS-07, A11Y-12)
- [ ] Tables and charts have a small-screen strategy (RS-08, RS-09)
- [ ] Dense tools have a declared small-screen job (RS-10)
- [ ] Works at 200 percent text zoom and 400 percent page zoom (RS-11)
- [ ] Rotation and resizing keep state (RS-13)
- [ ] No `100vh` or fixed-bar traps; safe areas respected (RS-14)
