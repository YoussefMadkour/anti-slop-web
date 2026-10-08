# Design Direction: Working Like a Designer

How to go from a product's purpose to concrete visual decisions: concept, palette, type,
composition. Load for workflow steps 1 to 6 whenever direction is being set (new product, new
surface, redesign, or a `DESIGN.md` that leaves palette or type open). With an existing brand or
a confirmed `DESIGN.md`, skip to the parts that are still open; never redesign a working system.

The kit has no house style. That does not mean making no choices: a designer commits to
specific colors, faces, and compositions, and can explain each one from the product.

---

## 1. Read the brief like a designer

Answer in a few lines before touching color or type:
- **Purpose:** what the product does for whom, and what this screen must get them to do.
- **Feeling:** three adjectives the interface should evoke, and three it must not (`DESIGN.md`
  §3). Make them specific: "calm, exact, quietly confident", not "modern, clean, professional".
- **Context:** where and how it is used (glare, low light, glanced at, read for an hour).
- **Domain material:** what the product's world looks like offline. A logistics tool has
  manifests, labels, and route maps; a bakery has flour, paper bags, and chalkboards; a
  research tool has journals and figures. This is where owned visual ideas come from.
- **Competitors:** what the category looks like, so you can choose to fit it or stand apart on purpose.

## 2. Explore directions before choosing

For a new product, surface, or redesign, sketch **two or three distinct directions** in words,
each a short paragraph:

```
Direction A: "Field manual"
Idea: the product as a well-made reference tool used outdoors.
Palette: warm paper neutrals, a deep forest green for action, safety orange only for alerts.
Type: a sturdy humanist sans for UI, tabular figures, condensed caps for section labels.
Composition: strict grid, ruled dividers instead of cards, dense but airy margins.
Signature: map-style coordinates and scale bars marking sections.
Fits: CHARACTER 6, DENSITY 6. Risk: could feel rustic for enterprise buyers.
```

Directions must differ in idea, not just in hue. Recommend one with a reason, and let the owner
choose (ask once). If the user asked you to just build, pick the recommendation, state it, and
proceed. Record the chosen direction in `DESIGN.md` §3 and §4.

## 3. Choose the palette

Work from meaning to values, not from a swatch library.

1. **Decide the color strategy** from CHARACTER and archetype: neutral-led with one action color
   (most applications and tools), a brand-led two-color voice, or a multi-hue identity with
   strict roles. See `references/color.md`.
2. **Find the primary hue** from, in order: the existing brand; the domain material (the green
   of survey maps, the blue of cyanotypes, the red of a stamp); the feeling adjectives; deliberate
   contrast with competitors. Write the reason in one line. "Blue means trust" is not a reason;
   "the blue of engineering drawings, because users are civil engineers" is.
3. **Decide temperature and saturation of the neutrals.** Neutrals cover most of the screen and
   set the mood more than the accent does: warm paper, cool steel, true gray.
4. **Generate scales and semantic tokens** with `scripts/palette.py`, which builds OKLCH scales
   from your seeds and reports contrast for key pairings in light and dark themes:
   `python3 scripts/palette.py --primary "#1f6f5c" --accent "#d9822b" --neutral-tint primary`
   The script may pick a darker step than the seed for buttons to meet contrast. If that loses
   the feeling, change how the color is used (as a surface or large area) rather than failing contrast.
5. **Assign roles and ratios:** where the primary appears, where the accent appears (one or two
   places), semantic colors for status only.
6. **Test on a real screen,** not on swatches: build the key screen, then look at it in
   grayscale (hierarchy must survive without color) and squinting (one clear focal point).

## 4. Choose the type

1. **Define the jobs:** UI text at small sizes, long reading, display moments, numbers, code.
   Fewer jobs means fewer faces.
2. **Shortlist three faces** that fit the jobs and the feeling, with one line each on why.
   Consider the system stack and a popular UI face honestly alongside expressive options;
   pick by legibility, numerals, language coverage, and voice (`references/typography.md`).
3. **Test with real content:** the product's actual headings, a dense table row, numbers,
   the longest label. Reject faces that fail at the smallest size used.
4. **Set the scale:** a ratio that fits DENSITY (tighter, about 1.125 to 1.2, for dense apps;
   wider, 1.25 to 1.414, for marketing and editorial), roles named, weights limited to what the
   hierarchy needs.

## 5. Compose

- **Start with the most important screen,** not the component library. Its job decides the
  hierarchy: one focal point, a clear reading order, secondary information visibly quieter.
- **Build hierarchy with contrast** of size, weight, color, and space before adding containers,
  borders, or effects. Every card, border, and shadow should earn its place.
- **Group with space:** tighter inside a group than between groups (UI-15).
- **Align to a grid** and let edges line up across sections; misaligned edges read as careless.
- **Imagery and icons** in one style that comes from the direction: real product screens,
  real photography, or illustration with a consistent hand.
- **One signature,** sustained (§4 of `DESIGN.md`), or restraint executed rigorously.

## 6. Critique like a designer

After building the key screen, take screenshots (narrow and wide, light and dark) and look:
- **First glance:** what do you see first, second, third? Does that match the screen's job?
- **Squint test:** blur your eyes. Is there one focal point and a clear structure?
- **Grayscale test:** does the hierarchy hold without color?
- **Edge test:** do left edges and baselines line up? Are spacings from the scale?
- **Swap test:** with another product's logo, would anything still feel specific?
- **Adjective test:** does it feel like the three adjectives, and not like the three to avoid?

Fix what fails, then run the audits. Iterate on the key screen before rolling the language out
to the rest of the product.
