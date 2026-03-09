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

print("Loading trained AGI Core Continuous...")
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
try:
    core.load('artifacts/agi_core_continuous_trained')
    print("Loaded.")
except Exception as e:
    print(f"Load failed: {e}")
    core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
    print("Using fresh core.")

print(f"Feature dim: {core.feature_dim}")
print(f"Epsilon: {core.q_agent.epsilon if core.q_agent else 'No Q agent'}")
print(f"Episode count: {core.episode_count if hasattr(core, 'episode_count') else 'N/A'}")

# Create dummy state vector (30 zeros)
state_vec = [0.0] * 30
if core.q_agent:
    q_vals = core.q_agent.nn.predict(state_vec)
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    print("\nQ-values for each tool (zero state):")
    for i, name in enumerate(tool_names):
        print(f"  {name:20} {q_vals[i]:.3f}")
    # Find top 3
    sorted_idx = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True)
    print("\nTop 3 actions:")
    for rank, idx in enumerate(sorted_idx[:3]):
        print(f"  {rank+1}. {tool_names[idx]:20} {q_vals[idx]:.3f}")
else:
    print("No Q agent.")

# Test decide_action with minimal inputs
workspace = {"files": []}
journal = "Test journal"
actions = []
print("\nTesting decide_action...")
try:
    tool, args, conf = core.decide_action(workspace, journal, actions)
    print(f"  Suggested: {tool} with args {args} (confidence {conf})")
except Exception as e:
    print(f"  Error: {e}")