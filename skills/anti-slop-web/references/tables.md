# Tables

Data tables: when to use them, markup, density, sorting, selection, actions, large data, and
small screens. Load for DASHBOARD, OPERATIONS, DATA_EXPLORATION, and data-heavy APPLICATION
screens. The project's `DESIGN.md` and design system override everything here.

## Table, list, or cards?
**What:** Choosing the container for a collection of records.
**Use when:**
- Table: users compare records across the same attributes, sort, or scan a column.
- List: records have one or two key attributes and users act on them one at a time (inbox,
  notifications).
- Cards: records are visual (products, media), heterogeneous, or need rich previews.
**Avoid when:**
- Cards for tabular data in dense tools; comparison across cards is slow.
- Tables for three-field records on mobile-first products.
**Archetypes:** Tables suit OPERATIONS, DATA_EXPLORATION, DASHBOARD, APPLICATION, DEVELOPER_TOOL.
Cards suit ECOMMERCE and media.
**Tradeoffs:**
- One collection can offer both views (grid and table toggle) when users genuinely differ.
**Accessibility:**
- Whatever the visual, tabular data needs table semantics so relationships between cells and
  headers are exposed (A11Y-11).
**Common AI misuse:** Div grids styled as tables; generic columns (Name, Status, Date, Actions)
chosen from the component, not the data.

## Semantic markup and scroll regions
**What:** Real `table`, `thead`, `th` with `scope`, a caption, and a focusable scroll container
when the table is wider than the viewport.

```html
<div class="table-scroll" role="region" aria-labelledby="orders-caption" tabindex="0">
  <table>
    <caption id="orders-caption">Open orders, sorted by due date</caption>
    <thead>
      <tr>
        <th scope="col" aria-sort="ascending">
          <button type="button">Due</button>
        </th>
        <th scope="col"><button type="button">Customer</button></th>
        <th scope="col" class="num">Amount</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><time datetime="2026-10-07">7 Oct</time></td>
        <th scope="row">Northwind Traders</th>
        <td class="num">1,240.00</td>
      </tr>
    </tbody>
  </table>
</div>
```

```css
.table-scroll { overflow-x: auto; }
.table-scroll:focus-visible { outline: 2px solid var(--focus-ring); }
.num { text-align: right; font-variant-numeric: tabular-nums; }
```

Notes: `aria-sort` goes only on the currently sorted column. The sort control is a button inside
the header, not a click handler on the `th`. The region is focusable so keyboard users can scroll
it (A11Y-02, A11Y-11).

## Alignment and numbers
**What:** Text left, numbers right, with tabular figures and consistent precision.
**Use when:**
- Numeric columns that users compare or total.
**Tradeoffs:**
- Right alignment lets digits line up by place value. Keep decimals consistent within a column.
- Units belong in the header ("Amount (USD)") rather than in every cell, unless units vary.
- Rounding helps summaries; OPERATIONS and finance usually need exact values.
**Accessibility:**
- Do not encode negative values only in red; use a minus sign or parentheses (A11Y-08).
**Common AI misuse:** Centered numbers in proportional figures that jitter as they update.

## Density and row height
**What:** Row height and padding matched to DENSITY.
**Use when:**
- Comfortable rows (around 48 to 56px) for occasional users and touch.
- Compact rows (around 32 to 40px) for power users scanning many records.
**Tradeoffs:**
- Zebra striping helps track wide rows across many columns; dividers alone are calmer and avoid
  clashing with hover and selection colors. Pick one primary row distinction.
- Compact rows still need interactive targets that meet minimum size (A11Y-12).
**Archetypes:** OPERATIONS and DATA_EXPLORATION tend compact; APPLICATION tends comfortable.
**Common AI misuse:** Shrinking text instead of padding to fit more rows.

## Sticky headers and first column
**What:** Headers that stay visible on vertical scroll; the identifying column visible on
horizontal scroll.
**Use when:**
- Long tables, and wide tables where users lose track of which row they are on.
**Tradeoffs:**
- Sticky elements take space on small screens; consider dropping the sticky column below a width.
**Accessibility:**
- Sticky positioning does not change semantics; ensure focused cells are not hidden under sticky
  headers (scroll padding).

