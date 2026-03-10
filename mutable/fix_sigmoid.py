# Fix sigmoid numerical stability

import numpy as np

# Replace sigmoid with tanh or ReLU for stability
# Sigmoid causes overflow with extreme values

# Original sigmoid:
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))

# Replace with tanh:
# def stable_sigmoid(x):
#     return np.tanh(x)

# Or ReLU:
# def stable_sigmoid(x):
#     return np.maximum(0, x)

# For neural networks, use tanh or ReLU instead of sigmoid
# Add input validation before activation layers

# Example: Clip input values to [-10, 10] before activation

def clip_input(x, clip_min=-10, clip_max=10):
    return np.clip(x, clip_min, clip_max)

# Dynamic domain checks for neural networks
# Check if input values are within expected range

def validate_input_range(x, expected_min=-10, expected_max=10):
    if not np.all((expected_min <= x) & (x <= expected_max)):
        raise ValueError(f