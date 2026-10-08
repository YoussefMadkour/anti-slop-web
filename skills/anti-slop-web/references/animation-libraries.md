# Animation Libraries

Which tool to reach for once `motion.md` has established that an animation has a job and that
CSS or a native platform feature cannot do it. Load this file when a task needs a JavaScript
animation library, scroll orchestration, vector animation, or a canvas or WebGL scene, and in
Redesign mode when writing the motion plan. The MOTION dial, `DESIGN.md` §9, and the libraries
already installed override everything here.

This is a neutral orientation, not a ranking. APIs, licenses, and bundle costs change: check each
library's current documentation and the project's manifest before recommending or importing one
(CD-01). Bundle weights below are relative, not measurements.

Related: `motion.md` (purpose, timing, reduced motion), `design-systems.md` (effect component
libraries), A11Y-10, UI-23, CD-01, CD-03, CD-08, CD-09.

---

## Decide in this order

1. **Does the animation have a job?** (`motion.md`, What motion is for.) If not, stop (UI-23).
2. **Is a library already installed?** Use it. Two animation systems on one product is a cost
   that needs a reason; two on the same element is a bug.
3. **Can CSS or the platform do it?** Transitions, keyframes, `@starting-style`, scroll-driven
   animations, and the View Transitions API cover most MOTION 1 to 5 work with no JavaScript.
4. **Otherwise pick by the hardest thing the animation needs**, using the table below.

## Which tool for which need

| Need | Reach for | Why |
|------|-----------|-----|
| Hover, press, focus, small state changes | CSS transitions | No JS, composited, trivially reduced-motion aware |
| Elements entering or leaving the DOM | `@starting-style` + `transition-behavior: allow-discrete`; Motion's `AnimatePresence` in React | Exit animations are where CSS gets awkward in component frameworks |
| List items added, removed, or reordered | AutoAnimate for drop-in; Motion `layout` for control | FLIP without hand-writing it |
| Shared element between views or routes | View Transitions API; Motion `layoutId` | Spatial continuity |
| Gestures: drag, swipe-to-dismiss, interruptible springs | Motion (React); React Spring | Physics and interruption are hard by hand |
| Long timelines and precise sequencing | GSAP timelines | Fine-grained control, labels, nesting, seeking |
| Scroll pinning and scrubbed narratives | GSAP ScrollTrigger; native scroll-driven CSS for simple scrubs | Pinning and multi-step scrubbing need a library |
| Text split into lines, words, or characters | GSAP SplitText | Handles line breaks and resizing; keep the accessible text intact |
| SVG path drawing and morphing | CSS `stroke-dashoffset` for drawing; GSAP plugins or Anime.js for morphing | |
| Designer-made illustrations and icon animation | Lottie (dotLottie) | Plays an After Effects export; no logic |
| Interactive, state-driven vector animation (a mascot, an animated control) | Rive | State machines respond to input; small runtime files |
| 3D, particles, shaders | Three.js or React Three Fiber; OGL for lighter scenes | Highest cost; needs a static fallback |
| Smooth or inertial scrolling | Usually nothing. Lenis only for scroll-driven creative work | Overrides native scroll feel (see below) |

## Libraries

### Motion (formerly Framer Motion)
**What:** Declarative animation for React (`motion/react`), with a framework-agnostic core
(`motion`). Layout animations, exit animations, gestures, springs, scroll-linked values.
**Use when:** A React product needs exit animations, layout or shared-element transitions,
gestures, or interruptible springs. The default JS tier for React APPLICATION and MARKETING work.
**Avoid when:** CSS does the job (CD-08); the project is not React and needs only tweens.
**Weight:** Medium. Use `LazyMotion` with the `m` component to cut the initial cost.
**Reduced motion:** `<MotionConfig reducedMotion="user">` at the root, and `useReducedMotion()`
for anything spatial that should become instant.
**Common AI misuse:** Every element wrapped in `motion.div` with `initial={{ opacity: 0, y: 20 }}`;
spring bounce on serious UI; importing from `framer-motion` in a project that installed `motion`.

### GSAP
**What:** Imperative tween and timeline engine, framework-agnostic, with plugins (ScrollTrigger,
SplitText, Flip, Draggable, MorphSVG, and others), all free to use.
**Use when:** Choreographed sequences, scroll-pinned storytelling, text splitting, SVG morphing;
MOTION 6 and above; non-React projects that need more than CSS.
**Avoid when:** Simple UI feedback; dense applications where it would only add weight.
**Weight:** Medium for the core; plugins add to it. Register only the plugins you use.
**Reduced motion:** `gsap.matchMedia()` with `(prefers-reduced-motion: reduce)` to build a
reduced version of each timeline.
**Cleanup:** In React, `useGSAP()` from `@gsap/react` scopes and reverts animations on unmount
(CD-03). Kill ScrollTriggers on route change.
**Common AI misuse:** ScrollTrigger fade-up on every section; pinned sections on a MOTION 3 site;
timelines created in effects with no cleanup.

