#!/usr/bin/env python3
"""
Helper script to inspect Q-values of a trained AGI core.
"""
import sys
sys.path.insert(0, '.')
# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core_continuous import AGICoreContinuous
import os
import numpy as np

def inspect_model(model_dir, num_states=5):
    """Load model and print Q-values for random states."""
    print(f"Loading model from {model_dir}")
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    if os.path.exists(model_dir):
        core.load(model_dir)
        print("Model loaded.")
    else:
        print("Model directory does not exist.")
        return
    
    q_agent = core.q_agent
    if q_agent is None:
        print("No Q agent found.")
        return
    
    # Generate random state vectors (simulating workspace summaries)
    for i in range(num_states):
        # Random feature vector (normalized)
        state_vector = np.random.randn(30)
        # Normalize roughly
        state_vector = (state_vector - np.mean(state_vector)) / (np.std(state_vector) + 1e-8)
        q_values = q_agent.nn.predict(state_vector)
        print(f"\nState {i+1}:")
        # Map indices to tool names
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        for idx, (tool, q) in enumerate(zip(tool_names, q_values)):
            print(f"  {idx:2d} {tool:20s}: {q:8.3f}")
        # Highlight max Q
        max_idx = np.argmax(q_values)
        max_q = q_values[max_idx]
        print(f"  -> Greedy action: {tool_names[max_idx]} (Q={max_q:.3f})")
        # Also show Q-values for productive tools only
        productive = ["write_file", "execute_code", "modify_self", "read_file"]
        productive_idx = [tool_names.index(t) for t in productive]
        print("  Productive tool Q-values:")
        for idx in productive_idx:
            print(f"    {tool_names[idx]:20s}: {q_values[idx]:8.3f}")
        # Compute softmax for productive tools
        prod_q = q_values[productive_idx]
        exp_q = np.exp(prod_q - np.max(prod_q))
        softmax = exp_q / exp_q.sum()
        print("  Softmax probabilities:")
        for idx, prob in zip(productive_idx, softmax):
            print(f"    {tool_names[idx]:20s}: {prob:.3f}")

if __name__ == "__main__":
    # Try latest model
    model_dir = "artifacts/agi_core_continuous_trained_gen22_v2"
    inspect_model(model_dir)
    # Also inspect gen21 for comparison
    model_dir2 = "artifacts/agi_core_continuous_trained_gen21"
    if os.path.exists(model_dir2):
        inspect_model(model_dir2)