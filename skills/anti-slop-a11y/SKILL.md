---
name: anti-slop-a11y
description: "Accessibility specialist for web UI built or reviewed by AI agents: semantic HTML, keyboard use, focus, contrast (with a contrast checker script), reduced motion, accessible names, form errors, table semantics, dialogs, target sizes, and state communication. Load with anti-slop-web for any interactive interface. Accessibility requirements override aesthetic anti-slop preferences."
license: MIT
---

# Anti-Slop Accessibility

Accessibility is not a finishing pass. In this kit's order of authority, the WCAG 2.2 AA floor
is a product requirement (layer 1): it outranks brand, taste, and every anti-slop heuristic.
When an aesthetic rule and an accessibility rule disagree, accessibility wins. A brand decides
how to meet the floor, never whether to.

AI agents fail accessibility in predictable ways: they build visuals without behavior
(`<div onClick>`), remove focus outlines for looks, assert contrast without computing it,
signal errors with color alone, and forget that modals, menus, and toasts have keyboard and
screen-reader contracts. The rules below target those habits.

Rules use the kit schema (Tell, Why, Default correction, Acceptable when, Scope, Severity). All
apply to every archetype unless noted. Severity labels set fix priority, but any finding that is
a WCAG 2.2 Level A or AA failure cannot be waived and blocks shipping, whatever its label. Run the procedure in
`../anti-slop-web/audits/accessibility-audit.md`.

## Contrast checker

Never assert that a color pair passes. Compute it.

```bash
python3 scripts/contrast.py "#6b7280" "#ffffff"
# 4.83:1  normal text AA: PASS  large text AA: PASS  non-text (3:1): PASS  AAA normal: FAIL
```

Pass `--min 3` when checking large text or non-text pairs, so the exit code reflects the right
threshold in CI. The script lives in `scripts/contrast.py` next to this file and needs only Python 3. Without it,
use the WCAG formula: for each sRGB channel `c = value / 255`, linearize
(`c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ^ 2.4`), luminance
`L = 0.2126 R + 0.7152 G + 0.0722 B`, ratio `(L_light + 0.05) / (L_dark + 0.05)`.
Thresholds: 4.5:1 normal text, 3:1 large text (24px, or 18.66px bold), 3:1 for UI component
boundaries, icons, focus indicators, and chart marks. For text over images or gradients, test
the lightest and darkest regions the text crosses, not one point.

---

### A11Y-01: Non-semantic interactive elements
**Tell:** `<div onClick>` or `<span>` acting as buttons or links; links used as buttons
(`<a href="#" onClick>`); custom checkboxes, selects, or tabs built from divs without roles and
keyboard support.
**Why:** Native elements bring focusability, keyboard activation, and a role for free. Div
controls are invisible to keyboard and assistive-technology users.
**Default correction:** `<button>` for actions, `<a href>` for navigation, native inputs for
form controls. Style them however the brand needs. Use ARIA roles only when no native element
fits, and then implement the full keyboard pattern from the WAI-ARIA Authoring Practices.
**Acceptable when:** A well-tested headless library provides the role and keyboard behavior.
**Severity:** P0.

### A11Y-02: Keyboard inaccessible
**Tell:** Controls that cannot be reached or operated with Tab, Shift+Tab, Enter, Space, Escape,
and arrow keys where the pattern expects them; hover-only menus; drag-and-drop with no
alternative; focus order that does not follow visual order; keyboard traps.
**Why:** Keyboard-only users, switch users, and many power users cannot complete the task.
**Default correction:** Keep DOM order aligned with visual order. Provide keyboard alternatives
for drag (move buttons, menus). Add a skip link on pages with repeated navigation.
**Acceptable when:** Never for functionality. Purely decorative interactions may be skipped.
**Severity:** P0.

