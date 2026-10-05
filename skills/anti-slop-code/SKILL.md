---
name: anti-slop-code
description: "Implementation specialist for UI code written by AI agents: unverified dependencies, stubs disguised as finished features, effects without cleanup, unnecessary client-side rendering, duplicated state, giant components, needless abstractions, gratuitous animation wrappers, layout-shifting and expensive animation, design-token bypass, and comment slop. Scoped to patterns AI agents introduce while producing UI, not a general software-engineering guide. Load with anti-slop-web for any implementation work."
license: MIT
---

# Anti-Slop Code

This skill covers the implementation habits AI agents show when they build interfaces. It is
deliberately narrow: general engineering practice (testing strategy, architecture, security
review) belongs to the project's own standards. Where the project has conventions, they win over
anything here.

Examples use React and Next.js because that is where these patterns are most common; the ideas
apply to Vue, Svelte, Astro, and plain HTML equally. Rules use the kit schema.

**Scope guardrail for review work:** when asked to clean up comments or style, change only what
was asked. Do not refactor logic, rename identifiers, or reformat files as a side effect.

---

### CD-01: Unverified dependencies
**Tell:** Imports of packages that are not in `package.json`; APIs from a different major version
than the one installed (Tailwind v4 `@theme` syntax in a v3 project, Next.js Pages Router APIs in an
App Router project, framer-motion imports when the project uses `motion`); icon names that do not
exist in the installed icon set.
**Why:** The code does not build, or builds and fails at runtime. Agents assume the most common
setup instead of reading the project.
**Default correction:** Read the manifest and lockfile before importing. Match installed versions.
If a package is needed, state the install command and why the existing dependencies cannot do it.
Prefer what is already installed over adding a library.
**Acceptable when:** Not applicable.
**Severity:** HIGH. P0 if the build breaks.

### CD-02: Stubs disguised as done
**Tell:** Click handlers that only `console.log`; `onSubmit` that does nothing; mock data hard-coded
in production components; `// TODO: implement` inside a feature reported as complete; API calls to
endpoints that do not exist; "coming soon" logic with no visible label.
**Why:** The UI looks finished and is not. This is the code side of FN-01.
**Default correction:** Implement it, or remove the control, or label it visibly and list it in the
delivery report. A TODO names the specific missing task and is reported, not hidden.
**Acceptable when:** Prototypes that are delivered and labeled as prototypes.
**Severity:** HIGH. User-visible stubs (a control that does nothing) are reported under FN-01
(P0); CD-02 covers stubs users cannot see directly (mock data, unimplemented API calls).

### CD-03: Effects without cleanup
**Tell:** Event listeners, intervals, timeouts, observers, subscriptions, WebSocket connections, or
animation instances (GSAP timelines, ScrollTrigger, Lottie, Three.js renderers) created in an effect
or lifecycle hook with no teardown; fetches without cancellation that set state after unmount.
**Why:** Memory leaks, duplicated handlers after navigation, stale state updates, and animations
that keep running on hidden pages.
**Default correction:** Return a cleanup function or use the framework's teardown hook; use
`AbortController` for fetches; use the animation library's scoped context or `revert()` helpers.
**Acceptable when:** Not applicable.
**Severity:** HIGH.

### CD-04: Client-side by default
**Tell:** `"use client"` at the top of pages and layouts; data fetched in `useEffect` when the
framework can fetch on the server; static marketing sections shipped as client components because
one child animates.
**Why:** Larger bundles, slower first paint, loading spinners for content that could have been in
the HTML, and worse SEO.
**Default correction:** Keep static layout and data fetching on the server where the framework
supports it. Push interactivity and animation into small client leaves. Use the framework's data
and caching primitives.
**Acceptable when:** Single-page apps without server rendering; highly interactive surfaces where
almost everything is client state.
**Severity:** MEDIUM.

### CD-05: Duplicated or derived state
**Tell:** State that is computed from props or other state and then synchronized with an effect;
the same data held in several components that drift apart; `useState` for constants; a separate
`isLoading`, `isError`, `isEmpty`, `data` quartet that can contradict itself.
**Why:** Extra renders, flicker, and bugs where two copies of the truth disagree.
**Default correction:** Derive during render. Lift state to the nearest common owner, or use the
project's data library. Model async status as one discriminated value.
**Acceptable when:** Memoized derivations of expensive computations, measured.
**Severity:** MEDIUM.

### CD-06: Giant components
**Tell:** One file of several hundred lines that fetches, transforms, holds every piece of state,
and renders the whole page, often generated in one pass.
**Why:** Hard to review, test, reuse, or change; every keystroke re-renders everything.
**Default correction:** Split along real boundaries: data loading, layout, independent interactive
regions, repeated items. Co-locate state with the part that uses it.
**Acceptable when:** Small pages where splitting would only add indirection.
**Severity:** MEDIUM.

### CD-07: Needless abstraction
**Tell:** Wrapper components, hooks, or utilities used exactly once; a `Button` with fifteen boolean
props instead of variants or `children`; config-driven rendering for three static items; a design
system built inside a single landing page; generic types and factories for one concrete case.
**Why:** Indirection without reuse makes the code harder to read than the duplication it avoids.
**Default correction:** Write the concrete thing. Extract when the second or third real use appears.
Prefer composition (`children`, slots) over prop explosions.
**Acceptable when:** The abstraction matches the project's established pattern.
**Severity:** MEDIUM.

