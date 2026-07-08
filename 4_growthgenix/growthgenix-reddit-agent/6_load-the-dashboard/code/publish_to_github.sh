#!/usr/bin/env bash
# publish_to_github.sh — push the fresh dashboard to GitHub so Netlify auto-deploys.
# Works around the mounted-folder git limitation by doing all git work in a temp dir.
# Reads GITHUB_TOKEN and GITHUB_REPO_URL from the project .env.local (gitignored).
set -euo pipefail

ROOM_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PROJECT_ROOT="$(cd "$ROOM_DIR/.." && pwd)"
ENV_FILE="$PROJECT_ROOT/.env.local"
SRC="$ROOM_DIR/output/index.html"

[ -f "$ENV_FILE" ] || { echo "No .env.local at $ENV_FILE"; exit 1; }
set -a; source "$ENV_FILE"; set +a
: "${GITHUB_TOKEN:?GITHUB_TOKEN missing}"; : "${GITHUB_REPO_URL:?GITHUB_REPO_URL missing}"
[ -f "$SRC" ] || { echo "No dashboard at $SRC — run write_dashboard.py first"; exit 1; }

AUTH_URL="$(echo "$GITHUB_REPO_URL" | sed -E "s#https://#https://x-access-token:${GITHUB_TOKEN}@#")"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

git clone --depth 1 "$AUTH_URL" "$WORK/repo" >/dev/null 2>&1
cd "$WORK/repo"
cp "$SRC" index.html
TRK="$ROOM_DIR/output/tracker.html"
[ -f "$TRK" ] && cp "$TRK" tracker.html  # Mission Control rides along at /tracker.html
git add -A
git -c user.email="reddit-agent@growthgenix.local" -c user.name="GrowthGenix Reddit Agent" \
    commit -q -m "Dashboard update $(date +%Y-%m-%d)" 2>/dev/null || { echo "No change to publish"; exit 0; }
git push -q origin HEAD >/dev/null 2>&1
echo "Published to GitHub"
