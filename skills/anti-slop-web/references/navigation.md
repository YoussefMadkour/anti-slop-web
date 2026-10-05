# Navigation

Global and local navigation patterns, how they adapt across widths, and how to show where
users are. Load this file for app shells, information architecture, menus, and page-to-page
movement. The brand, existing navigation users already know, and `DESIGN.md` §7 override
everything here. Changing a mature product's navigation has real retraining cost (UI-01).

Related: `layouts.md` (shells), `components.md` (tabs, drawers), `anti-slop-responsive`.

---

## Top navigation bar

**What:** Horizontal bar with logo, primary destinations, and utility actions.
**Use when:**
- Up to roughly five to seven primary destinations.
- Marketing sites, content sites, and simple applications.
**Avoid when:**
- Many sections or deep hierarchies (use a sidebar).
**Archetypes:** MARKETING, EDITORIAL, ECOMMERCE, simple APPLICATION.
**Tradeoffs:** Keeps full width for content; limited capacity; collapses earlier on narrow screens.
**Accessibility:**
- `<nav aria-label="Main">` with a list of links; `aria-current="page"` on the current item (A11Y-14, A11Y-17).
- Every item has a real destination (FN-01).
**Common AI misuse:** Links to Features, About, and Blog pages that do not exist (FN-01); a
floating glass navbar on every page (UI-09).

## Sidebar navigation (full, collapsible, rail)

**What:** Vertical list of destinations beside content; can collapse to an icon rail.
**Use when:**
- Applications with many sections, grouped navigation, or frequent switching.
- Users need persistent orientation.
**Avoid when:**
- Two or three sections; the sidebar wastes space.
- Marketing sites.
**Archetypes:** APPLICATION, DASHBOARD, OPERATIONS, DEVELOPER_TOOL, DATA_EXPLORATION.
**Tradeoffs:**
- Rails save space but rely on icon recognition; pair with tooltips and keep labels available.
- Collapsed state preference is worth remembering per user.
**Accessibility:**
- Group headings that toggle use buttons with `aria-expanded` (A11Y-17).
- Rail icons need accessible names (A11Y-06).
**Common AI misuse:** A sidebar clone with generic sections for a product that needs three pages (UI-07).

## Showing the current location

**What:** Visual and programmatic indication of where the user is.
**Options:** filled or tinted background, weight change, an underline, or a left-edge indicator
bar on vertical navigation.
**Use when:** Every navigation system.
**Notes:**
- A left-edge bar on the active item is a legitimate, widely understood pattern because it
  encodes state. Decorative left stripes on cards that mean nothing are a different matter (UI-20).
- Combine at least two cues (shape and color, or weight and color) so the state survives color
  blindness (A11Y-08).
**Accessibility:** `aria-current="page"` (or `"step"`, `"location"`) on the active item (A11Y-17).
**Common AI misuse:** Active state shown only by a slight color shift.

## Bottom tab bar

**What:** Three to five primary destinations fixed at the bottom of a mobile screen.
**Use when:**
- Mobile-first applications and PWAs with a few top-level destinations used often.
**Avoid when:**
- More than five destinations, or destinations used rarely.
- Desktop layouts (switch to sidebar or top nav at wider widths).
**Archetypes:** APPLICATION, ECOMMERCE (mobile), consumer products.
**Tradeoffs:** Excellent thumb reach and discoverability; takes permanent vertical space.
**Accessibility:**
- Labels under icons, not icons alone.
- Reserve space so the bar never covers content or the last form field (RS-14).
**Common AI misuse:** Fixed bar overlapping content, ignoring the device safe area.

PWA tip: on iOS in standalone mode a `position: fixed; bottom: 0` bar can sit under the home
indicator. A flex column shell with the bar as its last child plus safe-area padding is more robust:

```css
.app { display: flex; flex-direction: column; block-size: 100dvh; }
.app > main { flex: 1; min-block-size: 0; overflow-y: auto; }
.app > nav { padding-block-end: env(safe-area-inset-bottom); }
/* requires <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"> */
```

## Menu button (hamburger)

**What:** A button revealing navigation in a drawer or panel.
**Use when:**
- Narrow widths where the full navigation cannot fit.
- Secondary destinations on mobile, alongside a few visible primary ones.
**Avoid when:**
- Desktop widths with room for the navigation.
- The menu hides the only path to the product's main task.
**Archetypes:** All at narrow widths.
**Tradeoffs:** Saves space; hidden navigation is used less. A visible "Menu" label improves discoverability.
**Accessibility:**
- A real button with an accessible name and `aria-expanded`, controlling the panel (A11Y-06, A11Y-17).
- The opened drawer behaves like a dialog when modal: focus moves in, Escape closes, focus returns (A11Y-09).
**Common AI misuse:** An unlabeled icon that toggles nothing, or a menu that cannot be closed by keyboard (A11Y-02, A11Y-09).

## Tabs as navigation

**What:** Switching between peer views of the same object or section.
**Use when:** Two to about seven peer views (Overview, Activity, Settings).
**Avoid when:** Views are steps in a sequence (use a stepper) or unrelated destinations (use navigation).
**Archetypes:** APPLICATION, DASHBOARD, DEVELOPER_TOOL.
**Tradeoffs:** If tabs change the URL, they behave as navigation (links with `aria-current`);
if they swap panels in place, use the tabs pattern (`components.md`). Do not mix the two semantics.
**Accessibility:** Selected state exposed (A11Y-17); arrow-key behavior for in-page tabs (A11Y-02).
**Common AI misuse:** Pill tabs styled as buttons with no selected state for assistive technology.

