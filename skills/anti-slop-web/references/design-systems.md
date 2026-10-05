# Design Systems and Tokens

When to adopt an existing component system, how to make it the product's own, and how to
structure design tokens and themes. Load when choosing or extending a component library or
setting up tokens, together with `color.md`. The project's existing system and `DESIGN.md`
override everything here; a mature in-house system is direction, not something to replace.

## Adopt, extend, or build?
**What:** The decision between using a system as-is, customizing one, or building your own.
**Use when:**
- Adopt as-is: low CHARACTER products, internal tools, or apps living inside a platform (a Shopify
  admin app, a Microsoft Teams app) where matching the platform is the right identity.
- Adopt and re-tokenize: most products. Accessible behavior from the library, identity from your
  tokens.
- Build: you have a dedicated team, unusual interaction needs, or a strong brand that existing
  systems fight.
**Avoid when:**
- Building primitives such as comboboxes, dialogs, and menus from scratch without the capacity to
  get keyboard and screen reader behavior right. Use tested primitives.
**Archetypes:** All.
**Tradeoffs:**
- Full systems ship fast and consistent but carry a recognizable look and bundle weight.
- Unstyled primitives give full visual control and strong accessibility behavior but you design
  every surface.
- Copy-into-your-repo approaches give ownership and no lock-in but you maintain the code.
**Accessibility:**
- A library's accessibility claims cover its components used as documented. Custom compositions
  still need testing (A11Y-01 to A11Y-19).
**Common AI misuse:** Installing a library the project does not use, or mixing two (CD-01).

## Index of well-known systems

A neutral orientation, not a ranking. Check each project's current documentation, maintenance
status, and license before adopting.

| System | Ecosystem | Character | Accessibility posture | Often fits |
|---|---|---|---|---|
| MUI | React | Full component suite, Material roots | Mature, documented | Enterprise apps needing many components fast |
| Radix Primitives | React | Unstyled primitives | Strong focus on WAI-ARIA behavior | Custom design systems |
| React Aria | React | Hooks and unstyled components | Very thorough, international and touch aware | Systems where accessibility depth matters |
| Headless UI | React, Vue | Unstyled, small set | Solid for its components | Tailwind projects needing a few complex widgets |
| shadcn/ui | React | Copy-in components built on primitives | Inherits primitives | Teams wanting ownership of styled code |
| Ant Design | React | Full suite, dense enterprise look | Good, with gaps in complex widgets | Data-heavy admin tools |
| Mantine | React | Full suite plus hooks | Good | Batteries-included apps |
| Chakra UI | React | Styled components with style props | Good | Teams valuing style-prop ergonomics |
| IBM Carbon | React, Web Components, others | Enterprise, rigorous guidance | Strong, extensively documented | Enterprise data and operations products |
| Material Design 3 | Android, Flutter, Web | Opinionated platform language | Documented roles and contrast | Products aligned with Google platforms |
| Fluent UI | React, Web Components | Microsoft platform language | Strong | Microsoft 365 and Azure ecosystem apps |
| Polaris | React, Web Components | Shopify admin language | Strong | Shopify apps |
| Atlassian Design System | React | Atlassian product language | Strong | Jira and Confluence ecosystem apps |
| GOV.UK Design System | HTML, Nunjucks | Plain, research-tested public service patterns | Exceptionally well researched | Government and public services, form-heavy flows |
| U.S. Web Design System (USWDS) | HTML, CSS | Public service language | Strong, research-based | U.S. government and civic sites |

Public-sector systems are worth reading even if you never adopt them: their form, error, and
content guidance comes from large-scale user research.

## Re-tokenization and the CHARACTER dial
**What:** Mapping a library's theme variables to the product's own color, type, radius,
elevation, and motion tokens.
**Use when:**
- CHARACTER is mid or high (4 and above). Shipping untouched defaults makes the product look like
  the library's documentation site (UI-28).
