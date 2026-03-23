# Activation function stress tester

import numpy as np
from agi_core import safe_activation

def test_activation_stability(threshold=1e6):
    """Test activation functions with extreme values to catch overflows"
    
    # Test safe_activation with extreme inputs
    extreme_values = [1e-6, 1e6, -1e6, np.nan, np.inf, -np.inf]
    for val in extreme_values:
        try:
            result = safe_activation(val)
            print(f"Input: {val}, Output: {result}")
        except Exception as e:
            print(f"Error with {val}: {str(e)}")
            return False
    return True

if __name__ == "__main__":
    print("Starting activation stress test...")
    if test_activation_stability():