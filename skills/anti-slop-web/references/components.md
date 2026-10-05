# Components

Cards, buttons, badges, icons, feedback, overlays, and disclosure components: when each fits
and how each gets misused. Load this file when building or reviewing component-level UI. The
brand, the project's design system, and `DESIGN.md` §8 override everything here.

Related: `forms.md` (inputs and validation), `navigation.md` (menus, tabs as navigation),
`tables.md`, `motion.md` (overlay transitions), `anti-slop-a11y`.

---

## Cards

**What:** A bounded container grouping related content, often with its own action.
**Use when:**
- Each item is a self-contained object users act on as a unit (a product, a project, a document).
- Items mix media, text, and actions that must stay together.
- Content lives in a variable-width grid of equivalent objects.
**Avoid when:**
- Items are rows of comparable attributes: a table or list scans faster (`tables.md`).
- The content is a continuous argument: prose with headings reads better than boxes.
- Density is high: borders, dividers, and whitespace separate with less noise than boxes.
- Every section of a page becomes a card grid (UI-05).
**Variants and their jobs:**
- **Outlined** (border, no shadow): default in dense UIs.
- **Filled** (tinted background): low emphasis, nested groups.
- **Elevated** (shadow): only when the card genuinely floats or must stand out (UI-14).
- **Media-led:** images or previews first; blogs, products, templates.
- **Link card:** the whole card navigates; the heading is the real link.
- **Stat card:** label, value, comparison; see `dashboards.md`.
**Archetypes:** ECOMMERCE, APPLICATION, DASHBOARD, EDITORIAL indexes; MARKETING when items are equivalent.
**Tradeoffs:** Cards are flexible and responsive; they add visual weight and can flatten
hierarchy when everything is boxed (UI-06).
**Accessibility:**
- Do not nest interactive elements inside a fully clickable card; make the heading the link
  and stretch its hit area with a pseudo-element (A11Y-01).
- Mirror hover styles on `:focus-within` so keyboard users see the same affordance (A11Y-03).
**Common AI misuse:** Identical icon-title-blurb cards for features of unequal importance (UI-03).

```css
.card { position: relative; }
.card a::after { content: ""; position: absolute; inset: 0; }
.card:focus-within { outline: 2px solid var(--focus); outline-offset: 2px; }
```

## Buttons

**What:** Controls that perform actions. Links navigate; buttons act.
**Hierarchy:**
- **Primary:** the one main action in a region. One per region is a strong default (UI-06).
- **Secondary:** alternatives; outlined or tonal.
- **Tertiary or text:** low-emphasis actions, inline actions, "Cancel".
- **Destructive:** delete, revoke; visually distinct and separated from routine actions (FN-05).
- **Icon-only:** toolbars and dense rows; needs an accessible name (A11Y-06).
**States to design:** default, hover, active (pressed), focus-visible, disabled, loading.
**Use when:** An action happens on this page.
**Avoid when:**
- The control navigates to another page: use a link styled as needed.
- Two equally loud buttons compete for the same decision.
**Archetypes:** All.
**Tradeoffs:**
- Pressed feedback (a small translate or scale on `:active`) makes buttons feel responsive;
  keep it subtle and skip it for reduced motion if it involves movement.
- Disabled buttons hide why the action is unavailable; often better to keep it enabled and
  explain on submit, or show the reason nearby.
**Accessibility:**
- Use `<button>` and `<a>`, never clickable divs (A11Y-01).
- Visible focus with 3:1 contrast against adjacent colors (A11Y-03, A11Y-05).
- Loading state: keep the label readable, disable repeat submission, announce the result (A11Y-13).
- Minimum target size (A11Y-12).
**Common AI misuse:** Gradient primary plus ghost secondary with "Get Started" and "Learn More"
(CP-02, UI-08); arrows on every button (UI-20); buttons with no handler (FN-01).

## Radius

**What:** Corner rounding as part of the shape language.
**Options:**
- **A role-based scale**, for example small for inputs and tags, medium for cards, larger for
  dialogs, full rounding only for pills and avatars. Helps element types stay distinguishable.
- **A single radius everywhere**, used deliberately by brands with a strong sharp or soft
  identity, with type distinctions carried by color, borders, and size.
- Nested elements usually look better with a smaller radius than their container (inner radius
  roughly outer radius minus padding).
**Archetypes:** All; softer shapes tend toward consumer and friendly brands, sharper toward
institutional and technical ones, but brand decides.
**Tradeoffs:** Large radii consume space in dense layouts and clip content in tables.
**Accessibility:** None directly; very rounded inputs can be mistaken for buttons.
**Common AI misuse:** Pill-shaped everything (UI-13).

## Shadow and elevation

