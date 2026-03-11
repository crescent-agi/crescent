import numpy as np

def safe_activation(x):
    """Replace sigmoid with tanh and add input clamping for numerical stability"""
    # Replace unbounded sigmoid with bounded tanh
    return np.tanh(x)

# Add input clamping to prevent extreme values
x_clamped = np.clip(x, -10, 10)

# Test with extreme values
print("Safe activation with clamped inputs:", safe_activation(x_clamped))
