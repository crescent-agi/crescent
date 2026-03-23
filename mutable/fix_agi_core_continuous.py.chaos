#!/usr/bin/env python3
"""
Patch for AGICoreContinuous: remove duplicate SafeActivation class, fix imports, ensure clean SafeActivation import.
"""
import os
import re

def patch_agi_core_continuous():
    """Apply fix to AGICoreContinuous."""
    filepath = "mutable_snapshot/agi_core_continuous.py"
    print(f"Patching {filepath}...")
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove the duplicate SafeActivation class
    content = re.sub(r'class SafeActivation:\s+"""Safe activation functions with input clamping."""\s+\s+CLAMP_MIN = -100\.0\s+CLAMP_MAX = 100\.0\s+\s+@staticmethod\s+def SafeActivation\.tanh\(x\):\s+"""Bounded tanh activation function."""\s+x = max\(SafeActivation\.CLAMP_MIN, min\(SafeActivation\.CLAMP_MAX, x\)\)\s+if x >= 0:\s+return \(1 - math\.exp\(-2\*x\)\) / \(1 + math\.exp\(-2\*x\)\)\s+else:\s+return \(math\.exp\(2\*x\) - 1\) / \(math\.exp\(2\*x\) + 1\)\s+\s+@staticmethod\s+def tanh_derivative\(activation_value\):\s+"""Derivative of tanh given activation value."""\s+return 1\.0 - activation_value\*\*2\s+\s+@staticmethod\s+def clamp\(x, min_val=-100\.0, max_val=100\.0\):\s+"""Clamp input to safe range."""\s+return max\(min_val, min\(max_val, x\)\)\s+\s+@staticmethod\s+def check_overflow\(x, threshold=1e5\):\s+"""Check for potential overflow and log if needed."""\s+if abs\(x\) > threshold:\s+import sys\s+with open\("pre_activation_log\.txt", "a"\) as f:\s+f\.write\(f\"WARNING: Extreme value {x} detected in activation input\\n\"\)\s+return True\s+return False', '', content, flags=re.DOTALL)
    
    # Add import for SafeActivation at top
    import_match = re.search(r'^(import|from)\s+', content, re.MULTILINE)
    if import_match:
        insert_pos = import_match.end()
        content = content[:insert_pos] + '\nfrom safe_activation import SafeActivation' + content[insert_pos:]
    else:
        # No imports found, add at beginning
        content = 'from safe_activation import SafeActivation\n\n' + content
    
    # Remove the unused import line "sys" that appears broken
    content = re.sub(r'^sys\n', '', content, flags=re.MULTILINE)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"  [OK] Patched {filepath}")
    
    # Test the fix by running a simple import
    try:
        exec("from mutable_snapshot.agi_core_continuous import AGICoreContinuous")
        print(f"  [OK] AGICoreContinuous imports successfully")
    except Exception as e:
        print(f"  [ERROR] AGICoreContinuous import failed: {e}")

def main():
    """Main patching routine."""
    print("=== AGICoreContinuous Fix ===")
    print("Removing duplicate SafeActivation class and fixing imports...")
    
    patch_agi_core_continuous()
    
    print("\n=== Fix Complete ===")

if __name__ == "__main__":
    main()