### A11Y-03: Missing or invisible focus indicator
**Tell:** `outline: none` with no replacement; focus styles only on hover; focus rings with less
than 3:1 contrast against adjacent colors; focus hidden under sticky headers.
**Why:** Keyboard users cannot see where they are.
**Default correction:** A visible `:focus-visible` style meeting 3:1 against its surroundings in
every theme. Use `scroll-padding-top` so sticky headers do not cover focused elements.
**Acceptable when:** Never.
**Severity:** P0.

### A11Y-04: Text contrast below AA
**Tell:** Light grey body text, muted labels, placeholder text used as labels, white text on light
parts of a gradient or photo, disabled-looking text carrying real information.
**Why:** It excludes low-vision users and everyone in glare. The eye overestimates contrast on
grey pairs; agents repeat plausible but false claims.
**Default correction:** Compute every text pair with the checker. Add a scrim or solid block
behind text on imagery.
**Acceptable when:** Incidental text (truly disabled controls, logos, decorative text) is exempt
under WCAG 1.4.3.
**Severity:** P0 for body text, labels, and controls. HIGH for secondary text such as captions.

### A11Y-05: Non-text contrast
**Tell:** Input borders, toggle tracks, icon-only buttons, chart marks, or status indicators below
3:1 against adjacent colors.
**Why:** Users cannot find controls or tell states apart.
**Default correction:** 3:1 for component boundaries and meaningful graphics. If a borderless
input style is part of the brand, give it another 3:1 cue (fill contrast, underline).
**Acceptable when:** The component is identified by other means (a text label and a 3:1 fill).
**Severity:** HIGH.

### A11Y-06: Missing accessible names
**Tell:** Icon-only buttons with no label; inputs without an associated `<label>`; placeholder as
the only label; generic link text ("click here", "read more") repeated many times; images used
as buttons with empty alt.
**Why:** Screen-reader users hear "button" with no purpose; voice-control users cannot name the
target.
**Default correction:** Visible labels where possible; `aria-label` for icon-only controls; link
text that names the destination, or `aria-describedby` or visually hidden text to disambiguate.
The accessible name should contain the visible label text (WCAG 2.5.3).
**Acceptable when:** Never for interactive elements.
**Severity:** P0.

### A11Y-07: Form errors not associated or announced
**Tell:** Errors indicated only by a red border; messages not linked to their field; errors that
appear without announcement; error summary missing on long forms; focus not moved to the problem
after a failed submit; input cleared after an error.
**Why:** Users cannot find out what went wrong or fix it. This is critical form feedback (FN-04).
**Default correction:** Message text near the field, linked with `aria-describedby`; set
`aria-invalid="true"`; on submit failure, move focus to an error summary that links to each field,
or to the first invalid field. Keep the user's input. See `../anti-slop-web/references/forms.md`.
**Acceptable when:** Never.
**Severity:** P0.

### A11Y-08: Color as the only signal
**Tell:** Status shown only by hue (green or red dots, colored rows), required fields marked only
in red, chart series distinguishable only by color, links distinguished from body text only by color
with less than 3:1 difference.
**Why:** Excludes color-blind users, fails in forced-colors mode and in glare. In operations
software this can cause real mistakes.
**Default correction:** Pair color with text, an icon or shape, or a pattern. Underline links in
running text, or ensure 3:1 against body text plus a non-color cue on hover and focus.
**Acceptable when:** Color is redundant with another cue.
**Severity:** HIGH. P0 in OPERATIONS when status drives action.

### A11Y-09: Dialog and overlay behavior
**Tell:** Modals that do not move focus in, do not trap focus, cannot be closed with Escape, leave
the background interactive, or do not return focus to the trigger on close; menus and popovers that
cannot be dismissed; toasts that steal focus.
**Why:** Keyboard and screen-reader users get lost behind the overlay or cannot leave it.
**Default correction:** Use native `<dialog>` with `showModal()` (focus containment, Escape,
inert background) or a tested headless dialog. Label it with its visible title. Return focus to
the trigger. Non-modal overlays do not trap focus. Alert dialogs for destructive confirmation
require an explicit choice.
**Acceptable when:** Never for modal dialogs.
**Severity:** HIGH. P0 if users can get trapped or lose focus entirely.

