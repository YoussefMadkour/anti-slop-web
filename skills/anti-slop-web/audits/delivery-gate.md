# Delivery Gate

Workflow step 11. The last thing produced before handing work over. Compact by design: one line
per gate, then waivers, remaining risks, and a status. Detailed findings live in the audit
outputs; the gate summarizes them.

## Gates

| Gate | PASS means | Evidence expected |
|------|-----------|-------------------|
| Design direction | `DESIGN.md` exists or was updated; the build reads as the declared dials; signature present or restraint executed (UI-27) | Dials and signature named in one line |
| Brand alignment | Brand tokens, type, and voice applied; no unrequested clone (UI-26, UI-28) | Token source named |
| Content integrity | No fabricated proof, metrics, claims, or disguised placeholders (IN-01 to IN-06) | "All numbers and quotes supplied by owner" or list of labeled placeholders |
| Visual system | Type, color, shape, spacing, and components follow the project's system; no open UI-29 to UI-32 finding above LOW | Inventory counts (type sizes vs scale, raw colors, distinct radii, component sources) |
| Responsive | Responsive audit passed (RS rules) | Widths checked |
| Accessibility | Accessibility audit passed (A11Y rules) | What was run versus read |
| Required states | Every state in `DESIGN.md` §11 built for every relevant surface (FN-02 to FN-04) | States listed per surface |
| Performance | Lightest motion tier, transform and opacity animation, no layout shift sources, no unneeded client JS, dependencies verified (CD-01, CD-04, CD-09, CD-10) | Notable checks |
| Anti-slop | Design audit has no unwaived P0 or HIGH findings (UI, CP, CL) | Count by severity |

Each gate is `PASS`, `FAIL`, or `N/A` (with a reason).

## Status logic

- **DO NOT SHIP** if any P0 finding is open, in any catalog. P0 cannot be waived.
- **DO NOT SHIP** if any HIGH finding is open and not waived in `DESIGN.md` §13.
- **DO NOT SHIP** if any finding is a WCAG 2.2 Level A or AA failure, whatever its severity
  label, or if the Accessibility or Responsive gate is FAIL. These cannot be waived.
- **SHIP AS PROTOTYPE** if the only open issues are clearly labeled placeholders (missing real
  content, sample data) or a `Status: proposed` direction awaiting confirmation. Say what must
  happen before it can ship.
- **SHIP** otherwise. MEDIUM and LOW findings never block delivery on their own; list MEDIUM
  findings under remaining risks if unfixed.

Never report PASS for a check that was not performed. "Not verified" is an honest and acceptable
entry under remaining risks.

## Template

```
# Delivery Gate

Design direction: PASS (VARIANCE 3 / MOTION 1 / DENSITY 9 / CHARACTER 5; signature: shape-coded status language)
Brand alignment: PASS (tokens from packages/theme)
Content integrity: PASS (all figures from live API; no testimonials)
Visual system: PASS (type 6/6 sizes on scale, 0 raw colors, radii 3/3, one component source)
Responsive: PASS (320 to 1920, drag-through, touch emulated)
Accessibility: PASS (keyboard pass, 18 contrast pairs computed, reduced motion checked)
Required states: PASS (loading, empty, error, partial, offline, permission on all four panels)
Performance: PASS (no new client components above leaf level; CSS-only transitions)
Anti-slop: PASS (0 P0, 0 HIGH, 2 MEDIUM, 1 LOW)

Waivers:
- UI-08 Default AI palette: brand guide v3 specifies indigo as primary (DESIGN.md §13).

Notes:
- UI-12 passes without a waiver: dark theme is in scope for a control room.
- MOTION set to 1 because the product is an operations console; no entrance animation.

Remaining risks:
- Chart empty state not tested with live data.
- Keyboard navigation of the command menu needs manual verification with a screen reader.
- MEDIUM UI-15: section spacing on settings pages is uneven.

Final status: SHIP
```
