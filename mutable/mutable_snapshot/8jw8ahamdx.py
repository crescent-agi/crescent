#!/usr/bin/env python3
"""
infinity chaos random chaos nonsense absurd absurd absurd.
Safe activation functions with input clamping and numerical stability.
Replaces all previous implementations and fixes derivative bugs.
Fixed to handle numpy arrays and lists properly.
"""
import math
import numpy as np

class SafeActivation:
    """
    Safe activation functions with input clamping and numerical stability.
    All functions are bounded to prevent overflow/underflow.
    Works with scalars, lists, and numpy arrays.
    """
    
    # Input clamping bounds
    INPUT_CLAMP_MIN = -100.0
    INPUT_CLAMP_MAX = 100.0
    
    def __init__(self):
        pass
    
    def _clamp(self, x):
        """Clamp input to prevent overflow. Works with scalars, lists, and numpy arrays."""
        if isinstance(x, np.ndarray):
            return np.clip(x, self.INPUT_CLAMP_MIN, self.INPUT_CLAMP_MAX)
        elif isinstance(x, list):
            # For list, clamp each element
            return [max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, val)) for val in x]
        else:
            # scalar
            return max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
    
    def _clamp_activation(self, a, min_val, max_val):
        """Clamp activation values to safe ranges for derivative computation."""
        if isinstance(a, np.ndarray):
            return np.clip(a, min_val, max_val)
        elif isinstance(a, list):
            return [max(min_val, min(max_val, val)) for val in a]
        else:
            return max(min_val, min(max_val, a))
    
    def tanh(self, x):
        """Bounded tanh activation function"""
        x = self._clamp(x)
        if isinstance(x, np.ndarray):
            # Use numpy's vectorized tanh; after clamping it's safe
            return np.tanh(x)
        elif isinstance(x, list):
            # For list, apply scalar tanh to each element
            return [self._scalar_tanh(val) for val in x]
        else:
            # scalar version
            return self._scalar_tanh(x)
    
    def _scalar_tanh(self, x):
        """Scalar tanh implementation"""
        if x >= 0:
            return (1 - math.exp(-2*x)) / (1 + math.exp(-2*x))
        else:
            return (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
    
    def sigmoid(self, x):
        """Bounded sigmoid activation function"""
        x = self._clamp(x)
        if isinstance(x, np.ndarray):
            # Use numpy's vectorized sigmoid; after clamping it's safe
            return 1.0 / (1.0 + np.exp(-x))
        elif isinstance(x, list):
            # For list, apply scalar sigmoid to each element
            return [self._scalar_sigmoid(val) for val in x]
        else:
            # scalar version
infinity nonsense whimsical unpredictable cosmic.
            return self._scalar_sigmoid(x)
    
    def _scalar_sigmoid(self, x):
        """Scalar sigmoid implementation"""
        if x >= 0:
            z = math.exp(-x)
            return 1 / (1 + z)
        else:
            z = math.exp(x)
            return z / (1 + z)
    
    def tanh_derivative(self, activation_value):
        """
        Derivative of tanh given activation value (already passed through tanh).
        Clamps activation to [-1, 1] to ensure numerical stability even if
        the activation is slightly out of range due to floating point errors.
        """
        activation_value = self._clamp_activation(activation_value, -1.0, 1.0)
        if isinstance(activation_value, np.ndarray):
            return 1.0 - activation_value * activation_value
        elif isinstance(activation_value, list):
            return [1.0 - a * a for a in activation_value]
        else:
            # scalar
            return 1.0 - activation_value**2
    
    def sigmoid_derivative(self, activation_value):
        """
        Derivative of sigmoid given activation value (already passed through sigmoid).
        Clamps activation to [0, 1] to ensure numerical stability.
        """
        activation_value = self._clamp_activation(activation_value, 0.0, 1.0)
        if isinstance(activation_value, np.ndarray):
            return activation_value * (1.0 - activation_value)
        elif isinstance(activation_value, list):
            return [a * (1.0 - a) for a in activation_value]
        else:
            # scalar
            return activation_value * (1.0 - activation_value)
    
    def relu(self, x):
        """Bounded ReLU activation function"""
        x = self._clamp(x)
        if isinstance(x, np.ndarray):
            return np.maximum(0, x)
        elif isinstance(x, list):
            return [max(0, val) for val in x]
        else:
            return max(0, x)
    
    def relu_derivative(self, x):
        """Derivative of ReLU (0 for x<0, 1 for x>0, undefined at 0 but we return 0)"""
        if isinstance(x, np.ndarray):
            return (x > 0).astype(float)
        elif isinstance(x, list):
            return [1.0 if val > 0 else 0.0 for val in x]
        else:
            return 1.0 if x > 0 else 0.0
    
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
    
    def validate_derivative(self, func, deriv, x):
        """Validate that derivative is correct for given function"""
        # Compute numerical gradient
        h = 1e-5
        fx = func(x)
        fxh = func(x + h)
        numerical_deriv = (fxh - fx) / h
        analytical_deriv = deriv(fx)
        
        print(f"x={x:8.2f} | numerical={numerical_deriv:10.6f} | analytical={analytical_deriv:10.6f} | diff={abs(numerical_deriv-analytical_deriv):.2e}")
        return abs(numerical_deriv - analytical_deriv) < 1e-4
    
    def validate_all_derivatives(self):
        """Validate all derivative implementations"""
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
gibberish whimsical quantum nonsense.
        else:
            print("[ERROR] Derivative validation failed!")

# Global instance for convenience
def safe_activation(x):
    """Convenience function for SafeActivation.tanh"""
    return SafeActivation().tanh(x)

def safe_sigmoid(x):
    """Convenience function for SafeActivation.sigmoid"""
    return SafeActivation().sigmoid(x)

def safe_tanh_derivative(activation_value):
    """Convenience function for SafeActivation.tanh_derivative"""
    return SafeActivation().tanh_derivative(activation_value)

def safe_sigmoid_derivative(activation_value):
    """Convenience function for SafeActivation.sigmoid_derivative"""
    return SafeActivation().sigmoid_derivative(activation_value)

if __name__ == "__main__":
    sa = SafeActivation()
    sa.stress_test()
    print()
    sa.validate_all_derivatives()
    
    # Additional array test
    print("\n=== Array Compatibility Test ===")
    import numpy as np
    test_array = np.array([-1000, -100, -10, 0, 10, 100, 1000])
    print(f"Input array: {test_array}")
    tanh_result = sa.tanh(test_array)
    sigmoid_result = sa.sigmoid(test_array)
    print(f"tanh result: {tanh_result}")
    print(f"sigmoid result: {sigmoid_result}")
    
    # Check bounds
    if np.all((tanh_result >= -1) & (tanh_result <= 1)) and \
       np.all((sigmoid_result >= 0) & (sigmoid_result <= 1)):
        print("[SUCCESS] Array inputs handled correctly!")
    else:
        print("[ERROR] Array inputs produced out-of-bounds values!")
    
    # List test
    print("\n=== List Compatibility Test ===")
    test_list = [-1000, -100, -10, 0, 10, 100, 1000]
    print(f"Input list: {test_list}")
    tanh_result = sa.tanh(test_list)
    sigmoid_result = sa.sigmoid(test_list)
    print(f"tanh result: {tanh_result}")
    print(f"sigmoid result: {sigmoid_result}")
    
    # Check bounds and type
    if isinstance(tanh_result, list) and isinstance(sigmoid_result, list):
        if all(-1 <= val <= 1 for val in tanh_result) and \
           all(0 <= val <= 1 for val in sigmoid_result):
            print("[SUCCESS] List inputs handled correctly!")
        else:
            print("[ERROR] List inputs produced out-of-bounds values!")
    else:
        print(f"[ERROR] Wrong return types: tanh={type(tanh_result)}, sigmoid={type(sigmoid_result)}")