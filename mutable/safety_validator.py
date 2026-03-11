# Safety Validator for Neural Networks

import numpy as np

def clip_inputs(inputs, min_val=-1e5, max_val=1e5):
    """Clip inputs to prevent overflow in activation functions"""
    return np.clip(inputs, min_val, max_val)

def validate_activation(inputs):
    """Check for numerical instability in activation functions"""
    if np.any(np.abs(inputs) > 1e10):
        raise ValueError("Numerical instability detected in activation function")
    return inputs

# Example usage
if __name__ == "__main__":
    test_input = np.array([1e12, -1e12, 0.5, 2.0])
    print("Clipped input:", clip_inputs(test_input))
    print("Validated activation:", validate_activation(clip_inputs(test_input)))