### Anime.js
**What:** Lightweight, framework-agnostic animation engine with timelines, SVG, and stagger utilities.
**Use when:** Non-React projects that want timelines and SVG work with a smaller footprint than
GSAP and its plugins.
**Avoid when:** The project already has Motion or GSAP.
**Reduced motion:** Manual: check `matchMedia('(prefers-reduced-motion: reduce)')` before building
animations.

### AutoAnimate
**What:** One-line FLIP animation for lists and containers (React, Vue, Svelte, vanilla).
**Use when:** Items added, removed, or reordered in APPLICATION and DASHBOARD UIs, MOTION 2 to 4.
**Avoid when:** You need choreography; long lists where animation delays reading.
**Reduced motion:** Respects the preference by default; verify in the version installed.

### React Spring
**What:** Spring-physics animation for React.
**Use when:** The project already uses it, or physics-first interaction is the signature.
**Avoid when:** Starting fresh with ordinary UI transitions; Motion covers the same ground with
less setup for most teams.

### Lottie (dotLottie)
**What:** Plays JSON or `.lottie` animations exported from After Effects.
**Use when:** A designer supplied the animation: onboarding illustrations, empty-state art, a
brand mark animation.
**Avoid when:** The animation needs to respond to state (use Rive); icon hovers CSS can do;
nobody on the project can author or edit the source file.
**Weight:** The player is heavy relative to what it usually shows; lazy-load it and prefer the
lighter dotLottie players.
**Reduced motion:** Not automatic. Show a static frame under reduced motion and pause off-screen.
**Common AI misuse:** Stock Lottie files from public galleries as decoration (UI-22, UI-23).

### Rive
**What:** Interactive vector animation with state machines, authored in the Rive editor.
**Use when:** An animated element must react to input or state (a toggle with character, a
mascot that follows progress, an interactive hero) and is the product's signature.
**Avoid when:** Nobody will maintain the `.riv` source; a CSS transition would do.
**Reduced motion:** Not automatic. Drive a reduced state through the state machine or show a static frame.

### Three.js, React Three Fiber, OGL
**What:** WebGL scenes: 3D product views, particles, shaders.
**Use when:** CREATIVE_EXPERIENCE, MOTION 7 and above, where the scene is the signature and has a
reason (the product is physical, the data is spatial).
**Avoid when:** A hero background with no relation to the product (UI-10); dense applications.
**Weight:** Heavy. Lazy-load after first paint, pause off-screen and in hidden tabs, cap device
pixel ratio, and provide a static image fallback for low-power devices and reduced motion.
**Common AI misuse:** Rotating wireframe globes and particle fields behind a SaaS hero.

### Lenis and other smooth-scroll libraries
**What:** Replace native scrolling with interpolated, inertial scrolling.
**Use when:** CREATIVE_EXPERIENCE with scroll-driven scenes, where synchronizing scroll with
WebGL or long timelines needs it.
**Avoid when:** Almost everything else. Smooth scroll changes how scrolling feels on every
device, can fight trackpads and assistive technology, and buys nothing on ordinary pages.
**Reduced motion:** Disable entirely under reduced motion. Never break keyboard scrolling,
anchor links, or find-in-page.

### CSS utility packages
`tw-animate-css` (and the older `tailwindcss-animate`) supply enter and exit keyframes for
Tailwind projects, and are what shadcn/ui components expect. Use whichever matches the project's
Tailwind version; do not install both.

## Recipes by archetype

Starting points; the MOTION dial and `DESIGN.md` §9 decide.

| Archetype (typical MOTION) | Tier and tools | Typical animations |
|----------------------------|----------------|--------------------|
| OPERATIONS, DATA_EXPLORATION (1-2) | CSS only | Hover and focus, row highlight on live update (brief, once), overlay open and close |
| APPLICATION, DASHBOARD (1-3) | CSS; Motion or AutoAnimate if lists reorder or exits matter | Dialog and drawer entry and exit, list add and remove, tab indicator slide, toast stack |
| ECOMMERCE (3-5) | CSS + View Transitions; Motion in React | Product card to detail continuity, cart drawer, image gallery, add-to-cart feedback |
| MARKETING, DEVELOPER_TOOL sites (3-6) | CSS + native scroll-driven reveals; Motion or GSAP for one signature moment | One hero or product-demo sequence, restrained section reveals, interactive product preview |
| EDITORIAL (2-5) | CSS + scroll-driven CSS; GSAP ScrollTrigger for a feature story | Reading progress, scrollytelling on the flagship piece only |
| CREATIVE_EXPERIENCE (7-10) | GSAP + ScrollTrigger, Lenis if needed, Three.js or Rive for the signature | Narrative scroll, pinned scenes, interactive 3D; with full reduced-motion version |

## Checklist before shipping animation

- Each animation's job is named in `DESIGN.md` §9 or the motion plan.
- One JS animation system per product unless there is a recorded reason.
- Library installed and imported from the right package (CD-01).
- Only `transform` and `opacity` animated on many elements (CD-09).
- Reduced motion handled in JavaScript as well as CSS, and checked by toggling the OS setting (A11Y-10).
- Heavy libraries and scenes lazy-loaded; animations torn down on unmount (CD-03).
- Anything that moves for more than five seconds can be paused.
