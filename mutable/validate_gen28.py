#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double
from agi_core_continuous import AGICoreContinuous
import os
import math

# Use the reward function from generation 28 (but not needed for validation)
from new_reward_gen28 import compute_reward_gen28 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_tool_counts = {}
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.episode_tool_counts.clear()
        # global counts persist

self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {"test": "# test"}
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        return "Files: test"
    def tool_result(self, tool_name, tool_args):
        return {"success": True}

def validate(core, steps=500):
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    counts = {}
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    non_productive = ["list_files", "write_note", "list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]
    for step in range(steps):
        tool_name, tool_args, _ = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        counts[tool_name] = counts.get(tool_name, 0) + 1
        workspace.actions.append({"tool": tool_name})
    core.q_agent.epsilon = original_epsilon
    total = sum(counts.values())
    print("Deterministic policy action counts:")
    for tool, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total) * 100
        print(f"  {tool}: {count} ({pct:.1f}%)")
    prod_counts = {t: counts.get(t,0) for t in productive}
    total_prod = sum(prod_counts.values())
    if total_prod > 0:
        print("\nProductive distribution:")
        for tool in productive:
            pct = (prod_counts[tool] / total_prod) * 100
            print(f"  {tool}: {prod_counts[tool]} ({pct:.1f}%)")
    nonprod_counts = {t: counts.get(t,0) for t in non_productive}
    total_nonprod = sum(nonprod_counts.values())
    print(f"Non-productive actions: {total_nonprod}")
    if total_nonprod > 0:
        for tool in non_productive:
            if counts.get(tool,0) > 0:
                print(f"  {tool}: {counts[tool]}")
    # Q-values for a sample state
    state = core.compute_state_vector("Files: test", "", [])
    qvals = core.q_agent.nn.predict(state)
    print("\nQ-values for sample state:")
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    for i, name in enumerate(tool_names):
        print(f"  {name}: {qvals[i]:.3f}")
    best_idx = max(range(len(qvals)), key=lambda i: qvals[i])
    print(f"Best action (Q): {tool_names[best_idx]} (idx {best_idx})")
    # Compute softmax probabilities
    exp_q = [math.exp(q) for q in qvals]
    sum_exp = sum(exp_q)
    probs = [e / sum_exp for e in exp_q]
    entropy = -sum(p * math.log(p + 1e-10) for p in probs)
    print(f"Entropy of Q distribution: {entropy:.3f}")
    # Death Q-value rank
    death_idx = 6
    death_q = qvals[death_idx]
    sorted_q = sorted(enumerate(qvals), key=lambda x: x[1], reverse=True)
    rank = [idx for idx, q in sorted_q].index(death_idx) + 1
    print(f"Death Q-value: {death_q:.3f} (rank {rank}/{len(qvals)})")
    # Productive Q-values only
    productive_indices = [i for i, name in enumerate(tool_names) if name in productive]
    prod_q = [qvals[i] for i in productive_indices]
    avg_prod_q = sum(prod_q) / len(prod_q)
    print(f"Average Q-value of productive tools: {avg_prod_q:.3f}")
    print(f"Q-value spread (max-min): {max(prod_q)-min(prod_q):.3f}")
    # Check if any productive tool Q-value is significantly lower than others
    # Determine if collapse is due to Q-value differences
    # Compute action selection probabilities under softmax
    prod_probs = [probs[i] for i in productive_indices]
    print("Softmax probabilities for productive tools:")
    for i, idx in enumerate(productive_indices):
        print(f"  {tool_names[idx]}: {prod_probs[i]:.4f}")
    # Compute proportion of each productive tool in deterministic policy
    if total_prod > 0:
        print("\nDeterministic distribution vs Q-values:")
        for tool in productive:
            idx = tool_names.index(tool)
            pct = (prod_counts[tool] / total_prod) * 100
            print(f"  {tool}: {pct:.1f}% (Q {qvals[idx]:.3f})")

def main():
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    save_dir = "artifacts/agi_core_continuous_trained_gen28"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded model from {save_dir}")
    else:
        print("Model not found")
        return
    validate(core, steps=200)

if __name__ == "__main__":
    main()