## Sorting and filtering
**What:** Reordering and narrowing rows.
**Use when:**
- Users look for extremes or specific records.
**Tradeoffs:**
- Default sort should match the job (most urgent first in OPERATIONS, most recent in feeds).
- Show the active sort and filters visibly; a forgotten filter hides records.
- Client-side sorting is instant but only correct if all data is loaded; with pagination, sort on
  the server.
**Accessibility:**
- Announce result counts after filtering through a polite live region (A11Y-13).
- `aria-sort` reflects the current state (A11Y-17).

## Selection and bulk actions
**What:** Checkboxes per row plus an action bar for selected rows.
**Use when:**
- Users act on many records at once.
**Tradeoffs:**
- "Select all" should state whether it means this page or all matching records.
- A floating action bar is discoverable but can cover content; reserve space for it.
- Bulk destructive actions need confirmation naming the count and consequence, or undo (FN-05).
**Accessibility:**
- Row checkboxes have names that identify the row ("Select order 1042") (A11Y-06).
- The header checkbox exposes a mixed state when some rows are selected (A11Y-17).

## Row actions
**What:** Actions on a single row: inline buttons, a menu, or opening the record.
**Use when:**
- One or two frequent actions can be inline; more go in a menu.
**Tradeoffs:**
- Hover-revealed actions keep rows clean but are invisible on touch and to keyboard users until
  focused; show them on focus too, or keep them visible (RS-03).
- Destructive actions go last in menus and are visually distinct.
**Accessibility:**
- Menu buttons have names that include the row ("Actions for order 1042").
**Common AI misuse:** A three-dot menu on every row containing actions that do nothing (FN-01).

## Pagination, infinite scroll, and virtualization
**What:** Strategies for many rows.
**Tradeoffs:**
- Pagination supports jumping, sharing positions, and stable selection; suits admin and records.
- Load-more or infinite scroll suits feeds; it complicates footers, selection, and returning to a
  position.
- Virtualization renders only visible rows; it is necessary for very large client-side tables but
  breaks browser find, printing, and some assistive technology. Expose total counts and ensure
  rows are announced correctly.
**Archetypes:** Pagination for APPLICATION and OPERATIONS records; virtualization for
DATA_EXPLORATION.

## Inline editing
**What:** Editing cell values in place.
**Use when:**
- Frequent small edits by expert users (spreadsheets, admin consoles).
**Avoid when:**
- Edits need validation across fields or have consequences; use a form or drawer.
**Tradeoffs:**
- Clear edit affordance, explicit save or autosave with visible status, and error display at the
  cell (FN-04).
**Accessibility:**
- Editable cells need keyboard entry and exit (Enter, Escape) and announced validation errors
  (A11Y-07). Grid patterns with arrow-key navigation are substantial work; follow the WAI-ARIA
  grid pattern fully or do not claim it.

## Table states
- **Loading:** skeleton rows matching column widths for first load; for refreshes, keep rows and
  show a small updating indicator.
- **Empty:** first-run versus filtered-to-nothing messages, with the relevant action (FN-03).
- **Error:** inline message with retry; keep the header so users know what failed.
- **Partial:** mark rows or columns that failed to load.

## Small screens
**What:** Strategies when the table does not fit (RS-08).
- **Scroll region:** keep the table, make it a focusable horizontal scroll region with a visible
  cue that more columns exist. Best for true comparison tables.
- **Priority columns:** hide low-priority columns at narrow widths, with a way to see the full
  record.
- **Stacked rows:** each row becomes a block of label and value pairs. Good for records read one
  at a time; poor for comparison. Keep table semantics or provide equivalent structure.
- **Summary then detail:** a list of key fields that opens the full record.
**Common AI misuse:** Letting a wide table overflow the page, causing horizontal page scroll (RS-01).
