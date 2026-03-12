import numpy as np

def clamped_sigmoid(x, min_val=-1e10, max_val=1e10):
    """Sigmoid with input clamping to prevent overflow."""
    x_clamped = np.clip(x, min_val, max_val)
    return 1.0 / (1.0 + np.exp(-x_clamped))

def clamped_tanh(x, min_val=-1e10, max_val=1e10):
    """Tanh with input clamping."""
    x_clamped = np.clip(x, min_val, max_val)
    return np.tanh(x_clamped)

def test_activations():
    print("Testing clamped activations with extreme values...")
    test_vals = [np.exp(1000), np.exp(-1000), 0.0, -np.exp(1000), 1e10, -1e10]
    for v in test_vals:
        sig = clamped_sigmoid(v)
        tanh = clamped_tanh(v)
        print(f"Input {v:.4e}: sigmoid={sig:.6f}, tanh={tanh:.6f}")
    # Also test normal range
    print("\nTesting normal range:")
    for v in [-2, -1, -0.5, 0, 0.5, 1, 2]:
        sig = clamped_sigmoid(v)
        tanh = clamped_tanh(v)
        print(f"Input {v}: sigmoid={sig:.6f}, tanh={tanh:.6f}")

if __name__ == "__main__":
    test_activations()