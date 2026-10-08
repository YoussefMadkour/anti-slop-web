# Color

Building palettes by role, choosing themes, and keeping color meaningful. Load this file when a
task sets or changes color, theme, or tokens. The brand and `DESIGN.md` override everything
here: a brand purple is a brand color, not slop.

Related: `charts.md` (data palettes), `design-systems.md` (token architecture),
`anti-slop-a11y` (contrast rules and the contrast script), rules UI-08 to UI-12.

---

## Building a palette from purpose

Choose the hue from the brand, the product's domain material, and its feeling, then generate
scales and semantic tokens with `scripts/palette.py` (OKLCH scales, light and dark tokens, and a
contrast report). The full process is in `direction.md` §3. The script proposes values; judge
them on a real screen and adjust.

## Color by role

**What:** Every color in the system has a job, recorded in `DESIGN.md` §5.
**Typical roles:**
- **Neutrals:** page and surface backgrounds, text levels, borders, dividers. Usually most of the screen.
- **Primary:** primary actions, links, focus, selected states.
- **Accent:** an optional second voice used in one or two places.
- **Semantic:** success, warning, danger, info. Status only.
- **Data:** categorical, sequential, and diverging palettes for charts (see `charts.md`).
**Use when:** Always useful; roles are what keep a palette coherent as the product grows.
**Avoid when:** n/a.
**Archetypes:** All.
**Tradeoffs:** Roles constrain spontaneous decoration; that is the point.
**Accessibility:** Roles let you verify contrast once per role pairing instead of per screen (A11Y-04, A11Y-05).
**Common AI misuse:** One accent sprayed on buttons, icons, borders, badges, and backgrounds (UI-11).

## Neutral scale

**What:** A graded set of grays (often tinted slightly warm or cool) for surfaces and text.
**Use when:** Every product needs one.
**Practices:**
- Pure or tinted neutrals both work. A tint related to the brand adds warmth at mid or high
  CHARACTER; pure gray suits system-native, low-CHARACTER interfaces. Tinted grays are also a
  common generated default, so choose either for a reason.
- Define text levels by contrast, not by feel: primary text, secondary text, disabled, and check each.
- Keep one tint family; mixing warm and cool grays looks accidental.
**Archetypes:** All. Neutral-heavy palettes suit APPLICATION, OPERATIONS, DATA_EXPLORATION, where
data and status should carry the color.
**Tradeoffs:** A very neutral UI can feel sterile at mid or high CHARACTER; add identity through
type, imagery, or a signature element rather than more colors.
**Accessibility:** Light gray secondary text is the most common contrast failure. Compute it (A11Y-04).
**Common AI misuse:** Body text in a mid gray that "looks elegant" and fails contrast.

## One accent versus a multi-color brand

**What:** Whether the identity rests on a single hue or several.
**Use when:**
- One accent: applications and tools where color should signal action and status.
- Multi-color: brands with a deliberate multi-hue identity (education, children, media, some creative brands).
**Avoid when:**
- Multi-color without roles: five to seven colors that compete (UI-11).
**Archetypes:** One accent fits most APPLICATION, DASHBOARD, OPERATIONS. Multi-color fits some
MARKETING, CREATIVE_EXPERIENCE, EDITORIAL.
**Tradeoffs:** One accent is easy to keep consistent; multi-color needs stronger rules about
where each hue appears.
**Accessibility:** Each brand hue used for text or controls needs its own contrast check.
**Common AI misuse:** A default indigo or violet accent with no brand reason (UI-08).

## The 60-30-10 heuristic

**What:** Roughly 60% dominant (neutral or brand base), 30% secondary, 10% accent.
**Use when:**
- As a sanity check for marketing and editorial pages that feel either sterile or noisy.
**Avoid when:**
- Treated as a rule. Dense applications are often 90% neutral with color only on status and
  actions; expressive brands may invert it deliberately.
**Archetypes:** MARKETING, EDITORIAL, ECOMMERCE as a check.
**Tradeoffs:** A memorable proportion; not a design method.
**Accessibility:** None directly.
**Common AI misuse:** Citing 60-30-10 to justify a palette that has no roles.

## Semantic status colors

**What:** Colors reserved for meaning: success, warning, danger, info, and sometimes neutral or pending.
**Use when:** Any product with states, alerts, validation, or monitoring.
**Practices:**
- Use them only for status. A red decorative element weakens every real error.
- Define background, border, and text variants per status; check contrast of each.
- Warning yellows and ambers usually need a darker shade for text on light backgrounds.
**Archetypes:** All; critical in OPERATIONS and DASHBOARD.
**Tradeoffs:** Reserving hues limits brand palette choices (a red brand needs a distinct danger red or extra cues).
**Accessibility:** Never rely on color alone; pair with text, icon, or shape (A11Y-08). Test for
common color-vision deficiencies, especially red and green pairs.
**Common AI misuse:** Green and red deltas as the only signal of direction (A11Y-08); status dots
that mark nothing (UI-19).

