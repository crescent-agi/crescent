#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-/home/faris/crescent-agi}"
REPO_API_URL="${2:-https://api.github.com/repos/crescent-agi/crescent}"

cd "$PROJECT_DIR"
set -a
. ./.env
set +a

DEEPSEEK_STATUS="$(curl -s -o /tmp/crescent-deepseek.json -w "%{http_code}" -H "Authorization: Bearer $DEEPSEEK_API_KEY" https://api.deepseek.com/models)"
echo "deepseek_status=$DEEPSEEK_STATUS"

GITHUB_USER_STATUS="$(curl -s -o /tmp/crescent-github-user.json -w "%{http_code}" -H "Authorization: Bearer $GITHUB_TOKEN" -H "Accept: application/vnd.github+json" https://api.github.com/user)"
echo "github_user_status=$GITHUB_USER_STATUS"

GITHUB_REPO_STATUS="$(curl -s -o /tmp/crescent-github-repo.json -w "%{http_code}" -H "Authorization: Bearer $GITHUB_TOKEN" -H "Accept: application/vnd.github+json" "$REPO_API_URL")"
echo "github_repo_status=$GITHUB_REPO_STATUS"