### A11Y-10: Motion safety
**Tell:** Parallax, scroll-jacking, large zooms, auto-playing carousels and video, or looping
animation with no reduced-motion handling; content that moves, blinks, or auto-updates for more than
five seconds with no pause control; flashing more than three times per second.
**Why:** Vestibular disorders, attention disorders, and migraine triggers. Auto-moving content
also defeats readers and screen magnifier users.
**Default correction:** Make motion additive: define it inside
`@media (prefers-reduced-motion: no-preference)` and keep content fully visible without it.
Under reduced motion, replace spatial motion with instant changes or short fades. Provide pause,
stop, or hide for anything that moves on its own for more than five seconds.
**Acceptable when:** Motion that is essential to the information (a progress indicator) may stay,
simplified.
**Severity:** HIGH for missing reduced-motion handling on non-essential spatial motion. P0 for
auto-moving content with no pause (WCAG 2.2.2) or flashing content (WCAG 2.3.1).

### A11Y-11: Table semantics
**Tell:** Tabular data built from divs or CSS grid; tables without `<th>`; missing `scope`;
sortable headers that are not buttons or lack `aria-sort`; layout tables for non-tabular content.
**Why:** Screen-reader users cannot navigate by row and column or hear headers with values.
**Default correction:** Semantic `<table>`, `<thead>`, `<th scope>`, a `<caption>` or label;
sort controls as `<button>` inside the header with `aria-sort` on the active column. Wrap wide
tables in a focusable, labeled scroll region. See `../anti-slop-web/references/tables.md`.
**Acceptable when:** Data grids implementing the ARIA grid pattern fully, for spreadsheet-like editing.
**Scope:** Any page containing a data table (pricing and comparison tables included).
**Severity:** HIGH.

### A11Y-12: Target size
**Tell:** Interactive targets smaller than 24 by 24 CSS pixels without adequate spacing (WCAG 2.5.8);
tiny icon buttons, close buttons, and inline links packed together in touch interfaces.
**Why:** Users with tremor, large fingers, or a moving bus miss targets.
**Default correction:** At least 24 by 24 px everywhere; aim for about 44 by 44 px for primary
touch controls by extending the hit area with padding. Dense desktop tools may use 24 px targets
with spacing. Touch ergonomics beyond the floor: `anti-slop-responsive` RS-07.
**Acceptable when:** Inline links in running text, and controls whose size is set by the user agent.
**Severity:** HIGH.

### A11Y-13: Status messages not announced
**Tell:** "Saved", "3 results", "Upload failed", loading completion, or toast notifications that
appear visually but are not exposed to assistive technology.
**Why:** Screen-reader users do not know whether their action worked.
**Default correction:** Polite live regions (`role="status"`) for confirmations and counts;
`role="alert"` only for urgent errors. Do not move focus for non-critical messages. Toasts that hold
actions (Undo) must stay long enough and be reachable by keyboard.
**Acceptable when:** The change is already announced by a focus move or page change.
**Severity:** HIGH.

### A11Y-14: Headings and landmarks
**Tell:** Headings chosen for size rather than structure; skipped levels used for styling; no `<h1>`;
no `<main>`, `<nav>`, or `<header>` landmarks; several unlabeled `<nav>` elements.
**Why:** Screen-reader users navigate by headings and landmarks. A broken outline is a broken map.
**Default correction:** One `<h1>` per page, logical nesting, landmarks for major regions, labels
on repeated landmarks (`aria-label="Primary"`). Style headings independently of level.
**Acceptable when:** Application views whose structure is clear from landmarks may use fewer headings.
**Severity:** MEDIUM.

