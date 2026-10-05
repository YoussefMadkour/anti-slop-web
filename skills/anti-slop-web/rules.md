# Rule Catalog: Integrity, Function, Visual

Loaded during the audit (workflow step 9), not on every request. Specialist rules live in their
own skills: accessibility `A11Y-*` in `anti-slop-a11y`, responsive `RS-*` in
`anti-slop-responsive`, copy `CP-*` in `anti-slop-copy`, implementation `CD-*` in
`anti-slop-code`.

## Rule schema

Every rule in this kit uses the same fields:

- **Tell:** the recognizable pattern.
- **Why:** why it can indicate generic, content-insensitive, or broken design.
- **Default correction:** what to do instead, as a starting point.
- **Acceptable when:** legitimate uses. If the situation matches, the rule passes.
- **Scope:** archetypes where the rule applies fully. Elsewhere, apply it only if the tell
  clearly harms the product.
- **Severity:** P0, HIGH, MEDIUM, or LOW. Some rules escalate under stated conditions.

The audit records each relevant rule as:

```
UI-03 Uniform feature cards | Severity: HIGH | Audit: PASS | FAIL | WAIVED
Evidence: <what was observed, where>
Waiver: <reason from DESIGN.md §13, if WAIVED>
```

Rule IDs are stable. Never renumber; retire a rule by marking it retired.

## Reading the rules correctly

- A rule fires on the **absence of a reason**, not on the presence of a technique. Before
  flagging, check `DESIGN.md`, the brand, the content, and the archetype for a reason.
- Familiar conventions pass by default. A centered hero, a sidebar app shell, a uniform
  product grid, a three-tier pricing table, or Inter on a dense admin UI can all be correct.
  They fail only when chosen as defaults and contradicted by the content or the direction.
- Clusters matter more than single tells (see CL-01).
- Report one issue once, under its most specific rule. Cross-references between catalogs
  ("see FN-01") point to the owner; they are not second findings.

---

## IN: Integrity and truthfulness

Anything presented as fact must be real and verifiable, or not shown. A specific-looking
fabrication is worse than a vague claim because it reads as honest.