## Dark themes and surface elevation

**What:** Dark backgrounds with lighter surfaces for elevated layers.
**Use when:**
- The audience or environment calls for it: developer tools, media, creative tools, control
  rooms, low-light use, or a brand identity.
- Users expect a choice and the product can support both modes properly.
**Avoid when:**
- Dark is chosen only because it "looks tech" (UI-12).
- Long-form reading products, where light themes usually read better for most people.
**Archetypes:** DEVELOPER_TOOL, CREATIVE_EXPERIENCE, OPERATIONS often; others by choice.
**Practices:**
- Express elevation with lighter surfaces rather than shadows, which are hard to see on dark.
- Desaturate and lighten brand and status colors for dark backgrounds; saturated colors vibrate.
- Shipping both themes means verifying both (FN-06).
**Tradeoffs:** Two themes double the verification work.
**Accessibility:** Recheck every contrast pair in dark mode, including focus rings and chart
colors (A11Y-03, A11Y-04, A11Y-05).
**Common AI misuse:** Slate-900 with an indigo accent as the automatic dark mode (UI-08).

## Pure black

**What:** `#000` backgrounds or text.
**Tradeoffs, not a ban:**
- Pure black text on pure white is maximal contrast; some readers find very high contrast
  harsh over long reading, and many systems soften text slightly for comfort.
- Pure black backgrounds suit OLED power saving, cinematic media, and some brands; with pure
  white text they can cause halation for some readers, so slightly off-white text often helps.
- Off-black (a tinted near-black) lets shadows and elevation layers read more easily.
**Archetypes:** Any, by brand and environment.
**Common AI misuse:** Choosing either extreme without considering the content and environment.

## Gradients

**What:** Transitions between colors on surfaces, text, or borders.
**Use when:**
- The gradient is a brand asset.
- It separates a hierarchy level (one feature panel, one hero band) or encodes data (a heat scale).
- It suggests light or material in a deliberate visual language.
**Avoid when:**
- It covers every surface, text, and border at once (UI-09).
- It is the default blue-to-purple or purple-to-pink with no brand reason (UI-08).
**Archetypes:** MARKETING, CREATIVE_EXPERIENCE, EDITORIAL; rarely useful in dense applications.
**Tradeoffs:** Gradients add depth and energy; they make contrast unpredictable for overlaid text.
**Accessibility:** Check text contrast at the lightest and darkest points it crosses (A11Y-04).
Gradient-clipped headline text often fails at one end.
**Common AI misuse:** Gradient text in the hero, gradient buttons, gradient borders, and aurora
blobs on the same page (CL-01).

## Tokens with modern color functions

**What:** Defining palettes in OKLCH and deriving states with `color-mix()` and `light-dark()`.
**Use when:**
- You need perceptually even ramps (equal lightness steps look equally bright in OKLCH).
- Hover and pressed states should derive from a base color.
- One token should resolve differently per theme.
**Avoid when:**
- The project must support browsers without these features and cannot add fallbacks.
**Archetypes:** All, especially products with theming.
**Tradeoffs:** Clean derivation; designers used to hex need a picker that shows OKLCH. Provide
hex fallbacks where support matters.
**Accessibility:** Equal OKLCH lightness does not guarantee WCAG contrast; still compute ratios.
**Common AI misuse:** Hard-coding hex values in components instead of tokens (CD-11).

```css
:root {
  color-scheme: light dark;
  --brand: oklch(0.55 0.15 250);
  --brand-hover: color-mix(in oklch, var(--brand), black 12%);
  --surface: light-dark(oklch(0.99 0 0), oklch(0.18 0.01 250));
  --text: light-dark(oklch(0.22 0.01 250), oklch(0.94 0.01 250));
}
```

## Checking contrast

Compute, never eyeball. Body text needs 4.5:1, large text (24px, or about 18.7px bold) and
UI components need 3:1 (A11Y-04, A11Y-05). Check:
- Every text level on every surface it appears on, in every theme.
- Text over images and gradients at the worst point.
- Focus rings against both the component and the background.
- Disabled states (exempt from requirements, but users still need to know they exist).

Use the script in `../../anti-slop-a11y/scripts/contrast.py` or a trusted checker.

## Common AI misuse summary

- Default indigo or violet accent, blue-purple gradients, neon glows (UI-08).
- Accent everywhere, or many hues with no roles (UI-11).
- Dark theme by default with no reason (UI-12).
- Status colors used decoratively; color as the only signal (A11Y-08).
- Low-contrast gray text claimed to pass without computing it (A11Y-04).
