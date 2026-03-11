#!/usr/bin/env python3
"""
Agent Brain - Simplified version that works with safe activation.
Fixed import issues and focused on numerical stability.
"""
from safe_activation_fixed import SafeActivation
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

    def choose_action(self, state):
        # Use safe activation pattern with state
        # Handle different state formats
        if hasattr(state, 'flatten'):
            x = state.flatten()[np.newaxis, :]
        elif isinstance(state, list):
            x = np.array(state)[np.newaxis, :]
        else:
            x = np.array([state])[np.newaxis, :]
        
        # Apply tanh safely to each element
        safe_x = np.array([_sa.tanh(float(val)) for val in x.flatten()])
        # Simple policy: choose action based on first few values
        if len(safe_x) > 0:
            # Map to action space (0-6 for 7 tools, excluding declare_death=6 sometimes)
            action_value = safe_x[0] if len(safe_x) > 0 else 0.0
            action = int(abs(action_value) * 6) % 6  # 0-5, avoiding 6 (declare_death) for safety
            return action
        else:
            return 0

    @staticmethod
    def _compute_reward(self_obj, tool_name, tool_args, tool_result):
        """Compute reward based on tool execution result.
        self_obj: the DummySelf instance (tracking usage counts).
        """
        # Simple reward shaping
        if not tool_result.get("success", False):
            return -0.1  # Small penalty for failure
        
        # Reward for productive actions
        productive_tools = ["read_file", "write_file", "execute_code", "modify_self"]
        if tool_name in productive_tools:
            return 1.0
        elif tool_name == "write_note":
            return 0.5
        elif tool_name in ["list_files"]:
            return 0.1
        elif tool_name == "declare_death":
            return -1.0  # Penalize early death
        else:
            return 0.01  # Small default reward