## Breadcrumbs

**What:** The path from the root to the current page.
**Use when:** Hierarchies three or more levels deep; users arrive deep via search or links.
**Avoid when:** Flat sites; the breadcrumb duplicates the page title and one link.
**Archetypes:** ECOMMERCE, APPLICATION, DEVELOPER_TOOL (docs), DATA_EXPLORATION.
**Tradeoffs:** Cheap orientation; on mobile, show only the parent link to save space.
**Accessibility:** `<nav aria-label="Breadcrumb">` with an ordered list; the current page marked
`aria-current="page"` and not linked.
**Common AI misuse:** Breadcrumbs on a two-level marketing site.

## Command palette

**What:** A keyboard-invoked search for destinations and actions.
**Use when:**
- Power users, many destinations or actions, keyboard-centric products.
**Avoid when:**
- It is the only way to reach something; it supplements visible navigation.
- Casual consumer products where users will not discover it.
**Archetypes:** DEVELOPER_TOOL, APPLICATION, DATA_EXPLORATION, OPERATIONS.
**Tradeoffs:** Very fast for experts; needs good search ranking and an index of real actions.
**Accessibility:**
- Dialog with a combobox and listbox pattern; arrow keys move the active option; Enter activates;
  Escape closes (A11Y-02, A11Y-09).
- Show the shortcut in the UI and avoid conflicts with browser and screen-reader shortcuts.
**Common AI misuse:** A search trigger showing a shortcut that is not implemented (FN-01).

## Mega menu

**What:** A large panel of grouped links from a top navigation item.
**Use when:** Large sites with many categories (retail, institutions, documentation hubs).
**Avoid when:** Fewer than about fifteen destinations.
**Archetypes:** ECOMMERCE, EDITORIAL, large MARKETING sites.
**Tradeoffs:** Shows breadth at a glance; heavy on small screens (convert to nested accordion).
**Accessibility:**
- Open on click or Enter, not on hover alone; hover-only menus fail touch and keyboard users (RS-03, A11Y-02).
- Escape closes and returns focus to the trigger.
**Common AI misuse:** Hover-triggered menus that vanish when the pointer crosses a gap.

## Pagination, infinite scroll, and load more

**What:** Ways to move through long result sets.
**Choose:**
- **Pagination:** users need to return to a position, compare, share a page, or reach the
  footer. Best for tables, admin lists, search results with sorting.
- **Load more:** browsing feeds where position matters less but the footer must stay reachable.
- **Infinite scroll:** continuous discovery feeds (social, media) where users rarely need the
  footer or a specific position.
**Archetypes:** Pagination for APPLICATION, DASHBOARD, OPERATIONS, DATA_EXPLORATION; load more or
infinite for ECOMMERCE browsing and EDITORIAL feeds.
**Tradeoffs:** Infinite scroll breaks sorting, selection across pages, and footer access.
**Accessibility:**
- Pagination as `<nav aria-label="Pagination">` with `aria-current="page"`.
- When new items load, keep focus where it was and announce the change (A11Y-13).
**Common AI misuse:** Infinite scroll on an admin table with bulk selection.

## Stepper

**What:** Progress indicator for a multi-step task.
**Use when:** Three to about seven sequential steps (checkout, onboarding, setup wizards).
**Avoid when:** The task fits on one page; steps are not truly sequential.
**Archetypes:** ECOMMERCE, APPLICATION.
**Tradeoffs:** Sets expectations; adds navigation complexity (back, edit previous step).
**Accessibility:** Current step marked with `aria-current="step"`; completed and error states
conveyed in text, not only color (A11Y-08).
**Common AI misuse:** A three-step "How it works" graphic styled as a stepper on a marketing page
when the product has no such flow (IN-06).

## Skip links

**What:** A link at the start of the page that jumps to main content.
**Use when:** Any page with navigation before the main content, especially long sidebars and headers.
**Archetypes:** All.
**Accessibility:** Visible on focus; targets the `<main>` element (A11Y-02, A11Y-14).

```html
<a class="skip-link" href="#main">Skip to content</a>
<main id="main" tabindex="-1">...</main>
```

```css
.skip-link { position: absolute; inset-inline-start: 1rem; inset-block-start: -3rem; }
.skip-link:focus-visible { inset-block-start: 1rem; }
```

## Adapting navigation across widths

Guidance, not a fixed matrix. Choose transitions by the number of destinations and how often
they are used:

| Available width | Common pattern for apps | Common pattern for sites |
|-----------------|-------------------------|--------------------------|
| Narrow (phone) | Bottom tab bar for 3 to 5 primaries, menu for the rest | Menu button with label, primary CTA visible |
| Medium (tablet, small laptop) | Icon rail with tooltips, or collapsible sidebar | Condensed top nav, overflow in a "More" menu |
| Wide | Full sidebar, optional secondary panel | Full top nav |

Set the switch points where items stop fitting, not at device widths (RS-15). When navigation
changes form at a breakpoint, keep the user's place and open state sensible (RS-13).
