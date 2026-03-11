import numpy as np

SLOW_ACTIVATION_LIMIT = 1000  # Threshold for safe computation
MIN_SAFE_VALUE = -SLOW_ACTIVATION_LIMIT
MAX_SAFE_VALUE = SLOW_ACTIVATION_LIMIT

# Safe exponential with overflow protection
def safe_exp(values, min_val=MIN_SAFE_VALUE, max_val=MAX_SAFE_VALUE):
    """Apply safe exponential to each value with overflow/underflow checks"""
    return [np.clip(np.exp(v) if v <= 709 else max_val if v > 709 else min_val, min_val, max_val) for v in values]

# Validate numerical magnitude
def validate_magnitude(value, source='magnitude_check'):
    """Check if value is within safe numerical range"""
    if isinstance(value, (int, float)):
        if abs(value) > 1e10:
            return {f"{source}: {value:.2e}"}
    elif isinstance(value, (list, np.ndarray)):
        issues = [{f"{source}[{i}]": v:.2e} for i, v in enumerate(value) if abs(v) > 1e10]
        return issues if issues else None

# Enhanced safe activation with multiple layers of protection
def robust_safe_activation():
    """Primary safety wrapper with adaptive clipping"""
    def apply(x):
        """Apply safe activation with adaptive clipping"""
        if np.isinf(x).any() or np.isnan(x).any():
            x = np.nan_to_num(x, nan=0.0, posinf=MAX_SAFE_VALUE, neginf=MIN_SAFE_VALUE)
        if x.std() > 1e5:  # Detect explosive gradients
            x = np.clip(x, -100, 100)
        return x
    return apply