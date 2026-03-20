#!/bin/bash
# Crescent AGI Disk Cleanup Script
# Keeps last 100 generations, deletes older ones

RUNS_DIR="/home/faris/crescent-agi/runs"
LOG_FILE="/home/faris/crescent-agi/crescent.log"
KEEP_GENS=100

# Delete old generations (keep last KEEP_GENS)
cd "$RUNS_DIR" || exit 1
ls -d gen-* 2>/dev/null | sort -V | head -n -$KEEP_GENS | xargs rm -rf 2>/dev/null

# Trim log file if over 50MB
if [ -f "$LOG_FILE" ]; then
    LOG_SIZE=$(stat -c%s "$LOG_FILE" 2>/dev/null || echo 0)
    if [ "$LOG_SIZE" -gt 52428800 ]; then
        tail -c 10485760 "$LOG_FILE" > "$LOG_FILE.tmp"
        mv "$LOG_FILE.tmp" "$LOG_FILE"
    fi
fi

# Clean up __pycache__ directories
find /home/faris/crescent-agi -name __pycache__ -type d -exec rm -rf {} + 2>/dev/null

# Report disk usage
echo "Disk usage after cleanup:"
df -h / | tail -1
