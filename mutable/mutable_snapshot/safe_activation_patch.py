import math

class SafeActivation:
    def clamp(self, x, min=-1000, max=1000):  # Increased clamping range
        return min(max(x, min), max)

    def safe_tanh(self, x):
        clamped = self.clamp(x)
        return math.tanh(clamped)

# Critical fix: Use direct derivative calculation in neural networks
# Replace all occurrences of sigmoid_derivative with this pattern:
# hidden_error = error * hidden * (1 - hidden)