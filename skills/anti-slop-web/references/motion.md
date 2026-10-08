# Motion

What animation is for, how much a product should have, and how to implement it safely and
cheaply. Load this file when a task adds transitions, scroll effects, or animated feedback.
The MOTION dial in `DESIGN.md` §2 and §9, and the brand, override everything here. Durations
below are starting points, not limits.

Related: `animation-libraries.md` (choosing a library), `components.md` (overlays), `charts.md` (data animation), A11Y-10, UI-23, CD-03, CD-08, CD-09.

---

## What motion is for

Every animation should have one of these jobs. If it has none, remove it (UI-23).
- **Feedback:** confirm an input was received (press, toggle, save).
- **State change:** show that something appeared, disappeared, expanded, or reordered.
- **Spatial continuity:** show where something came from or went (a drawer from the edge, a card
  expanding into a detail view).
- **Attention:** draw the eye to one thing that changed or needs action, once.
- **Narrative:** at high MOTION, tell a deliberate story where the motion is part of the message.

## MOTION dial bands

| Band | What it looks like | Typical archetypes |
|------|--------------------|--------------------|
| 1-3 | Hover, focus, and press feedback; instant or very short state transitions; no scroll effects; nothing moves unless the user or the data did | OPERATIONS, DATA_EXPLORATION, APPLICATION, DASHBOARD |
| 4-6 | Transitions that explain change (overlays, accordions, route changes), light reveals on long marketing pages, subtle loading animation | MARKETING, ECOMMERCE, EDITORIAL, DEVELOPER_TOOL sites |
| 7-10 | Choreographed sequences, scroll-driven storytelling, physics, WebGL or canvas scenes | CREATIVE_EXPERIENCE, launches, campaigns |

The build must read as the declared band: a MOTION 2 product with scroll choreography, or a
MOTION 8 campaign that barely moves, is a mismatch (UI-27).

## Implementation tiers (lightest first)

Use the lightest tier that achieves the effect, and avoid running two systems on the same elements.
1. **CSS transitions and keyframes:** hover, press, small state changes. No JavaScript.
2. **Native platform features:** `@starting-style` for entry animations, scroll-driven
   animations, the View Transitions API.
3. **A JS animation library:** coordinated sequences, layout animations, gestures, interruptible
   springs. Verify it is installed before importing (CD-01). Choosing one:
   `animation-libraries.md`.
4. **Scroll orchestration libraries:** pinning and scrubbing long narratives.
5. **Canvas or WebGL:** scenes, particles, 3D. Highest cost; needs a fallback.

Common AI misuse: wrapping every element in a library's motion component when CSS would do (CD-08).

## Duration and easing

**What:** How long motion lasts and how it accelerates.
**Starting points:**

| Category | Duration (starting point) |
|----------|---------------------------|
| Press and toggle feedback | about 100ms |
| Hover changes | 100 to 150ms |
| Tooltips, small fades | 150 to 200ms |
| Menus, popovers, accordions | 200 to 250ms |
| Dialogs, drawers, page transitions | 200 to 350ms |
| Exits | often shorter than the matching entrance |
| Narrative and data animation | longer, set by the story; keep UI responsive meanwhile |

**Easing by purpose:**
- Entering: decelerate (ease-out) so things arrive quickly and settle.
- Leaving: accelerate (ease-in) so they get out of the way.
- Moving on screen: ease-in-out.
- Springs: useful for gestures and interruptible, physical interactions; not a universal default.
  Bounce on data, errors, or serious products usually reads as frivolous.
- Linear: appropriate for continuous progress, scrubbing, and loops.
**Tradeoffs:** Interface feedback that lasts longer than about 400ms tends to feel sluggish;
narrative motion at high MOTION can run longer because watching it is the point.
**Common AI misuse:** Every transition at 500ms with spring bounce (UI-23).

## Animate cheap properties

**What:** `transform` and `opacity` are composited and do not trigger layout.
**Practices:**
- Avoid animating `width`, `height`, `top`, `left`, `margin`, and large `filter` or `box-shadow`
  areas on many elements (CD-09).
- Avoid `transition: all`; list the properties you mean.
- Use `will-change` sparingly and only on elements about to animate.
- Hover effects should not shift surrounding layout: scaling a whole card in a grid can overlap
  neighbors and cause jitter. Scaling an image inside a clipped frame, or changing border and
  shadow, often reads better. A small scale on a single isolated element is fine.
- Height animations for accordions can use `interpolate-size: allow-keywords` where supported, or
  the grid-rows technique.

## Reduced motion

**What:** Respecting users who ask the operating system for less motion (A11Y-10).
**Practices:**
- Additive approach: content is visible and functional with no animation; motion is added only
  when the user has not asked for reduction. This also means content never stays invisible if
  scripts fail.
- Under reduced motion, replace spatial motion (slides, parallax, zooms, scroll effects) with
  instant changes or short opacity fades. Keep essential feedback.
