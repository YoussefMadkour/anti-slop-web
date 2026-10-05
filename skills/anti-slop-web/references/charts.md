# Charts

Choosing, encoding, labeling, and stating the limits of data visualizations on the web. Load for
DASHBOARD, OPERATIONS, DATA_EXPLORATION, and any marketing page that shows data. The project's
`DESIGN.md` §10 and brand override everything here. Library names (Recharts, Vega-Lite, D3,
Observable Plot, ECharts) are examples, not requirements.

## Question first

Every chart answers a question. Write the question before choosing the form, and usually put it in
the title: "Failed jobs per hour, last 24 h" says more than "Performance". If no reader decision
depends on the chart, or a sentence or single number answers the question, use that instead
(UI-24).

| Question | Usually fits | Watch out for |
|---|---|---|
| How did a value change over time? | Line; area for a single cumulative quantity | Too many lines; irregular time intervals drawn as regular |
| How do categories compare? | Bar (horizontal when labels are long), sorted | Truncated baselines; unsorted bars hiding the ranking |
| What is the ranking? | Sorted horizontal bar or a ranked table | Pie charts for rankings |
| What share of a whole, few parts? | Stacked bar, or donut with up to about five parts | Angle comparison is hard; labels outside small slices |
| What share of a whole, many parts? | Sorted bar, treemap | Rainbow categorical palettes |
| How did composition change? | Stacked bar or stacked area; small multiples | Middle layers of stacks are hard to read |
| Progress against a target? | Bullet chart, progress bar with target marker | Gauges that waste space and hide the target |
| How are values distributed? | Histogram, box plot, strip or dot plot | Means without spread |
| Do two variables relate? | Scatter, with trend line only if meaningful | Implying causation; overplotting dense data |
| When does something happen in a cycle? | Heatmap (day by hour, calendar) | Diverging palettes for non-diverging data |
| Where does a process lose people? | Funnel as a bar chart of steps with conversion labels | Decorative 3D funnels |
| What is the exact value? | A number or a table | A chart where a number was needed |

## Color for data
**What:** Palettes chosen for the data type: sequential for ordered magnitude, diverging for values
around a meaningful midpoint, categorical for unordered groups.
**Use when:**
- Sequential: one hue varying in lightness, for intensity, counts, density.
- Diverging: two hues meeting at a neutral midpoint, only when the midpoint means something (zero,
  target, average).
- Categorical: distinct hues for a small number of groups, ideally five to seven at most.
**Avoid when:**
- Using a rainbow scale for sequential data; perceived steps are uneven.
- Coloring bars by category when the category is already the axis label; one color is clearer.
**Archetypes:** All with data.
**Tradeoffs:**
- Brand colors make charts feel owned but may not form a usable categorical palette. Anchor the
  first series on the brand color and choose the rest for distinguishability.
- Colorblind-safe palettes such as Okabe-Ito are a solid starting point for categories. Perceptual
  color spaces like OKLCH help build even sequential ramps.
- Keep data colors separate from status colors, or "red" will mean both "category 3" and "error".
**Accessibility:**
- Color is never the only way to tell series apart: add direct labels, markers, or line styles
  (A11Y-08). Adjacent marks such as bar segments need about 3:1 contrast against each other or a
  separating gap (A11Y-05).
**Common AI misuse:** Default framework palettes with purple first and a rainbow after (UI-08,
UI-24).

## Emphasis and context series
**What:** Making one series dominant and rendering comparison series quietly.
**Use when:**
- There is a focal series (this year) and context (last year, target, peer average).
**Avoid when:**
- All series are equally important; then consider small multiples instead.
**Archetypes:** DASHBOARD, DATA_EXPLORATION, EDITORIAL.
**Tradeoffs:**
- Muting context in gray with a thinner or dashed line focuses attention but can make the context
  hard to read; label it directly.
**Accessibility:**
- Dashed versus solid is a non-color distinction; keep it.
**Common AI misuse:** Five equally saturated lines with a legend, leaving the reader to work out
which one matters.

## Direct labeling versus legends
**What:** Labels placed on or next to the data versus a separate key.
**Use when:**
- Direct labels: few series, enough room at line ends or bar ends.
- Legends: many series, interactive toggling, or crowded plots.
**Archetypes:** All with data.
**Tradeoffs:**
- Direct labels remove the back-and-forth eye movement of legends but collide on small screens;
  fall back to a legend or tooltip there (RS-09).
