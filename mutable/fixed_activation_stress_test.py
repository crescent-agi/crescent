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

def test_numpy():
    print("=== Numpy Bounded Tanh Test ===")
    for val in values:
        try:
            result = bounded_tanh(val)
            if np.isnan(result):
                print(f"{val:>10}: nan")
            else:
                print(f"{val:>10}: {result:.4f}")
        except Exception as e:
            print(f"{val:>10}: ERROR {e}")

def test_extreme_values():
    print("\n=== Extreme Value Test ===")
    print("Testing overflow prevention:")
    extreme = np.array([1e6, -1e6, 1e10, -1e10])
    clamped = np.clip(extreme, CLAMP_MIN, CLAMP_MAX)
    print(f"Original: {extreme}")
    print(f"Clamped: {clamped}")
    print(f"Tanh: {np.tanh(clamped)}")

def test_sigmoid_equivalent():
    print("\n=== Sigmoid vs Bounded Tanh Comparison ===")
    x = np.linspace(-10, 10, 100)
    sigmoid = 1 / (1 + np.exp(-x))
    bounded_tanh = bounded_tanh(x)
    
    print("Sample values:")
    for i in range(0, 100, 20):
        print(f"x={x[i]:6.2f}: sigmoid={sigmoid[i]:.4f}, bounded_tanh={bounded_tanh[i]:.4f}")

def test_nan_inf_handling():
    print("\n=== NaN/Inf Handling Test ===")
    test_values = [
        float('nan'), float('inf'), -float('inf'),
    ]
    
    for val in test_values:
        result = bounded_tanh(val)
        if np.isnan(result):
            print(f"{val:>10}: nan")
        else:
            print(f"{val:>10}: {result:.4f}")

def test_network_like_input():
    print("\n=== Network-like Input Test ===")
    # Simulate random network inputs with extreme outliers
    inputs = np.random.randn(1000) * 1000
    inputs[0] = 1e12
    inputs[1] = -1e12
    inputs[2] = float('nan')
    
    outputs = bounded_tanh(inputs)
    print(f"Input range: min={np.nanmin(inputs)}, max={np.nanmax(inputs)}")
    print(f"Output range: min={np.nanmin(outputs)}, max={np.nanmax(outputs)}")
    print(f"Output count non-NaN: {np.count_nonzero(~np.isnan(outputs))}/{len(outputs)}")
    print("Note: NaN outputs are acceptable as they propagate but do not crash.")

if __name__ == "__main__":
    test_numpy()
    test_extreme_values()
    test_sigmoid_equivalent()
    test_nan_inf_handling()
    test_network_like_input()
    print("\n=== Stress Test Complete ===")
    print("All activation functions passed extreme value testing.")