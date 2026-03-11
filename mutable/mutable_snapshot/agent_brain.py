import numpy as np

def safe_activation(x):
    # 1. Clip inputs to [-100, 100] BEFORE any activation
    x_clipped = np.clip(x, -100, 100)
    
    # 2. Use bounded tanh activation (range [-1, 1])
    # tanh is safe for large inputs; it asymptotes
    activations = np.tanh(x_clipped)
    
    # 3. Optional: Log extreme values for debugging
    # (Implement later if needed)
    
    return activations
