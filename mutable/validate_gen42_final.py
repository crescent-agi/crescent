#!/usr/bin/env python3
import sys, os, random
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

import patch_weight_clipping
import patch_qreg_v3

from agi_core_continuous import AGICoreContinuous
from new_reward_gen42 import compute_reward_gen42 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_total = 0
        self.episode_tool_counts = {}
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0

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

def validate():
    core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                             learning_rate=0.001, exploration_rate=0.5,
                             epsilon_decay=0.98, epsilon_min=0.1, use_features=True)
    save_dir = "artifacts/agi_core_continuous_trained_gen42_curiosity"
    if os.path.exists(save_dir):
        core.load(save_dir)
        print(f"Loaded model from {save_dir}")
    else:
        print("Model not found")
        return
    original_epsilon = core.q_agent.epsilon
    core.q_agent.epsilon = 0.0
    workspace = SimWorkspace()
    self.reset()
    counts = {}
    productive = ["write_file", "execute_code", "modify_self", "read_file"]
    total_reward = 0.0
    for step in range(500):
        tool_name, tool_args, _ = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        total_reward += reward
        counts[tool_name] = counts.get(tool_name, 0) + 1
        workspace.actions.append({"tool": tool_name})
    core.q_agent.epsilon = original_epsilon
    total = sum(counts.values())
    avg_reward = total_reward / total if total > 0 else 0
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
            if 15 <= pct <= 35:
                print("    -> within target")
            else:
                print("    -> OUT OF RANGE")
    print(f"\nAverage reward per step: {avg_reward:.3f}")
    # Q-values
    state = core.compute_state_vector("Files: test", "", [])
    qvals = core.q_agent.nn.predict(state)
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    print("\nQ-values for sample state:")
    for i, name in enumerate(tool_names):
        print(f"  {name}: {qvals[i]:.3f}")
    best_idx = max(range(len(qvals)), key=lambda i: qvals[i])
    print(f"Best action (Q): {tool_names[best_idx]}")
    death_q = qvals[6]
    productive_indices = [0,1,3,5]
    prod_qs = [qvals[i] for i in productive_indices]
    if death_q < min(prod_qs):
        print(f"Death Q-value ({death_q:.3f}) is lowest (good).")
    else:
        print(f"Death Q-value ({death_q:.3f}) is NOT lowest (bad).")

if __name__ == "__main__":
    validate()