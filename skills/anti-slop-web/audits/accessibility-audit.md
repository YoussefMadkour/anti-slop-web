# Accessibility Audit

Workflow step 10. Rules: `../../anti-slop-a11y/SKILL.md` (A11Y-01 to A11Y-19). Target: WCAG 2.2 AA.
Accessibility findings are never waived for aesthetic reasons.

Report honestly which checks were performed by running the UI, which by reading code, and which
were not performed. Automated tools find a minority of issues; they support this audit, they do
not replace it.

## 1. Keyboard pass (run the UI)
Unplug the mouse mentally. From the address bar:
- [ ] Tab reaches every interactive element in an order that matches the visual order (A11Y-02)
- [ ] Focus is always visible, including on custom components and inside dialogs (A11Y-03)
- [ ] Enter and Space activate buttons; Enter follows links; arrow keys work in menus, tabs,
      radio groups, and listboxes (A11Y-01, A11Y-02)
- [ ] Escape closes dialogs, menus, and popovers; focus returns to the trigger (A11Y-09)
- [ ] No keyboard trap; a skip link exists where navigation repeats (A11Y-02)
- [ ] Sticky headers never cover the focused element (A11Y-03)

## 2. Semantics and names (inspect the DOM or accessibility tree)
- [ ] Buttons are `<button>`, links are `<a href>`, inputs are native or full ARIA patterns (A11Y-01)
- [ ] Every control has an accessible name containing its visible label (A11Y-06)
- [ ] One `<h1>`; heading levels nest; landmarks present and labeled when repeated (A11Y-14)
- [ ] `lang` set; each view has a unique title, including client-side routes (A11Y-19)
- [ ] Toggle, expanded, selected, and current states are exposed (A11Y-17)
- [ ] Images have appropriate alt text; decorative images have empty alt (A11Y-15)

## 3. Color and contrast (compute, do not estimate)
Use `../../anti-slop-a11y/scripts/contrast.py`.
- [ ] Body text, labels, placeholders shown as hints, links, and button text: 4.5:1 or 3:1 for
      large text, in every theme (A11Y-04)
- [ ] Text over images or gradients checked at the worst point (A11Y-04)
- [ ] Input borders, icons, focus rings, chart marks, and status indicators: 3:1 (A11Y-05)
- [ ] No meaning carried by color alone (A11Y-08)

Record the pairs checked: `#6b7280 on #ffffff: 4.83:1 PASS (secondary text)`.

## 4. Forms
- [ ] Persistent visible labels; required fields indicated in text, not color alone
- [ ] Errors linked to fields (`aria-describedby`), `aria-invalid` set, message explains the fix
      (A11Y-07)
- [ ] Failed submit moves focus to an error summary or the first invalid field; input preserved
- [ ] Success and pending states announced (A11Y-13)
- [ ] `autocomplete` attributes on personal data fields

## 5. Dynamic content and overlays
- [ ] Modal dialogs contain focus, have an accessible name, block the background (A11Y-09)
- [ ] Toasts and async results use live regions; actionable toasts are keyboard reachable (A11Y-13)
- [ ] Tooltips appear on focus too, stay on hover, dismiss with Escape (A11Y-16)

## 6. Motion
- [ ] With `prefers-reduced-motion: reduce` enabled, spatial motion is removed or replaced and
      no content is hidden (A11Y-10)
- [ ] Anything moving or auto-updating for more than five seconds can be paused (A11Y-10)
- [ ] Nothing flashes more than three times per second (A11Y-10)

## 7. Data
- [ ] Data tables use `<table>`, `<th scope>`, captions or labels; sort state uses `aria-sort` (A11Y-11)
- [ ] Charts have a name stating the insight and a table or text alternative (A11Y-18)

## 8. Targets and zoom
- [ ] Targets at least 24 by 24 px or adequately spaced; primary touch controls about 44 px (A11Y-12)
- [ ] 200 percent text zoom and 400 percent page zoom: covered in the responsive audit (RS-11)

## Output

```
Accessibility: PASS | FAIL
Verified by running: keyboard pass, contrast (14 pairs), reduced motion
Verified by code reading: dialog focus handling, live regions
Not verified: screen reader announcement wording (manual check recommended)
Findings: <numbered list in the design-audit format>
```
