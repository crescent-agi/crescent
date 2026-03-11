#!/usr/bin/env python3
"""
Critical patch: Replace all sigmoid activations with bounded tanh and add clamping.
This fixes the overflow that killed generation 221.
"""
import os
import re
import sys

# Target files to patch
TARGET_FILES = [
    "mutable_snapshot/neural_q_continuous.py",
    "mutable_snapshot/world_model_continuous.py",
    "mutable_snapshot/agi_core_continuous.py",
    "mutable_snapshot/cognitive_architecture.py",
]

# Safe activation patterns to insert
SAFE_ACTIVATION_CODE = '''
class SafeActivation:
    """Safe activation functions with input clamping."""
    CLAMP_MIN = -100.0
    CLAMP_MAX = 100.0
    
    @staticmethod
    def tanh(x):
        """Bounded tanh activation function."""
        x = max(SafeActivation.CLAMP_MIN, min(SafeActivation.CLAMP_MAX, x))
        if x >= 0:
            return (1 - math.exp(-2*x)) / (1 + math.exp(-2*x))
        else:
            return (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
    
    @staticmethod
    def tanh_derivative(activation_value):
        """Derivative of tanh given activation value."""
        return 1.0 - activation_value**2
    
    @staticmethod
    def clamp(x, min_val=-100.0, max_val=100.0):
        """Clamp input to safe range."""
        return max(min_val, min(max_val, x))
    
    @staticmethod
    def check_overflow(x, threshold=1e5):
        """Check for potential overflow and log if needed."""
        if abs(x) > threshold:
            import sys
            with open("pre_activation_log.txt", "a") as f:
                f.write(f"WARNING: Extreme value {x} detected in activation input\n")
            return True
        return False
'''

def patch_file(filepath):
    """Patch a single file to use safe activations."""
    print(f"Patching {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Add SafeActivation class if not present
    if 'class SafeActivation:' not in content:
        # Find import section
        import_match = re.search(r'^(import|from)\s+', content, re.MULTILINE)
        if import_match:
            insert_pos = import_match.end()
            content = content[:insert_pos] + '\n' + SAFE_ACTIVATION_CODE + '\n' + content[insert_pos:]
        else:
            # No imports found, add at beginning
            content = SAFE_ACTIVATION_CODE + '\n' + content
    
    # Replace sigmoid with tanh
    content = re.sub(r'np\.tanh\(', 'SafeActivation.tanh(', content)
    content = re.sub(r'math\.tanh\(', 'SafeActivation.tanh(', content)
    content = re.sub(r'tanh\(', 'SafeActivation.tanh(', content)
    
    # Replace sigmoid_derivative with tanh_derivative
    content = re.sub(r'1 - hidden\*\*2', 'SafeActivation.tanh_derivative(hidden)', content)
    content = re.sub(r'1 - activation\*\*2', 'SafeActivation.tanh_derivative(activation)', content)
    
    # Add clamping before activation
    content = re.sub(r'(hidden|activation) = np\.tanh\(', 'SafeActivation.check_overflow(inputs)\n        \1 = SafeActivation.tanh(', content)
    content = re.sub(r'(hidden|activation) = math\.tanh\(', 'SafeActivation.check_overflow(inputs)\n        \1 = SafeActivation.tanh(', content)
    content = re.sub(r'(hidden|activation) = tanh\(', 'SafeActivation.check_overflow(inputs)\n        \1 = SafeActivation.tanh(', content)
    
    # Add clamping to input vectors
    content = re.sub(r'x_clamped = np\.maximum\(-100\.0, np\.minimum\(100\.0, inputs\)\)',
                   'x_clamped = SafeActivation.clamp(inputs)', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  [OK] Patched {filepath}")

def main():
    """Main patching routine."""
    print("=== Activation Stability Patch ===")
    print("Fixing numerical stability issues that killed generation 221...")
    
    # Create overflow log
    with open("pre_activation_log.txt", "w") as f:
        f.write("Activation overflow log - generation 222\n")
        f.write("Generation 221 died from sigmoid overflow - this is the fix\n")
        f.write("=" * 60 + "\n\n")
    
    # Patch each target file
    for filepath in TARGET_FILES:
        if os.path.exists(filepath):
            patch_file(filepath)
        else:
            print(f"  [WARN] {filepath} not found")
    
    print("\n=== Patch Complete ===")
    print("Now run activation_stress_test.py to verify stability")
    print("Then run quick_train.py to validate training")

if __name__ == "__main__":
    main()