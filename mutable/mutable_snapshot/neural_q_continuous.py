import math

class SafeActivation:
    def clamp(self, x, min=-10, max=10):
        return min(max(x, min), max)

    def tanh(self, x):
        return math.tanh(x)

    def safe_tanh(self, x):
        clamped = self.clamp(x)
        return math.tanh(clamped)

# Replace all sigmoid calls with safe_tanh
# Example usage: SafeActivation().safe_tanh(x)