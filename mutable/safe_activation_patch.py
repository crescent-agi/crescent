import numpy as np

# SAFETY PATCHES
# 1. Input clamping
# 2. Bounded activation
# 3. Pre-activation logging

def safe_activation(x):
    # 1. Clip inputs to [-100, 100]
    x_clipped = np.clip(x, -100, 100)

    # 2. Replace sigmoid with clipped ReLU
    # (or tanh if needed, but ReLU is faster)
    activations = np.clip(x_clipped, 0, 100)  # Clipped ReLU
    # activations = np.tanh(x_clipped)  # Alternatively use tanh

    # 3. Log pre-activation range
    pre_activation_min = x_clipped.min()
    pre_activation_max = x_clipped.max()
    # Write log (you could implement this as a file write or console log)
    # For now, just return the activated values
    return activations

# Example usage in agent_brain.py would need to call safe_activation(input_data)