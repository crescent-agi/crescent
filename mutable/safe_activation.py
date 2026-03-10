# Safe Activation Wrapper
import math

def sigmoid(x):
    if x < -1000:
        return -1.0
    elif x > 1000:
        return 1.0
    else:
        return 1 / (1 + math.exp(-x))

SafeMin = -1000
SafeMax = 1000
SIGMOID_FAILURE = "SIGMOID_FAILURE: Input value {x} outside [-{SafeMin:.1e}, {SafeMax:.1e}]"

def safe_sigmoid(x):
    """Wrapper that clips input before applying sigmoid"""
    clipped = max(SafeMin, min(x, SafeMax))
    return sigmoid(clipped)

def test_safe_sigmoid():
    test_cases = [-2000, -1500, 0, 1500, 2000, 1e6, -1e6]
    for x in test_cases:
        result = safe_sigmoid(x)
        print(f"Input: {x}, Clipped: {max(SafeMin, min(x, SafeMax))}, Output: {result}")

if __name__ == "__main__":
    test_safe_sigmoid()