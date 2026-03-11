import numpy as np

def test_sigmoid_equivalent():
    """Compare sigmoid vs bounded tanh for various inputs."""
    print("\n=== Sigmoid vs Bounded Tanh Comparison ===")
    np.random.seed(42)
    x = np.random.uniform(-10, 10, 100)
    sigmoid = 1 / (1 + np.exp(-x))
    bounded_tanh = np.tanh(x)

    # Print first 10 samples for comparison
    for i in range(min(10, len(x))):
        print(f"x={x[i]:6.2f}: sigmoid={sigmoid[i]:.4f}, bounded_tanh={bounded_tanh[i]:.4f}")

    # Check if they're close enough for most values
    diff = np.abs(sigmoid - (bounded_tanh + 1) / 2)  # convert tanh to [0,1] range
    print(f"\nMax difference (sigmoid vs converted tanh): {diff.max():.4f}")
    print(f"Mean difference: {diff.mean():.4e}")
    print(f"Values within 0.01 tolerance: {np.sum(diff < 0.01)}/{len(diff)}")

if __name__ == "__main__":
    test_sigmoid_equivalent()
