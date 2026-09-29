#!/usr/bin/env bash
# Build founder-os.zip for claude.ai Settings → Skills → Upload skill.
# Claude.ai cannot install skills via git/SSH inside the chat — use this ZIP instead.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_NAME="founder-os"
OUT="${1:-$ROOT/founder-os-claude-ai.zip}"
TMP="$(mktemp -d)"

cleanup() { rm -rf "$TMP"; }
trap cleanup EXIT

mkdir -p "$TMP/$SKILL_NAME"

rsync -a \
  --exclude '.git' \
  --exclude '.DS_Store' \
  --exclude '*.zip' \
  --exclude 'node_modules' \
  "$ROOT/" "$TMP/$SKILL_NAME/"

rm -f "$OUT"
(cd "$TMP" && zip -r "$OUT" "$SKILL_NAME" >/dev/null)

echo "Created: $OUT"
echo "Zip layout (must show ${SKILL_NAME}/SKILL.md):"
unzip -l "$OUT" | head -20