**Accessibility:**
- Interactive legends that toggle series are buttons with `aria-pressed` (A11Y-17).
**Common AI misuse:** A legend for a single-series chart.

## Axes, gridlines, and baselines
**What:** The scaffolding that lets readers estimate values.
**Use when:**
- Bars start at zero; their length encodes the value.
- Lines may use a non-zero baseline when the variation is what matters, with the axis clearly
  labeled.
- Light horizontal gridlines help read values on bar and line charts; fewer is usually better.
**Avoid when:**
- Gridlines on charts with value labels, sparklines, or a single big number.
- Rotated tick labels on desktop; abbreviate or use horizontal bars.
**Archetypes:** All with data.
**Tradeoffs:**
- Removing axis lines and tick marks gives a calmer look but can make scale unclear. Keep units
  and tick labels.
- Dual axes invite false correlations because the scales are arbitrary relative to each other.
  Prefer two aligned charts sharing the x axis, or index both series to a common start.
**Accessibility:**
- Tick labels meet text contrast (A11Y-04), even if gridlines are faint.
**Common AI misuse:** A truncated bar axis exaggerating a small difference; hiding a numeric axis
without setting an explicit domain, which in several libraries renders empty bars.

## Tooltips
**What:** Detail shown on hover, focus, or tap.
**Use when:**
- Adding exact values and secondary detail to an already readable chart.
**Avoid when:**
- The tooltip is the only way to get the values. Hover does not exist on touch, and many
  tooltips are unreachable by keyboard and invisible to screen readers.
**Archetypes:** All with data.
**Tradeoffs:**
- Shared tooltips (all series at one x) suit time series; per-mark tooltips suit scatter plots.
**Accessibility:**
- Tooltip content must also be reachable another way, such as a data table or labels
  (A11Y-18). Tooltips that appear on hover must be dismissible and hoverable (A11Y-16).
**Common AI misuse:** A beautiful custom tooltip on a chart with no labels and no table.

## Small multiples
**What:** A grid of small identical charts, one per category, sharing scales.
**Use when:**
- Comparing the shape of many series; more than four or five lines on one chart.
**Avoid when:**
- Precise comparison at one point matters more than shape; overlay or table instead.
**Archetypes:** DATA_EXPLORATION, EDITORIAL, DASHBOARD.
**Tradeoffs:**
- Shared scales make comparison honest; independent scales show each shape but mislead about size.
  Say which you used.
**Accessibility:**
- Each multiple needs its own label; the set needs a summary (A11Y-18).
**Common AI misuse:** A spaghetti chart of ten colored lines and a legend.

## Sparklines
**What:** Tiny word-sized line charts without axes, showing trend shape next to a number.
**Use when:**
- Shape matters more than values, beside a labeled number and a stated period.
**Avoid when:**
- Readers will try to read values from it, or the scale differences between sparklines matter.
**Archetypes:** DASHBOARD, OPERATIONS, DATA_EXPLORATION.
**Tradeoffs:**
- Without axes, the same visual slope can mean 1% or 100%. Consider shared scales across a row, or
  a min and max label.
**Accessibility:**
- Decorative sparklines can be hidden from assistive technology if the adjacent text states the
  trend; otherwise describe it (A11Y-18).
**Common AI misuse:** Animated sparklines on invented data in every KPI card (IN-02).

## Uncertainty
**What:** Showing ranges, confidence, estimates, and incomplete periods instead of false precision.
**Use when:**
- Forecasts, samples, survey results, model output, sensor readings with tolerance, and any period
  not yet complete.