- Auto-playing motion longer than five seconds needs a pause control regardless of preference.
- Respect the preference in JavaScript-driven animation too, not only CSS.

```css
/* Content is visible by default. Hiding starts only once the script has run and added .js
   to <html> (document.documentElement.classList.add("js")), so a failed script hides nothing. */
@media (prefers-reduced-motion: no-preference) {
  .js .reveal { transition: opacity 250ms ease-out, transform 250ms ease-out; }
  .js .reveal:not(.is-visible) { opacity: 0; transform: translateY(0.5rem); }
}
```

## Scroll-driven animation

**What:** Animation progress tied to scroll position, natively in CSS.
**Use when:**
- Reading progress indicators, gentle reveals on long pages, narrative sections at mid to high MOTION.
**Avoid when:**
- Content users need immediately is hidden until scrolled into view.
- Dense applications.
**Archetypes:** MARKETING, EDITORIAL, CREATIVE_EXPERIENCE.
**Tradeoffs:** No JavaScript and smooth; not supported everywhere, so treat as progressive enhancement.
**Accessibility:** Gate behind reduced motion; content must be readable without the animation (A11Y-10).
**Common AI misuse:** Fade-up on every element down the page (UI-23).

```css
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .reveal {
      animation: rise linear both;
      animation-timeline: view();
      animation-range: entry 0% entry 40%;
    }
  }
}
@keyframes rise { from { opacity: 0; transform: translateY(1rem); } }
```

## View transitions

**What:** Browser-managed transitions between DOM states or pages, including shared elements.
**Use when:**
- Route or tab changes where continuity helps (a list item expanding into its detail page).
**Avoid when:**
- Every navigation in a dense tool gets a flourish users must wait through.
**Archetypes:** APPLICATION, ECOMMERCE, EDITORIAL.
**Tradeoffs:** Same-document transitions are broadly supported; cross-document support varies.
Wrap in a feature check and keep durations short.
**Accessibility:** Disable or reduce under reduced motion.

## Stagger

**What:** Children of a group animating in sequence.
**Use when:** A small group appears at once and order helps comprehension (a menu, a short list).
**Avoid when:** Long lists or tables; users wait for content they need now.
**Tradeoffs:** Keep total stagger time short (a few hundred milliseconds); cap the number of
staggered items and show the rest instantly.
**Common AI misuse:** Staggering a 50-row table.

## Ambient and looping animation

**What:** Motion with no user trigger: floating shapes, pulsing dots, animated gradients, marquees.
**Use when:**
- It carries meaning (a live indicator for genuinely live data) or is the signature at high
  MOTION and CHARACTER.
**Avoid when:**
- It decorates (UI-23); it marks no state (UI-19); it runs on a dense working screen.
**Tradeoffs:** Constant motion costs battery and attention; animated background gradients repaint every frame.
**Accessibility:** Pausable, respects reduced motion; anything that moves for more than five
seconds needs a pause, stop, or hide control (A11Y-10).
**Common AI misuse:** Bobbing blobs behind the hero; endless pulsing status dots.

## Parallax and scroll-jacking

**What:** Layers moving at different speeds; or scripts taking over scroll behavior.
**Use when:**
- Subtle parallax on a single hero image at mid to high MOTION.
- Scroll-controlled narratives in CREATIVE_EXPERIENCE with a clear way out.
**Avoid when:**
- Text moves; scroll speed or direction is hijacked on ordinary pages (UI-01).
**Tradeoffs:** Vestibular disorders can be triggered by large parallax and zooming motion.
**Accessibility:** Disable under reduced motion; never break keyboard scrolling or find-in-page.

## Count-up numbers and marquees

- **Count-up:** animating KPIs from zero delays the real value and can mislead mid-animation.
  Reasonable on a marketing page for a real number; avoid in dashboards, where users want the
  value now. Show the final value immediately under reduced motion.
- **Marquee:** moving logo strips are hard to read and must pause on hover and focus, offer a
  control, and stop under reduced motion. A static grid of real logos is usually better (IN-01 for the logos themselves).

## Performance and cleanup

- Every animation set up in an effect is torn down on unmount: timelines, observers, listeners,
  animation frames (CD-03).
- Isolate perpetual animations in small components so they do not re-render large trees.
- Lazy-load heavy animation libraries and canvas scenes; do not block first render.
- Pause off-screen animation (IntersectionObserver) and when the tab is hidden.

## Creative experiences

At MOTION 7 to 10 in CREATIVE_EXPERIENCE, scroll-driven scenes, physics, custom cursors, and
WebGL are legitimate tools. Conditions that keep them acceptable:
- Core content and navigation reachable without the effect (keyboard, touch, reduced motion).
- A performance budget tested on mid-range phones.
- A reduced-motion version that still tells the story.
- The motion is the sustained signature, not a single firework (UI-27).