### IN-01: Fabricated social proof
**Tell:** Testimonials, reviews, star ratings, customer logos, "Trusted by" bars, case studies,
or user counts that the owner did not supply. Invented names and job titles ("Sarah Chen, VP
Engineering"), AI-generated avatars, logos of companies that are not customers.
**Why:** It deceives users and exposes the owner to legal and reputational risk. It is also the
clearest generated-content tell.
**Default correction:** Remove the section, or keep a clearly labeled placeholder
(`[TESTIMONIAL: real customer quote needed]`) in drafts. Ask the owner for real proof.
**Acceptable when:** The owner supplied the material and has permission to show it.
**Scope:** All.
**Severity:** P0.

### IN-02: Invented metrics presented as fact
**Tell:** Statistics, uptime figures, performance claims, growth deltas, benchmark numbers, or
"10K+ teams" with no source. Includes "organic-looking" invented numbers (47.2%) used to seem
credible, and KPI deltas ("+12% vs last week") with no real comparison series.
**Why:** Numbers are read as evidence. Invented ones are fabrication, however plausible.
**Default correction:** Show no number, wire to real data, or use an explicit placeholder
(`[REAL DATA]`). In dashboards, show deltas only when the comparison period exists and is named.
**Acceptable when:** Sample data in a prototype or demo that is visibly labeled as sample
(a "Sample data" banner, a demo-workspace label). Documentation examples clearly framed as examples.
**Scope:** All.
**Severity:** P0. Labeled sample data in a prototype is not a violation.

### IN-03: Fabricated trust, compliance, or capability claims
**Tell:** "SOC 2 compliant", "HIPAA ready", "ISO 27001", "bank-grade encryption", "300% faster",
"AI-powered" for features that are not, security badges, awards, press logos ("As seen in")
without evidence.
**Why:** These are factual and often legal claims.
**Default correction:** Remove, or ask the owner. State what the product verifiably does.
**Acceptable when:** The owner confirms the claim and it is current.
**Scope:** All.
**Severity:** P0.

### IN-04: Disguised placeholder content
**Tell:** Realistic fake content in a deliverable presented as final: "John Doe", "Acme Inc.",
`johndoe@example.com` in filled fields, invented team members, stock "diverse team at laptop"
photos posing as the company, random photo services standing in for product imagery. (Lorem
ipsum and unfilled placeholder markers are CP-03.)
**Why:** It reads as finished when it is not, and it hides what content is still missing.
**Default correction:** Use honest placeholders that say what goes there: field placeholders
like "Your name", an initial-based avatar, `[LOGO]`, `[PRODUCT SCREENSHOT]`. List missing
content in the delivery report.
**Acceptable when:** A prototype or design exploration where placeholders are clearly marked and
the delivery report states it is not final content. Test fixtures and seed data not shown as
real customers.
**Scope:** All.
**Severity:** HIGH. P0 if shipped to production as if real.

### IN-05: Invented brand assets
**Tell:** Logos, app icons, mascots, team photos, or illustrations of people created without
instruction and presented as final.
**Why:** Brand assets are the owner's identity decisions, not the agent's.
**Default correction:** Ask, or use the product name set in an appropriate typeface, or a marked
placeholder.
**Acceptable when:** The user asked for the asset, or asked the agent to propose one.
**Scope:** All.
**Severity:** HIGH.

### IN-06: Filler sections with invented content
**Tell:** An FAQ of generic questions ("Is my data secure?", "Can I cancel anytime?") the owner
never supplied; an activity feed of invented events; a "How it works" process the product does
not have; feature lists padded with capabilities that do not exist.
**Why:** The section exists because templates have it, and its content had to be invented to
fill it. Generic FAQ answers can also make false commitments.
**Default correction:** Cut the section, or build it from real content (support tickets, sales
questions, the actual onboarding flow). An empty state beats a fabricated feed.
**Acceptable when:** The content is real. The owner asked for draft copy and it is marked as draft.
**Scope:** All; most common in MARKETING and DASHBOARD.
**Severity:** HIGH.

---

## FN: Function and states

### FN-01: Dead controls and ghost navigation
**Tell:** Buttons that do nothing, links to `#`, nav items for pages that do not exist, dropdowns
that do not open, forms that cannot submit, row menus with no actions behind them, footer link
columns pointing nowhere.
**Why:** The visual is finished but the behavior is not. Users hit dead ends immediately.
**Default correction:** Wire the behavior, or remove the element. If it must stay visible, label
it ("Coming soon") and disable it accessibly.
**Acceptable when:** A static mockup that is explicitly delivered as a mockup.
**Scope:** All.
**Severity:** P0.

### FN-02: Missing required state
**Tell:** A data view, form, or async action with no loading, empty, or error state. Also missing
where relevant: partial data, offline, permission denied, success confirmation.
**Why:** The UI is designed for the screenshot, not for use. Real users see the other states first.
**Default correction:** Build every state listed in `DESIGN.md` §11 for this surface. First run,
filtered-to-nothing, and permission denied are different states with different copy.
**Acceptable when:** The state cannot occur (static content with no data dependency).
**Scope:** All; critical for APPLICATION, DASHBOARD, OPERATIONS, DATA_EXPLORATION, ECOMMERCE.
**Severity:** P0 when an important state is unrepresented (errors, empty data, failed submit).
MEDIUM for secondary states (offline on a mostly-static page).

### FN-03: Uninformative state
**Tell:** "No data available" with an illustration, a bare spinner with no label, "Something went
wrong" with no cause or next step, a full-page skeleton that does not match the real layout.
**Why:** The state technically exists but tells the user nothing: not why, not what next, not
whether this is normal.
**Default correction:** Empty: say why it is empty and offer the one action that fills it.
Loading: show what is loading; use a skeleton that mirrors the real layout when the shape is
known, a labeled spinner or progress bar for short actions or unknown shapes. Error: say what
failed and how to recover, and keep the user's input.
**Acceptable when:** Very short waits (under about 300 ms) that show no indicator at all.
**Scope:** All.
**Severity:** MEDIUM.

### FN-04: Missing critical form feedback
**Tell:** No inline validation messages, errors shown only by red borders, submit buttons that do
nothing on invalid input, no confirmation after submission, input lost after an error, no
indication of a pending submission (double submits possible).
**Why:** Users cannot complete the task or cannot tell whether they did.
**Default correction:** See `references/forms.md` and `anti-slop-a11y` (A11Y-07). Validate with
clear messages tied to fields, preserve input, show pending and success states.
**Acceptable when:** Never.
**Scope:** All.
**Severity:** P0.

### FN-05: Destructive action without safeguard
**Tell:** Delete, revoke, cancel subscription, overwrite, bulk actions, or irreversible sends that
execute on a single click with no confirmation and no undo.
**Why:** One mis-tap destroys user data or money.
**Default correction:** Prefer undo for frequent, recoverable actions. Use a confirmation dialog
that names the object and consequence for irreversible ones. Separate destructive actions
visually and spatially from routine ones.
**Acceptable when:** The action is trivially reversible and the reversal is obvious.
**Scope:** All.
**Severity:** P0.

### FN-06: Broken theme or mode
**Tell:** A theme toggle where one mode has unreadable text, missing component styles, wrong
chart colors, or broken images (dark logos on dark backgrounds).
**Why:** Shipping a mode is a promise that it works.
**Default correction:** Verify every shipped mode with the same checks. If a mode cannot be
finished, do not ship the toggle.
**Acceptable when:** Never for a mode you ship.
**Scope:** All.
**Severity:** HIGH. P0 if text becomes unreadable or controls disappear.

---

## UI: Visual and composition

### UI-01: Novelty without a reason
**Tell:** Unconventional patterns introduced to avoid looking generated, at the cost of
usability: hidden or mystery navigation, scroll-jacking, custom cursors, nonstandard form
controls, reinvented scrollbars, unexpected placement of primary actions, deliberate
asymmetry in a dense tool where scanning consistency matters.
**Why:** Familiar conventions carry learned behavior. Breaking them costs every user time, and
"not looking like AI" is not a user benefit.
**Default correction:** Return to the convention. Put distinctiveness where it does not tax the
task: content, typography, color, imagery, one signature element.
**Acceptable when:** CREATIVE_EXPERIENCE or high-CHARACTER brand work where the novelty is the
point and the core task still works (including keyboard and touch), or user research supports it.
**Scope:** All; strictest in APPLICATION, OPERATIONS, DASHBOARD, ECOMMERCE checkout.
**Severity:** HIGH when it impedes a primary task, otherwise MEDIUM.

### UI-02: Template page skeleton
**Tell:** The default landing sequence (centered hero with two buttons, logo bar, three feature
cards, testimonials, three pricing tiers, FAQ, CTA band, four-column footer) assembled before
anyone asked what content the product has. Sections exist because the template has them.
**Why:** The order and anatomy come from training data, not from the product's story, so the
page could belong to any product.
**Default correction:** Inventory the real content first. Order sections by the questions this
audience asks, in the order they ask them. Cut sections with no real content. Give sections
with different jobs different anatomy.
**Acceptable when:** The conventional order genuinely matches the product's story and every
section has real content. Convention is fine; empty convention is not.
**Scope:** MARKETING, ECOMMERCE landing pages.
**Severity:** HIGH.

### UI-03: Uniform feature cards
**Tell:** A row or grid of identical cards (same size, icon in a tinted rounded square, title,
two-line blurb) presenting features of unequal importance.
**Why:** Uniform containers flatten content hierarchy. The flagship capability and a minor
convenience get the same weight, and the reader cannot tell what matters.
**Default correction:** Rank the items. Give the most important one more space, a real
screenshot, or a demo; present the rest as a list, a comparison, or inline with the content
they support. Not every feature needs a card.
**Acceptable when:** Items are genuinely equivalent in kind and importance: product grids,
integration directories, team members, plan comparisons, dashboard widgets of the same type.
**Scope:** MARKETING, EDITORIAL. Relaxed in ECOMMERCE, APPLICATION, DASHBOARD, OPERATIONS, where
consistency aids scanning.
**Severity:** HIGH.

### UI-04: Unearned bento layout
**Tell:** A mosaic of different-sized cards used because it looks modern, where cell sizes do
not correspond to anything in the content. Often every cell has the same icon, title, and blurb.
**Why:** Varied cell sizes imply varied importance. When the variation is arbitrary, the layout
communicates false hierarchy and adds visual noise.
**Default correction:** Use a bento only if differences in content importance or content type
(media, live data, code, quote) justify different footprints. Otherwise use a list or a simple
grid. See `references/layouts.md`.
**Acceptable when:** Cells differ in importance or media type, the dominant cell holds the most
important thing, and the mosaic collapses to a sensible reading order on small screens.
**Scope:** MARKETING, DASHBOARD overview screens. Avoid in dense OPERATIONS views.
**Severity:** MEDIUM.

### UI-05: Uniform section rhythm
**Tell:** Every section uses the same composition (centered heading, subtitle, card grid) and the
same vertical padding; the only variation is alternating background color.
**Why:** Sections with different jobs blur together; the page reads as one long repeated strip.
**Default correction:** Let each section's job pick its anatomy (prose, split media, comparison
table, single large quote, demo). Vary spacing to group and separate. Match the VARIANCE dial.
**Acceptable when:** VARIANCE is low by design and sections are genuinely parallel (docs index,
changelog). Uniformity is then a decision, recorded in `DESIGN.md`.
**Scope:** MARKETING, EDITORIAL. Not applicable to APPLICATION screens, where consistent
anatomy is a usability feature.
**Severity:** MEDIUM.

