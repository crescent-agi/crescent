import numpy as np
from safe_activation_patch import SafeActivation

def test_activation_stress(func, extreme_values):
    """Test SafeActivation with extreme inputs across multiple functions."""
    for x in extreme_values:
        try:
            result = func(x)
            print(f"Input: {x:.2e}, Output: {result:.2e}")
        except Exception as e:
            print(f"Input: {x:.2e}, Error: {e}")

def main():
    print("=== SafeActivation Stress Test ===")
    
    # Create extreme test values
    extremes = [
        -1e10, -1e5, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 1e5, 1e10,
        np.nan, np.inf, -np.inf
    ]
    
    # Test SafeActivation with clipping
    print("\nTesting SafeActivation sigmoid:")
    safe_act = SafeActivation()
    test_activation_stress(safe_act.sigmoid, extremes)
    
    print("\nTesting SafeActivation tanh:")
    test_activation_stress(safe_act.tanh, extremes)
    
    print("\nTesting SafeActivation leaky_relu:")
    test_activation_stress(safe_act.leaky_relu, extremes)
    
    # Test raw sigmoid for comparison
    print("\nTesting raw sigmoid:")
    def raw_tanh(x):
        return 1 / (1 + np.exp(-x))
    test_activation_stress(raw_sigmoid, extremes)
    
    # Test other activation functions
    print("\nTesting tanh:")
    test_activation_stress(np.tanh, extremes)
    
    print("\nTesting ReLU:")
    test_activation_stress(lambda x: max(0, x), extremes)
    
    print("\nTesting Leaky ReLU:")
    test_activation_stress(lambda x: x if x > 0 else 0.01 * x, extremes)
    
    print("\n=== Stress Test Complete ===")

if __name__ == "__main__":
    main()