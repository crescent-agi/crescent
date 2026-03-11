import math

class SafeActivation:
    def clamp(self, x, min=-5, max=5):
        return min(max(x, min), max)
    
    def safe_tanh(self, x):
        clamped = self.clamp(x)
        return math.tanh(clamped)
    
    def add_logging(self, name, x):
        print(f"[LOG] {name}: raw={x}, clamped={self.clamp(x)}")

# Example wrapper for dangerous activations
def safe_sigmoid(x):
    safe_act = SafeActivation()
    safe_act.add_logging("sigmoid_input", x)
    clamped = safe_act.clamp(x)
    return 1 / (1 + math.exp(-clamped))

# Apply clamp with tighter bounds for safety
def aggressive_clamp(x, min=-3, max=3):
    return max(min(x, max), min)

# Expose the functions in the module
__all__ = ['SafeActivation', 'safe_sigmoid', 'aggressive_clamp']