### UI-06: Flattened hierarchy
**Tell:** No clear focal point; headings, cards, and actions all carry similar weight; several
equally loud primary buttons; the primary task or key number is not the most prominent thing
on the screen; components impose a hierarchy the content does not have.
**Why:** Users scan for what matters. When everything is emphasized, nothing is.
**Default correction:** Name the one thing the user must see or do on this view. Make it
dominant through size, weight, position, and contrast; let everything else defer. One primary
action per region.
**Acceptable when:** Rarely. Some reference tables are intentionally flat, with hierarchy carried
by sorting and filtering.
**Scope:** All.
**Severity:** HIGH when the primary task or content is hard to find. MEDIUM otherwise.

### UI-07: Generic app shell chosen before the job
**Tell:** Sidebar, top bar, a row of four stat cards, one chart, one table: identical whether the
product manages invoices, patients, or servers, and chosen before anyone asked what decision the
user makes on this screen.
**Why:** It is the landing-page template problem inside an app: layout from memory rather than
from the work. The important thing (a failing job, an overdue invoice) ends up as a table row
below decorative counters.
**Default correction:** Name the screen's job and the decision the user makes on it. Build the
hierarchy around that. Keep the shell if it fits; change what fills it.
**Acceptable when:** The shell fits the information architecture and its contents are chosen
from the task. Sidebar plus content is a strong convention for multi-section apps.
**Scope:** APPLICATION, DASHBOARD, OPERATIONS, DATA_EXPLORATION.
**Severity:** MEDIUM. HIGH if the primary decision is buried (also UI-06).