**Avoid when:**
- CHARACTER is low and the library is the chosen system. A bank console that looks like Carbon is
  consistent, not generic.
**Archetypes:** All.
**Tradeoffs:**
- Re-tokenizing color and type gives most of the identity for little cost. Changing component
  anatomy (how a select works) gives little identity for much risk.
- Keep the library's focus and state behavior; restyle focus rings to the brand but keep them
  visible and contrast-compliant (A11Y-03).
**Common AI misuse:** Default radius, default indigo, default shadows everywhere (UI-08, UI-13,
UI-28).

## Three-tier tokens
**What:** Primitive tokens (raw values), semantic tokens (meaning), and component tokens (where a
semantic value is used). Components reference semantic or component tokens, not primitives.
**Use when:**
- Any product with themes, multiple brands, or more than a handful of components.
**Avoid when:**
- A one-page site; a short set of CSS variables is enough.
**Tradeoffs:**
- More indirection to learn, but themes and rebrands become remaps instead of rewrites.
- Too many component tokens recreate the problem; add them only where components need to diverge.

```css
:root {
  /* primitive */
  --blue-600: #2456c7;  --blue-300: #8fb0f2;  --gray-950: #121417;  --gray-50: #f7f8fa;
  /* semantic */
  --color-action-primary: var(--blue-600);
  --color-surface-page: var(--gray-50);
  --color-text-primary: var(--gray-950);
  /* component */
  --button-primary-bg: var(--color-action-primary);
}
[data-theme="dark"] {
  --color-action-primary: var(--blue-300);
  --color-surface-page: var(--gray-950);
  --color-text-primary: var(--gray-50);
}
```

Values are illustrative. Theme changes happen in the semantic layer only.

## W3C design token format
**What:** The Design Tokens Community Group (DTCG) JSON format: tokens with `$value` and `$type`,
aliases with `{group.token}` references.
**Use when:**
- Tokens move between tools (design files, code, documentation) or across platforms.
**Avoid when:**
- A single web codebase where CSS variables are the source of truth.
**Tradeoffs:**
- Tool support is growing but uneven; a build step (for example Style Dictionary) turns the JSON
  into CSS, iOS, and Android outputs.

## Theming and dark mode
**What:** Supporting more than one theme through the semantic layer.
**Use when:**
- Users expect it, the environment demands it (see `dashboards.md` on control rooms), or the brand
  calls for it.
**Tradeoffs:**
- Every theme doubles visual QA. If you cannot verify a theme, do not ship its toggle (FN-06).
- Dark themes need their own values for elevation (lighter surfaces for higher layers instead of
  shadows), status colors, and chart palettes, not inverted light values.
- Following the system preference (`prefers-color-scheme`) is a good default when both themes are
  maintained; an explicit toggle can override it.
**Accessibility:**
- Verify contrast for every pair in every theme (A11Y-04, A11Y-05).

## Mixing systems
**What:** Using components from more than one library.
**Tradeoffs:**
- Common and sometimes reasonable (a headless combobox inside a styled system), but each library
  brings its own tokens, focus styles, z-index scale, and CSS reset. Conflicts surface as
  inconsistent focus rings, stacking bugs, and doubled bundle size.
- If you mix, wrap foreign components in your tokens and test overlays together.
**Common AI misuse:** Importing a second component library for one widget without checking the
manifest (CD-01), producing two visual languages on one screen.

## Platform-native identity
At low CHARACTER, looking like the platform is a valid identity. Users of a Shopify app, a Teams
tab, or an internal tool built on the company system benefit from familiarity. Record the choice in
`DESIGN.md` §8 ("Component library: Polaris, not re-tokenized, to match Shopify admin") so audits
do not flag it under UI-28 or UI-26.

## Documenting decisions
Record in `DESIGN.md`: which system and version, whether it is re-tokenized and why, where the
tokens live, which components are custom, and any library default intentionally kept. A short,
accurate record prevents later agents from "fixing" deliberate choices.
