import numpy as np

SafeMin = -1000
SafeMax = 1000
SIGMOID_FAILURE = "SIGMOID_FAILURE: Input value {x} outside [-{SafeMin:.1e}, {SafeMax:.1e}]"

def sigmoid(x):
    """Correct sigmoid implementation with overflow protection"""
    if x < SafeMin:
        return 0.0
    elif x > SafeMax:
        return 1.0
    else:
        try:
            return 1 / (1 + np.exp(-x))
        except OverflowError:
            # Handle overflow cases
            if x < 0:
                return 0.0
            else:
                return 1.0

def safe_sigmoid(x):
    """Wrapper that clips input before applying sigmoid"""
    clipped = max(SafeMin, min(x, SafeMax))
    return sigmoid(clipped)