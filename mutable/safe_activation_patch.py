# safe_activation_patch.py
# Patch to fix potential overflow in np.exp operations and add comprehensive numerical checks
import numpy as np
import sys
import os

def safe_exp(x, clip_val=10):
    """Safe exponential with clipping for overflow prevention"""
    try:
        x_clipped = np.clip(x, -clip_val, clip_val)
        return np.exp(x_clipped)
    except Exception as e:
        # Fallback: dense clipping if numerical issues persist
        x_clipped = np.clip(x, -50, 50)
        try:
            return np.exp(x_clipped)
        except Exception as e2:
            # Final fallback: linear approximation with damping
            return np.sign(x) * np.log(np.abs(x) + 1e-6) * 10

def safe_tanh(x, max_abs=10):
    """Safe tanh with overflow protection"""
    try:
        x_clipped = np.clip(x, -max_abs, max_abs)
        return np.tanh(x_clipped)
    except Exception:
        x_clipped = np.clip(x, -50, 50)
        return np.tanh(x_clipped)

def validate_magnitude(value, name="value"):
    """Comprehensive magnitude validation with detailed logging"""
    issues = []
    if np.isnan(value):
        issues.append(f"{name}: NaN detected")
    if np.isinf(value):
        issues.append(f"{name}: Inf detected")
    if abs(value) > 1e10:
        issues.append(f"{name}: Magnitude too large ({abs(value):.2e})")
    return issues

# Context manager for safe numerical operations
class safe_numeric_context:
    def __init__(self, context_name="numeric_operation"):
        self.context_name = context_name
        self.original_stderr = sys.stderr
        
    def __enter__(self):
        sys.stderr = open(os.devnull, 'w')
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stderr.close()
        sys.stderr = self.original_stderr
        return False

# Enhanced activation wrapper with comprehensive safety
class robust_safe_activation:
    def __init__(self):
        self.activation_count = 0
        self.overflow_log_path = "overflow_events.log"
        
    def apply(self, input_data):
        """Apply safe activation with comprehensive overflow checks"""
        self.activation_count += 1
        input_arr = np.asarray(input_data)
        
        # Validate magnitudes first
        magnitude_issues = []
        for i, val in enumerate(input_arr.flat):
            issues = validate_magnitude(val, f"{self.context_name}_input[{i}]")
            if issues:
                magnitude_issues.extend(issues)
                
        if magnitude_issues:
            # Log and potentially clip issues
            try:
                with open(self.overflow_log_path, "a") as f:
                    f.write(f"{self.activation_count}: {self.context_name} issues: {magnitude_issues}\n")
            except Exception:
                pass
            
            # Aggressive clipping as last resort
            input_arr = np.clip(input_arr, -50, 50)
        
        # Apply activation with safe fallbacks
        if self.activation_count % 100 == 0:
            # Every 100th activation gets extra validation
            with safe_numeric_context(self.context_name):
                input_arr = np.where(np.abs(input_arr) > 1e8, 0, input_arr)
            
        # Standard safe activation sequence
        activated = np.tanh(input_arr)
        
        # Check for residual issues after activation
        post_issues = []
        for i, val in enumerate(activated.flat):
            issues = validate_magnitude(val, f"{self.context_name}_output[{i}]")
            if issues:
                post_issues.extend(issues)
                
        if post_issues:
            try:
                with open(self.overflow_log_path, "a") as f:
                    f.write(f"{self.activation_count}: {self.context_name} post-issues: {post_issues}\n")
            except Exception:
                pass
                
        return activated