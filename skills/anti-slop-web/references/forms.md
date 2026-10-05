# Forms

Labels, validation, errors, control choice, multi-step flows, and submission feedback. Load for
any form-heavy work (sign-up, checkout, settings, data entry) together with `components.md` and
the `anti-slop-a11y` skill. The project's `DESIGN.md` and design system override everything here.

Forms are where generated UI most often fails functionally: inputs render, but nothing validates,
errors are red borders, and submission gives no feedback (FN-04).

## Labels
**What:** A visible, persistent label for every input.
**Use when:**
- Always for data entry (A11Y-06).
**Tradeoffs:**
- Top-aligned labels scan fastest, survive long translations, and work at every width. They are
  the default to beat.
- Left-aligned labels suit dense settings screens on wide displays where vertical space matters;
  they reflow poorly on small screens.
- Floating labels save space but shrink the label to small text, can lower contrast, and are easy
  to break with autofill. They are acceptable when the label stays visible, readable, and
  contrast-compliant in every state. Placeholder-only labels are not acceptable: the label
  disappears on input and placeholder text usually fails contrast.
**Accessibility:**
- Programmatically associate labels (`<label for>`), including for checkboxes and radios.
**Common AI misuse:** Placeholder text as the only label; placeholders filled with fake data
("John Doe") that look like entered values (IN-04).

## Help text and required fields
**What:** Hints about format or purpose, and marking which fields are required or optional.
**Use when:**
- Help text for format constraints ("At least 12 characters") before the user errs, not only after.
**Tradeoffs:**
- If most fields are required, mark the optional ones; if most are optional, mark the required
  ones. Explain the marker once.
- Ask only for what you need. Every optional field is friction.
**Accessibility:**
- Connect help text with `aria-describedby`. Do not convey "required" only with a red asterisk
  color; use the `required` attribute and text (A11Y-08).

## Validation timing
**What:** When to check input and show errors.
**Tradeoffs:**
- On submit: simplest, least intrusive; users find all errors at once.
- On blur (leaving a field): catches errors near their cause; avoid firing on fields the user has
  not touched.
- While typing: useful for confirming success (password strength, username available); hostile
  for errors, because users see "invalid email" before they finish typing.
- A common blend: validate on blur after the first interaction, re-validate while typing once a
  field has an error so users see it clear.
- Server validation is always required; client validation is a convenience.

## Error messages and error summary
**What:** Messages that say what is wrong and how to fix it, next to the field, plus a summary for
long forms.
**Use when:**
- Every field that can fail (FN-04).
**Tradeoffs:**
- "Enter a date in the format DD/MM/YYYY" beats "Invalid input". Avoid blame and jargon.
- For forms longer than a screen, an error summary at the top with links to each field helps
  users find problems; move focus to it after a failed submit.
**Accessibility:**
- Mark invalid fields with `aria-invalid` and connect the message with `aria-describedby`
  (A11Y-07). Pair the red border with an icon and text (A11Y-08).

```html
<label for="email">Work email</label>
<p id="email-hint" class="hint">We send the invoice here.</p>
<input id="email" name="email" type="email" autocomplete="email"
       aria-invalid="true" aria-describedby="email-hint email-error">
<p id="email-error" class="error">Enter an email address like name@company.com</p>
```

**Common AI misuse:** Errors shown only as a red border; generic "Something went wrong" (CP-09).

## Input types, autocomplete, and mobile keyboards
**What:** The right `type`, `autocomplete`, and `inputmode` for each field.
**Tradeoffs and notes:**
- `type="email"`, `type="tel"`, `type="url"` change mobile keyboards and enable browser help.
- `inputmode="numeric"` with `pattern` suits codes and card numbers; `type="number"` suits true
  quantities and has awkward spinner and scroll behavior for identifiers.
- `autocomplete` tokens (`name`, `email`, `street-address`, `one-time-code`, `new-password`) speed
  entry and help users with motor and memory impairments.
- Do not split single values (phone, date) into many boxes unless the format is truly fixed;
  pasting breaks.
**Accessibility:**
- Correct `autocomplete` is part of WCAG 2.2 (input purpose).

## Grouping
**What:** `fieldset` and `legend` for related controls; sections with headings for long forms.
**Use when:**
- Radio groups and checkbox groups always need a group label.
- Address blocks, payment details, and other clusters.
**Accessibility:**
- The legend is read with each control in the group.

