# CLAUDE.md / AGENTS.md snippet

Paste this block into a project's `CLAUDE.md` (Claude Code), `AGENTS.md` (Codex and others), or
the equivalent file your agent reads at session start. Adjust paths if you vendored the kit
somewhere other than `.agents/anti-slop-web/` or installed it as a Claude Code plugin.

```md
## Web UI work
For any task that designs, builds, or reviews web UI, use the anti-slop-web skill
(Claude Code: the `anti-slop-web` skill; other agents: read
`.agents/anti-slop-web/skills/anti-slop-web/SKILL.md`).
- Read `DESIGN.md` at the project root first; it is the source of truth for direction.
  Update it rather than overwriting it.
- Load specialist skills only when relevant (a11y, responsive, copy, code) and reference files
  only for the current task.
- Never invent testimonials, logos, metrics, or claims; use labeled placeholders.
- Finish UI work with the delivery gate in
  `.agents/anti-slop-web/skills/anti-slop-web/audits/delivery-gate.md`.
```
