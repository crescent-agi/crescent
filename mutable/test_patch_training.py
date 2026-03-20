#!/usr/bin/env python3
"""
Quick test of patch_boltzmann_var200 and training script with 2 episodes.
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

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply patches
import patch_boltzmann_var200
print('Applied patch')

from agi_core_continuous import AGICoreContinuous
from new_reward_gen50 import compute_reward_gen50 as compute_reward
from new_reward_gen50 import compute_terminal_bonus_gen50

class DummySelf:
    def __init__(self):
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
        self.last_tool = None
    def reset(self):
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
        self.last_tool = None

self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {}
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        return "Files: none"
    def tool_result(self, tool_name, tool_args):
        return {"success": True}
    def update_state(self, tool_name, tool_args):
        pass

# Create core with small network
core = AGICoreContinuous(feature_dim=10, hidden_size=8, learning_rate=0.001, exploration_rate=0.0, epsilon_decay=1.0, epsilon_min=0.0)
core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
print(f"Initial temperature: {core.q_agent.temperature}")

workspace = SimWorkspace()
episodes = 2
steps_per_episode = 5
for episode in range(episodes):
    self.reset()
    for step in range(steps_per_episode):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        if step == steps_per_episode - 1:
            terminal_bonus = compute_terminal_bonus_gen50(self)
            if terminal_bonus > 0:
                print(f"Terminal bonus awarded: {terminal_bonus}")
                reward += terminal_bonus
        print(f"Episode {episode+1}, step {step+1}: action {tool_name}, reward {reward:.2f}")
        core.learn_from_outcome(
            reward,
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.decay_temperature()
    print(f"Temperature after episode: {core.q_agent.temperature:.3f}")
print("Test completed.")