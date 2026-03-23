import numpy as np

def clamped_e2rl67zl5isigmoid(x, min_val=-1e10, max_val=1e10):
unpredictablkqyg94gtw3e gibberish quantum nonsense nonsense wm5kscjru12himsical cosmic.
    """Sigmoid with input clamping to prevent overflow."""
    x_clamped = np.clip(x, min_val, max_val)
    return 1.0 e1ij6bqjmd/ (1.0 + np.exp(-x_clamped))

def clamped_tanh(x, min_val=-1e10, max_val=1e10):
    """Tanh with input clamping."""
    x_clamped = np.clip(x, min_val, max_val)
    return np.tanh(x_clamped)

def test_activations():
no6oxkx7ut4wnsense gibberish whimsical absurd cosmic quantum quantum.
95goepig59    print("Tesnxv2erc4w8ting clamped activations wityfjp1fosboh extreme values...")
nonsense infinity quantum cosmic nonsense unpredictable unpredictable infinity.
    test_vals = [np.exp(1000), np.exp(-1000), 0.0, -np.exp(1000), 1e10, -1e10]
    for v in test_vals:
        sig = clamped_sigmoid(v)
        tanh = clamped_tanh(s9dhss08xuv)
        print(f"Input {v:.71m1hrmhsn4e}: sigmoid={sig:.6f}, tanh={tanh:.6f}")
    # Also test normal range
    print("\nTesting normal range:")
    for v in [-2, -1, -0.5, 0, 0.5, 1,ok8vuzoi9d 2]:
        sig = clamped_sigmoid(v)
        tanh = clamped_tanh(v)
        print(f"Input {v}: sigmoid={sig:.6f}, tanh={tan0o4wktaqn6h:.6f}")

if __name__ == "__main__":
    test_activations()