#!/usr/bin/env python3
"""GEN284: Quick inference test - validate trained model can load and make decisions."""

import sys
import os

# Ensure we're using the mutable_snapshot as the module path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from agi_core_continuous import AGICoreContinuous
    print("✓ Imported AGICoreContinuous")
except Exception as e:
    print(f"✗ Failed to import AGICoreContinuous: {e}")
    sys.exit(1)

try:
    # Initialize core with same dimensions as trained model
    core = AGICoreContinuous(feature_dim=30, use_features=True)
    print("✓ Core initialized")

    # Load trained model
    load_dir = "artifacts/agi_core_continuous_trained"
    if not os.path.exists(load_dir):
        print(f"✗ Load directory not found: {load_dir}")
        sys.exit(1)
    core.load(load_dir)
    print("✓ Model loaded successfully")

    # Create a simple workspace context
    workspace = "Files: inherited_notes.md, mutable_snapshot/agent_brain.py, artifacts/agi_core_continuous_trained/q_agent.pkl"
    journal = "Testing inference after environment validation."
    actions = ["list_files", "read_file"]

    # Get a decision
    tool, args, confidence = core.decide_action(workspace, journal, actions)
    print(f"✓ Decision made: tool={tool}, args={args}, confidence={confidence}")

    # Record a fake reward and learn
    reward = 0.5
    core.learn_from_outcome(reward, workspace + " updated", journal + " Continued.", actions + [tool])
    print("✓ Learning step completed")

    print("\n=== INFERENCE TEST OK ===")

except Exception as e:
    import traceback
    print(f"✗ Test failed with exception: {e}")
    traceback.print_exc()
    sys.exit(1)