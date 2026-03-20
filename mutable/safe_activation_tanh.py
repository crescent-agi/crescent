import math

class SafeActivationTanh:
    def __init__(self):
        self.lower_bound = -500  # Clamp extreme values
        self.upper_bound = 500

    def tanh(self, x):
        clamped_x = max(self.lower_bound, min(x, self.upper_bound))
        return math.tanh(clamped_x)

# Usage example:
# activation = SafeActivationTanh().tanh(input_value)