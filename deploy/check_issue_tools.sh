#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-/home/faris/crescent-agi}"

cd "$PROJECT_DIR"
set -a
. ./.env
set +a
source venv/bin/activate

python - <<'PY'
import yaml
from core.github_issues import GitHubIssues

with open("config.yaml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

gh = GitHubIssues(cfg)
print(gh.list_open_issues(label="human", limit=5))
PY
