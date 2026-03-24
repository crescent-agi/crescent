from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Safety-patched AGI Core.
"""
# Import safe activation
from agent_brain import safe_tanh

# Replace all sigmoid calls with safe_tanh
# Replace all sigmoid_derivative calls with tanh_derivative

class NeuralQ:
    def __init__(self):
        self.state = 0
        self.activation_cache = []

    def forward(self, x):
        # Safety clamp first
        x_clipped = np.clip(x, -100, 100)
        # Log extreme values
        if len(self.activation_cache) > 0:
            prev_min, prev_max = self.activation_cache[-1]
            curr_min, curr_max = x_clipped.min(), x_clipped.max()
            if abs(prev_min) > 50 or abs(prev_max) > 50:
                print(f"EMERGENCY: Previous activation violated bounds [{prev_min:.2f}, {prev_max:.2f}]!")
        self.activation_cache.append((x_clipped.min(), x_clipped.max()))
        
        # Apply safe tanh
        return safe_tanh(x_clipped)

    def SafeActivation().tanh_derivative(self, x):
        s = self.SafeActivation().tanh(x)
        return s * (1 - s)  # CORRECT: derivative of sigmoid, not tanh

    # Replace all other sigmoid calls with safe_tanh
    def forward(self, x):
        return safe_tanh(x)

    def forward_with_logging(self, x):
        # Safety clamp first
        x_clipped = np.clip(x, -100, 100)
        # Log extreme values
        if len(self.activation_cache) > 0:
            prev_min, prev_max = self.activation_cache[-1]
            curr_min, curr_max = x_clipped.min(), x_clipped.max()
            if abs(prev_min) > 50 or abs(prev_max) > 50:
                print(f"EMERGENCY: Previous activation violated bounds [{prev_min:.2f}, {prev_max:.2f}]!")
        self.activation_cache.append((x_clipped.min(), x_clipped.max()))
        
        # Apply safe tanh
        return safe_tanh(x_cl)