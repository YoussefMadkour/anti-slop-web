---
name: anti-slop-copy
description: "Copy and microcopy specialist for web UI built or reviewed by AI agents: generic hype language, fabricated proof, vague CTAs, fake names and statistics, placeholder marketing language, formulaic sentence rhythm, chatbot residue, unnecessary emoji, unhelpful error and empty-state text, and product-specific wording. Load with anti-slop-web whenever a task writes or edits user-facing text."
license: MIT
---

# Anti-Slop Copy

Interface copy is part of the design. Generated copy has recognizable habits: inflated verbs,
claims with nothing behind them, every list in threes, and buttons that say "Get Started" no
matter what they do. The fix is specificity, and specificity has to come from the product, the
owner, or real data, never from invention.

Two rules govern everything below:

1. **Never invent facts.** A rewrite adds no number, name, quote, customer, date, benchmark, or
   capability that is not in the source material or supplied by the user. If a sentence needs a
   real detail to work, ask for it or write the plain version without it. Fabricated proof is
   covered by `IN-01` to `IN-04` in `../anti-slop-web/rules.md` and is always P0 or HIGH.
2. **Do not sterilize.** Copy with no voice is as machine-like as copy full of tells. If the
   owner supplies a voice (a style guide, a writing sample, existing pages), match it. A writing
   sample outranks this skill's stylistic preferences.

Rules use the kit schema and apply to every archetype unless noted.

## Look for clusters, not single tells

Many patterns below appear in good human writing. One em dash, one "however", one set of three,
or one short punchy sentence proves nothing. Flag a pattern when it repeats or appears alongside
others. Preserve signs of a real writer: specific, hard-to-invent detail, mixed feelings,
irregular sentence lengths, asides, and deliberate quirks.

---

### CP-01: Hype vocabulary
**Tell:** Elevate, unlock, unleash, supercharge, empower, revolutionize, seamless, effortless,
cutting-edge, next-generation, world-class, robust, powerful, game-changing, "AI-powered" as a
headline, "for modern teams", "in seconds".
**Why:** These words signal an intent to impress without saying anything. They fit every product,
so they describe none.
**Default correction:** Say what the product does, for whom, by what mechanism.
"Elevate your team's workflow" becomes "Assign, review, and ship pull requests from one queue."
**Acceptable when:** The word is literal and accurate ("robust" in an engineering spec with a
stated tolerance), or the brand voice deliberately uses it and the claim is true.
**Scope:** MARKETING, ECOMMERCE, EDITORIAL; also onboarding and empty states in apps.
**Severity:** HIGH when hype words carry the headline or recur across the page; MEDIUM for an
isolated instance.

### CP-02: Vague calls to action
**Tell:** "Get Started", "Learn More", "Try Now", "Explore", "Discover", "Submit" used regardless
of what happens next.
**Why:** The label is the user's best prediction of what the click does. Vague labels add doubt.
**Default correction:** Name the action or its result: "Create workspace", "See pricing for teams",
"Book a 20-minute demo", "Save changes", "Send invoice".
**Acceptable when:** The convention is genuinely clear in context ("Next" in a wizard, "Search").
**Severity:** MEDIUM.

### CP-03: Placeholder marketing language left in
**Tell:** Lorem ipsum, "Your tagline here", "Feature one", "Lorem Inc.", "[Company] helps teams do
X", template headlines ("The future of X is here", "Transform your workflow"), unfilled
`[placeholder]` markers in a deliverable presented as final.
**Why:** It shows the page was generated and never written.
**Default correction:** Write from the product's real content, or mark the gap explicitly and list
it in the delivery report as missing content.
**Acceptable when:** Drafts and prototypes where placeholders are clearly labeled.
**Severity:** HIGH.

### CP-04: Significance inflation and empty claims
**Tell:** "A new era of", "marking a pivotal moment", "a testament to", "industry-leading",
"trusted by teams everywhere", "experts agree", unnamed authorities, generic positive conclusions
("The future looks bright").
**Why:** Ceremony where content should be; claims without a subject or source.
**Default correction:** State the concrete effect, name the source, or cut the sentence. End on
the last useful fact.
**Acceptable when:** A named, real source supports the claim.
**Severity:** MEDIUM. Escalates to IN-03 (P0) if it asserts a factual claim that is false.

### CP-05: Generic names for specific things
**Tell:** Feature names like "Advanced Analytics", "Smart Automation", "Powerful Integrations",
"Seamless Collaboration", "AI Insights".
**Why:** Adjective plus category tells the reader nothing about what the feature is.
**Default correction:** Name the actual thing: "Funnel drop-off by step", "Auto-assign by CODEOWNERS",
"Two-way Salesforce sync".
**Acceptable when:** The product's own established feature name.
**Scope:** MARKETING, APPLICATION navigation and settings labels.
**Severity:** MEDIUM.

### CP-06: Redundant headline and subhead
**Tell:** The subhead restates the headline in longer words; a section intro repeats the section
title. (An eyebrow badge repeating the headline is UI-18.)
**Why:** It adds reading without adding information.
**Default correction:** Headline says what; subhead says how, for whom, or why it is different.
**Acceptable when:** A deliberate restatement for scanning on long pages (docs section intros).
**Severity:** MEDIUM.

