# Dashboards

Composition, widgets, filters, states, and update behavior for screens that summarize the state
of something and route attention. Load for DASHBOARD, OPERATIONS, and DATA_EXPLORATION work,
together with `charts.md` and `tables.md`. The project's `DESIGN.md` and brand override
everything here.

## Three archetypes, three different dashboards

The word "dashboard" covers screens with different jobs. Decide which one you are building before
choosing a layout.

| | DASHBOARD | OPERATIONS | DATA_EXPLORATION |
|---|---|---|---|
| Core question | "How are we doing, and what needs attention?" | "What is happening right now, and what must I do?" | "What does the data say about my question?" |
| Typical user | Manager, owner, team lead, checking a few times a day | Operator on shift, watching for hours | Analyst or curious user, in sessions |
| Values | Summaries, trends, rounded where precision is not needed | Exact current values, units, timestamps | Precise values, comparisons, distributions |
| Layout | Overview first, detail on demand | Stable; positions are learned and must not move | Flexible; the user rearranges the view |
| Motion | Light transitions | None beyond state change | Transitions that preserve context when filtering |
| Color | Muted chrome, status and data carry color | Reserved almost entirely for alarm states | Reserved for data encodings |
| Must have | Real comparison periods | Alarm hierarchy, acknowledgement, staleness | Provenance, filtering, uncertainty, export |

Many products mix these. A logistics product may have an OPERATIONS live board and a DASHBOARD
weekly summary. Classify each screen separately.

## Job-first composition
**What:** Start from the decision the user makes on this screen, then arrange everything else
around that decision.
**Use when:**
- Always, as a design process. It is the main correction for UI-07.
**Avoid when:**
- Not applicable. What changes per archetype is the answer, not the question.
**Archetypes:** DASHBOARD, OPERATIONS, DATA_EXPLORATION, APPLICATION.
**Tradeoffs:**
- Job-first layouts can look less "complete" than a full template shell. That is acceptable; a
  screen with three things that matter beats one with twelve that look balanced.
- Different roles may have different jobs. Saved views or role-specific defaults usually serve
  this better than one screen that tries to answer everyone.
**Accessibility:**
- Put the primary content first in source order so keyboard and screen reader users reach it
  without passing every widget (A11Y-19).
- Give each region a heading so the screen is navigable by headings (A11Y-14).
**Common AI misuse:** Sidebar, four stat cards, one line chart, one table, chosen before the job
is known (UI-07). The failing job or overdue invoice ends up as row 14 of a table below decorative
counters (UI-06).

A useful exercise: write the screen's job as a sentence ("See which shipments will miss their
delivery window today and reassign them"). Whatever directly serves that sentence goes at the top
and gets the most space. Whatever does not serve it moves to a secondary view or disappears.

## App shell fit
**What:** The frame around dashboard content: sidebar, top bar, or neither.
**Use when:**
- A persistent sidebar fits multi-section products with five or more destinations.
- A top bar alone fits products with few sections or wall-mounted displays.
- No shell fits a single-purpose screen, a kiosk, or a TV display.
**Avoid when:**
- The shell takes more width than the data needs at the target resolution. Control-room displays
  often run full screen with navigation hidden.
**Archetypes:** APPLICATION, DASHBOARD, OPERATIONS, DATA_EXPLORATION.
**Tradeoffs:**
- Fixed sidebar and header with an independently scrolling main area keeps context visible but
  complicates printing and small screens.
- A collapsible rail saves width but hides labels; pair icons with tooltips and accessible names.
**Accessibility:**
- Landmarks (`nav`, `main`, `header`) and a skip link to main content (A11Y-14).
- The current page marked with `aria-current="page"` (A11Y-17).
**Common AI misuse:** Copying a well-known product's shell including its colors and spacing
(UI-26). See `navigation.md` for shell patterns.

## KPI and stat cards
**What:** A label, a value, and optionally a comparison and a small trend.
**Use when:**
- A handful of numbers genuinely answer the screen's question at a glance.
- The numbers change slowly enough that a glance is meaningful.
**Avoid when:**
- The numbers are not real yet. Show nothing or a labeled placeholder (IN-02).
- The KPIs are there because dashboards usually have a KPI row. If nobody acts on "Total users",
  it does not need a card.
