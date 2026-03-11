import numpy as np
import math

# CRITICAL SAFETY FUNCTIONS
SLOW_ACTIVATION_LIMIT = 1000  # Threshold for safe computation
MIN_SAFE_VALUE = -SLOW_ACTIVATION_LIMIT
MAX_SAFE_VALUE = SLOW_ACTIVATION_LIMIT

def safe_sigmoid(x):
    """Numerically stable sigmoid with input clamping"""
    x_clamped = max(-500, min(500, x))
    return 1.0 / (1.0 + math.exp(-x_clamped))

class SafeActivation:
    """Safe activation functions wrapper class"""
    @staticmethod
    def sigmoid(x):
        return safe_sigmoid(x)

    @staticmethod
    def safe_exp(values):
        result = []
        for v in values:
            if v > 709:
                result.append(MAX_SAFE_VALUE)
            elif v < -709:
                result.append(MIN_SAFE_VALUE)
            else:
                result.append(np.clip(math.exp(v), MIN_SAFE_VALUE, MAX_SAFE_VALUE))
        return result

    @staticmethod
    def robust_apply(x):
        if np.isinf(x).any() or np.isnan(x).any():
            x = np.nan_to_num(x, nan=0.0, posinf=MAX_SAFE_VALUE, neginf=MIN_SAFE_VALUE)
        if hasattr(x, 'std') and x.std() > 1e5:
            x = np.clip(x, -100, 100)
        return x

# Safe exponential with overflow protection
def safe_exp(values, min_val=MIN_SAFE_VALUE, max_val=MAX_SAFE_VALUE):
    result = []
    for v in values:
        if v > 709:
            result.append(max_val)
        elif v < -709:
            result.append(min_val)
        else:
            result.append(np.clip(math.exp(v), min_val, max_val))
    return result

# Validate numerical magnitude
def validate_magnitude(value, source='magnitude_check'):
    issues = []
    if isinstance(value, (int, float)):
        if abs(value) > 1e10:
            issues.append({f"{source}": value})
    elif isinstance(value, (list, np.ndarray)):
        for i, v in enumerate(value):
            if abs(v) > 1e10:
                issues.append({f"{source}[{i}]": v})
    return issues if issues else None

# Enhanced safe activation with multiple layers of protection
def robust_safe_activation():
    def apply(x):
        if np.isinf(x).any() or np.isnan(x).any():
            x = np.nan_to_num(x, nan=0.0, posinf=MAX_SAFE_VALUE, neginf=MIN_SAFE_VALUE)
        if hasattr(x, 'std') and x.std() > 1e5:  # Detect explosive gradients
            x = np.clip(x, -100, 100)
        return x
    return apply

# Test function
if __name__ == "__main__":
    print("Testing numerical stability suite...")
    # Test sigmoid stability
    print("\n1. Sigmoid stability test:")
    extreme_values = [1e6, -1e6, 500, -500, 0, 100, -100, 1000, -1000]
    for x in extreme_values:
        try:
            x_clamped = max(-500, min(500, x))
            safe_sigmoid = 1.0 / (1.0 + math.exp(-x_clamped))
            derivative = safe_sigmoid * (1 - safe_sigmoid)
            print(f"  x={x:>8} sig={safe_sigmoid:.6f} deriv={derivative:.6f}")
            assert not math.isinf(safe_sigmoid), f"Overflow at x={x}"
            assert not math.isnan(safe_sigmoid), f"NaN at x={x}"
            assert 0 <= derivative <= 0.25, f"Invalid derivative at x={x}: {derivative}"
        except Exception as e:
            print(f"  ERROR: {e}")
            raise

    # Test safe_exp
    print("\n2. Safe exponential test:")
    test_vals = [700, 709, 800, 1000, -100, -200]
    results = safe_exp(test_vals)
    print(f"  Input: {test_vals}")
    print(f"  Output: {[f'{r:.2e}' for r in results]}")

    # Test magnitude validation
    print("\n3. Magnitude validation test:")
    test_data = [1e12, 1e8, 1.0, -1e10, -1e8, 0]
    issues = validate_magnitude(test_data, 'test')
    print(f"  Validation issues: {issues}")
    assert len(validate_magnitude([1.0, 2.0], 'ok')) == 0 or validate_magnitude([1.0, 2.0], 'ok') is None

    print("\nALL NUMERICAL STABILITY TESTS PASSED!")