### CD-08: Gratuitous animation wrappers
**Tell:** `motion.div` around every element; an animation library imported for a hover color
change; identical `initial={{ opacity: 0, y: 20 }}` copied onto every section; a scroll library and
a UI animation library both controlling the same elements.
**Why:** Bundle weight and runtime cost for effects CSS does for free; competing animation systems
fight over the same properties. The visual side is UI-23.
**Default correction:** Use the lightest tier: CSS transitions and keyframes, then native
scroll-driven CSS, then a JS library for orchestration, physics, layout animation, or gestures.
Keep each element under one animation system.
**Acceptable when:** The project standardizes on a motion library and uses it consistently.
**Severity:** LOW.

### CD-09: Expensive animation properties
**Tell:** Animating `width`, `height`, `top`, `left`, `margin`, or `box-shadow` on large areas;
`transition: all`; `will-change` on many elements permanently; animated `filter: blur()` on large
layers; animated gradient backgrounds via `background-position` on full sections.
**Why:** Layout and paint on every frame: jank, battery drain, hot laptops.
**Default correction:** Animate `transform` and `opacity`. List transitioned properties explicitly.
Apply `will-change` just before an animation and remove it after. For size changes, consider the
View Transitions API, FLIP techniques, or `interpolate-size` where supported.
**Acceptable when:** Small elements where measurement shows no cost.
**Severity:** MEDIUM.

### CD-10: Layout shift sources
**Tell:** Images and embeds without dimensions or `aspect-ratio`; web fonts swapping with very
different metrics; content injected above existing content after load; skeletons whose size does
not match the loaded content; hover effects that change layout size.
**Why:** Content jumps under the user's cursor or finger, causing mis-clicks.
**Default correction:** Reserve space (`width`, `height`, `aspect-ratio`), use fallback font metric
overrides or `size-adjust`, match skeleton dimensions to the real layout, use transforms for
hover effects.
**Acceptable when:** Not applicable.
**Severity:** MEDIUM.

### CD-11: Design-token bypass
**Tell:** Hard-coded hex values, pixel values, and font stacks in components when the project has
tokens or a theme; Tailwind arbitrary values (`bg-[#6366f1]`) for colors the theme defines; dynamic
class names built by string interpolation (`text-${color}-500`) that the build cannot detect.
**Why:** The design system drifts, themes break, and dark mode misses components.
**Default correction:** Use the project's tokens or theme variables. Add a token if one is missing
and the value will recur. Use complete class names in lookup maps.
**Acceptable when:** One-off values with no system meaning (an illustration's coordinates).
**Severity:** MEDIUM.

### CD-12: Unstable list keys
**Tell:** `key={index}` on lists that can reorder, filter, or insert; keys generated with
`Math.random()` or `crypto.randomUUID()` during render.
**Why:** Inputs lose their values, animations attach to the wrong items, state jumps between rows.
**Default correction:** Use stable IDs from the data.
**Acceptable when:** Static lists that never change order.
**Severity:** MEDIUM.

### CD-13: Patch scripts
**Tell:** A Python or Node script that edits CSS or source files with string replacement to add a
feature (dark mode, a theme, responsive fixes), left in the repository or run as part of the build.
**Why:** The feature lives outside the code it changes; the next edit breaks it silently.
**Default correction:** Implement the change in the source where it belongs.
**Acceptable when:** Established codemods run once and reviewed, not left as runtime machinery.
**Severity:** MEDIUM.

### CD-14: Comment slop
**Tell:** Comments that restate the code (`// Set loading to true`); step narration (`// Step 1:
validate input`); banner separators and ALL CAPS section headers; emoji in comments; end-of-block
markers; documentation blocks that only echo the signature; vague TODOs ("improve this later").
**Why:** Noise that hides the comments that matter and marks code as generated.
**Default correction:** Delete them. Keep comments that explain why: business rules, constraints,
workarounds, edge cases, protocol details, performance or security tradeoffs. One or two lines,
in a plain voice. A TODO names a specific task.
**Acceptable when:** Project conventions that require structured doc comments for public APIs.
**Severity:** LOW.

### CD-15: Debug leftovers and specificity spam
**Tell:** `console.log` in shipped components; commented-out blocks; `z-index: 9999` and `z-50` on
ordinary elements; `!important` used to win specificity fights.
**Why:** Noise, leaked internal data in the console, and stacking contexts that break the next
overlay.
**Default correction:** Remove logs and dead code. Define a small z-index scale for systemic layers
(sticky header, dropdown, modal, toast). Fix specificity at the source.
**Acceptable when:** Logging through the project's logger at an appropriate level.
**Severity:** LOW.

---

## Code checklist (quick)

- [ ] Every import exists in the manifest at the installed version (CD-01)
- [ ] No control is a stub without a visible label and a reported TODO (CD-02)
- [ ] Every effect, listener, timer, and animation instance is cleaned up (CD-03)
- [ ] Server rendering used where the framework supports it; client leaves are small (CD-04)
- [ ] No synced copies of derived state (CD-05)
- [ ] Components split on real boundaries; no single-use abstractions (CD-06, CD-07)
- [ ] Lightest animation tier; transform and opacity; no layout shift (CD-08 to CD-10)
- [ ] Tokens used; no interpolated class names (CD-11)
- [ ] Stable keys; no patch scripts; no debug leftovers or comment noise (CD-12 to CD-15)
