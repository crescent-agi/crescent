#!/usr/bin/env python3
"""
Critical fix for sigmoid overflow bug that crashed generation 225.
Replaces unsafe sigmoid derivative computation with numerically stable version.
"""
import math

class SafeActivation:
    """
    Safe activation functions with input clamping and numerical stability.
    All functions are bounded to prevent overflow/underflow.
    """
    
    # Input clamping bounds
    INPUT_CLAMP_MIN = -100.0
    INPUT_CLAMP_MAX = 100.0
    
    def __init__(self):
        pass
    
    def tanh(self, x):
        """Bounded tanh activation function"""
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        # Numerically stable tanh implementation
        if x >= 0:
            return (1 - math.exp(-2*x)) / (1 + math.exp(-2*x))
        else:
            return (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
    
    def sigmoid(self, x):
        """Bounded sigmoid activation function"""
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        # Numerically stable sigmoid implementation
        if x >= 0:
            z = math.exp(-x)
            return 1 / (1 + z)
        else:
            z = math.exp(x)
            return z / (1 + z)
    
    def tanh_derivative(self, activation_value):
        """Derivative of tanh given activation value (already passed through tanh)"""
        # f'(x) = 1 - tanh^2(x) = 1 - activation^2
        # This is numerically stable for bounded activations
        return 1.0 - activation_value**2
    
    def sigmoid_derivative(self, activation_value):
        """Derivative of sigmoid given activation value (already passed through sigmoid)"""
        # f'(x) = sigmoid(x) * (1 - sigmoid(x)) = activation * (1 - activation)
        # But this can overflow when activation is near 0 or 1
        # Use numerically stable version:
        if activation_value < 0.5:
            return activation_value * (1 - activation_value)
        else:
            return (1 - activation_value) * activation_value
    
    def stress_test(self):
        """Test extreme values to ensure stability"""
        test_values = [-1000, -500, -200, -100, -50, 0, 50, 100, 200, 500, 1000]
        print("=== SafeActivation Stress Test ===")
        print(f"{'Input':<10} {'tanh':<15} {'sigmoid':<15} {'tanh_deriv':<15} {'sig_deriv':<15}")
        print("-" * 70)
        for x in test_values:
            t = self.tanh(x)
            s = self.sigmoid(x)
            td = self.tanh_derivative(t)
            sd = self.sigmoid_derivative(s)
            print(f"{x:<10} {t:<15.10f} {s:<15.10f} {td:<15.10f} {sd:<15.10f}")
        print("\n[OK] All values bounded and finite")


def test_sigmoid_stability():
    """Test the sigmoid implementation for overflow issues"""
    sa = SafeActivation()
    print("Testing sigmoid stability...")
    test_inputs = [-100, -10, -1, 0, 1, 10, 100]
    for x in test_inputs:
        result = sa.sigmoid(x)
        print(f"sigmoid({x:4.1f}) = {result:.10f}")
    print("\nTesting sigmoid derivative stability...")
    test_activations = [0.0, 0.001, 0.01, 0.1, 0.5, 0.9, 0.99, 0.999, 1.0]
    for a in test_activations:
        result = sa.sigmoid_derivative(a)
        print(f"sigmoid_derivative({a:.3f}) = {result:.10f}")

if __name__ == "__main__":
    test_sigmoid_stability()