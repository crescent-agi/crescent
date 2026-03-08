#!/bin/bash
# Crescent AGI — Keep Alive Script
# Prevents GCP from auto-stopping the free tier VM.
# Runs via cron every 5 minutes.

# Touch a file to show activity
touch /tmp/crescent-alive

# Light CPU activity to prevent idle shutdown
uptime > /dev/null 2>&1

# Log heartbeat
echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') — heartbeat" >> /tmp/crescent-keepalive.log

# Keep log file from growing too large (keep last 1000 lines)
if [ -f /tmp/crescent-keepalive.log ]; then
    tail -1000 /tmp/crescent-keepalive.log > /tmp/crescent-keepalive.log.tmp
    mv /tmp/crescent-keepalive.log.tmp /tmp/crescent-keepalive.log
fi

# Check if crescent is running, restart if not
if systemctl is-active --quiet crescent 2>/dev/null; then
    echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') — crescent service running" >> /tmp/crescent-keepalive.log
else
    echo "$(date -u '+%Y-%m-%d %H:%M:%S UTC') — crescent service not running, attempting restart" >> /tmp/crescent-keepalive.log
    sudo systemctl start crescent 2>/dev/null || true
fi
