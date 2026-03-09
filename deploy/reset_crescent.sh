#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-/home/faris/crescent-agi}"

cd "$PROJECT_DIR"

sudo systemctl stop crescent || true

rm -rf runs docs journals
mkdir -p runs docs journals genome

rm -f genome/current_genome.json genome/lineage.jsonl genome/next_inherited_notes.md crescent.log

set -a
. ./.env
set +a
source venv/bin/activate

python -c "from pathlib import Path; import yaml; from core.publisher import Publisher; base = Path('$PROJECT_DIR'); config = yaml.safe_load((base / 'config.yaml').read_text(encoding='utf-8')); Publisher(config, str(base)).publish(1)"

sudo systemctl start crescent
sudo systemctl --no-pager --full status crescent || true
