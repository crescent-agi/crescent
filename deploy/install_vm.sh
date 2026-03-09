#!/bin/bash
set -euo pipefail

PROJECT_DIR="${1:?project dir required}"
CURRENT_USER="$(whoami)"

sudo apt-get update -y
sudo apt-get install -y python3 python3-pip python3-venv git

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

rm -f crescent-deploy.zip crescent-deploy.tar setup_vm.sh keep_alive.sh crescent.service

if [ ! -d venv ]; then
  python3 -m venv venv
fi

source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created $PROJECT_DIR/.env from .env.example. Fill in DEEPSEEK_API_KEY before starting the service."
fi

sed \
  -e "s|__SERVICE_USER__|$CURRENT_USER|g" \
  -e "s|__PROJECT_DIR__|$PROJECT_DIR|g" \
  "$PROJECT_DIR/deploy/crescent.service" | sudo tee /etc/systemd/system/crescent.service > /dev/null

sudo systemctl daemon-reload
sudo systemctl enable crescent

if grep -q "^DEEPSEEK_API_KEY=your-deepseek-api-key-here" .env; then
  echo "Skipping service start until DEEPSEEK_API_KEY is set in $PROJECT_DIR/.env"
else
  sudo systemctl restart crescent
  sudo systemctl --no-pager --full status crescent || true
fi