**What:** Shadows communicate that a surface floats above another.
**Use when:**
- Menus, popovers, dialogs, toasts, dragged items, sticky headers over scrolled content.
- A brand's material language uses depth consistently.
**Avoid when:**
- Every card and section gets a soft shadow; nothing then reads as elevated (UI-14).
- Dark themes, where lighter surfaces show elevation better.
**Archetypes:** All, sparingly in dense ones.
**Tradeoffs:** Shadows tinted toward the background color look more natural than pure black.
**Accessibility:** Do not rely on a shadow alone to show a boundary; it fails non-text contrast
for many users (A11Y-05). Pair with a border where the edge matters.
**Common AI misuse:** Large blurred shadows on every component.

## Badges, tags, and status labels

**What:** Small labels for status, category, or count.
**Use when:**
- They carry a real state (Draft, Overdue, Failed) or a real category used for filtering.
- Counts that users act on (unread items).
**Avoid when:**
- The label is marketing decoration ("AI-powered", "New" with no date) (UI-18).
- A dot or badge marks nothing (UI-19).
**Archetypes:** APPLICATION, DASHBOARD, OPERATIONS, ECOMMERCE.
**Tradeoffs:** Too many badges in a row become noise; reserve strong color for states that need attention.
**Accessibility:**
- Text inside the badge, not color alone (A11Y-08).
- Removable tags need a button with a label like "Remove filter: Overdue" (A11Y-06).
- Count badges on icons need the count in the accessible name ("Notifications, 3 unread").
**Common AI misuse:** The capsule with thin border, glow, dot, and uppercase text (UI-18).

## Icons

**What:** Glyphs supporting labels or standing in for them in tight spaces.
**Use when:**
- They speed recognition of repeated actions (search, close, settings) or object types.
- Space is tight and the icon is conventional, paired with a tooltip and accessible name.
**Avoid when:**
- No relevant icon exists; a label alone is clearer (UI-21).
- Every feature heading gets an icon in a tinted square.
**Archetypes:** All. DEVELOPER_TOOL and OPERATIONS may use dense technical iconography.
**Practices:** One family, consistent sizes per context, one stroke width, `currentColor` so
icons follow text color.
**Tradeoffs:** Icons are faster for experts and ambiguous for newcomers.
**Accessibility:** Decorative icons `aria-hidden="true"`; icon-only controls need an accessible
name (A11Y-06); meaningful icons need 3:1 contrast (A11Y-05).
**Common AI misuse:** Sparkles, rockets, and lightning bolts as feature icons; emoji as interface
icons; mixed icon sets (UI-21).

## Empty states

