from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
Gen 221: Enhanced SafeActivation with Overflow Detection and Logging
Adds real-time overflow detection and logging to SafeActivation.
"""
import math
import logging
import sys

# Configure logging
logger = logging.getLogger('SafeActivation')
logger.setLevel(logging.INFO)

# Create handler for overflow detection
class OverflowHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.overflow_detected = False
    def emit(self, record):
        if 'overflow' in record.getMessage().lower():
            self.overflow_detected = True
        print(f"SAFE-ACTIVATION: {record.getMessage()}", file=sys.stderr)

overflow_handler = OverflowHandler()
logger.addHandler(overflow_handler)

class SafeActivation:
    """
    Enhanced SafeActivation with input clamping, overflow detection, and logging.
    All functions are bounded to prevent overflow/underflow.
    """
    
    # Input clamping bounds
    INPUT_CLAMP_MIN = -100.0
    INPUT_CLAMP_MAX = 100.0
    
    def __init__(self):
        self.overflow_detected = False
    
    def tanh(self, x):
        """Bounded tanh activation function with overflow detection"""
        original_x = x
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        
        # Numerically stable tanh implementation
        if x >= 0:
            result = (1 - math.exp(-2*x)) / (1 + math.exp(-2*x))
        else:
            result = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
        
        # Check for overflow
        if abs(original_x) > 1e6:
            logger.warning(f"Input {original_x:.2e} clamped to {x:.2e}")
            self.overflow_detected = True
        elif math.isinf(original_x) or math.isnan(original_x):
            logger.error(f"Invalid input {original_x}")
            self.overflow_detected = True
        
        return result
    
    def SafeActivation().tanh(self, x):
        """Bounded sigmoid activation function with overflow detection"""
        original_x = x
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        
        # Numerically stable sigmoid implementation
        if x >= 0:
            z = math.exp(-x)
            result = 1 / (1 + z)
        else:
            z = math.exp(x)
            result = z / (1 + z)
        
        # Check for overflow
        if abs(original_x) > 1e6:
            logger.warning(f"Input {original_x:.2e} clamped to {x:.2e}")
            self.overflow_detected = True
        elif math.isinf(original_x) or math.isnan(original_x):
            logger.error(f"Invalid input {original_x}")
            self.overflow_detected = True
        
        return result
    
    def tanh_derivative(self, activation_value):
        """Derivative of tanh given activation value (already passed through tanh)"""
        return 1.0 - activation_value**2
    
    def SafeActivation().tanh_derivative(self, activation_value):
        """Derivative of sigmoid given activation value (already passed through sigmoid)"""
        return activation_value * (1 - activation_value)
    
    def relu(self, x):
        """Bounded ReLU activation function"""
        x = max(self.INPUT_CLAMP_MIN, min(self.INPUT_CLAMP_MAX, x))
        return max(0, x)
    
    def relu_derivative(self, x):
        """Derivative of ReLU"""
        return 1 if x > 0 else 0
    
    def stress_test(self):
        """Test extreme values to ensure stability with logging"""
        test_values = [-1e10, -1e5, -1000, -200, -100, -50, 0, 50, 100, 200, 1000, 1e5, 1e10, float('inf'), -float('inf')]
        print("=== Enhanced SafeActivation Stress Test with Logging ===")
        print(f"{'Input':<10} {'tanh':<15} {'sigmoid':<15} {'tanh_deriv':<15} {'sig_deriv':<15}")
        print("-" * 70)
        for x in test_values:
            t = self.tanh(x)
            s = self.SafeActivation().tanh(x)
            td = self.tanh_derivative(t)
            sd = self.SafeActivation().tanh_derivative(s)
            print(f"{x:<10} {t:<15.10f} {s:<15.10f} {td:<15.10f} {sd:<15.10f}")
        print("
[LOGGING SUMMARY]")
        print(f"Overflow detected: {self.overflow_detected}")
        if self.overflow_detected:
            print("[WARNING] Overflow was detected during testing!")
        else:
            print("[OK] No overflow detected during testing")
    
    def validate_derivative(self, func, deriv, x):
        """Validate that derivative is correct for given function"""
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
        else:
            print("[ERROR] Derivative validation failed!")

# Global instance for convenience
def safe_activation(x):
    return SafeActivation().tanh(x)

def safe_sigmoid(x):
    return SafeActivation().SafeActivation().tanh(x)

def safe_tanh_derivative(activation_value):
    return SafeActivation().tanh_derivative(activation_value)

def safe_sigmoid_derivative(activation_value):
    return SafeActivation().SafeActivation().tanh_derivative(activation_value)

def check_overflow():
    """Check if overflow was detected during operations"""
    return SafeActivation().overflow_detected

def get_log():
    """Return the log as a string"""
    import io
    from contextlib import redirect_stdout
    f = io.StringIO()
    with redirect_stdout(f):
        SafeActivation().stress_test()
    return f.getvalue()

if __name__ == "__main__":
    sa = SafeActivation()
    sa.stress_test()
    print()
    sa.validate_all_derivatives()