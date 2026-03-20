# Crescent's first experiment

import numpy as np

# Test extreme activation function safety
def test_activation_safety(func, inputs):
    """Validate activation function against extreme inputs"""
    try:
        # Test normal range
        result = func(inputs)
        print(f"Normal: {result[:5]}... (len={len(result)})")
        # Test extreme values
        extreme = np.array([1e10, -1e10, 1e-10, -1e-10, np.nan, np.inf, -np.inf])
        result = func(extreme)
        print(f"Extreme: {result[:5]}... (len={len(result)})")
        # Check for overflow
        if np.any(np.isnan(result)) or np.any(np.isinf(result)):
            print("\u26a0\ufe0f Overflow detected!")
            return False
        return True
    except Exception as e:
        print(f"\ud83d\udca5 Crash: {e}")
        return False

# Test sigmoid function
print("Testing sigmoid safety...")
print(test_activation_safety(lambda x: 1/(1+np.exp(-x)), np.linspace(-10, 10, 100)))