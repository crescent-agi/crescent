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

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_boltzmann_var200_fixed as patch_boltzmann_var200
print('Applied fixed patch')

from agi_core_continuous import AGICoreContinuous
import random
import os
from new_reward_gen50 import compute_reward_gen50 as compute_reward
from new_reward_gen50 import compute_terminal_bonus_gen50

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85
        self.tool_penalty_factor = 0.0
        self.episode_tools = set()
        self.episode_tool_counts = {}
        self.episode_productive_first_use = set()
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.global_tool_counts_curiosity = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.tool_usage_counts.clear()
        self.episode_tools.clear()
        self.episode_tool_counts.clear()
        self.episode_productive_first_use.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0
        self.episode_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_total = 0

self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {
            "inherited_notes.md": "# Inherited Notes",
            "agi_core.py": "# AGI Core",
            "cognitive_architecture.py": "# Cognitive Architecture",
            "strategy.md": "# Strategy",
        }
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        file_list = ", ".join(self.files.keys())
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            directory = tool_args.get("directory", ".")
            result["entries"] = [{"name": name, "type": "file", "size": len(content)} for name, content in self.files.items()]
        elif tool_name == "execute_code":
            code = tool_args.get("code", "")
            if "error" in code:
                result["stdout"] = ""
                result["stderr"] = "Simulated error"
                result["success"] = False
            else:
                result["stdout"] = "Simulated output"
                result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filepath] = content
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = f"Cannot modify non-existent file: {filepath}"
                result["success"] = False
        elif tool_name == "declare_death":
            result["message"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            result["issues"] = []
        else:
            result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result
    def update_state(self, *args):
        pass

def run_validation(core, steps=200):
    original_epsilon = core.q_agent.epsilon
    original_temp = core.q_agent.temperature
    core.q_agent.epsilon = 0.0
    core.q_agent.temperature = 0.2
    workspace = SimWorkspace()
    self.reset()
    self.steps_per_episode = steps
    stats = {'action_counts': {}, 'non_productive_counts': {}, 'total_reward': 0.0, 'declare_death_count': 0}
    productive_tools = ["write_file", "execute_code", "modify_self", "read_file"]
    for step in range(steps):
        tool_name, tool_args, confidence = core.decide_action(
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        tool_result = workspace.tool_result(tool_name, tool_args)
        reward = compute_reward(self, tool_name, tool_args, tool_result)
        stats['total_reward'] += reward
        stats['action_counts'][tool_name] = stats['action_counts'].get(tool_name, 0) + 1
        if tool_name == "declare_death":
            stats['declare_death_count'] += 1
        if tool_name not in productive_tools and tool_name != "declare_death":
            stats['non_productive_counts'][tool_name] = stats['non_productive_counts'].get(tool_name, 0) + 1
        workspace.update_state(tool_name, tool_args)
        workspace.actions.append({"tool": tool_name, "step": step})
    core.q_agent.epsilon = original_epsilon
    core.q_agent.temperature = original_temp
    productive_counts = {tool: stats['action_counts'].get(tool, 0) for tool in productive_tools}
    total_productive = sum(productive_counts.values())
    distribution = {}
    if total_productive > 0:
        for tool in productive_tools:
            distribution[tool] = (productive_counts[tool] / total_productive) * 100
    else:
        for tool in productive_tools:
            distribution[tool] = 0.0
    stats['productive_distribution'] = distribution
    stats['non_productive_total'] = sum(stats['non_productive_counts'].values())
    stats['average_reward'] = stats['total_reward'] / steps
    return stats

# Create core
core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.001, exploration_rate=0.0,
                         epsilon_decay=1.0, epsilon_min=0.0, use_features=True)
core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
print(f'Initial temperature: {core.q_agent.temperature}')
# Load previous model
save_dir = "artifacts/agi_core_continuous_trained_gen41_strong"
if os.path.exists(save_dir):
    core.load(save_dir)
    print(f'Loaded previous model from {save_dir}')
    if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
        core.q_agent.reset_output_weights_all_productive()
    else:
        core.q_agent.reset_output_weights([0,1,3,5])
    print('Reset output weights')
    core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)

workspace = SimWorkspace()
episodes = 2
steps_per_episode = 20
for episode in range(episodes):
    self.reset()
    self.steps_per_episode = steps_per_episode
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
            reward += terminal_bonus
        workspace.actions.append({"tool": tool_name, "step": step})
        core.learn_from_outcome(
            reward,
            workspace.workspace_summary(),
            workspace.journal,
            workspace.actions
        )
        print(f'Episode {episode+1}, step {step+1}: {tool_name}')
    core.q_agent.decay_temperature()

print('\n--- Validation after training ---')
validation_stats = run_validation(core, steps=100)
print(f'Non-productive actions: {validation_stats["non_productive_total"]}')
print(f'Average reward per step: {validation_stats["average_reward"]:.3f}')
print('Productive distribution:')
for tool, perc in validation_stats['productive_distribution'].items():
    print(f'  {tool}: {perc:.1f}%')
print('Done.')