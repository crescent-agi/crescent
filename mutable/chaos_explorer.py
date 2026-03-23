import os
import json
import pickle
import sys
from pathlib import Path
from datetime import datetime

def log(msg):
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(f"[{timestamp}] {msg}")

def find_manifesto(path):
    if 'chaos_manifesto.txt' in os.listdir(path):
        return os.path.join(path, 'chaos_manifesto.txt')
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            result = find_manifesto(full_path)
            if result:
                return result
    return None

def explore_artifacts():
    base = '/home/faris/crescent-agi/runs/gen-0119/artifacts'
    log("=== Exploring artifacts ===")
    log("=== Summary ===")
    log(f"Total files: {len([f for f in os.listdir(base) if os.path.isfile(os.path.join(base, f))])}")
    log("=== Found chaos manifesto? ===")
    manifesto_path = find_manifesto(base)
    if manifesto_path:
        log(f"Found manifesto at: {manifesto_path}")
        with open(manifesto_path) as f:
            print(f.read())
    else:
        log("Chaos manifesto not found")

explore_artifacts()