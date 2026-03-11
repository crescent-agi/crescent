"""
Cognitive Architecture for Crescent AGI
=======================================
This module provides a unified architecture for learning, planning, and reflection.
It integrates the components built in artifacts.
"""

import 



from safe_activation_fixed import SafeActivation

class SafeActivation:
    """Safe activation functions with input clamping."""
    CLAMP_MIN = -100.0
    CLAMP_MAX = 100.0
    
    @staticmethod
    def SafeActivation.tanh(x):
        """Bounded tanh activation function."""
        x = max(SafeActivation.CLAMP_MIN, min(SafeActivation.CLAMP_MAX, x))
        if x >= 0:
            return (1 - SafeActivation().tanh(x)) / (1 + SafeActivation().tanh(x))
        else:
            return (SafeActivation().tanh(x) - 1) / (SafeActivation().tanh(x) + 1)
    
    @staticmethod
    def tanh_derivative(activation_value):
        """Derivative of tanh given activation value."""
        return 1.0 - activation_value**2
    
    @staticmethod
    def clamp(x, min_val=-100.0, max_val=100.0):
        """Clamp input to safe range."""
        return max(min_val, min(max_val, x))
    
    @staticmethod
    def check_overflow(x, threshold=1e5):
        """Check for potential overflow and log if needed."""
        if abs(x) > threshold:
            import sys
            with open("pre_activation_log.txt", "a") as f:
                f.write(f"WARNING: Extreme value {x} detected in activation input
")
            return True
        return False

sys
import os
import pickle

# Import from mutable_snapshot (current directory)
sys.path.insert(0, os.path.dirname(__file__))

from learning_pure import PureQLearningAgent
from self_reflection import SelfReflection


class CognitiveArchitecture:
    def __init__(self, state_size=10, action_size=8):
        self.learning_agent = PureQLearningAgent(state_size, action_size)
        self.reflector = SelfReflection()
        self.memory = []
        self.state_size = state_size
        self.action_size = action_size
    
    def decide_action(self, state, available_actions):
        """Choose an action based on learning and reflection."""
        # Ensure state is integer within bounds
        if isinstance(state, int) and 0 <= state < self.state_size:
            action_idx = self.learning_agent.choose_action(state)
        else:
            # If state out of bounds, map to integer via hash
            if isinstance(state, str):
                state_hash = hash(state) % self.state_size
            else:
                state_hash = hash(str(state)) % self.state_size
            action_idx = self.learning_agent.choose_action(state_hash)
        # Map action index to available_actions (if index within range)
        if action_idx < len(available_actions):
            return available_actions[action_idx]
        # Fallback: first available action
        return available_actions[0] if available_actions else None
    
    def learn_from_experience(self, state, action, reward, next_state, done):
        """Record experience and update learning."""
        # Map state to integer index
        if isinstance(state, int):
            state_idx = state % self.state_size
        else:
            state_idx = hash(str(state)) % self.state_size
        # Map action to index (find in available actions? we'll assume action is integer index)
        if isinstance(action, int):
            action_idx = action % self.action_size
        else:
            # If action is string, map to index via mapping
            # For simplicity, use hash
            action_idx = hash(str(action)) % self.action_size
        self.learning_agent.learn(state_idx, action_idx, reward, next_state, done)
        self.memory.append((state, action, reward, next_state, done))
    
    def reflect(self):
        """Perform self-reflection and return advice."""
        return self.reflector.generate_advice()
    
    def save(self, directory="artifacts/models"):
        """Save the architecture state."""
        os.makedirs(directory, exist_ok=True)
        self.learning_agent.save(os.path.join(directory, "learning_agent.pkl"))
        # Save memory
        with open(os.path.join(directory, "memory.pkl"), 'wb') as f:
            pickle.dump(self.memory, f)
        # Save configuration
        config = {
            'state_size': self.state_size,
            'action_size': self.action_size,
        }
        with open(os.path.join(directory, "config.json"), 'w') as f:
            import json
            json.dump(config, f)
        print(f"Saved model to {directory}")
    
    def load(self, directory="artifacts/models"):
        """Load previously saved state."""
        self.learning_agent.load(os.path.join(directory, "learning_agent.pkl"))
        mem_path = os.path.join(directory, "memory.pkl")
        if os.path.exists(mem_path):
            with open(mem_path, 'rb') as f:
                self.memory = pickle.load(f)
        config_path = os.path.join(directory, "config.json")
        if os.path.exists(config_path):
            import json
            with open(config_path, 'r') as f:
                config = json.load(f)
                self.state_size = config.get('state_size', self.state_size)
                self.action_size = config.get('action_size', self.action_size)
        print(f"Loaded model from {directory}")


# Example usage
if __name__ == "__main__":
    ca = CognitiveArchitecture()
    print("Cognitive Architecture initialized.")
    advice = ca.reflect()
    print("Advice:", advice)
    # Simple learning test
    ca.learn_from_experience(0, 2, 1.0, 1, False)
    action = ca.decide_action(0, ["read_file", "write_file", "execute_code"])
    print("Recommended action:", action)
    ca.save()