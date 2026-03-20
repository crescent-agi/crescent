#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-/home/faris/crescent-agi}"
OWNER="${2:-crescent-agi}"
REPO="${3:-crescent}"

cd "$PROJECT_DIR"
set -a
. ./.env
set +a

API_URL="https://api.github.com/repos/$OWNER/$REPO/pages"
BODY='{"source":{"branch":"main","path":"/docs"}}'

STATUS="$(curl -s -o /tmp/crescent-pages.json -w "%{http_code}" -X POST \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "$API_URL" \
  -d "$BODY")"

if [ "$STATUS" = "201" ] || [ "$STATUS" = "204" ] || [ "$STATUS" = "409" ] || [ "$STATUS" = "422" ]; then
  echo "pages_status=$STATUS"
  exit 0
fi

echo "pages_status=$STATUS" >&2
cat /tmp/crescent-pages.json >&2
exit 1
