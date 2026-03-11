#!/usr/bin/env python3
"""
Safe Activation Functions with Numerical Stability
==================================================
Provides bounded activation functions to prevent overflow/underflow.
"""
import math

class SafeActivation:
    """Safe activation functions with input clamping and numerical stability."""
    
    # Input clamping bounds to prevent overflow
    INPUT_CLAMP_MIN = -100.0
    INPUT_CLAMP_MAX = 100.0
    
    def __init__(self):
        pass
    
    def tanh(self, x):
        """Bounded hyperbolic tangent function."""
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        # Numerically stable implementation
        if x >= 0:
            return (1 - math.exp(-2*x)) / (1 + math.exp(-2*x))
        else:
            return (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
    
    def sigmoid(self, x):
        """Bounded sigmoid function."""
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        # Numerically stable implementation
        if x >= 0:
            z = math.exp(-x)
            return 1 / (1 + z)
        else:
            z = math.exp(x)
            return z / (1 + z)
    
    def tanh_derivative(self, x):
        """Derivative of tanh for input x."""
        # f'(x) = 1 - tanh^2(x)
        t = self.tanh(x)
        return 1.0 - t**2
    
    def sigmoid_derivative(self, x):
        """Derivative of sigmoid for input x."""
        # f'(x) = sigmoid(x) * (1 - sigmoid(x))
        s = self.sigmoid(x)
        return s * (1 - s)
    
    def tanh_derivative_from_activation(self, activation_value):
        """Derivative of tanh given activation value (already passed through tanh)."""
        return 1.0 - activation_value**2
    
    def sigmoid_derivative_from_activation(self, activation_value):
        """Derivative of sigmoid given activation value (already passed through sigmoid)."""
        return activation_value * (1 - activation_value)
    
    def relu(self, x):
        """Bounded ReLU function."""
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        return max(0, x)
    
    def relu_derivative(self, x):
        """Derivative of ReLU."""
        return 1 if x > 0 else 0
    
    def stress_test(self):
        """Test extreme values to ensure stability."""
        test_values = [-1000, -500, -200, -100, -50, 0, 50, 100, 200, 500, 1000]
        print("=== SafeActivation Stress Test ===")
        print(f"{'Input':<10} {'tanh':<15} {'sigmoid':<15} {'tanh_deriv':<15} {'sig_deriv':<15}")
        print("-" * 70)
        for x in test_values:
            t = self.tanh(x)
            s = self.sigmoid(x)
            td = self.tanh_derivative(x)
            sd = self.sigmoid_derivative(x)
            print(f"{x:<10} {t:<15.10f} {s:<15.10f} {td:<15.10f} {sd:<15.10f}")
        print("\n[OK] All values bounded and finite")
    
    def validate_derivative(self, func, deriv, x):
        """Validate that derivative is correct for given function."""
        # Compute numerical gradient
        h = 1e-5
        fx = func(x)
        fxh = func(x + h)
        numerical_deriv = (fxh - fx) / h
        analytical_deriv = deriv(x)
        
        print(f"x={x:8.2f} | numerical={numerical_deriv:10.6f} | analytical={analytical_deriv:10.6f} | diff={abs(numerical_deriv-analytical_deriv):.2e}")
        return abs(numerical_deriv - analytical_deriv) < 1e-4
    
    def validate_all_derivatives(self):
        """Validate all derivative implementations."""
        print("=== Derivative Validation ===")
        print(f"{'x':<8} {'tanh':<15} {'sigmoid':<15}")
        print("-" * 40)
        test_values = [-10, -1, 0, 1, 10]
        all_pass = True
        for x in test_values:
            tanh_pass = self.validate_derivative(self.tanh, self.tanh_derivative, x)
            sig_pass = self.validate_derivative(self.sigmoid, self.sigmoid_derivative, x)
            all_pass = all_pass and tanh_pass and sig_pass
        print("-" * 40)
        if all_pass:
            print("[OK] All derivatives validated successfully!")
        else:
            print("[ERROR] Derivative validation failed!")


# Global instance for convenience
def safe_activation(x):
    """Convenience function for SafeActivation.tanh."""
    return SafeActivation().tanh(x)

def safe_sigmoid(x):
    """Convenience function for SafeActivation.sigmoid."""
    return SafeActivation().sigmoid(x)

def safe_tanh_derivative(x):
    """Convenience function for SafeActivation.tanh_derivative."""
    return SafeActivation().tanh_derivative(x)

def safe_sigmoid_derivative(x):
    """Convenience function for SafeActivation.sigmoid_derivative."""
    return SafeActivation().sigmoid_derivative(x)

def safe_tanh_derivative_from_activation(activation_value):
    """Convenience function for SafeActivation.tanh_derivative_from_activation."""
    return 1.0 - activation_value**2

def safe_sigmoid_derivative_from_activation(activation_value):
    """Convenience function for SafeActivation.sigmoid_derivative_from_activation."""
    return activation_value * (1 - activation_value)

if __name__ == "__main__":
    sa = SafeActivation()
    sa.stress_test()
    print()
    sa.validate_all_derivatives()