### A11Y-15: Image alternatives
**Tell:** Informative images with no alt text; decorative images with descriptive alt that adds
noise; alt text like "image" or the file name; complex images (diagrams, screenshots used as
evidence) with no longer description.
**Why:** Users who cannot see the image lose its information, or wade through noise.
**Default correction:** Describe the information or function, not the pixels. `alt=""` for
decorative images and icons next to text. Provide a text equivalent for complex graphics.
**Acceptable when:** Not applicable.
**Severity:** MEDIUM. HIGH when the image carries essential information or acts as a control.

### A11Y-16: Hover and focus content
**Tell:** Tooltips or popovers that appear on hover only; content that vanishes when the pointer
moves toward it; tooltips that cannot be dismissed with Escape; essential information available
only in a tooltip.
**Why:** Fails keyboard and touch users and screen magnifier users (WCAG 1.4.13).
**Default correction:** Show on hover and focus, keep visible while hovered, dismiss with Escape.
Put essential information in the page, not in a tooltip. Interactive content belongs in a popover,
not a tooltip.
**Acceptable when:** Native `title` tooltips for redundant information.
**Severity:** MEDIUM.

### A11Y-17: State not exposed
**Tell:** Toggle buttons without `aria-pressed`; disclosure and accordion triggers without
`aria-expanded`; current page in navigation without `aria-current`; selected tabs or options
without `aria-selected`; disabled controls with no explanation of why or how to enable them.
**Why:** Visual state changes that are not exposed leave screen-reader users guessing.
**Default correction:** Native elements where possible (`<details>`, checkboxes, radio groups);
otherwise the correct ARIA state attributes, kept in sync. Explain disabled states nearby or
prefer enabled controls that explain on use.
**Acceptable when:** Not applicable.
**Severity:** HIGH.

### A11Y-18: Charts without a text alternative
**Tell:** Charts rendered as SVG or canvas with no accessible name, no summary of the insight, and no
way to read the values except hovering.
**Why:** Screen-reader and keyboard users cannot get the data; touch users cannot hover.
**Default correction:** A container with an accessible name stating the key insight, plus a data
table (visible or toggleable) or a text summary with the essential values. Keyboard access to data
points where interaction matters. See `../anti-slop-web/references/charts.md`.
**Acceptable when:** Decorative sparklines next to a text value that carries the information.
**Scope:** Any page containing a chart.
**Severity:** HIGH.

### A11Y-19: Page language, title, and reading order
**Tell:** Missing `lang` attribute; every page titled the same; CSS reordering (flex `order`, grid
placement, absolute positioning) that makes the reading order disagree with the visual order.
**Why:** Screen readers mispronounce content, users cannot tell tabs apart, and reading order
becomes nonsensical.
**Default correction:** Set `lang` (and on passages in other languages); unique, descriptive
titles per view (including client-side route changes); keep source order meaningful.
**Acceptable when:** Not applicable.
**Severity:** MEDIUM.

---

## What this skill does not do

- It does not replace testing with assistive technology or with disabled users. Automated checks
  catch a minority of issues; report what was verified manually and what was not.
- It does not make every choice binary. Above the floor, apply judgment (layer 3).

## Accessibility checklist (quick)

- [ ] Every interactive element is native or fully implements its ARIA pattern (A11Y-01)
- [ ] Whole flow usable with keyboard only; focus visible throughout (A11Y-02, A11Y-03)
- [ ] Every text and UI color pair computed, in every theme (A11Y-04, A11Y-05)
- [ ] Every control has an accessible name (A11Y-06)
- [ ] Form errors linked, announced, and recoverable (A11Y-07)
- [ ] No color-only meaning (A11Y-08)
- [ ] Dialogs, menus, and toasts follow their contracts (A11Y-09, A11Y-13)
- [ ] Reduced motion honored; no unpausable auto-motion (A11Y-10)
- [ ] Data tables and charts are semantic and have alternatives (A11Y-11, A11Y-18)
- [ ] Targets at least 24 px; primary touch controls about 44 px (A11Y-12)
- [ ] States exposed; headings, landmarks, titles, and language set (A11Y-14, A11Y-17, A11Y-19)
