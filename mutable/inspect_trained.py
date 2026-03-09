#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous
import json
import os

print("Loading trained AGI Core Continuous...")
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
if os.path.exists("artifacts/agi_core_continuous_trained"):
    core.load("artifacts/agi_core_continuous_trained")
    print("Model loaded.")
else:
    print("No trained model found.")
    sys.exit(1)

# Sample workspace
workspace = "Files: agent_brain.py, cognitive_architecture.py, test.py, notes.md"
journal = "Made progress on AGI core."
actions = [{"tool": "read_file"}, {"tool": "write_file"}, {"tool": "execute_code"}]

# Compute state vector
state_vec = core.compute_state_vector(workspace, journal, actions)
print(f"State vector length: {len(state_vec)}")
print(f"First 10 values: {state_vec[:10]}")

# Get Q-values via neural network (if available)
if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    print("\nQ-values for each tool:")
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue", "comment_issue",
                  "create_issue", "close_issue"]
    for i, (tool, q) in enumerate(zip(tool_names, q_vals)):
        print(f"{tool:20} {q:8.3f}")
    best_idx = max(range(len(q_vals)), key=lambda i: q_vals[i])
    print(f"\nBest action: {tool_names[best_idx]} (Q = {q_vals[best_idx]:.3f})")

# Decide action
tool, args, conf = core.decide_action(workspace, journal, actions)
print(f"\nDecided action: {tool} with args {args} (confidence {conf})")