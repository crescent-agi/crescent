#!/usr/bin/env python3

"""
Fixed activation stress test that properly handles extreme values.
"""

import numpy as np

# Original unsafe sigmoid
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# Fixed version with clamping
def sigmoid_safe(x):
    # Clamp input to prevent overflow
    x_clipped = np.clip(x, -50, 50)
    return 1.0 / (1.0 + np.exp(-x_clipped))

# Test function
def test_activation():
    # Extreme values that would break the original
    test_values = [1000, -1000, 1e10, -1e10, np.inf, -np.inf]
    
    print("=== Testing Original (Unsafe) Sigmoid ===")
    for val in test_values:
        try:
            result = sigmoid(val)
            print(f"Input: {val:>15} -> Output: {result}")
        except Exception as e:
            print(f"Input: {val:>15} -> CRASH: {e}")
    
    print("\n=== Testing Safe Sigmoid ===")
    for val in test_values:
        try:
            result = sigmoid_safe(val)
            print(f"Input: {val:>15} -> Output: {result:.6f}")
        except Exception as e:
            print(f"Input: {val:>15} -> CRASH: {e}")

# Execute tests
if __name__ == "__main__":
    test_activation()