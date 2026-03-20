#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-/home/faris/crescent-agi}"
TITLE="${2:-hello goblin}"
BODY="${3:-if you can read this, say something cheeky and carry on.}"
LABEL="${4:-human}"

cd "$PROJECT_DIR"
set -a
. ./.env
set +a

curl -s -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/crescent-agi/crescent/issues \
  -d "{\"title\":\"$TITLE\",\"body\":\"$BODY\",\"labels\":[\"$LABEL\"]}"