- The screen's real content is a list of items needing action. Lead with the list.
**Archetypes:** DASHBOARD, DATA_EXPLORATION. In OPERATIONS, prefer status summaries ("3 lines
stopped") over business KPIs.
**Tradeoffs:**
- Four equal cards imply four equally important numbers. If one matters most, make it larger or
  give it the trend chart, and let the others be smaller or a single line of text.
- Rounding (12.4K) aids glanceability in summaries but hides changes that matter in operations
  and finance. Choose precision per metric and state the unit.
- Sparklines add trend context cheaply but can mislead without a labeled period and scale.
**Accessibility:**
- The value, its unit, and the comparison must be readable as text; do not rely on a colored
  arrow alone (A11Y-08).
- Tabular figures keep numbers from shifting when they update.
**Common AI misuse:** Four cards of invented numbers each with a green "+12% this week" (IN-02).
A delta appears only when a real comparison period exists and is named on screen.

### Delta intent versus direction

Direction (up or down) and judgment (good or bad) are different properties. Error rate going up is
bad; revenue going up is good; for some metrics neither direction is inherently good. Let the
metric definition declare intent, and derive color from intent, not from the arrow.

```html
<!-- Color comes from data-intent; the arrow and the text come from direction. -->
<p class="kpi-delta" data-intent="negative">
  <span aria-hidden="true">&#9650;</span>
  <span>Up 3.1 points</span>
  <span class="visually-hidden">(worse)</span>
  <span class="kpi-delta__period">vs. previous 7 days</span>
</p>
```

```css
.kpi-delta[data-intent="positive"] { color: var(--status-success-text); }
.kpi-delta[data-intent="negative"] { color: var(--status-danger-text); }
.kpi-delta[data-intent="neutral"]  { color: var(--text-muted); }
```

Direction ("Up") and judgement ("worse") are both in text, so the meaning survives without color
(A11Y-08), and the period is always visible. Make the judgement visible text when users are not
already trained on the metric.

## The primary chart
**What:** One chart that is clearly the largest element, answering the screen's main question.
**Use when:**
- The main question is about change over time, comparison, or distribution.
**Avoid when:**
- The answer is a single number or a short list. A sentence or a table is clearer (UI-24).
**Archetypes:** DASHBOARD, DATA_EXPLORATION.
**Tradeoffs:**
- One dominant chart creates a clear focal point; several equal charts create a grid users must
  scan one by one. Equal charts suit small multiples, where comparison is the point.
- Reserve a fixed height so the layout does not jump when data arrives (CD-10).
**Accessibility:**
- Title the chart with its question, and provide a text summary or data table (A11Y-18).
**Common AI misuse:** A generic "Overview" line chart filling empty space (UI-24). See `charts.md`.

## Filters, toolbars, and saved views
**What:** Controls that change what the dashboard shows: date range, segment, status, search,
plus saved combinations.
**Use when:**
- Users routinely look at different slices of the same data.
**Avoid when:**
- The screen serves one fixed question. Extra filters add cognitive load and empty states.
**Archetypes:** DASHBOARD, DATA_EXPLORATION, APPLICATION. In OPERATIONS, keep filters minimal and
make the active filter impossible to miss, because a forgotten filter can hide an alarm.
**Tradeoffs:**
- A horizontal filter bar keeps full width for content and suits a handful of filters. A side
  panel suits many facets (DATA_EXPLORATION, ECOMMERCE).
- Applying filters instantly feels fast but can trigger expensive queries; an explicit Apply
  button suits heavy queries.
- Showing applied filters as removable chips makes the current scope visible and reversible.
- Encode filter state in the URL so views can be shared and survive reloads.
**Accessibility:**
- Filter controls are real form controls with labels (A11Y-06). Removable chips have buttons
  with names like "Remove filter: Region North".
- Announce result count changes politely (A11Y-13).
**Common AI misuse:** Filter controls that render but do not filter anything (FN-01).

### Date ranges

Offer presets that match how the business thinks (today, last 7 days, this month, quarter to date,
fiscal year) and a custom range for the rest. Show the active range in words near the content it
affects, including the time zone when users span zones. Make partial periods explicit: "This month
(through 14 Oct)" prevents a half-month bar from reading as a collapse.

## Widget chrome
**What:** The frame around each widget: title, subtitle or period, actions, and body.
**Use when:**
- Widgets are independent units with their own data and actions.
**Avoid when:**
- Content flows as one piece. Boxing every paragraph adds noise; use spacing and headings.
**Archetypes:** DASHBOARD, OPERATIONS, DATA_EXPLORATION.
**Tradeoffs:**
- Bordered cards on a tinted page separate widgets without shadows; shadows suit floating
  elements (UI-14).
- Per-widget menus (export, expand, settings) are useful but should contain only actions that
  exist (FN-01).
**Accessibility:**
- Widget titles are headings (A11Y-14). Icon-only actions have accessible names (A11Y-06).
**Common AI misuse:** Uniform heavy cards with large radius and shadow around every widget
(UI-13, UI-14).

## Density modes
**What:** Letting the same screen run at more than one density, usually comfortable and compact.
**Use when:**
- Users differ: occasional users want comfortable spacing, power users want more rows on screen.
- DENSITY is high (7 or above) and the product also serves newcomers.
**Avoid when:**
- The audience is uniform. One well-chosen density is simpler to build and test.
**Archetypes:** APPLICATION, DASHBOARD, OPERATIONS, DATA_EXPLORATION.
**Tradeoffs:**
- Every density is another layout to verify for overflow, truncation, and target size.
- Compact density must still meet target size minimums for interactive elements (A11Y-12) and
  contrast for small text (A11Y-04).
**Accessibility:**
- Persist the preference. Respect user zoom; density is not a substitute for text resizing (RS-11).
**Common AI misuse:** Shrinking font size to 11px to fit more, instead of reducing padding and
chrome.

## Refresh and stale-while-revalidate
**What:** Keeping data current without blanking the screen.
**Use when:**
- Data changes during a session.
**Avoid when:**
- Data is static for the session; a manual refresh button is enough.
**Archetypes:** DASHBOARD, OPERATIONS, DATA_EXPLORATION.
**Tradeoffs:**
- Showing stale data with a quiet "Updating" indicator keeps context, but users must know the
  data may be old. Always show "Last updated" with a time.
- Polling is simple; push (websockets, server-sent events) is fresher but needs reconnection and
  offline handling.
**Accessibility:**
- Do not announce every refresh to screen readers. Announce meaningful changes (a new alarm)
  through a polite or assertive live region as appropriate (A11Y-13).
**Common AI misuse:** Replacing the whole dashboard with a skeleton on every refresh, so the user
loses their place.

## Real-time updates without layout jumps
**What:** Updating values in place while the layout stays still.
**Use when:**
- OPERATIONS and live monitoring, where users learn positions.
**Avoid when:**
- Not applicable; stability is good everywhere it is possible.
**Archetypes:** OPERATIONS, DASHBOARD.
**Tradeoffs:**
- Re-sorting a live list by severity brings new problems to the top, but rows jumping under the
  pointer cause mis-clicks. Options: pause re-sorting while the pointer or focus is in the list,
  insert new items with a "3 new alarms" banner the user clicks to apply, or keep a fixed
  position per asset.
- Brief highlight of a changed value helps notice change; keep it short and non-flashing.
**Accessibility:**
- Nothing flashes more than three times per second. Highlights respect reduced motion (A11Y-10).
- Live content that updates automatically can be paused if it moves or scrolls on its own (A11Y-10).
**Common AI misuse:** Animated count-ups on every update, which delay reading the real value and
make values unreadable while they tick.

## Alarm and alert hierarchy
**What:** A small, fixed set of severity levels with distinct, learnable encodings.
**Use when:**
- OPERATIONS always; any product where something can go wrong and someone must respond.
**Avoid when:**
- Not applicable for operations. For a summary dashboard, a simple "needs attention" state may be
  enough.
**Archetypes:** OPERATIONS, DASHBOARD.
**Tradeoffs:**
- Fewer levels are easier to learn. Three or four levels (critical, warning, advisory, normal) is
  a common ceiling. If everything is critical, operators learn to ignore it.
- Acknowledgement separates "seen" from "resolved"; it needs who and when, and should not clear
  the underlying condition.
- Sound and blinking are strong channels; reserve them for the top level and allow muting with an
  indicator that alarms are muted.
**Accessibility:**
- Encode severity redundantly: shape or icon, text label, and color (A11Y-08). Test with
  color-blindness simulation and under glare.
- Critical alarms that need immediate action can use an assertive live region; lower levels use
  polite announcements (A11Y-13).
**Common AI misuse:** Pulsing dots and red badges on things that are not alarms (UI-19), which
trains users to ignore the real ones.

## States
**What:** Everything the dashboard shows besides the happy path.
**Use when:**
- Always for data views (FN-02).
**Archetypes:** All data-driven archetypes.
**Tradeoffs and patterns:**
- **First run, no data yet:** explain what will appear and offer the one action that makes it
  appear (connect a source, import a file). Optionally offer clearly labeled sample data (IN-02).
- **Filtered to nothing:** say which filters caused it and offer to clear them. This is a
  different message from first run.
- **Loading:** when the layout is known, use skeletons that match the real widget sizes. For short
  or unknown waits, a labeled spinner or progress indicator is fine. Load widgets independently so
  a slow chart does not block fast numbers.
- **Zero but present:** render the chart with zero values and real axes. Zero is data. Guard
  percentages against division by zero.
- **Partial data:** one source failed while others loaded. Show what loaded, mark what did not,
  and offer retry for the failed part only.
- **Stale or offline:** show the last known values with their age and a clear stale marker. In
  OPERATIONS, stale data presented as current is dangerous; consider dimming values past a
  threshold and an explicit "Sensor offline since 14:02" label.
- **Error:** what failed, whether data is affected, and how to retry. Keep the rest of the
  dashboard usable.
- **Permission denied:** say what the user cannot see and how to request access, rather than
  showing an empty widget.
**Accessibility:**
- Loading regions can use `aria-busy`; announce completion only if it matters (A11Y-13).
**Common AI misuse:** "No data available" with an illustration for every case (FN-03); a full-page
skeleton that does not resemble the real layout.

## Color tokens for surfaces and status
**What:** Semantic tokens for page, surface, raised surface, border, text levels, and status.
**Use when:**
- Any dashboard, so status colors stay reserved for status and themes can be swapped.
**Archetypes:** All.
**Tradeoffs:**
- Separating elevation by surface tone instead of shadow keeps dense screens calm.
- Status colors need separate tokens for text, background, and border so each combination can meet
  contrast. A bright warning yellow works as a fill with dark text, rarely as text on white.
**Accessibility:**
- Verify every text and status pairing, in every theme (A11Y-04, A11Y-05, FN-06).
**Common AI misuse:** The accent color used for data series, status, and buttons at once, so the
user cannot tell an alarm from a link (UI-11). See `color.md`.

```css
:root {
  --surface-page: #f6f7f9;  --surface-card: #ffffff;  --border-default: #dde1e6;
  --text-primary: #16191d;  --text-muted: #5b636e;
  --status-danger-text: #a61b1b;  --status-danger-bg: #fdecec;
  --status-warning-text: #7a4b00; --status-warning-bg: #fff4d6;
}
```

Values are illustrative; derive yours from the brand and verify contrast.

## Dark themes for control rooms
**What:** Dark surfaces chosen for low-light environments and long viewing sessions.
**Use when:**
- Control rooms, broadcast, security operations, vehicles, anywhere ambient light is low and a
  bright screen would cause glare or ruin night vision.
**Avoid when:**
- Users work in bright offices or outdoors; dark themes wash out in daylight.
**Archetypes:** OPERATIONS, DEVELOPER_TOOL, CREATIVE_EXPERIENCE.
**Tradeoffs:**
- Saturated status colors on dark backgrounds can glow and vibrate. Use slightly desaturated
  variants with sufficient contrast.
- Very dark near-black surfaces with pure white text can cause halation for some users; slightly
  lighter surfaces and off-white text reduce it.
- Large walls of mostly dark screens make an alarm color more noticeable, which is the point.
**Accessibility:**
- Contrast rules apply exactly as in light themes (A11Y-04). Check status colors separately.
**Common AI misuse:** Dark because it looks technical, in a product used in daylight (UI-12). In
control rooms it is legitimate and needs no waiver beyond a reason in `DESIGN.md`.

## Command palette
For keyboard-first dashboards, a command palette gives fast access to entities and actions. See
`navigation.md` for the pattern and its accessibility requirements.

## Considerations checklist

These are considerations to weigh against DENSITY and archetype, not rules:
- Does the most important thing on screen serve the job sentence?
- Is every number real, with unit, precision, and comparison period appropriate to its use?
- Are status colors reserved for status, and is status readable without color?
- Does the layout stay still when data updates?
- Is "last updated" visible wherever staleness matters?
- Are first-run, filtered-empty, partial, stale, and error states designed and distinct?
- Is density achieved by trimming chrome and padding rather than shrinking text below comfort?
- Does chrome (sidebar, headers, card borders) recede so data carries the visual weight?
