#!/usr/bin/env python3
"""
Manual fix for AGICoreContinuous: remove duplicate SafeActivation class and fix imports.
"""
import os

def fix_agi_core_continuous():
    """Apply fix to AGICoreContinuous."""
    filepath = "mutable_snapshot/agi_core_continuous.py"
    print(f"Fixing {filepath}...")
    
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    # Remove the duplicate SafeActivation class (lines 5-38)
    # Find where the SafeActivation class ends
    new_lines = []
    in_safe_activation_class = False
    for line in lines:
        if "class SafeActivation:" in line:
            in_safe_activation_class = True
            continue
        if in_safe_activation_class and line.strip() == "":
            # Check if this is the end of the class (after the check_overflow method)
            # Look ahead to see if next non-empty line is "sys"
            continue
        if in_safe_activation_class and line.strip().startswith("sys"):
            in_safe_activation_class = False
            new_lines.append(line)  # keep the "sys" line
            continue
        if in_safe_activation_class:
            continue
        new_lines.append(line)
    
    # Now add the proper import at the top
    import_added = False
    final_lines = []
    for line in new_lines:
        if not import_added and (line.strip().startswith("import") or line.strip().startswith("from")):
            final_lines.append("from safe_activation import SafeActivation\n")
            import_added = True
        final_lines.append(line)
    
    # Write back
    with open(filepath, 'w') as f:
        f.writelines(final_lines)
    
    print(f"  [OK] Fixed {filepath}")
    
    # Test the fix
    try:
        exec("from mutable_snapshot.agi_core_continuous import AGICoreContinuous")
        print(f"  [OK] AGICoreContinuous imports successfully")
    except Exception as e:
        print(f"  [ERROR] AGICoreContinuous import failed: {e}")

def main():
    """Main fixing routine."""
    print("=== AGICoreContinuous Fix ===")
    print("Removing duplicate SafeActivation class and fixing imports...")
    
    fix_agi_core_continuous()
    
    print("\n=== Fix Complete ===")

if __name__ == "__main__":
    main()