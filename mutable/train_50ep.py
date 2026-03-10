#!/usr/bin/env python3
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

from train_continuous import run_training
import time

if __name__ == "__main__":
    start_time = time.time()
    core, stats = run_training(episodes=50, steps_per_episode=10, feature_dim=30, hidden_size=32)
    elapsed = time.time() - start_time
    print(f"\nTotal training time: {elapsed:.1f} seconds")
    print(f"Declare death count: {stats['declare_death_count']}")
    print(f"Write file count: {stats['write_file_count']}")
    print(f"Execute code count: {stats['execute_code_count']}")
    # Inspect Q-values
    if core.q_agent:
        print(f"\nEpsilon after training: {core.q_agent.epsilon:.4f}")
        # Sample state
        from feature_extractor import FeatureExtractor
        extractor = FeatureExtractor(history_size=10)
        sample_features = extractor.extract("Files: agi_core.py, agent_brain.py", "", [])
        q_vals = core.q_agent.nn.predict(sample_features)
        # Map action indices to tool names
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                     "modify_self", "declare_death", "list_issues", "read_issue", "comment_issue",
                     "create_issue", "close_issue"]
        print("Q-values for sample state:")
        for i, q in enumerate(q_vals):
            print(f"  {tool_names[i]:15s} {q:6.3f}")
        best_idx = max(range(len(q_vals)), key=lambda i: q_vals[i])
        print(f"Best action: {tool_names[best_idx]} ({q_vals[best_idx]:.3f})")