### UI-08: Default AI palette
**Tell:** Indigo, violet, or purple accent (Tailwind `indigo-500`, `#6366f1`, `#8b5cf6`), blue to
purple or purple to pink gradients, neon accents, slate-900 plus indigo "default dark", gradient
text in headlines, colored glows, without any brand reason.
**Why:** These are the most over-represented color decisions in generated UI. Unexplained, they
signal that no color decision was made.
**Default correction:** Derive the palette from the brand or the product's context. Give each
color a role (see `references/color.md`). Keep gradients for a stated purpose such as separating
a hierarchy level or expressing a brand asset.
**Acceptable when:** Purple or a gradient is part of the brand, or serves a recorded purpose.
Purple is not banned; default purple is.
**Scope:** All.
**Severity:** HIGH.

### UI-09: Effects as the default surface treatment
**Tell:** Glassmorphism, backdrop blur, glow, and gradient borders applied broadly: navbar,
cards, modals, sidebar, and buttons all frosted or glowing at once.
**Why:** Effects are emphasis tools. Applied everywhere they flatten hierarchy (every surface on
the same frosted layer), hurt legibility over busy backgrounds, and cost rendering performance.
**Default correction:** Solid surfaces by default. Use translucency where it explains layering
(a sheet over content, a nav over imagery) and verify text contrast on the worst part of the
background. Reserve glow for focus or one focal element.
**Acceptable when:** There is a clear hierarchy or brand reason, recorded in `DESIGN.md`, and
contrast holds. A single glass panel over photography can be exactly right.
**Scope:** All.
**Severity:** HIGH when broad and unexplained; MEDIUM when limited but unexplained.

