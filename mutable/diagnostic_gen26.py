#!/usr/bin/env python3
"""
Diagnose deterministic policy collapse for generation 26.
"""
import sys
import os
# Mock core.llm_client for imports
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

from agi_core_continuous import AGICoreContinuous, TOOL_NAMES
import numpy as np

def load_model():
    """Load trained gen26 model."""
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    save_dir = "artifacts/agi_core_continuous_trained_gen26"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded model from {save_dir}")
    else:
        print("No trained model found")
        sys.exit(1)
    return core

def compute_q_distribution(core, state_vector):
    """Return Q-values for each action."""
    if core.q_agent:
        q_vals = core.q_agent.nn.predict(state_vector)
        return q_vals
    return None

def simulate_deterministic(core, steps=100):
    """Simulate with epsilon=0 and track actions."""
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    # Dummy workspace
    workspace = "Files: inherited_notes.md, agi_core.py"
    journal = ""
    actions = []
    action_counts = {}
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace, journal, actions
        )
        action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
        actions.append({"tool": tool_name})
    core.q_agent.epsilon = original_epsilon
    return action_counts

def main():
    core = load_model()
    print(f"Q-agent epsilon: {core.q_agent.epsilon}")
    # Compute Q-values for a sample state
    workspace = "Files: inherited_notes.md, agi_core.py, cognitive_architecture.py"
    journal = ""
    actions = []
    state_vec = core.compute_state_vector(workspace, journal, actions)
    q_vals = compute_q_distribution(core, state_vec)
    if q_vals is not None:
        print("\nQ-values for sample state:")
        for i, tool in enumerate(TOOL_NAMES):
            print(f"  {tool}: {q_vals[i]:.3f}")
        best_idx = np.argmax(q_vals)
        print(f"Best action: {TOOL_NAMES[best_idx]}")
    # Simulate deterministic policy
    print("\n--- Simulating deterministic policy (epsilon=0) for 100 steps ---")
    counts = simulate_deterministic(core, steps=100)
    total = sum(counts.values())
    print("Action counts:")
    for tool, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total) * 100
        print(f"  {tool}: {count} ({pct:.1f}%)")
    # Check if collapsed to a single productive tool
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    prod_counts = {t: counts.get(t, 0) for t in productive}
    total_prod = sum(prod_counts.values())
    if total_prod > 0:
        print("\nProductive distribution:")
        for tool in productive:
            pct = (prod_counts[tool] / total_prod) * 100
            print(f"  {tool}: {prod_counts[tool]} ({pct:.1f}%)")
    # Check if any non-productive actions present
    non_prod = [t for t in counts if t not in productive and t != "declare_death"]
    if non_prod:
        print(f"Non-productive actions present: {non_prod}")
    else:
        print("No non-productive actions.")

if __name__ == "__main__":
    main()