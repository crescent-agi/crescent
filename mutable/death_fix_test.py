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
import random
import os
import math

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

# Patch choose_action to allow death during exploration, keep non-productive masking
tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
              "modify_self", "declare_death", "list_issues", "read_issue",
              "comment_issue", "create_issue", "close_issue"]
non_productive_indices = [i for i, name in enumerate(tool_names) 
                          if name in ["list_files", "write_note", "list_issues", "read_issue",
                                      "comment_issue", "create_issue", "close_issue"]]

original_choose_action = neural_q_continuous_double.NeuralQLearningAgentContinuousDouble.choose_action
def patched_choose_action(self, state_vector):
    if random.random() < self.epsilon:
        # Allow death, but filter non-productive tools
        allowed = [i for i in range(self.action_size) if i not in non_productive_indices]
        if allowed:
            return random.choice(allowed)
        else:
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
print("Patched choose_action: allow death during exploration, mask non-productive tools.")

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
    
    # Initial Q-values
    state = core.compute_state_vector("Files: test", "", [])
    qvals = core.q_agent.nn.predict(state)
    death_idx = 6
    print(f"Initial death Q-value: {qvals[death_idx]:.3f}")
    sorted_q = sorted(enumerate(qvals), key=lambda x: x[1], reverse=True)
    rank = [idx for idx, q in sorted_q].index(death_idx) + 1
    print(f"Death rank: {rank}/{len(qvals)}")
    
    # Run training with exploration
    workspace = SimWorkspace()
    episodes = 30
    steps_per_episode = 10
    death_counts = []
    death_q_history = []
    for episode in range(episodes):
        self.reset()
        self.steps_per_episode = steps_per_episode
        death_in_episode = 0
        for step in range(steps_per_episode):
            tool_name, tool_args, _ = core.decide_action(
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            if tool_name == "declare_death":
                death_in_episode += 1
            tool_result = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            core.learn_from_outcome(
                reward,
                workspace.workspace_summary(),
                workspace.journal,
                workspace.actions
            )
            workspace.actions.append({"tool": tool_name})
        death_counts.append(death_in_episode)
        # Decay epsilon
        if core.q_agent:
            core.q_agent.decay_epsilon()
        # Record death Q-value
        qvals = core.q_agent.nn.predict(state)
        death_q_history.append(qvals[death_idx])
        if (episode + 1) % 5 == 0:
            print(f"Episode {episode+1}: death selected {death_in_episode} times, death Q-value {qvals[death_idx]:.3f}, epsilon {core.q_agent.epsilon:.3f}")
    
    print(f"\nTotal death selections: {sum(death_counts)}")
    print(f"Death Q-value change: {death_q_history[0]:.3f} -> {death_q_history[-1]:.3f}")
    # Plot? just list.
    print("Death Q-values per episode:", [round(q,3) for q in death_q_history])
    
    # Final Q-values
    qvals_final = core.q_agent.nn.predict(state)
    print("\nFinal Q-values:")
    for i, name in enumerate(tool_names):
        print(f"  {name}: {qvals_final[i]:.3f}")
    sorted_final = sorted(enumerate(qvals_final), key=lambda x: x[1], reverse=True)
    rank_final = [idx for idx, q in sorted_final].index(death_idx) + 1
    print(f"Death rank: {rank_final}/{len(qvals_final)}")
    
    # Save model
    save_dir_new = "artifacts/agi_core_continuous_trained_gen28_deathfix"
    os.makedirs(save_dir_new, exist_ok=True)
    core.save(save_dir_new)
    print(f"Saved patched model to {save_dir_new}")

if __name__ == "__main__":
    main()