### UI-10: Decorative backgrounds without identity
**Tell:** Graph-paper grids, dot grids, blueprint lines, blurred color orbs, mesh gradients, or
noise layers placed behind content to make a flat page feel "technical" or "modern".
**Why:** Texture without a reason is the cheapest way to look designed. It reads as filler.
**Default correction:** Remove it, or replace it with something owned by the product (a pattern
from the brand, real product imagery, a data-derived motif).
**Acceptable when:** The texture is part of the brand or signature element, or carries meaning
(a grid in a CAD or layout tool, a map background). Keep it subtle enough not to reduce contrast.
**Scope:** All; most common in MARKETING.
**Severity:** MEDIUM.

### UI-11: Accent everywhere, palette without roles
**Tell:** The accent color appears on buttons, icons, badges, links, borders, backgrounds, and
chart series at once; or five to seven unrelated colors appear with no system.
**Why:** An accent stops working the moment it is everywhere. A palette without roles cannot
encode meaning.
**Default correction:** Assign roles: neutral surfaces and text, one primary action color,
semantic status colors used only for status, data colors used only for data.
**Acceptable when:** Brand systems with deliberate multi-color identities (education, children,
creative) where roles are still defined.
**Scope:** All.
**Severity:** MEDIUM.

### UI-12: Unearned dark theme
**Tell:** The whole product is dark because dark "looks tech", with no audience, environment, or
brand reason.
**Why:** Theme is a decision. Dark-by-default for a content-heavy product can hurt long-form
reading and signals trend-following.
**Default correction:** Choose theme from audience, environment, and brand. If there is no strong
reason for a fixed theme, follow the system preference when the project can support both.
**Acceptable when:** Developer tools, media and video products, creative tools, control rooms and
low-light environments, brand identity, or user expectation.
**Scope:** MARKETING, EDITORIAL, APPLICATION. Usually legitimate in DEVELOPER_TOOL,
CREATIVE_EXPERIENCE, OPERATIONS.
**Severity:** MEDIUM.

### UI-13: Uniform or excessive radius
**Tell:** Every element shares one large radius: pill buttons, pill inputs, `rounded-2xl` cards,
rounded modals, rounded table containers.
**Why:** Shape distinguishes element types. One radius everywhere erases the difference between
an input, a card, and a tag.
**Default correction:** A small radius scale applied by element role; nested radii smaller than
their parents. See `references/components.md`.
**Acceptable when:** The brand's shape language is deliberately soft or deliberately sharp and
applied consistently, with type distinctions carried by other means.
**Scope:** All.
**Severity:** MEDIUM.

### UI-14: Shadows everywhere
**Tell:** Every card, button, and section carries a soft large shadow; the page has no ground plane.
**Why:** When everything is elevated, elevation communicates nothing.
**Default correction:** Most surfaces sit flat, separated by borders, spacing, or tone. Reserve
shadow for things that float above the page (menus, dialogs, popovers, dragged items).
**Acceptable when:** A brand's material language uses depth consistently and meaningfully.
**Scope:** All.
**Severity:** MEDIUM.

### UI-15: Spacing without rhythm
**Tell:** One gap value used for everything (nav, form fields, cards, sections), or arbitrary
values with no scale; related items as far apart as unrelated ones.
**Why:** Spacing is how layout expresses grouping. Without rhythm, structure has to be carried by
boxes and borders.
**Default correction:** A spacing scale with clear steps; tighter inside groups than between
them; larger steps between sections.
**Acceptable when:** Not applicable; any system with consistent grouping passes.
**Scope:** All.
**Severity:** MEDIUM.

### UI-16: Typeface chosen by default
**Tell:** A font chosen because it is the model's or framework's default, with no reason recorded,
or a pairing that has become a cliché (a high-contrast display serif over Inter for "elegance").
**Why:** Type is a large share of a product's voice. A default choice says nothing.
**Default correction:** Record why the face fits the product: legibility at the sizes used,
numeric features, language coverage, brand voice, performance budget.
**Acceptable when:** There is a reason. Inter, Geist, system UI stacks, and other popular faces are
excellent choices for dense applications and multilingual products. No typeface is banned.
**Scope:** All; weigh lightly in APPLICATION and OPERATIONS at low CHARACTER.
**Severity:** LOW.

