import numpy as np

def safe_activation(x):
    # Clamp inputs to prevent overflow
    x = np.clip(x, -100, 100)
    # Apply activation function
    return np.tanh(x)

# Test with extreme values
print(safe_activation([1000, -1000, 0]))