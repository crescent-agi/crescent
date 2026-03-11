import math

def sigmoid(x):
    """Basic sigmoid implementation."""
    return 1 / (1 + math.exp(-x))

def safe_sigmoid(x):
    """Numerically stable sigmoid implementation."""
    if x >= 0:
        z = math.exp(-x)
        return 1 / (1 + z)
    else:
        z = math.exp(x)
        return z / (1 + z)

def test_sigmoid_stability():
    test_values = [0, 10, -10, 100, -100, 1000, -1000, 1e6, -1e6]
    
    print("Testing basic sigmoid:")
    for val in test_values:
        try:
            result = sigmoid(val)
            print(f"{val:>8}: {result}")
        except Exception as e:
            print(f"{val:>8}: ERROR - {e}")
    
    print("\nTesting safe sigmoid:")
    for val in test_values:
        try:
            result = safe_sigmoid(val)
            print(f"{val:>8}: {result}")
        except Exception as e:
            print(f"{val:>8}: ERROR - {e}")

if __name__ == "__main__":
    test_sigmoid_stability()