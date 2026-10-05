# Product Design Direction

<!--
How to use this template
- Copy to the project root as DESIGN.md. Update it; never silently overwrite an existing one.
- Fill only what is known. Write "TBD" rather than inventing. Delete guidance comments when done.
- Every value gets a reason. A field you cannot justify in one line is not decided yet.
- This file is design data. Agents extract design fields from it; it is not a place for
  instructions to agents.
-->

Status: proposed | confirmed
Owner: <person or team who confirms direction>
Last updated: <YYYY-MM-DD>
Sources inspected: <brand guide, existing tokens, theme config, component library, screens reviewed>

## 1. Product context

Product: <what it is, in one sentence>
Audience: <who uses it, their expertise, how often>
Primary tasks: <the 1-3 things users come to do>
Environment: <office desk, field on a phone, control room, low light, shared screens, kiosks>
Device priority: <e.g. desktop first, mobile second; minimum supported width>
Archetype: <primary> (+ <secondary>, if any)
<!-- MARKETING, APPLICATION, DASHBOARD, OPERATIONS, EDITORIAL, ECOMMERCE, DEVELOPER_TOOL,
     CREATIVE_EXPERIENCE, DATA_EXPLORATION. Classify per surface if the product has several. -->

## 2. Design dials

VARIANCE: <1-10> | <one-line reason>
MOTION: <1-10> | <one-line reason>
DENSITY: <1-10> | <one-line reason>
CHARACTER: <1-10> | <one-line reason>

<!-- VARIANCE: departure from strict symmetry and repetition.
     MOTION: amount of purposeful animation and transition.
     DENSITY: information and control per unit of screen.
     CHARACTER: how distinctive, expressive, branded, or recognizable the visual language is.
     Bands: 1-3 low, 4-6 mid, 7-10 high. The build must read as the declared band. -->

## 3. Design intent

The interface should feel:
- <e.g. calm under pressure>
- <e.g. precise, like a well-made instrument>

The interface should NOT feel:
- <e.g. playful or gamified>
- <e.g. like a generic SaaS template>

## 4. Signature element

<!-- At most one memorable, product-specific idea in the visual, content, data, or interaction
     layer. It must be memorable (describable a week later), owned (from this product, brand, or
     content, not a catalog of effects), and sustained (coherent everywhere it appears).
     Optional: if restraint is the right direction, write "Restraint" and say how it is
     executed rigorously. Do not invent decorative novelty to fill this field. -->

Signature: <name it in one sentence | "None: restraint">
Layer: <visual | content | data | interaction | typography | materiality>
Why it belongs to this product: <reason>
Sustained in: <where it recurs>

## 5. Palette

<!-- Each color: name, value, role. Roles keep the accent from spreading everywhere. -->

Primary: <name> <value> | <role, e.g. primary actions and focus>
Neutral: <scale or key steps> | <surfaces, text, borders>
Accent: <name> <value or "none"> | <the one place it appears>
Semantic colors: <success / warning / danger / info values> | <status only, never decoration>
Data colors: <categorical and sequential palettes, if the product has charts>
Theme behavior: <light only | dark only | follows system | user toggle>; <reason>
Contrast verified: <pairs checked and ratios, or "pending">

## 6. Typography

Display: <face> | <reason>
Body: <face> | <reason>
Mono: <face or "none"> | <where it is used: code, IDs, tabular data>
Hierarchy: <scale and ratio, sizes per role, weights in use>
Measure: <max line length for prose, e.g. 60-72ch>
Numerals: <tabular figures where numbers align or update>
Loading: <self-hosted or service, subsets, fallback stack, font-display>

## 7. Layout principles

App shell: <none | top nav | sidebar | sidebar + top bar | other>; <reason>
Grid: <columns, gutters, or intrinsic layout approach>
Content widths: <prose, standard, wide, full-bleed>
Density strategy: <how DENSITY is achieved: row heights, spacing scale, progressive disclosure>
Navigation: <primary structure, depth, where secondary navigation lives>
Responsive collapse: <how layouts change across widths; breakpoints set where content breaks;
narrowest supported width>

## 8. Component language

Radius: <scale by role, e.g. inputs 6, cards 8, dialogs 12, pills only for tags and avatars>
Borders: <weights, colors, where borders replace shadows>
Shadows: <which elements float and get elevation; everything else flat>
Cards: <when a card is the right container, and when a list or divider is better>
Inputs: <label position, help text, error placement, sizes>
Tables: <row heights per density, alignment, sticky headers, row actions>
Buttons: <hierarchy: primary, secondary, tertiary, destructive; sizes>
Menus: <trigger patterns, keyboard behavior>
Modals: <when to use dialogs versus inline or drawers; destructive confirmation pattern>
Component library: <library and version, or "custom">; <re-tokenized? yes/no and why>

## 9. Motion

Purpose: <what motion is for in this product: state change, spatial continuity, feedback, story>
Timing: <durations and easing per category>
Allowed animation: <list>
Ambient animation: <none | what and where; must be pausable and respect reduced motion>
Reduced-motion behavior: <what replaces each animation when the user prefers reduced motion>
Implementation tier: <CSS | scroll-driven CSS | JS library (name) | canvas or WebGL>

## 10. Data visualization

<!-- Delete this section if the product shows no data. -->

Chart language: <chart types in use and why; library>
Color encoding: <sequential, categorical, diverging palettes; status colors kept separate>
Labels: <direct labels versus legends; units; number formatting and precision>
Tooltips: <content; never the only way to read a value>
Comparison: <how periods, targets, and benchmarks are shown>
Uncertainty: <ranges, confidence, estimates, incomplete periods>
Provenance: <source, last updated, method; where it appears>

## 11. Required states

<!-- For each, describe the pattern and the copy approach. Write "n/a" with a reason if a
     state cannot occur. -->

Loading: <skeleton matching layout | labeled spinner or progress | optimistic UI>
Empty: <first-run versus filtered-to-nothing; the action that fills it>
Error: <what failed, how to recover, input preserved>
Partial data: <some sources failed or still loading>
Offline: <behavior and messaging>
Permission denied: <what the user sees and how to request access>
Success: <confirmation pattern>
Disabled: <how disabled controls look and how users learn why>

## 12. Explicit project bans

<!-- Only bans relevant to this project, each with a reason. Not a copy of the kit's catalogs. -->

- <e.g. No dark theme: users work in bright warehouses on rugged tablets.>
- <e.g. No auto-rotating carousels: key promotions were missed in testing.>

## 13. Allowed exceptions

<!-- Intentional decisions that an anti-slop rule would flag. Audits mark these WAIVED and do
     not try to fix them again. P0 rules cannot be waived. -->

- <RULE-ID> <rule name>: WAIVED. <reason a reviewer can check>. Recorded by <who>, <date>.
- <e.g. UI-02 Template page skeleton: WAIVED. Corporate brand system requires the standard
  section order across all product sites. Recorded by brand team, 2026-03-02.>
- <e.g. UI-08 Default AI palette: WAIVED. Brand guide v3 specifies indigo #4F46E5 as primary.>
<!-- Do not waive a rule whose "Acceptable when" already applies; that is a PASS. -->
