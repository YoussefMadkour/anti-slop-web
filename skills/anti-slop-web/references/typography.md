# Typography

Choosing typefaces, building scales, and setting type that reads well at every size and zoom
level. Load this file when a task sets or changes type, or builds a text-heavy page. The brand
and `DESIGN.md` override everything here. No typeface is banned and none is required.

Related: `color.md` (text contrast), `layouts.md` (measure), A11Y-04 and RS-12.

---

## Choosing a typeface

**What:** Selecting faces for display, body, and (optionally) monospace roles.
**Use when:** Starting direction, or when existing type cannot serve a new need (numbers, languages).
**Decide by, in roughly this order:**
- **Legibility at the sizes you use.** Dense UIs at 13 to 14px need open apertures, a generous
  x-height, and clear distinctions between `Il1` and `0O`.
- **Numerals.** Tabular figures for tables and updating numbers; lining versus old-style for prose.
- **Language coverage.** Every script, accent, and symbol the product needs, including currency.
- **Voice.** What the face says about the product: institutional, warm, technical, editorial, playful.
- **Performance.** Number of files, variable versus static, subsetting, licensing for web use.
**Avoid when:**
- The only reason is "it is distinctive" or "it is not Inter". Distinctive with poor legibility is a regression.
**Archetypes:** All. CHARACTER drives how much voice the face should carry.
**Tradeoffs:**
- System font stacks: zero load cost, native feel, little identity. Strong choice at low CHARACTER.
- Popular UI faces (Inter, Geist, and peers): excellent for dense interfaces, common everywhere.
- Expressive display faces: identity and memorability, more files, more risk at small sizes.
**Accessibility:** Body text needs adequate size, contrast (A11Y-04), and resizability (RS-11).
**Common AI misuse:** A face picked because it is the model's default with no reason recorded (UI-16).

### The replacement-roster problem
Banning the common defaults just creates a new default list. If every agent swaps Inter for
the same four "characterful" grotesks, those become the new tell. Treat any list of fonts as
examples, and choose from the product's needs. Illustrative examples of voice, not recommendations:

| Voice | Illustrative directions |
|-------|-------------------------|
| Institutional, trustworthy | Humanist sans for body, a sturdy serif for headings |
| Technical, precise | Neutral grotesk or the system stack, plus a monospace for data |
| Editorial, literary | Text serif for body with strong italics, contrasting display |
| Warm, consumer | Rounded or humanist sans, generous spacing |
| Expressive, brand-led | A display face with clear personality, used structurally |

### Shortlist and test
Shortlist three faces with one line each on why they fit; include the system stack or a popular
UI face as an honest option. Set the product's real headings, a dense table row, numbers, and the
longest label in each, at the smallest size used. Keep the one that serves the jobs and the voice;
record the reason in `DESIGN.md` §6. Process: `direction.md` §4.

## Pairing

**What:** Combining faces for display and body.
**Use when:**
- The display role needs a voice the body face cannot provide.
- Editorial work wants contrast between headings and reading text.
**Avoid when:**
- One well-chosen family with several weights already gives enough contrast. A single family is
  often the stronger choice for applications.
**Archetypes:** MARKETING, EDITORIAL, CREATIVE_EXPERIENCE pair often; APPLICATION and OPERATIONS rarely need to.
**Tradeoffs:**
- Each family adds weight and visual complexity. Two families plus an optional mono is a
  common ceiling, not a rule.
- Pair by contrast in structure (serif with sans, geometric with humanist), with similar x-heights.
**Accessibility:** Display faces used for anything longer than a headline need body-level legibility.
**Common AI misuse:** A high-contrast display serif over a neutral sans as an automatic "premium"
pairing, regardless of brand (UI-16).

## Modular scale

**What:** Font sizes derived from a ratio, giving consistent steps.
**Use when:** Any multi-level hierarchy. Pick the ratio by density:

| Context | Ratio (example) | Typical base |
|---------|-----------------|--------------|
| Dense application, operations | 1.125 to 1.2 | 13 to 14px |
| General UI, docs | 1.2 to 1.25 | 15 to 16px |
| Marketing, editorial | 1.25 to 1.333+ | 16 to 18px |
| Expressive, creative | 1.5 and beyond for display | 16 to 20px |

**Avoid when:**
- The scale produces more sizes than the hierarchy needs. Four to six sizes usually cover a product.
**Archetypes:** All.
**Tradeoffs:** Ratios give coherence; real products often round values and adjust a step or two by eye.
**Accessibility:** Use `rem` so sizes follow user preferences.
**Common AI misuse:** Giant display sizes on every heading, flattening the hierarchy they were
meant to create (UI-06, UI-17).

## Per-role settings

Starting points that most well-set type converges on. Adjust to the face.

| Role | Line height | Tracking | Weight |
|------|-------------|----------|--------|
| Display (very large) | 1.0 to 1.15 | slightly tight | one deliberate weight |
| Headings | 1.15 to 1.3 | slightly tight to neutral | medium to bold |
| Small titles | 1.3 to 1.45 | neutral | medium |
| Body | 1.45 to 1.7 | neutral | regular |
| Labels, buttons | 1.2 to 1.4 | neutral to slightly open | medium |
| Small caps and uppercase labels | 1.3 to 1.4 | open (letter spacing helps uppercase) | medium |

General tendencies: line height decreases as size increases; tracking tightens as size
increases; uppercase text needs extra tracking.