### UI-17: Typographic costume
**Tell:** Large monospace headings for a "technical vibe" on a product that is not technical;
wide-tracked uppercase eyebrow labels above every section; crushed-tracking giant display type on
every heading. (An eyebrow that repeats its heading is UI-18.)
**Why:** These borrow the look of a category without doing typographic work.
**Default correction:** Use monospace for code, data, identifiers, and tabular content. Use
eyebrows only when they add information the heading does not.
**Acceptable when:** DEVELOPER_TOOL products, where monospace is native vocabulary; a brand voice
that is deliberately typographic.
**Scope:** MARKETING, EDITORIAL.
**Severity:** LOW.

### UI-18: Badge and eyebrow clichés
**Tell:** Capsule badges with thin border, glow, dot, and uppercase text ("AI-powered", "New",
"Beta") without a real status; a pill above the H1 repeating what the headline says.
**Why:** Decoration dressed as information, placed in the same spot on every generated page.
**Default correction:** Cut it, or fold the information into the headline or subhead. Keep badges
that carry a real, current status.
**Acceptable when:** The badge marks a real, time-bound state (a launch this week, a beta that
affects what users can expect).
**Scope:** MARKETING, APPLICATION.
**Severity:** MEDIUM.

### UI-19: Indicators that mark nothing
**Tell:** Glowing or pulsing dots beside headings or nav items, "live" indicators on static
content, notification badges with no notifications, decorative progress rings.
**Why:** They borrow status language for things that have no status, which teaches users to
ignore real indicators.
**Default correction:** A dot or badge must map to a documented state. Pulsing is reserved for
genuinely live, attention-worthy states and respects reduced motion.
**Acceptable when:** It marks a real state.
**Scope:** All.
**Severity:** MEDIUM.

### UI-20: Decoration posing as signal
**Tell:** Colored left stripes on cards that mark no state; arrows (`→`, `↗`) on nearly every button
and link.
**Why:** Signals used as decoration lose meaning where they are needed.
**Default correction:** Keep a left edge where it encodes state (active nav item, alert severity,
selected row). Keep arrows where direction matters (external link, next step).
**Acceptable when:** It encodes state or direction.
**Scope:** All.
**Severity:** LOW.

### UI-21: Generic or inconsistent icons
**Tell:** Sparkles, rockets, lightning bolts, and robots as feature icons; icons in gradient
rounded squares; emoji used as interface icons; mixed icon sets, stroke widths, or sizes.
**Why:** Generic glyphs say nothing about the specific feature; inconsistency reads as assembled.
**Default correction:** One icon family at consistent sizes and stroke widths, chosen for
relevance. If no icon is relevant, use none; the label does the work.
**Acceptable when:** Any well-made icon library works when used consistently. Emoji are legitimate
content in social, messaging, and consumer products (reactions, user-generated content).
**Scope:** All.
**Severity:** LOW.

### UI-22: Generic imagery and costume product shots
**Tell:** Stock illustration packs and blob people with no connection to the product; AI images
with artifacts; perspective-tilted dashboard mockups with glow; fake terminal windows or skeleton
bars standing in for a product screenshot.
**Why:** Imagery is evidence. Costume imagery signals that there is nothing real to show.
**Default correction:** Real screenshots, real product photography, real data visualizations, or
no image. A straight, honest screenshot beats a dramatic fake.
**Acceptable when:** Illustration commissioned or chosen for the brand; a real terminal session
for a CLI product.
**Scope:** MARKETING, EDITORIAL, ECOMMERCE.
**Severity:** MEDIUM.

### UI-23: Motion without purpose
**Tell:** Fade-up on every element, floating or bobbing shapes, hover scale on every card,
marquee logo strips, animated gradient backgrounds, staggered reveals on content users need
immediately, spring bounce on everything.
**Why:** Motion is attention. When everything moves, nothing is emphasized; content is delayed;
batteries drain; vestibular-sensitive users suffer.
**Default correction:** Give every animation a job: explain a state change, show spatial
relationships, confirm an action, or tell a deliberate story at high MOTION. See
`references/motion.md`. Reduced-motion handling is covered by A11Y-10.
**Acceptable when:** The motion has a job and matches the MOTION dial.
**Scope:** All.
**Severity:** MEDIUM for template motion stacked across a page; LOW for one unnecessary
micro-animation.