### CP-07: Formulaic rhythm
**Tell:** Every list in threes; "It's not just X, it's Y"; "No X. No Y. Just Z."; runs of dramatic
fragments; aphorism templates ("X is the new Y"); false ranges ("from first click to final
invoice"); synonym cycling to avoid repetition; every paragraph the same length.
**Why:** The rhythm is a template, so the copy sounds assembled.
**Default correction:** Use the number of items the content has. Say the plain version of the
emphatic construction. Vary sentence length. Repeat the clearest word instead of cycling synonyms.
**Acceptable when:** Used once, deliberately, where the emphasis is earned.
**Severity:** MEDIUM.

### CP-08: Chatbot residue and signposting
**Tell:** "I hope this helps", "Let me know if you have questions", "Let's dive in", "Here's what
you need to know", "In today's fast-paced world", "Honestly?", "At its core".
**Why:** Conversation artifacts pasted into a product. They slow the reader and expose the source.
**Default correction:** Delete the frame; start with the substance.
**Acceptable when:** Conversational products where the voice is intentionally chatty and specific.
**Severity:** MEDIUM.

### CP-09: Unhelpful microcopy
**Tell:** (The wording side of FN-03; report a state that lacks cause or next step under FN-03.)
"Invalid input", "Error 500", "No data", "Are you sure?", disabled
buttons with no hint why, success messages that do not say what succeeded.
**Why:** Microcopy is where users get unstuck. Generic messages leave them stuck.
**Default correction:** Errors say what happened, why if known, and what to do next, in the user's
terms: "Card declined by your bank. Try another card or contact the bank." Empty states say why
and how to fill them. Confirmations name the object and the consequence: "Delete 3 invoices? This
cannot be undone." Success says what happened: "Invoice INV-2041 sent to billing@client.example."
**Acceptable when:** Not applicable.
**Scope:** APPLICATION, DASHBOARD, OPERATIONS, ECOMMERCE, DATA_EXPLORATION.
**Severity:** MEDIUM. Missing feedback entirely is FN-04 (P0).

### CP-10: Inconsistent terminology
**Tell:** The same object called a project, a workspace, and a space on different screens; buttons
that say "Remove" in one place and "Delete" for the same action elsewhere; mixed tone between
marketing site and app for no reason.
**Why:** Users assume different words mean different things.
**Default correction:** Keep a short glossary in `DESIGN.md` or the codebase; one name per concept;
one verb per action.
**Acceptable when:** Not applicable.
**Severity:** MEDIUM.

### CP-11: Unnecessary emoji
**Tell:** Emoji leading headings, bullets, buttons, and toasts: rocket on launch, checkmark on
every feature, fire on the CTA.
**Why:** Decoration that carries no information and flattens the brand voice into the generated default.
**Default correction:** Remove; if a mark is needed, use a relevant icon or nothing.
**Acceptable when:** Consumer, social, and messaging products whose voice includes emoji; user-
generated content; reactions. Emoji used as interface icons are UI-21.
**Severity:** LOW.

### CP-12: Punctuation and formatting tics
**Tell:** Clusters of em dashes; bold on every key term; every list item starting with a bolded
label and a colon; scare quotes; ALL CAPS for emphasis; title case on every heading against the
product's style.
**Why:** Mechanical emphasis is emphasis nowhere.
**Default correction:** Let sentences carry emphasis. Choose one heading case and use it. Use em
dashes as sparingly as any punctuation, or follow the brand style guide.
**Acceptable when:** The brand voice or the owner's writing uses them deliberately.
**Severity:** LOW.

### CP-13: Over-sterilized voice
**Tell:** After cleanup, the copy is accurate but flat, interchangeable, and voiceless; the owner's
own distinctive phrasing has been "corrected" away.
**Why:** Removing tells is half the job. Voice is what makes copy belong to the product.
**Default correction:** Restore the owner's phrasing and specific details; pick a voice consistent
with `DESIGN.md` §3 and CHARACTER.
**Acceptable when:** Low-CHARACTER institutional products where plain, neutral language is the voice.
**Severity:** LOW.

---

## Placeholders that are honest

When real content is missing, say so in the interface draft and in the delivery report:

| Need | Honest placeholder |
|------|--------------------|
| Testimonial | `[TESTIMONIAL: real customer quote and name needed]` or omit the section |
| Statistic | `[REAL DATA: active teams]` or no number |
| Customer logos | Omit the logo bar until real logos with permission exist |
| Person in a form field | Field placeholder "Your name", never "John Doe" as a value |
| Product image | `[PRODUCT SCREENSHOT: dashboard overview]` |

## Draft, audit, final

1. **Draft** from real source material: product docs, the owner's notes, existing pages.
2. **Audit** with two questions: what makes this read as generated, and does it state any fact,
   name, number, or claim not in the source?
3. **Revise** for both answers, then read it aloud once.

## Copy checklist (quick)

- [ ] No invented numbers, names, quotes, logos, or claims (IN-01 to IN-04)
- [ ] No hype vocabulary; features named specifically (CP-01, CP-05)
- [ ] CTAs name the action (CP-02)
- [ ] No placeholder language left in a final deliverable (CP-03)
- [ ] Errors, empty states, and confirmations say what and what next (CP-09)
- [ ] One term per concept (CP-10)
- [ ] Voice present and consistent with `DESIGN.md` (CP-13)
