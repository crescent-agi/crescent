# Safe activation functions for numerical stability
import numpy as np

# DIRECT FIX: Adding numpy import to resolve NameError

def safe_sigmoid(x):
    # Numerically stable sigmoid implementation
    if x >= 0:
        z = np.exp(-x)
        return 1 / (1 + z)
    else:
        z = np.exp(x)
        return z / (1 + z)

# Test the safe sigmoid
if __name__ == "__main__":
    test_values = np.array([-1000, -500, -100, 0, 100, 500, 1000])
    results = [safe_sigmoid(x) for x in test_values]
    print('Safe sigmoid test:')
    print('Values:', test_values)
    print('Results:', results)
    print('\u2705 Safe sigmoid implementation ready'