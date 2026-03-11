import numpy as np

def sigmoid(x):
    if x < -1000:
        return -1.0
    elif x > 1000:
        return 1.0
    else:
        return 1 / (1 + np.exp(-x))

SafeMin = -1000
SafeMax = 1000
SIGMOID_FAILURE = "SIGMOID_FAILURE: Input value {x} outside [-{SafeMin:.1e}, {SafeMax:.1e}]"

try:
    if np.isnan(x) or np.isinf(x):
        raise ValueError(SIGMOID_FAILURE.format(x=x))
except ValueError as e:
    """Return tuple (value, error) for error handling"""
    return -1.0, e

try:
    clipped = max(SafeMin, min(x, SafeMax))
    return sigmoid(clipped)
except:
    return -1.0, "UNEXPECTED_ERROR: Safe sigmoid failed"


# Status: Added NaN/inf rejection and error propagation
# Next: Test with extreme values in training loop