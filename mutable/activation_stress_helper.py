import numpy as np

# Extreme input cases to test activation functions
TEST_INPUTS = [
    [-1e6, 1e6],  # Overflow/underflow extremes
    [np.nan],      # NaN handling
    [np.inf, -np.inf],
    [0.99999999, -0.99999999],  # Sigmoid near saturation
    [1e-12, -1e-12],  # Near-zero values
    [3.14, -3.14],  # Random large values
    [None],  # None handling
]

# Run all tests
if __name__ == "__main__":
    for input_val in TEST_INPUTS:
        try:
            # Simulate activation function call (replace with actual function)
            result = safe_activation(input_val)
            print(f"Input: {input_val} -> Output: {result}")
        except Exception as e:
            print(f"ERROR: {e} for input {