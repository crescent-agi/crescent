#!/usr/bin/env python3
"""
Critical patch: Fix sigmoid overflow by replacing math.exp() with bounded SafeActivation.
This prevents the exact bug that killed generation 221.
"""
import os
import re

# Target files to patch
TARGET_FILES = [
    "mutable_snapshot/neural_q.py",
    "mutable_snapshot/neural_q_continuous.py",
    "mutable_snapshot/cognitive_architecture.py",
    "mutable_snapshot/agi_core_continuous.py",
]

# Safe activation patterns to insert
SAFE_ACTIVATION_IMPORT = '''
from safe_activation_fixed import SafeActivation
'''

SAFE_ACTIVATION_METHODS = '''
    def tanh(self, x):
        """Use SafeActivation to prevent overflow"""
        return SafeActivation().tanh(x)
    
    def tanh_derivative(self, activation_value):
        """Safe derivative of tanh"""
        return 1.0 - activation_value**2
'''

def patch_file(filepath):
    """Patch a single file to use safe activations."""
    print(f"Patching {filepath}...")
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Add SafeActivation import if not present
    if 'from safe_activation_fixed import SafeActivation' not in content:
        # Find import section
        import_match = re.search(r'^(import|from)\s+', content, re.MULTILINE)
        if import_match:
            insert_pos = import_match.end()
            content = content[:insert_pos] + '\n' + SAFE_ACTIVATION_IMPORT + '\n' + content[insert_pos:]
        else:
            # No imports found, add at beginning
            content = SAFE_ACTIVATION_IMPORT + '\n' + content
    
    # Replace unsafe tanh with safe version
    content = re.sub(r'def tanh\(self, x\):\s*\n\s*"""Bounded tanh activation function"""\s*\n\s*x = max\(SafeActivation\.CLAMP_MIN, min\(SafeActivation\.CLAMP_MAX, x\)\)\s*\n\s*if x >= 0:\s*\n\s*return \(1 - math\.exp\(-2\*x\)\) / \(1 + math\.exp\(-2\*x\)\)\s*\n\s*else:\s*\n\s*return \(math\.exp\(2\*x\) - 1\) / \(math\.exp\(2\*x\) + 1\)\s*\n',
                   SAFE_ACTIVATION_METHODS, content)
    
    # Replace unsafe derivative with safe version
    content = re.sub(r'def tanh_derivative\(self, activation_value\):\s*\n\s*"""Derivative of tanh given activation value\(already passed through tanh\)"""\s*\n\s*return 1\.0 - activation_value\*\*2\s*\n',
                   SAFE_ACTIVATION_METHODS, content)
    
    # Replace direct math.exp() calls with SafeActivation
    content = re.sub(r'math\.exp\(-2\*x\)', 'SafeActivation().tanh(x)', content)
    content = re.sub(r'math\.exp\(2\*x\)', 'SafeActivation().tanh(x)', content)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  [OK] Patched {filepath}")

def main():
    """Main patching routine."""
    print("=== Sigmoid Overflow Fix ===")
    print("Fixing numerical stability issues that killed generation 221...")
    
    # Patch each target file
    for filepath in TARGET_FILES:
        if os.path.exists(filepath):
            patch_file(filepath)
        else:
            print(f"  [WARN] {filepath} not found")
    
    print("\n=== Patch Complete ===")
    print("Run sigmoid_stability_test.py to verify stability")
    print("Then run quick_train.py to validate training")

if __name__ == "__main__":
    main()