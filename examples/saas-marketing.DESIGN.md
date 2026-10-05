# Product Design Direction

<!-- Fictional example. Illustrates reasoning; do not copy values as a preset. -->

Status: confirmed
Owner: Ledgerline (fictional) marketing lead
Last updated: 2026-09-12
Sources inspected: Brand guide v2 (logo, two brand colors, wordmark face), existing product
screenshots, current marketing site (WordPress theme, being replaced), sales call notes with the
ten most frequent prospect questions.

## 1. Product context

Product: Ledgerline (fictional), month-end close software that reconciles bank feeds against the
general ledger for finance teams of 5 to 50 people.
Audience: Controllers and finance managers at mid-size companies; skeptical of automation claims,
evaluated by IT and auditors.
Primary tasks: Understand what the product reconciles and how; see real screens; book a demo or
start a trial.
Environment: Office desktops and laptops during work hours; links forwarded by email to colleagues.
Device priority: Desktop first; mobile must read well because forwarded links are opened on phones.
Minimum width 320px.
Archetype: MARKETING

## 2. Design dials

VARIANCE: 6 | Sections have different jobs (process, proof, pricing); varied composition helps,
but the audience values order and calm.
MOTION: 4 | Motion explains the reconciliation flow; nothing ambient.
DENSITY: 3 | One idea per section for a skeptical reader; detail lives behind links.
CHARACTER: 7 | The category is full of interchangeable blue SaaS sites; a recognizable, owned
look supports recall in a long sales cycle.

## 3. Design intent

The interface should feel:
- Exact, like a well-kept ledger
- Calm and confident without boasting
- Transparent about how the product works

The interface should NOT feel:
- Like a generic AI startup page
- Salesy or hyped
- Playful or casual about money

## 4. Signature element

Signature: The "tick-mark trail": the accountant's reconciliation tick mark, drawn in the brand
green, used to mark matched items in a real anonymized reconciliation shown in the hero and reused
as the list marker and step indicator throughout the site.
Layer: content and visual
Why it belongs to this product: Tick marks are what accountants physically write when they
reconcile by hand; the product automates exactly that act.
Sustained in: hero product image, process section step markers, pricing feature lists, success
state of the demo form.

## 5. Palette

Primary: Ledger green #1F5E4A | primary actions, focus ring, tick marks
Neutral: warm grays from #FAF8F4 (page) to #1C1B19 (text) | surfaces, text, borders
Accent: Paper #F1EBDD | one alternating band for the pricing section only
Semantic colors: success #1F7A3D, warning #8A5A00, danger #A42A2A, info #2D5B8C | form states only
Data colors: none beyond green and grays (no charts on the marketing site)
Theme behavior: light only; marketing site read in offices, and the paper motif depends on it
Contrast verified: text #1C1B19 on #FAF8F4 16.22:1; green #1F5E4A on #FAF8F4 7.17:1; white on
green 7.61:1 (computed with contrast.py)

## 6. Typography

Display: Source Serif 4 semibold | echoes printed financial statements; brand guide specifies it
Body: Source Sans 3 | high legibility, wide language support, pairs with the serif family
Mono: none on the marketing site
Hierarchy: 1.25 scale; H1 clamp(2.25rem, 1.8rem + 2vw, 3.5rem); body 1.0625rem
Measure: 64ch for prose
Numerals: tabular figures in the hero reconciliation and pricing
Loading: self-hosted, Latin subset, font-display swap with metric-matched fallbacks

## 7. Layout principles

App shell: top nav with five real destinations (Product, Pricing, Security, Docs, Sign in)
Grid: 12 columns at wide widths, intrinsic stacking below
Content widths: prose 64ch, standard 1120px, product images up to 1280px
Density strategy: one message per section; supporting detail linked
Navigation: sticky top bar that shrinks on scroll; menu button labeled "Menu" on small screens
Responsive collapse: hero splits text and product image above about 960px and stacks below with the
image after the headline; breakpoints placed where line lengths break

## 8. Component language

Radius: 4px on inputs and buttons, 8px on images and panels; no pills except tags
Borders: 1px warm gray; borders separate, shadows rarely used
Shadows: only on the sticky nav after scroll and on dialogs
Cards: avoided for features; the process is a numbered vertical sequence
Inputs: label above, help text below label, error below field
Tables: pricing comparison table with row headers
Buttons: one filled primary per section ("Book a 30-minute demo"), secondary as text link
Menus: none beyond mobile nav
Modals: none; demo booking is a page
Component library: custom, small

## 9. Motion

Purpose: show the matching process step by step
Timing: 200ms ease-out for UI feedback; the process diagram advances 400ms per step when scrolled
into view, once
Allowed animation: tick marks drawing on matched rows; focus and hover transitions
Ambient animation: none
Reduced-motion behavior: tick marks appear already drawn; process shown in final state
Implementation tier: CSS plus scroll-driven animations with a static fallback

## 10. Data visualization

Not applicable; the marketing site shows real product screenshots, not charts.

## 11. Required states

Loading: demo form submit shows "Booking..." on the button; calendar slots load with a labeled
skeleton list
Empty: no available slots this week shows the next available week and an email option
Error: submission failure keeps all fields and offers retry plus a direct email address
Partial data: n/a, no data views
Offline: form shows "You appear to be offline. Your details are kept; try again when connected."
Permission denied: n/a
Success: confirmation page names the booked time, time zone, and who will attend, with a
calendar file
Disabled: submit stays enabled; validation explains what is missing on submit

## 12. Explicit project bans

- No testimonials, customer logos, or customer counts until real, approved ones are supplied
  (IN-01, IN-02). The proof section uses the security documentation and a real anonymized
  reconciliation instead.
- No time-saved or accuracy percentages until the owner provides a sourced figure.
- No stock photos of people at laptops.

## 13. Allowed exceptions

No waivers recorded. Two decisions look like common tells but pass on their own
"Acceptable when" clauses, so they are noted here for reviewers rather than waived:

- UI-02 Template page skeleton: PASS. The page keeps the conventional order (hero, how it
  works, security, pricing, FAQ, demo) because it matches the sequence of questions in the
  sales call notes, and every section has real content; the FAQ is built from those notes.
- UI-25 Template pricing: PASS. The product genuinely has three plans; the middle plan is
  highlighted because it is the plan most current customers are on, per billing data supplied
  by the owner.
