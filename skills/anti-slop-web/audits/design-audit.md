# Design Audit

Workflow step 9. Checks the build against `DESIGN.md` and the rule catalogs. Run it on your own
output before delivery, or on an existing UI when asked to review.

## Inputs

- `DESIGN.md` (direction, dials, signature, bans, waivers in §13)
- The rendered UI: run it if at all possible; screenshots at narrow and wide widths help
- `../rules.md` (IN, FN, UI, CL) and, as relevant, `../../anti-slop-copy/SKILL.md` (CP) and
  `../../anti-slop-code/SKILL.md` (CD)

If there is no `DESIGN.md`, audit against the product context you can establish and note
"no recorded direction" as a remaining risk. Do not invent a direction and then fail the UI
for not matching it.

## Procedure

### 1. Direction check
For each view, answer in one line each:
- What is this view's job, and is the most important thing the most prominent? (UI-06)
- Does the view read as the declared VARIANCE, MOTION, DENSITY, and CHARACTER bands? (UI-27)
- Is the signature element present, single, and sustained, or is restraint executed rigorously?
  Name it in one sentence without looking at the code. (UI-27)
- Does it respect the brand and the explicit bans in `DESIGN.md` §12?
- Swap test, for MARKETING and CHARACTER 5 or above: if the logo and product name were swapped
  for a competitor's, would anything still feel specific to this product? If not, look for the
  cause in UI-02, UI-03, UI-08, UI-22, and CP-01.

### 2. Integrity scan (always)
Every number, name, quote, logo, claim, badge, and asset: where did it come from? Anything not
supplied by the owner or real data is IN-01 to IN-06. This scan is not optional and P0 findings
here cannot be waived.

### 3. Function scan (always)
Every control does something real (FN-01). Every data view and form has its states (FN-02 to
FN-04). Destructive actions are safeguarded (FN-05). Every shipped theme works (FN-06).

### 4. Visual and copy scan (scoped)
Walk the UI rules and CP rules that are **in scope for the archetype** (see `../archetypes.md`).
For each candidate finding:
1. Is there a reason? Check `DESIGN.md`, brand, content, and archetype. If the rule's
   "Acceptable when" applies, it passes (record PASS with the reason, not a waiver).
2. Is it waived in §13? Mark `WAIVED` and move on.
3. Otherwise record it with evidence.

Do not flag a convention because it is common. Flag it when it contradicts the content or the
direction, or when it appears as part of a cluster.

### 5. Cluster check
Count unexplained, in-scope UI and CP tells per view (each issue once). Three or more with at
least one MEDIUM: add one CL-01 finding (HIGH) listing them.

### 6. Code scan (when implementation is in scope)
Walk CD rules against the changed files. Limit findings to what affects users, maintainability
of the UI, or the delivery claims.

## Finding format

Number findings so the user can choose which to fix.

```
1. UI-03 Uniform feature cards | HIGH | FAIL
   Evidence: /features, six identical cards; "Audit log export" and "Dark mode" get equal weight.
   Fix: lead with audit log export as a full-width section with a real screenshot; list the rest.

2. UI-08 Default AI palette | HIGH | WAIVED
   Waiver: DESIGN.md §13, brand guide v3 specifies indigo as primary.

3. IN-02 Invented metrics | P0 | FAIL
   Evidence: hero shows "12,000+ teams"; no source supplied.
   Fix: remove, or replace with [REAL DATA: active teams] and ask the owner.
```

Order findings P0, HIGH, MEDIUM, LOW. Keep LOW findings brief; they never block delivery.

## Rules of conduct

- **Reasons over rules.** A finding with a plausible recorded reason is not a finding.
- **No novelty as a fix.** Never resolve a template tell by making the interface stranger (UI-01).
- **Mature UIs.** When auditing an established product, flag regressions and real defects; do not
  propose a redesign because the existing style differs from this kit's heuristics.
- **Do not re-fix waivers.** If a waived decision now causes a real defect (for example a brand
  color that fails contrast), report the defect under its own rule (A11Y-04), not the waived one.
- **Evidence.** Every FAIL cites where and what. Every PASS on a P0 rule is backed by what was
  checked.