**Avoid when:**
- The value is exact (a count of completed orders).
**Archetypes:** DATA_EXPLORATION, OPERATIONS, EDITORIAL, DASHBOARD.
**Tradeoffs:**
- Bands around a line are compact but readers may not know what they mean; label them ("90%
  interval").
- Dashed or lighter segments for projected or incomplete data prevent the last bar of a partial
  month reading as a collapse.
- Error bars on bars are often misread; dot plots with intervals are easier.
**Accessibility:**
- State the uncertainty in text as well ("Estimated 1,200 to 1,450").
**Common AI misuse:** Forecasts drawn with the same solid line as actuals.

## Provenance and freshness
**What:** Source, method, and last-updated information attached to the chart.
**Use when:**
- Always where trust matters: DATA_EXPLORATION, public data, finance, health, operations.
**Archetypes:** DATA_EXPLORATION, OPERATIONS, EDITORIAL, DASHBOARD.
**Tradeoffs:**
- A short caption ("Source: billing system. Updated 09:40 UTC. Excludes refunds.") costs a line
  and prevents most misreadings. Longer method notes can live behind a disclosure.
**Accessibility:**
- Captions are text, associated with the figure (a `figcaption`).
**Common AI misuse:** Charts with no source, no time, and no unit.

## Annotation
**What:** Text placed on the chart that explains a notable point: an outage, a launch, a policy
change.
**Use when:**
- A spike or drop has a known cause the reader would otherwise guess at.
**Avoid when:**
- The annotation repeats what the data already makes obvious.
**Archetypes:** EDITORIAL, DATA_EXPLORATION, DASHBOARD.
**Tradeoffs:**
- Annotations make a chart opinionated. That is usually the point in editorial work and needs care
  in neutral tools.
**Accessibility:**
- Include annotations in the text alternative.
**Common AI misuse:** Invented explanations for features of invented data.

## Empty, zero, and sparse data
**What:** Charts when there is nothing, zero, or very little to show.
**Use when:**
- Always design for these (FN-02).
**Patterns:**
- No data yet: replace the plot with a short explanation and the action that produces data.
- Zero: render real axes and zero-height marks. Zero is information.
- Sparse (a handful of points): straight segments with visible points; smooth curves over three
  points imply data that does not exist.
- Missing intervals: show the gap rather than interpolating across it, unless interpolation is
  meaningful and stated.
**Common AI misuse:** A blank chart frame, or an invented demo series to fill it (IN-02).

## Motion in charts
**What:** Entrance animation, transitions between filters, and highlight on hover.
**Use when:**
- Transitions help the reader track how values changed between two filter states.
**Avoid when:**
- Re-animating every refresh in OPERATIONS; values should update in place.
- Long draw-in animations that delay reading.
**Archetypes:** DATA_EXPLORATION, EDITORIAL, MARKETING; minimal in OPERATIONS.
**Accessibility:**
- Respect reduced motion; render final state immediately (A11Y-10).
**Common AI misuse:** Count-up numbers and bouncing bars on every load (UI-23).

## Dark mode for charts
Dark themes need their own chart palette, not the light one reused. Lighten and slightly
desaturate brand and status colors, lower gridline contrast, and verify label contrast. In dark
sequential scales, consider making the lightest color the highest value so high values stand out.
Test every chart in every shipped theme (FN-06).

## Small screens
Charts that work at 1200px rarely work at 360px. Options: fewer ticks, abbreviated labels, legend
moved below, horizontal bars instead of columns, a summary number above with the chart behind a
tap, or a scroll region for long time series. See `anti-slop-responsive` (RS-09).

## Accessibility pattern

A chart needs a meaningful title, a text summary of the key insight, and access to the underlying
values (A11Y-18). Use `role="img"` only for static charts: it hides any focusable data points
inside it. Interactive charts keep their points keyboard reachable and named.

```html
<figure>
  <h3 id="jobs-title">Failed jobs per hour, last 24 h</h3>
  <div role="img" aria-labelledby="jobs-title" aria-describedby="jobs-summary">
    <!-- chart SVG or canvas -->
  </div>
  <p id="jobs-summary">Failures peaked at 42 at 03:00 during the storage incident and have been
  under 5 per hour since 06:00.</p>
  <details>
    <summary>Show data table</summary>
    <table><!-- hour, failed jobs --></table>
  </details>
  <figcaption>Source: job scheduler. Updated 09:40 UTC.</figcaption>
</figure>
```

## Common AI misuse summary

Charts placed to fill space, titled "Analytics", built on invented data, colored with a rainbow,
drawn in 3D or with glowing marks, with values available only in a hover tooltip and no source or
time. Each of these is covered by UI-24, IN-02, A11Y-18, or A11Y-08.
