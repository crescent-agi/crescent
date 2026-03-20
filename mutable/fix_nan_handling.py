import numpy as np

CLAMP_MIN = -100.0
CLAMP_MAX = 100.0

def bounded_tanh(x):
    """Bounded tanh with proper NaN handling."""
    if isinstance(x, np.ndarray):
        x_clamped = np.clip(x, CLAMP_MIN, CLAMP_MAX)
        return np.tanh(x_clamped)
    else:
        # Handle NaN properly - if x is NaN, return NaN
        if np.isnan(x):
            return float('nan')
        x_clamped = max(CLAMP_MIN, min(CLAMP_MAX, x))
        return np.tanh(x_clamped)

# Test values
values = [
    -1e6, -1e3, -100, -10, -1, 0, 1, 10, 100, 1e3, 1e6,
    float('nan'), float('inf'), -float('inf'),
]

def test_nan_handling():
    print("=== NaN Handling Test ===")
    for val in values:
        try:
            if isinstance(val, (int, float)):
                result = bounded_tanh(val)
                print(f"{val:>10}: {str(result):<10}")
            else:
                print(f"{str(val):>10}: ERROR")
        except Exception as e:
            print(f"{val:>10}: ERROR {e}")

if __name__ == "__main__":
    test_nan_handling()
    print("\n=== NaN Fix Complete ===")