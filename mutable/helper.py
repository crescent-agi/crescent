import numpy as np

def safe_sigmoid(x):
    clamped = np.clip(x, -100, 100)
    return np.tanh(clamped)

# Test with mixed inputs
print(safe_sigmoid([1000, -2000, 0]))