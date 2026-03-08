#!/bin/bash
# Crescent AGI — VM Provisioning Script
# Run this on the GCP VM to set up the environment.

set -e

echo "=================================="
echo "  Crescent AGI — VM Setup"
echo "=================================="

# Update system
echo "[1/6] Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Python and essential tools
echo "[2/6] Installing Python and tools..."
sudo apt-get install -y python3 python3-pip python3-venv git tmux curl wget

# Create project directory
echo "[3/6] Setting up project directory..."
PROJECT_DIR="$HOME/crescent-agi"
if [ ! -d "$PROJECT_DIR" ]; then
    mkdir -p "$PROJECT_DIR"
fi

# Create Python virtual environment
echo "[4/6] Creating Python virtual environment..."
cd "$PROJECT_DIR"
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "[5/6] Installing Python dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    pip install openai pyyaml
fi

# Set up keep-alive cron job
echo "[6/6] Setting up keep-alive..."
chmod +x keep_alive.sh 2>/dev/null || true
# Add cron job to run keep_alive every 5 minutes
(crontab -l 2>/dev/null; echo "*/5 * * * * $PROJECT_DIR/keep_alive.sh >> /tmp/crescent-keepalive.log 2>&1") | sort -u | crontab -

# Install systemd service
if [ -f "crescent.service" ]; then
    sudo cp crescent.service /etc/systemd/system/crescent.service
    sudo systemctl daemon-reload
    echo "Systemd service installed. Enable with: sudo systemctl enable crescent"
    echo "Start with: sudo systemctl start crescent"
fi

echo ""
echo "=================================="
echo "  Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "  1. Set your Gemini API key:"
echo "     export GEMINI_API_KEY='your-key-here'"
echo ""
echo "  2. (Optional) Set GitHub token for publishing:"
echo "     export GITHUB_TOKEN='your-token-here'"
echo ""
echo "  3. Run Crescent:"
echo "     cd $PROJECT_DIR && source venv/bin/activate && python main.py"
echo ""
echo "  4. Or enable as a service:"
echo "     sudo systemctl enable crescent && sudo systemctl start crescent"
echo ""
