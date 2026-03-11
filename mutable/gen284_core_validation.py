#!/usr/bin/env python3
"""GEN284: Core validation - test all critical components."""

import sys
import os

print("GEN284: Running core validation...")

# Test 1: AgentBrain
try:
    from agent_brain import AgentBrain
    brain = AgentBrain()
    action = brain.choose_action([0.5, -0.3, 0.7])
    print(f"✓ AgentBrain: choose_action returned {action}")
except Exception as e:
    print(f"✗ AgentBrain test failed: {e}")
    sys.exit(1)

# Test 2: AGICoreContinuous
try:
    from agi_core_continuous import AGICoreContinuous
    core = AGICoreContinuous(feature_dim=30, use_features=False)
    print("✓ AGICoreContinuous: initialized")

    # Decision
    workspace = "Files: test.py, model.pkl"
    journal = "Initial test."
    actions = ["list_files"]
    tool, args, conf = core.decide_action(workspace, journal, actions)
    print(f"✓ AGICoreContinuous: decision = {tool} (conf={conf})")

    # Learning
    core.learn_from_outcome(0.5, workspace + " updated", journal + " Learned.", actions + [tool])
    print("✓ AGICoreContinuous: learning step ok")
except Exception as e:
    print(f"✗ AGICoreContinuous test failed: {e}")
    import traceback; traceback.print_exc()
    sys.exit(1)

# Test 3: SafeActivation (already validated but include for completeness)
try:
    from safe_activation_fixed import SafeActivation
    sa = SafeActivation()
    assert sa.sigmoid(0) == 0.5
    assert sa.tanh(100) == 1.0
    assert sa.tanh(-100) == -1.0
    print("✓ SafeActivation: stable")
except Exception as e:
    print(f"✗ SafeActivation test failed: {e}")
    sys.exit(1)

# Test 4: Check that artifacts exist
required_artifacts = [
    "artifacts/agi_core_continuous_trained/q_agent.pkl",
    "artifacts/agi_core_continuous_trained/world_model.pkl"
]
for path in required_artifacts:
    if not os.path.exists(path):
        print(f"✗ Missing artifact: {path}")
        sys.exit(1)
    else:
        print(f"✓ Found artifact: {path}")

print("\n=== ALL VALIDATIONS PASSED ===")
print("GEN284: System ready for experimental work.")
