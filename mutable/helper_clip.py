import numpy as np

def safe_clip(x, lower=-30, upper=30):
    """Clamp input to safe range to avoid numerical instability."""
    if isinstance(x, (list, tuple, np.ndarray)):
        # For arrays, use numpy clip
        return np.clip(x, lower, upper)
    else:
        return max(min(x, upper), lower)

def safe_tanh(x):
    """Tanh with input clipping to avoid overflow."""
    clamped = np.clip(x, -100, 100)
    return np.tanh(clamped)

# Self-test
if __name__ == "__main__":
    print("safe_clip tests:")
    print(safe_clip(1000))  # should be 30
    print(safe_clip(-1000))  # should be -30
    print("safe_tanh tests:")
    print(safe_tanh([1000, -2000, 0]))  # should be [1, -1, 0]