**Weights:** Three weights (regular, medium, bold) cover most products and reduce font loading.
Variable fonts make more weights cheap; the limit then is clarity of hierarchy, not file count.
Very light weights for body text on screens are hard to read.

## Measure

**What:** Line length of running text.
**Use when:** Any paragraph text. Roughly 45 to 75 characters per line reads comfortably; 60 to
72 is a common target.
**Avoid when:** Data tables and code, where line length follows content.
**Archetypes:** All with prose; critical for EDITORIAL.
**Tradeoffs:** Narrow measures waste wide screens; pair with asides or breakouts (`layouts.md`).
**Accessibility:** Set in `ch` or `rem`; long lines are hard for readers with dyslexia; avoid
justified text without hyphenation (uneven word spacing).
**Common AI misuse:** Hero paragraphs spanning 1200px, or centered multi-line body copy.

## Fluid type

**What:** Font sizes that scale with the viewport between a minimum and maximum.
**Use when:**
- Display and heading sizes that would be too large on phones and too small on desktops.
**Avoid when:**
- Body text in dense applications, where a fixed rem step per breakpoint is simpler and more predictable.
**Archetypes:** MARKETING, EDITORIAL, CREATIVE_EXPERIENCE.
**Tradeoffs:** Smooth scaling; harder to reason about exact sizes.
**Accessibility:**
- Always include a `rem` component and clamp. Pure `vw` sizes do not grow when users zoom,
  which can fail resize-text requirements (RS-12, RS-11).
- Test at 200% zoom.
**Common AI misuse:** `font-size: 5vw` on headings.

```css
h1 { font-size: clamp(2rem, 1.4rem + 2.5vw, 3.5rem); }
h2 { font-size: clamp(1.5rem, 1.2rem + 1.2vw, 2.25rem); }
body { font-size: 1rem; }
```

## Tabular and numeric settings

**What:** OpenType features that make digits equal width, plus number formatting.
**Use when:**
- Tables, KPIs, timers, prices in lists, anything that updates or aligns in columns.
**Avoid when:**
- Running prose, where proportional figures read more naturally.
**Archetypes:** DASHBOARD, OPERATIONS, DATA_EXPLORATION, ECOMMERCE, DEVELOPER_TOOL.
**Tradeoffs:** Tabular figures align and stop numbers from jittering on update; monospace is not
required for this and costs readability in labels.
**Accessibility:** Right-align numeric columns; format with locale-aware separators.
**Common AI misuse:** Switching every number to a monospace face to look "data-driven" (UI-17).

```css
.data, td.num, .kpi { font-variant-numeric: tabular-nums; }
```

## Uppercase labels and eyebrows

**What:** Small uppercase text with added tracking above headings or as category labels.
**Use when:**
- It carries information the heading does not (section numbering, category, status).
- Table headers and dense metadata where uppercase saves vertical space.
**Avoid when:**
- Every section gets one by habit, restating the heading (UI-17, UI-18).
**Archetypes:** EDITORIAL, DASHBOARD (column headers), MARKETING sparingly.
**Tradeoffs:** Adds structure; uppercase is slower to read at length.
**Accessibility:** Type the text in normal case and apply `text-transform: uppercase` in CSS; text typed in capitals may be spelled out letter by letter by some screen readers.
**Common AI misuse:** "HOW IT WORKS" over a heading that says how it works.

## Monospace

**What:** Fixed-width faces.
**Use when:** Code, commands, IDs, hashes, logs, keyboard shortcuts, tabular technical data.
**Avoid when:** Headings and marketing copy for a non-technical product used as "tech vibe" (UI-17).
**Archetypes:** DEVELOPER_TOOL natively; DATA_EXPLORATION and OPERATIONS for identifiers.
**Tradeoffs:** Precise and scannable for code; wide and tiring for prose.
**Accessibility:** Ensure enough size; monospace often looks smaller at the same font size.
**Common AI misuse:** Large monospace hero headings on a wellness app.

## Web font loading

**What:** Delivering font files without hurting performance or layout stability.
**Use when:** Any custom face.
**Practices:**
- Self-host or use a reliable service; subset to needed scripts.
- Preload only the one or two files used above the fold.
- `font-display: swap` (or `optional` for non-critical faces) avoids invisible text.
- Match fallback metrics (`size-adjust`, `ascent-override`) to reduce layout shift when the
  face swaps in (CD-10).
- Prefer a variable font when you need several weights.
**Archetypes:** All.
**Tradeoffs:** Each extra file costs load time, especially on mobile networks.
**Accessibility:** Invisible text while fonts load excludes slow-connection users.
**Common AI misuse:** Importing six weights of two families from a font service in a `<link>` and
using two of them; adding a font dependency that is not installed (CD-01).

```css
@font-face {
  font-family: "Brand Sans";
  src: url("/fonts/brand-sans.woff2") format("woff2");
  font-weight: 100 900;
  font-display: swap;
}
@font-face {
  font-family: "Brand Sans Fallback";
  src: local("Arial");
  size-adjust: 104%;
}
body { font-family: "Brand Sans", "Brand Sans Fallback", system-ui, sans-serif; }
```

## Common AI misuse summary

- The default roster chosen without a reason, or a "replacement roster" applied to every project (UI-16).
- Hierarchy by size alone, with every heading huge (UI-06).
- Gradient-filled headline text that fails contrast at one end (UI-08, A11Y-04).
- Monospace and tracked uppercase as costume (UI-17).
- Fixed pixel sizes that ignore user preferences, or `vw` type that ignores zoom (RS-12).
