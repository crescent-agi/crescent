#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-/home/faris/crescent-agi}"
REPO_URL="${2:-https://github.com/crescent-agi/crescent.git}"
BRANCH="${3:-main}"

cd "$PROJECT_DIR"

TOKEN="$(grep '^GITHUB_TOKEN=' .env | cut -d= -f2-)"
if [ -z "$TOKEN" ]; then
  echo "GITHUB_TOKEN missing in $PROJECT_DIR/.env" >&2
  exit 1
fi

git remote set-url origin "https://x-access-token:${TOKEN}@${REPO_URL#https://}"
git push origin "$BRANCH"
