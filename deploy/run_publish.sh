#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:-/home/faris/crescent-agi}"
GENERATION="${2:-9999}"

cd "$PROJECT_DIR"
set -a
. ./.env
set +a
source venv/bin/activate

python -c "from pathlib import Path; import yaml; from core.publisher import Publisher; base = Path('$PROJECT_DIR'); config = yaml.safe_load((base / 'config.yaml').read_text(encoding='utf-8')); Publisher(config, str(base)).publish($GENERATION)"
