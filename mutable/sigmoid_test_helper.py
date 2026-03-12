# Helper script for sigmoid stability testing
import numpy as np

def test_sigmoid_stability(x_min, x_max, num_samples=1000):
    """Test sigmoid stability across extreme input range"""
    xs = np.linspace(x_min, x_max, num_samples)
    results = []
    for x in xs:
        try:
            result = 1 / (1 + np.exp(-x))
            results.append(result)
        except Exception as e:
            results.append(f"Error: {e}")
    return results

# Test with extreme values
test_sigmoid_stability(-1000, 1000)