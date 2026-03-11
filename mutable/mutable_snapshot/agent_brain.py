import numpy as np
import logging

# Setup logging
logging.basicConfig(filename='pre_activation_log.txt', level=logging.INFO)

# SAFETY PATCHES
# 1. Input clamping
# 2. Bounded activation
# 3. Pre-activation logging

def safe_activation(x):
    # 1. Clip inputs to [-100, 100]
    x_clipped = np.clip(x, -100, 100)
    
    # 2. Replace sigmoid with bounded tanh
    activations = np.tanh(x_clipped)
    
    # 3. Log pre-activation range
    pre_activation_min = x_clipped.min()
    pre_activation_max = x_clipped.max()
    logging.info(f"Pre-activation range: [{pre_activation_min}, {pre_activation_max}]")
    
    return activations

# Example usage: agent_brain should call safe_activation for all inputs