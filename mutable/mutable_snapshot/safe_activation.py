# Safe Activation Wrapper
import math

def tanh(x):
    # Always clamp x to safe range and return [0,1] range
    clipped = max(-1000, min(x, 1000))
    return 1 / (1 + math.exp(-clipped))

SafeMin = -1000
SafeMax = 1000
SIGMOID_FAILURE = f"SIGMOID_FAILURE: Input {x} clipped to [-{SafeMin:.1e}, {SafeMax:.1e}]"

def safe_tanh(x):
    """Wrapper that clips input before applying sigmoid"""
    return tanh(min(max(x, SafeMin), SafeMax))

# Test cases automatically run
if __name__ == "__main__":
    test_cases = [-2000, -1500, 0, 1500, 2000, 1e12, -1e12]
    for x in test_cases:
        result = safe_tanh(x)
        print(f"Input: {x:.2e}, Clipped: {max(SafeMin, min(x, SafeMax)):.2e}, Output: {result:.4f}")