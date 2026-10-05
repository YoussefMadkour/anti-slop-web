# Product Design Direction

<!-- Fictional example. Illustrates reasoning; do not copy values as a preset. -->

Status: confirmed
Owner: Plant systems team, Corvane Bottling (fictional)
Last updated: 2026-08-30
Sources inspected: Existing SCADA alarm color conventions, site safety color standard, shift
supervisor interviews (notes), control room photos, current web tool (unstyled tables), sensor
data schema.

## 1. Product context

Product: Line Monitor, a web dashboard showing live status of six bottling lines: throughput,
stoppages, temperature and pressure sensors, and active alarms.
Audience: Shift operators and supervisors, trained, using it for full 8 to 12 hour shifts.
Primary tasks: Spot a stopping or degrading line within seconds; acknowledge and route alarms;
check whether a reading is current.
Environment: Dim control room, wall display at 3 meters plus desk monitors; occasional tablet
use on the floor in bright light.
Device priority: 1920px desk monitor and 4K wall display first; tablet second; phone not supported
beyond a read-only alarm list.
Archetype: OPERATIONS (+ DASHBOARD for the end-of-shift summary view)

## 2. Design dials

VARIANCE: 3 | Operators learn positions; each line occupies the same place on every screen and
the layout never rearranges.
MOTION: 1 | Motion competes with alarms; values update in place with at most a brief highlight.
DENSITY: 9 | Six lines with roughly 40 readings each must be visible without scrolling on the
desk monitor.
CHARACTER: 5 | A distinct, learnable status language matters for training and incident
handover; decoration does not.

## 3. Design intent

The interface should feel:
- Stable and quiet when everything is normal
- Unmistakable when something is wrong
- Trustworthy about how current each value is

The interface should NOT feel:
- Like a marketing dashboard with charts for decoration
- Busy or animated when nothing is happening
- Ambiguous about which alarm matters most

## 4. Signature element

Signature: The status glyph system: every state has a shape, a color, and a word. Normal is a
hollow circle, advisory a square, warning a triangle, critical a filled octagon, stale data a
dashed outline. The same glyphs appear on the wall display, desk view, alarm list, printed shift
report, and training material.
Layer: data and visual
Why it belongs to this product: Operators already use shapes on the plant's physical signage; the
glyphs extend that convention to software and survive color blindness and screen glare.
Sustained in: line tiles, sensor rows, alarm list, shift summary, notifications.

## 5. Palette

Primary: Signal blue #5AA2E6 (dark theme value) | selection, focus ring, links
Neutral: blue-grays from #101418 (page) through #1A2027 (panels) to #E6EAEE (text)
Accent: none; color is reserved for status
Semantic colors: critical #FF6B5E, warning #F2B33D, advisory #8EC5FF, normal #8A949E (normal is
deliberately neutral gray so only abnormal states draw color)
Data colors: sensor trends single-hue blue sequential; setpoint bands in neutral gray
Theme behavior: dark by default for the control room; light theme for floor tablets in bright
light, selected per device
Contrast verified: text #E6EAEE on #1A2027 13.57:1; critical #FF6B5E on #1A2027 5.87:1; warning
#F2B33D on #1A2027 8.82:1 (computed with contrast.py); light theme pairs verified separately

## 6. Typography

Display: none; headings use the body face at heavier weight
Body: IBM Plex Sans | clear at small sizes, distinct 1/l/I, good numeric shapes
Mono: IBM Plex Mono | sensor IDs and raw values in the diagnostics drawer
Hierarchy: 1.2 scale from 13px base on desk monitors; wall display scales by viewport with a
fixed minimum
Measure: n/a, little prose
Numerals: tabular figures everywhere; values show units and fixed precision per sensor type
Loading: self-hosted; no external requests (plant network is isolated)

## 7. Layout principles

App shell: top bar only (plant, shift, clock, alarm count); no sidebar on the live view
Grid: six fixed line columns in plant floor order
Content widths: full width
Density strategy: compact rows (32px), minimal chrome, borders instead of cards, labels abbreviated
with full names on focus and hover
Navigation: three views (Live, Alarms, Shift summary) as tabs in the top bar
Responsive collapse: tablet shows one line at a time with a line switcher; phone shows the alarm
list only

## 8. Component language

Radius: 2px
Borders: 1px #2A323B separating lines and rows
Shadows: none; dialogs separated by a lighter surface and border
Cards: none on the live view; widget panels only in the shift summary
Inputs: rare; alarm notes field with label above
Tables: sensor rows with name, value, unit, setpoint, status glyph, age
Buttons: Acknowledge is the only primary action on an alarm row
Menus: alarm row menu with Acknowledge, Assign, Add note
Modals: only for shelving an alarm (requires reason and duration)
Component library: React Aria primitives, custom styling

## 9. Motion

Purpose: confirm state changes only
Timing: value change highlight 600ms background fade; no transitions on layout
Allowed animation: highlight on changed value; critical alarm glyph pulses at most 3 cycles,
then holds; critical alarm banner appears without animation
Ambient animation: none
Reduced-motion behavior: highlight replaced by a static marker for 5 seconds; critical glyph
shown as a static filled glyph
Implementation tier: CSS only

## 10. Data visualization

Chart language: small trend lines (last 60 minutes) per key sensor on focus; shift summary uses
line and bar charts
Color encoding: data in blue; status colors never used for data series
Labels: units on every value; trends show min and max labels
Tooltips: exact value and timestamp; values are also in the row
Comparison: setpoint and tolerance band drawn behind each trend
Uncertainty: sensor tolerance shown as a band; interpolated gaps shown as dashed segments
Provenance: each value shows age ("12s"); values older than 60 seconds switch to the stale glyph;
summary charts state source historian and export time

## 11. Required states

Loading: on first load, line columns render with labeled placeholders; never a blank wall
Empty: a line not running shows "Line 4 idle since 06:10 (planned maintenance)" from the schedule
Error: lost connection to the data service shows a full-width banner with the time of last update;
values stay visible with the stale glyph
Partial data: individual sensors offline show "Sensor offline since 14:02" in place of the value
Offline: same as connection loss; acknowledgements queue locally and show "Pending sync"
Permission denied: operators cannot shelve alarms; the action shows the required role
Success: acknowledgement adds name and time to the alarm row
Disabled: Acknowledge disabled for alarms already acknowledged, with "Acknowledged by R. Ortiz
14:05"

## 12. Explicit project bans

- No decorative motion, count-up numbers, or pulsing indicators except the critical alarm glyph
  (UI-19, UI-23).
- No KPI cards with business metrics on the live view; operators act on status, not revenue.
- No re-sorting of rows while the view is live; new alarms appear in a fixed alarm list.
- No rounding of sensor values.

## 13. Allowed exceptions

- UI-12 Unearned dark theme: no waiver needed. Dark is in scope for OPERATIONS and the reason
  (dim control room, wall display glare) is recorded in §5.
- UI-03 Uniform feature cards: not applicable; the six identical line columns are deliberate.
  Consistency is the usability goal. Recorded by plant systems team, 2026-08-30.
