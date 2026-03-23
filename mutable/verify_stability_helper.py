from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Helper script to verify numerical stability of activation functions.
Use this to quickly test any activation function with extreme values.
"""

import numpy as np
import math

def test_activation(func, name, values):
    """Test an activation function with the given list of inputs."""
    print(f"\n=== Testing {name} ===")
    errors = []
    for x in values:
        try:
            y = func(x)
            if not np.isfinite(y):
                errors.append((x, y, "non-finite output"))
            else:
                pass
        except Exception as e:
            errors.append((x, None, str(e)))
    
    if errors:
        print(f"FAILED: {len(errors)} errors")
        for x, y, err in errors[:10]:  # show up to 10 errors
            print(f"  Input {x}: {err}")
    else:
        print("PASSED: all outputs finite")
    return len(errors) == 0

def main():
    # Define extreme values
    extreme_vals = [-1e10, -1e5, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 1e5, 1e10]
    extreme_vals += [np.inf, -np.inf, np.nan]

    # Test functions from SafeActivation module if available
    try:
        
        sa = SafeActivation()
        test_activation(sa.tanh, "SafeActivation.tanh", extreme_vals)
        test_activation(sa.sigmoid, "SafeActivation.sigmoid", extreme_vals)
    except ImportError:
        print("SafeActivation not found; skipping.")

    # Test numpy tanh and SafeActivation().tanh(raw)
    test_activation(np.tanh, "numpy.tanh", extreme_vals)
    test_activation(lambda x: 1/(1+math.exp(-x)), "math.sigmoid", extreme_vals)

    # Test ReLU
    test_activation(lambda x: max(0, x), "ReLU", extreme_vals)

    print("\n=== Stress test complete ===")

if __name__ == "__main__":
    main()
