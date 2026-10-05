#!/usr/bin/env bash
# anti-slop-web installer (macOS, Linux, Git Bash on Windows).
# Copies skills/ and agents/ into your Claude Code config directory (~/.claude by default).
# Override the target with: CLAUDE_HOME=/path/to/.claude ./install.sh
# Project-level install:     CLAUDE_HOME=./.claude ./install.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"
SKILLS_DST="$CLAUDE_HOME/skills"
AGENTS_DST="$CLAUDE_HOME/agents"

echo "anti-slop-web -> $CLAUDE_HOME"
mkdir -p "$SKILLS_DST" "$AGENTS_DST"

for dir in "$SCRIPT_DIR"/skills/*/; do
  name="$(basename "$dir")"
  if [ -e "$SKILLS_DST/$name" ]; then echo "  replace skill: $name"; else echo "  install skill: $name"; fi
  rm -rf "${SKILLS_DST:?}/$name"
  cp -R "$dir" "$SKILLS_DST/$name"
done

for file in "$SCRIPT_DIR"/agents/*.md; do
  name="$(basename "$file")"
  if [ -e "$AGENTS_DST/$name" ]; then echo "  replace agent: $name"; else echo "  install agent: $name"; fi
  cp "$file" "$AGENTS_DST/$name"
done

echo
echo "Done. Skills are available in new sessions; the agent is dispatchable after restarting Claude Code."
echo "Optional: add docs/claude-md-snippet.md to your project's CLAUDE.md."