**What:** What a view shows when it has no content.
**Kinds (they need different copy):** first run, filtered to nothing, cleared or completed,
permission denied, error-caused emptiness.
**Practices:**
- Say why it is empty and offer the one action that fills it ("No invoices yet. Create one or
  import from CSV.").
- For filtered-to-nothing, show the active filters and a way to clear them.
- Optionally show sample data, clearly labeled as sample (IN-02).
**Archetypes:** All with data.
**Tradeoffs:** Illustrations add warmth at mid or high CHARACTER and noise at low.
**Accessibility:** The message is text, not only an image (A11Y-15).
**Common AI misuse:** "No data available" with a stock illustration (FN-03).

## Loading: skeletons, spinners, progress

**What:** Indicators that work is happening.
**Choose by situation:**
- **Skeleton:** the layout of the result is known (a list, a card, a table). Mirrors the real
  shape to avoid layout shift.
- **Labeled spinner:** short actions or unknown result shapes ("Saving", "Searching").
- **Progress bar:** long operations with measurable progress (uploads, imports).
- **Nothing:** waits under roughly 300ms; flashing an indicator is worse than none.
- **Optimistic UI:** reversible actions that almost always succeed, with clear rollback on failure.
- **Stale-while-revalidate:** keep showing old data with a subtle refresh indicator rather than blanking.
**Archetypes:** All.
**Tradeoffs:** Skeletons that do not match the final layout cause the shift they were meant to prevent.
**Accessibility:**
- Expose busy state (`aria-busy` on the region) and announce completion or failure (A11Y-13).
- Shimmer animations respect reduced motion (A11Y-10).
- Progress bars use `role="progressbar"` with values, or the native `<progress>` element.
**Common AI misuse:** A bare spinner with no label; a full-page skeleton unrelated to the real
layout; shimmer used as decoration on loaded content (FN-03, UI-23).

## Feedback: toasts, inline alerts, banners

**What:** Messages about results and conditions.
**Choose by persistence and scope:**
- **Inline message:** tied to a field or region; validation, local errors. Stays until resolved.
- **Banner:** page or app-wide condition (offline, trial ending, degraded service). Persistent, dismissible if non-critical.
- **Toast:** brief confirmation of a completed action, ideally with Undo. Not for errors users must act on.
- **Dialog:** only when the user must decide before continuing.
**Archetypes:** All.
**Tradeoffs:** Toasts are easy to miss; anything important belongs inline or in a banner.
**Accessibility:**
- Toasts and async results go into a live region (`role="status"`, or `role="alert"` for errors) (A11Y-13).
- Auto-dismissing toasts need enough time, pause on hover and focus, and must not contain the
  only path to an action (WCAG timing).
**Common AI misuse:** Every result shown as a toast, including errors with no recovery (FN-04).

## Tooltips and popovers

**What:** Tooltips label or briefly explain; popovers hold interactive content anchored to a trigger.
**Use when:**
- Tooltip: naming an icon-only control, expanding an abbreviation, a short hint.
- Popover: small forms, filters, pickers, previews with links.
**Avoid when:**
- Essential information lives only in a tooltip (touch users and many keyboard users miss it).
- Interactive content inside a tooltip; use a popover.
**Archetypes:** APPLICATION, DASHBOARD, DEVELOPER_TOOL, DATA_EXPLORATION.
**Tradeoffs:** Tooltips reduce clutter; they hide information behind a gesture.
**Accessibility:**
- Show on hover and focus, dismissible with Escape, hoverable without disappearing (A11Y-16).
- Popovers manage focus and close on Escape; the native `popover` attribute handles light dismiss.
**Common AI misuse:** Chart values readable only in hover tooltips (A11Y-18, RS-09).

## Dialogs, drawers, sheets

**What:** Overlays that take focus. Modal dialogs block the page; drawers and sheets slide from an edge.
**Choose:**
- **Dialog:** a focused decision or short form.
- **Alert dialog:** destructive or irreversible confirmation; requires an explicit choice (FN-05).
- **Drawer or side sheet:** details or editing while keeping context visible; filters; mobile navigation.
- **Bottom sheet:** mobile actions and selections within thumb reach.
- **Full page:** long or complex forms; do not cram them into a modal.
**Avoid when:**
- The content is informational and could sit inline.
- Dialogs stack on dialogs.
**Archetypes:** All.
**Tradeoffs:** Modals interrupt; frequent ones train users to dismiss without reading.
**Accessibility (A11Y-09):**
- Focus moves into the dialog, is contained while open, and returns to the trigger on close.
- Escape closes and takes the safe, non-destructive option. Alert dialogs for destructive
  confirmation never auto-dismiss or close on an outside click; the user makes an explicit choice
  or presses Escape to cancel.
- Background is inert; the dialog has an accessible name from its visible title.
- The native `<dialog>` element with `showModal()` provides most of this behavior.
**Common AI misuse:** A div styled as a modal with no focus management; confirmation dialogs with
vague buttons ("OK", "Cancel") instead of naming the consequence ("Delete project").

```html
<dialog id="confirm-delete" aria-labelledby="cd-title">
  <h2 id="cd-title">Delete "Q3 forecast"?</h2>
  <p>This removes the file for everyone on the team. It cannot be undone.</p>
  <form method="dialog">
    <button value="cancel">Keep file</button>
    <button value="confirm" class="danger">Delete file</button>
  </form>
</dialog>
<!-- open with document.getElementById("confirm-delete").showModal() -->
```

## Accordions and tabs

**What:** Disclosure patterns that show one part of content at a time.
**Use when:**
- Accordion: long sets of independent sections users scan by heading (FAQs, settings groups, mobile filters).
- Tabs: a few peer views of the same object, where users rarely need two at once.
**Avoid when:**
- Users need to compare content across sections (show it all, or use a table).
- Content is essential for everyone; hiding it adds clicks and can hide it from find-in-page in some browsers (`<details>` and `hidden="until-found"` help).
**Archetypes:** All.
**Tradeoffs:** Saves space; hidden content is skipped more often.
**Accessibility:**
- Accordions: a button in each heading with `aria-expanded`; native `<details>` and `<summary>`
  work well for simple cases (A11Y-17).
- Tabs: `tablist`, `tab`, `tabpanel` roles, arrow-key movement between tabs, the selected tab
  exposed with `aria-selected` (A11Y-02, A11Y-17).
**Common AI misuse:** An FAQ accordion filled with invented questions (IN-06).

## Avatars

**What:** Images or initials representing people or organizations.
**Use when:** Collaboration, comments, assignment, account menus.
**Avoid when:** As decoration on marketing pages for people who do not exist (IN-01, IN-04).
**Practices:** Initials or a neutral generated shape when no photo exists; stable color per person derived from an ID.
**Archetypes:** APPLICATION, DASHBOARD, OPERATIONS (assignees).
**Accessibility:** Alt text with the person's name when the avatar is the only identification;
empty alt when the name is printed beside it (A11Y-15).
**Common AI misuse:** AI-generated faces for invented testimonials or team pages (IN-01, IN-05).
