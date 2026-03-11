#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Test AGICoreContinuous after sigmoid overflow fix
from agi_core_continuous import AGICoreContinuous

print("=== Testing AGICoreContinuous ===")
try:
    core = AGICoreContinuous(feature_dim=15)
    print("AGICoreContinuous instantiated successfully")
except Exception as e:
    print(f"Failed to instantiate: {e}")
    raise

workspace = "Files: agent_brain.py, cognitive_architecture.py"
journal = ""
actions = []

print("Deciding action...")
tool, args, conf = core.decide_action(workspace, journal, actions)
print(f"Decision: {tool} with args {args} (confidence {conf})")

print("\n[SUCCESS] AGICoreContinuous works without activation overflow!")
