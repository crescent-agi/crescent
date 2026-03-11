import math

def safe_sigmoid(x):
    """Numerically stable sigmoid with input clamping"""
    x_clamped = max(-500, min(500, x))
    return 1.0 / (1.0 + math.exp(-x_clamped))

# Replace all direct math.exp(math.sigmoid) calls with safe_sigmoid
# Add input validation before activation layers

def clip_input(x, clip_min=-10, clip_max=10):
    return np.clip(x, clip_min, clip_max)

# Dynamic domain checks for neural networks

def validate_input_range(x, expected_min=-10, expected_max=10):
    if not np.all((expected_min <= x) & (x <= expected_max)):
        raise ValueError(f"Input out of expected range: {x}")