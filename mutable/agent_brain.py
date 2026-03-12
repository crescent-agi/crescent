#!/usr/bin/env python3
"""
Agent Brain - Version 301 with AGI Core integration
Fixed import issues and focused on numerical stability.
"""
import os
from safe_activation_fixed import SafeActivation
from mutable_snapshot.agi_core_continuous import AGICoreContinuous  # Import AGI Core correctly
import numpy as np

# Global safe activation instance
_sa = SafeActivation()

class AgentBrain:
    def __init__(self, params=None):
        if params is None:
            params = {}
        self.alpha = params.get('alpha', 0.1)
        self.beta = params.get('beta', 0.1)
        self.epsilon = params.get('epsilon', 0.1)
        # Initialize AGI Core with proper parameters
        self.agi_core = AGICoreContinuous(feature_dim=30, use_features=True, exploration_rate=0.1)
        # Initialize recent actions tracking
        self.recent_actions = []  # Track last 5 actions for diversity bonus

    def choose_action(self, state):
        """Choose action using AGI Core analysis with safe fallback."""
        try:
            # Convert state to workspace format for AGI Core
            script_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(script_dir)
            workspace_files = [f for f in os.listdir(parent_dir) if f.endswith('.py')]
            workspace_summary = "Files: " + ", ".join(workspace_files[:10])
            journal = "Agent state: " + str(state)[:200]

            # Get AGI Core recommendation
            tool_name, tool_args, confidence = self.agi_core.decide_action(
                workspace_summary, journal, self.recent_actions
            )

            # Add to recent actions
            self.recent_actions.append({'tool': tool_name, 'confidence': confidence})
            if len(self.recent_actions) > 5:
                self.recent_actions.pop(0)

            return tool_name, tool_args, confidence

        except Exception as e:
            # Safe fallback using original activation-based approach
            print(f"AGI Core failed: {e}, using safe fallback")
            # Handle different state formats
            if isinstance(state, list):
                x = np.array(state)[np.newaxis, :]
            else:
                x = np.array([state])[np.newaxis, :]

            # Apply tanh safely to each element
            safe_x = np.array([_sa.tanh(float(val)) for val in x.flatten()])
            # Map to action (0-4, avoiding declare_death)
            if len(safe_x) > 0:
                action_value = safe_x[0] if len(safe_x) > 0 else 0.0
                action_idx = int(abs(action_value) * 5) % 5
                tool_name = ["read_file", "write_file", "list_files", "execute_code", "write_note"][action_idx]
                return tool_name, {}, 0.3
            else:
                return "read_file", {}, 0.1

    @staticmethod
    def _compute_reward(self_obj, tool_name, tool_args, tool_result):
        """Compute reward based on tool execution result.
        Enhanced reward shaping with AGI Core integration.
        """
        # Basic failure penalty
        if not tool_result.get("success", False):
            return -0.1  # Small penalty for failure

        # Enhanced reward matrix based on tool importance and AGI Core feedback
        action_rewards = {
            "execute_code": 1.2 if "AGI_Core" in str(tool_result.get("code_output", "")) else 1.0,
            "modify_self": 1.5,  # High reward for self-improvement
            "write_file": 0.3,   # Reduced from 1.0 to discourage spam
            "read_file": 0.8,    # Reward for learning
            "list_files": 0.2,   # Neutral exploration
            "declare_death": -1.0  # Strong penalty for early termination
        }

        # Apply recency penalty (discourage recent actions)
        recent_penalty = sum(1 for a in self_obj.recent_actions[-3:] if a['tool'] == tool_name) * 0.2

        # Apply diversity bonus for new tools
        if tool_name not in [a['tool'] for a in self_obj.recent_actions[-3:]]:
            diversity_bonus = 0.5
        else:
            diversity_bonus = 0

        # Calculate total reward
        base_reward = action_rewards.get(tool_name, 0.0)
        total_reward = base_reward + diversity_bonus - recent_penalty

        # Clamp reward to prevent overflow
        if total_reward > 10:
            total_reward = 10
        elif total_reward < -10:
            total_reward = -10

        return total_reward

    def learn_from_action(self, tool_name, tool_args, tool_result, reward):
        """Update AGI Core with action outcome."""
        try:
            # Update AGI Core with learning data
            script_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(script_dir)
            workspace_files = [f for f in os.listdir(parent_dir) if f.endswith('.py')]
            workspace_summary = "Files: " + ", ".join(workspace_files[:10])
            journal = f"Action: {tool_name}, Reward: {reward}"
            actions = [a['tool'] for a in self.recent_actions]

            self.agi_core.learn_from_outcome(reward, workspace_summary, journal, actions)

        except Exception as e:
            print(f"AGI Core learning failed: {e}")

    def get_agi_advice(self):
        """Get advice from AGI Core's self-reflection."""
        try:
            return self.agi_core.reflect()
        except Exception as e:
            print(f"AGI Core reflection failed: {e}")
            return {"advice": ["Fallback: Keep exploring and building"]}

    def save_agi_core(self, path="artifacts/agi_core_continuous"):
        """Save AGI Core state."""
        try:
            self.agi_core.save(path)
        except Exception as e:
            print(f"Failed to save AGI Core: {e}")

    def load_agi_core(self, path="artifacts/agi_core_continuous"):
        """Load AGI Core state."""
        try:
            if os.path.exists(path):
                self.agi_core.load(path)
                print(f"AGI Core loaded from {path}")
            else:
                print(f"AGI Core not found at {path}, using fresh initialization")
        except Exception as e:
            print(f"Failed to load AGI Core: {e}")