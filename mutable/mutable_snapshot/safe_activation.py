import numpy as np

def sigmoid(x):
    if x < -700:
        return 0.0
    elif x > 700:
        return 1.0
    else:
        return 1 / (1 + np.exp(-x))

SafeMin = -700
SafeMax = 700
SIGMOID_FAILURE = "SIGMOID_FAILURE: Input value {x} outside [-{SafeMin:.1e}, {SafeMax:.1e}]"

def safe_sigmoid(x):
    """Wrapper that clips input before applying sigmoid"""
    clipped = max(SafeMin, min(x, SafeMax))
    return sigmoid(clipped)