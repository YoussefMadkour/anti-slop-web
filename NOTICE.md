# Notice and Attribution

anti-slop-web is an original consolidation that incorporates and adapts ideas, structure, and
some material from three MIT-licensed projects. Concepts were evaluated, merged, and rewritten
rather than copied wholesale. Where wording or structure is substantially adapted, the upstream
copyright and license notices below apply to that material. This repository does not claim
original authorship of the adapted ideas.

Upstream versions reviewed: the default branch of each repository as of 2026-10-05
(jhuse25/anti-slop-design-skills at cf80583, Vanszs/Anti-AI-UI at fd2a142,
miqdadbadjuber/anti-slop at 388cbe3, its skill version 3.2.20).

See [docs/source-map.md](docs/source-map.md) for which ideas came from which project, and
[docs/not-carried-over.md](docs/not-carried-over.md) for what was deliberately left out.

The lists below summarize the main adapted ideas; docs/source-map.md is the complete mapping.

## Upstream projects

### 1. jhuse25/anti-slop-design-skills
https://github.com/jhuse25/anti-slop-design-skills

Adapted: the design-before-implementation workflow, the project `DESIGN.md` concept, the
VARIANCE, MOTION, and DENSITY dials, the signature element (memorable, owned, sustained; one or
none), brand re-tokenization, required loading, empty, and error states, responsive and motion
performance guidance, dependency verification, server and client component separation, and the
pre-flight gate concept.

That project's own NOTICE states that its discipline was independently reimplemented after
studying google-labs-code/stitch-skills (Apache License 2.0) and Leonxlnx/taste-skill, and that it
does not redistribute their text. anti-slop-web does not use material from those projects directly.

```
MIT License

Copyright (c) 2026 jhuse25


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 2. miqdadbadjuber/anti-slop
https://github.com/miqdadbadjuber/anti-slop

Adapted: the "filter, not style guide" philosophy, the Tell, Why, Fix entry structure, purpose-gated
rules (technique allowed, reason required), tiered severity, the delivery gate with evidence, the
UI, copywriting, accessibility ("human"), mobile layout, and code-comment concerns, prevention of
fabricated testimonials, metrics, logos, and claims, content-driven structure, the app and dashboard
patterns, the "look for clusters, not isolated tells" principle, honest placeholders, the "one
decisive question" approach to ambiguous direction, and the contrast-checking approach (the script
in this repository is a new implementation).

```
MIT License

Copyright (c) 2026 Miqdad Badjuber (antislop)


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### 3. Vanszs/Anti-AI-UI
https://github.com/Vanszs/Anti-AI-UI

Adapted, mainly as reference knowledge: layout skeletons and intrinsic layout primitives,
typography scales and per-role settings, component, form, navigation, and overlay patterns,
motion timing and reduced-motion techniques, dashboard and chart guidance, the design-system index
and token tiers, the severity scale vocabulary (P0, HIGH, MEDIUM, LOW), and the idea of a
combined "instant" signature of co-occurring tells (adapted here as the CL-01 cluster rule).

Notes on provenance within that repository:
- Its `ui-ux-pro-max/` directory is third-party work by NextLevelBuilder
  (https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, MIT), included there with permission.
  anti-slop-web does **not** use any of that directory's data, scripts, or text.
- Its `Anti-AI-SLop` and `component-reference-design` skill files carry an `author: b4r7x`
  metadata field. They are used here under the repository's published MIT license, and only as
  rewritten and adapted material.
- Its references cite many public design systems and authors (Every Layout, Josh Comeau,
  Refactoring UI, NN/g, W3C WAI-ARIA Authoring Practices, IBM Carbon, Material Design, and others).
  Those are cited for context; no material from them is reproduced here.

```
MIT License

Copyright (c) 2025 Vanszs


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## This repository

New material by Youssef Madkour (the authority hierarchy, the CHARACTER dial, archetype classification, rule scoping
by archetype, the waiver mechanism, the unified rule schema and IDs, the reference library rewrite,
the audits, the agent, and the contrast script) is released under the MIT License in
[LICENSE](LICENSE).
