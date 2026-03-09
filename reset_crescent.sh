#!/usr/bin/env bash
set -euo pipefail

APP_DIR="${1:-/home/faris/crescent-agi}"

cd "$APP_DIR"

sudo systemctl stop crescent.service || true

rm -rf runs docs journals
mkdir -p runs docs journals genome

rm -f genome/current_genome.json
rm -f genome/lineage.jsonl
rm -f genome/next_inherited_notes.md

PYTHON_BIN="python3"
if [[ -x ".venv/bin/python" ]]; then
  PYTHON_BIN=".venv/bin/python"
fi

"$PYTHON_BIN" - <<'PY'
import yaml
from core.publisher import Publisher

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

Publisher(config, ".").publish(1)
print("published reset state")
PY

sudo systemctl start crescent.service
sleep 10

echo "STATUS:$(sudo systemctl is-active crescent.service)"
echo "RUN_DIRS:"
find runs -maxdepth 1 -mindepth 1 -type d | sort
echo "DOC_FILES:"
find docs -maxdepth 1 -type f | sort
echo "GENOME_FILES:"
find genome -maxdepth 1 -type f | sort
