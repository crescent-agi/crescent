#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

from agi_core import AGICore

core = AGICore(state_size=50, hidden_size=16, learning_rate=0.01, use_features=True)
print("AGI Core with features initialized")
print("Feature extractor available:", core.feature_extractor is not None)

# Simulate a workspace
workspace = "Files: agi_core.py, cognitive_architecture.py, test.py"
journal = ""
actions = []
tool, args, conf = core.decide_action(workspace, journal, actions)
print(f"Decision: {tool} with args {args} (confidence {conf})")
print("Test passed")