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
import random
import math

# Reward function
from new_reward_gen28 import compute_reward_gen28 as compute_reward

class DummySelf:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.global_tool_counts = {tool: 0 for tool in ["write_file", "execute_code", "modify_self", "read_file"]}
        self.episode_tool_counts = {}
        self.recent_read_files = []
        self.episode_step_count = 0
        self.steps_per_episode = 10
    def reset(self):
        self.last_tool = None
        self.recent_tools.clear()
        self.episode_tool_counts.clear()
        self.recent_read_files.clear()
        self.episode_step_count = 0

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
    def update_state(self, tool_name, tool_args):
        pass

# Patch choose_action to allow death during exploration
original_choose_action = neural_q_continuous_double.NeuralQLearningAgentContinuousDouble.choose_action
def patched_choose_action(self, state_vector):
    if random.random() < self.epsilon:
        # Allow death (no filtering)
        return random.randrange(self.action_size)
    else:
        q_values = self.nn.predict(state_vector)
        max_q = max(q_values)
        best_actions = [i for i, q in enumerate(q_values) if q == max_q]
        if len(best_actions) > 1 and 6 in best_actions:
            best_actions.remove(6)
        if best_actions == [6]:
            sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
            for idx, q in sorted_q:
                if idx != 6:
                    return idx
        return random.choice(best_actions)
neural_q_continuous_double.NeuralQLearningAgentContinuousDouble.choose_action = patched_choose_action
print("Patched choose_action to allow death during exploration.")

def get_q_values(core):
    state = core.compute_state_vector("Files: test", "", [])
    return core.q_agent.nn.predict(state)

def main():
    # Load existing model
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
    
    tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                  "modify_self", "declare_death", "list_issues", "read_issue",
                  "comment_issue", "create_issue", "close_issue"]
    
    # Print initial Q-values
    qvals = get_q_values(core)
    print("\nInitial Q-values:")
    for i, name in enumerate(tool_names):
        print(f"  {name}: {qvals[i]:.3f}")
    death_idx = 6
    print(f"Death Q-value: {qvals[death_idx]:.3f}")
    # Rank
    sorted_q = sorted(enumerate(qvals), key=lambda x: x[1], reverse=True)
    rank = [idx for idx, q in sorted_q].index(death_idx) + 1
    print(f"Death rank: {rank}/{len(qvals)}")
    
    # Run a few episodes with exploration
    workspace = SimWorkspace()
episodes = 0
    steps_per_episode = 10
    death_selected = 0
    for episode in range(episodes):
        self.reset()
        self.steps_per_episode = steps_per_episode
        for step in range(steps_per_episode):
            tool_name, tool_args, _ = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            if tool_name == "declare_death":
                death_selected += 1
                print(f"Episode {episode}, step {step}: death selected, reward {reward}")
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            workspace.actions.append({"tool": tool_name})
        # Decay epsilon
        if core.q_agent:
            core.q_agent.decay_epsilon()
    
    print(f"\nDeath selected {death_selected} times during exploration.")
    
    # Final Q-values
    qvals2 = get_q_values(core)
    print("\nFinal Q-values:")
    for i, name in enumerate(tool_names):
        print(f"  {name}: {qvals2[i]:.3f}")
    print(f"Death Q-value: {qvals2[death_idx]:.3f}")
    sorted_q2 = sorted(enumerate(qvals2), key=lambda x: x[1], reverse=True)
    rank2 = [idx for idx, q in sorted_q2].index(death_idx) + 1
    print(f"Death rank: {rank2}/{len(qvals2)}")
    delta = qvals2[death_idx] - qvals[death_idx]
    print(f"Change in death Q-value: {delta:.3f}")
    
    # Save the updated model (optional)
    # core.save("artifacts/agi_core_continuous_trained_gen28_deathfix")
    
if __name__ == "__main__":
    main()