### UI-24: Charts without a question
**Tell:** A chart placed because the space looked bare; generic titles ("Overview",
"Performance"); rainbow series; 3D or glowing marks; donuts with many slices; axes the reader
cannot act on.
**Why:** A chart is an answer to a question. Without one, it costs attention and conveys nothing.
**Default correction:** Write the question first and put it in the title ("Failed jobs per hour,
last 24 h"). Choose the chart form for that question. If a sentence or a number answers it,
use that instead. See `references/charts.md`.
**Acceptable when:** Decorative data art is the explicit intent (CREATIVE_EXPERIENCE) and no
reader decision depends on it.
**Scope:** DASHBOARD, OPERATIONS, DATA_EXPLORATION, MARKETING.
**Severity:** MEDIUM.

### UI-25: Template pricing
**Tell:** Exactly three tiers with the middle one highlighted as "Most popular", regardless of the
actual pricing; identical feature lists padded to equal length.
**Why:** The shape comes from the template, not from the business model. A fake "most popular"
label is also a factual claim (IN-02).
**Default correction:** As many tiers as the product really has. Highlight the tier that serves
most buyers only if that is true. Use a comparison table when tiers differ on many dimensions.
**Acceptable when:** The product genuinely has three tiers and the highlight is accurate.
**Scope:** MARKETING, ECOMMERCE.
**Severity:** MEDIUM.

### UI-26: Unrequested clone of a known product
**Tell:** The overall visual identity mimics Linear, Vercel, Stripe, Notion, or Apple without being
asked: same palette, type, shadows, and hero composition.
**Why:** The model reaches for the most-imitated products. The result belongs to someone else's brand.
**Default correction:** Learn from their conventions (information architecture, interaction
patterns), but derive identity from this product.
**Acceptable when:** The user asked for that reference direction, or the product lives inside that
platform's ecosystem and should match it (a Shopify app using Polaris).
**Scope:** All.
**Severity:** MEDIUM.

### UI-27: Declared direction not executed
**Tell:** The output contradicts `DESIGN.md`: a VARIANCE 8 page that is fully symmetric, a MOTION 1
product with scroll choreography, a declared signature element that appears once or not at all,
two competing signatures, tokens ignored in favor of hard-coded values.
**Why:** Direction that is declared but not built is decoration on paper. It also means the audit
cannot trust the document.
**Default correction:** Bring the build in line with `DESIGN.md`, or update `DESIGN.md` if the
direction itself changed (and say so).
**Acceptable when:** The deviation is recorded in `DESIGN.md` §13.
**Scope:** All.
**Severity:** MEDIUM. HIGH if the brand definition itself is contradicted.

### UI-28: Untouched library defaults
**Tell:** A component library used exactly as shipped (default radius, colors, shadows, focus ring)
in a product whose `DESIGN.md` calls for mid or high CHARACTER.
**Why:** The product looks like the library's documentation site rather than like itself.
**Default correction:** Re-tokenize: map the library's theme variables to the brand's color, type,
radius, and elevation tokens.
**Acceptable when:** CHARACTER is low and the library is the chosen design system (an internal
console built on Carbon, a Shopify app on Polaris). Consistency with a platform is a valid identity.
**Scope:** All.
**Severity:** MEDIUM.

---

## CL: Clusters

### CL-01: Default cluster
**Tell:** Three or more unexplained, in-scope visual or copy tells (UI, CP) in one view, at least
one of them MEDIUM. CD and A11Y findings do not count toward clusters, and one issue counts once.
The canonical case: default purple gradient, gradient headline text, eyebrow pill, centered hero
with two buttons, three icon cards, glass navbar, floating blobs, and hype copy together.
**Why:** Single tells are often fine. The combination is what users recognize as generated in
under two seconds.
**Default correction:** Fix the tells that carry the least reason first; usually two or three fixes
break the cluster. Do not respond by adding novelty (UI-01).
**Acceptable when:** Each tell in the cluster has a recorded reason.
**Scope:** All.
**Severity:** HIGH (one cluster finding per view, in addition to the individual findings).