## Choosing controls
| Situation | Usually fits | Notes |
|---|---|---|
| One of 2 to 5 options, all worth seeing | Radio group | Visible options aid comparison |
| One of many fixed options | Select | Native select is accessible and mobile-friendly |
| One of very many, searchable | Combobox | Follow the WAI-ARIA combobox pattern, or use a tested library |
| Several independent on/off choices | Checkboxes | Submit with the form |
| A setting that applies immediately | Switch | Implies instant effect; do not use inside forms that need Save |
| A single agreement | One checkbox | Never pre-checked for consent |
| A number in a small range | Stepper or slider | Sliders are imprecise; pair with a text input |

**Common AI misuse:** Switches everywhere because they look modern; custom div dropdowns without
keyboard support (A11Y-01, A11Y-02).

## Date inputs
**Tradeoffs:**
- Native date inputs are accessible and mobile-friendly but vary in look across browsers.
- Custom date pickers need full keyboard support and a typed alternative; memorable dates such as
  birth dates are faster to type than to pick.
- Ranges need presets for common periods (see `dashboards.md`) and clear time zone handling.

## File upload
**Tradeoffs:**
- A drop zone is a convenience; a real file input button must remain available for keyboard and
  touch users.
- State accepted types and size limits before upload. Show per-file progress, errors, and remove
  actions. Keep uploaded files if another field fails validation.

## Password fields
**Tradeoffs:**
- A show/hide toggle reduces errors. Allow paste so password managers work.
- Show requirements up front. Avoid arbitrary composition rules; length matters most.
- Use `autocomplete="new-password"` on sign-up and `current-password` on sign-in.

## CAPTCHA and bot protection
**Tradeoffs:**
- Visual and audio puzzles exclude many users. Prefer invisible or low-friction methods (rate
  limiting, honeypot fields, risk-based challenges) and provide an accessible alternative path
  when a challenge is unavoidable.

## Multi-step forms
**What:** Splitting long processes into steps.
**Use when:**
- Steps are logically distinct and later steps depend on earlier answers.
**Avoid when:**
- The form is short; steps add clicks and hide the total effort.
**Tradeoffs:**
- Show progress (step 2 of 4) and let users go back without losing data.
- Validate per step; a review step before final submission reduces errors in high-stakes flows.
**Accessibility:**
- Move focus to the new step's heading and update the page title (A11Y-19).

## Long forms and drafts
- Save drafts automatically or explicitly for forms that take more than a few minutes; show save
  status ("Saved 2 minutes ago").
- Warn before navigating away with unsaved changes.
- Preserve every entered value after a validation or server error. Clearing a form after an error
  is a functional defect (FN-04).

## Submission feedback
**What:** Pending, success, and failure states for submit.
**Use when:**
- Every form that sends data (FN-04).
**Patterns:**
- Pending: disable resubmission, show progress on the button or near it, keep the label readable
  ("Saving...").
- Success: confirm what happened and what happens next ("Invoice sent to finance@northwind.example.
  You will get a copy."). Move focus or announce it (A11Y-13).
- Failure: say what failed, keep the input, offer retry.
**Common AI misuse:** A submit handler that only logs to the console (CD-02).

## Destructive actions
**What:** Deleting, cancelling, revoking, overwriting.
**Patterns (FN-05):**
- Prefer undo for frequent, recoverable actions.
- For irreversible actions, a confirmation dialog that names the object and the consequence, with
  the destructive button labeled by the action ("Delete project") rather than "OK".
- For very high stakes, type-to-confirm (the project name).
- Separate destructive actions spatially from routine ones (a danger zone in settings).
**Accessibility:**
- Confirmation dialogs follow dialog behavior: focus moves in, Escape cancels, focus returns
  (A11Y-09).

## Inline editing
For editing values in place in lists and tables, see `tables.md`. Make edit mode obvious, show
save status, and surface errors at the field.

## Checklist
- Every input has a visible label and correct `type` and `autocomplete`.
- Errors say how to fix, sit next to the field, and are programmatically associated.
- Input survives errors; pending, success, and failure states exist.
- Destructive actions have undo or confirmation.
- The form works with keyboard only and on a phone with the on-screen keyboard open (RS-03).
