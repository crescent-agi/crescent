# Implement dynamic domain checks for all activation layers
import numpy as np

class SafeActivation:
    def __init__(self, min_val=-10, max_val=10):
        self.min_val = min_val
        self.max_val = max_val
    
    def clamp_input(self, x):
        """Ensure inputs stay within safe bounds for activation functions"""
        return np.clip(x, self.min_val, self.max_val)
    
    def tanh_activation(self, x):
        """Tanh with safety checks"""
        clamped = self.clamp_input(x)
        if not np.all(np.isfinite(clamped)):
            raise ValueError("Finite input required for activation")
        return np.tanh(clamped)
    
    def relu_activation(self, x):
        """ReLU with safety checks"""
        clamped = self.clamp_input(x)
        if not np.all(np.isfinite(clamped)):
            raise ValueError("Finite input required for activation")
        return np.clip(clamped, 0, self.max_val)

# Apply to all relevant activation points in network
# Example:
# safe_act = SafeActivation(-10, 10)
# activated_value = safe_act.tanh_activation(pre_activation_output)