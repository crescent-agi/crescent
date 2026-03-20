#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path
from datetime import datetime

# Add your generation-specific anomaly detection logic here

def analyze_generation(generation_dir):
    # Extract generation number from directory name
    gen_match = re.search(r'gen(\d+)$', generation_dir.name)
    if not gen_match:
        return None
    generation = int(gen_match.group(1))
    
    # Read key files
    stats_path = generation_dir / 'training_stats.json'
    if not stats_path.exists():
        return {"warning": "missing training_stats.json"}
    
    try:
        with open(stats_path) as f:
            stats = json.load(f)
    except json.JSONDecodeError:
        return {"error": "invalid JSON in training_stats.json"}
    
    # Check for anomalies in rewards/episodes
    reward_trend = stats.get('reward_trend', [])  # hypothetical field
    if any(r < 0 for r in reward_trend[:-3]):  # sudden drops
        return {"anomaly": "reward_collapse", "ep_range": "last 3 episodes"}
    
    # Example memory usage check (simplified)
    memory_size = get_memory_size(generation_dir)  # implement size check
    if memory_size > 500e6:  # 500MB threshold
        return {"anomaly": "memory_spike", "size_mb": memory_size}
    
    return None

def scan_artifacts():
    root = Path('.')
    artifact_dirs = [p for p in root.rglob('artifacts/*/cognitive') if p.is_dir()]
    print(f"===" + """{len(artifact_dirs)} directories found""" + "===" + "")
    
    anomalies = []
    for dir in artifact_dirs:
        result = analyze_generation(dir)
        if result:
            anomalies.append((dir, result))
    
    # Log major anomalies
    if anomalies:
        with open("anomaly_log.json", "w") as f:
            json.dump({"timestamp": datetime.now().isoformat(), "findings": anomalies}, f)
        write_note("[journal] Anomaly log written to anomaly_log.json")
    else:
        write_note("[journal] No significant anomalies detected")

if __name__ == "__main__":
    scan_artifacts()