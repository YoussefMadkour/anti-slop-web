# Responsive Audit

Workflow step 10. Rules: `../../anti-slop-responsive/SKILL.md` (RS-01 to RS-15).

Run the UI and resize it. Screenshots at fixed widths are samples; the real test is dragging the
viewport slowly from the narrowest supported width to the widest and watching where it breaks.

## 1. Widths to check
Minimum: 320, 375, 768, 1024, 1280, and 1440 or wider. Plus the full drag-through. Add any width
named in `DESIGN.md` §1 (device priority) or §7 (responsive collapse).

At each width:
- [ ] No horizontal page scroll; check `scrollWidth` versus `clientWidth` (RS-01)
- [ ] Nothing important hidden or clipped (RS-02)
- [ ] The layout is a designed state, not a squeezed one (RS-04)
- [ ] Spacing and type are in an appropriate register for the width (RS-06)

## 2. Touch pass
Use touch emulation or a device.
- [ ] Every hover interaction has a tap equivalent; nothing requires drag only (RS-03)
- [ ] Navigation opens, closes, and is usable with one thumb (RS-03, RS-07)
- [ ] Focus an input near the bottom: the keyboard does not cover it (RS-03)
- [ ] Fixed or sticky bars do not cover the last content or the primary action; safe areas
      respected (RS-14)
- [ ] Primary touch controls about 44 px with spacing (RS-07, A11Y-12)

## 3. Content-specific checks
- [ ] Each table has a strategy at narrow widths: scroll region, priority columns, or stacked
      rows (RS-08)
- [ ] Charts remain readable: labels, ticks, legend, tap to inspect (RS-09)
- [ ] Dense tools: the small-screen job is clear and surfaced first (RS-10)
- [ ] Long strings (URLs, IDs, emails, code) wrap or scroll inside their container (RS-01)

## 4. Zoom and reflow
- [ ] Browser text zoom 200 percent: no clipping or overlap (RS-11, RS-12)
- [ ] Page zoom 400 percent at 1280 px width (320 CSS px): single-direction scrolling except for
      maps, diagrams, and wide data tables (RS-11)

## 5. Transitions between states
- [ ] Resize and rotate mid-task: form input, selection, open panels, and scroll position survive
      (RS-13)
- [ ] Breakpoints sit where content breaks, not only at device widths (RS-15)

## Output

```
Responsive: PASS | FAIL
Widths checked: 320, 375, 768, 1024, 1280, 1440, drag-through
Touch: emulated (device not available)
Zoom: 200% text PASS, 400% page PASS
Findings: <numbered list in the design-audit format>
```
