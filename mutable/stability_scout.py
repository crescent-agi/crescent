from safe_activation_fixed import SafeActivation
#!/usr/bin/env python3
"""
stability_scout.py - Hunts down numerical instability in the codebase.
Scans Python files for dangerous patterns: unbounded sigmoid, missing clamping,
derivative bugs, and unsafe activation calls.
"""

import os
import re
from pathlib import Path

def scan_file(filepath):
    """Scan a single file for stability red flags."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        return None

    # Skip this scanner itself
    if 'stability_scout.py' in str(filepath):
        return None

    issues = []
    lines = content.split('\n')

    # Check for unbounded sigmoid usage
    for i, line in enumerate(lines, 1):
        if 'sigmoid' in line.lower() and 'safe' not in line.lower():
            issues.append(f"Line {i}: unbounded sigmoid usage: {line.strip()}")
        if 'math.exp' in line and 'sigmoid' not in line.lower():
            issues.append(f"Line {i}: raw math.exp (possible overflow): {line.strip()}")
        if 'tanh' in line and 'safe' not in line.lower() and 'numpy' not in line.lower():
            issues.append(f"Line {i}: unbounded tanh (math.tanh): {line.strip()}")
        if 'derivative' in line.lower() and 'sigmoid_derivative' in line.lower():
            # Check if it's the buggy version that reapplies sigmoid
            if 'SafeActivation().sigmoid' in line:
                issues.append(f"Line {i}: BUGGY derivative - reapplies sigmoid: {line.strip()}")

    # Check for missing input clamping before activations
    for i, line in enumerate(lines, 1):
        if any(act in line for act in ['SafeActivation().tanh(', 'tanh(', 'relu(']):
            # Look for clamping in nearby lines
            has_clamp = any('clamp' in lines[max(0, j):min(len(lines), j+5)] or 'max(' in lines[max(0, j):min(len(lines), j+5)] for j in [i-3, i-2, i-1])
            if not has_clamp and 'safe' not in line.lower():
                issues.append(f"Line {i}: activation without obvious clamping: {line.strip()}")

    return issues if issues else None

def main():
    # Scan multiple critical directories
    scan_dirs = [
        '.',  # root python files
        'mutable_snapshot',
        'artifacts/agi_core_continuous_trained_gen42_final/cognitive',
        'artifacts/agi_core_continuous_trained_gen49_medium/cognitive'
    ]
    target_extensions = {'.py'}
    total_issues = 0
    file_issues = {}

    for scan_dir in scan_dirs:
        if not os.path.exists(scan_dir):
            continue
        for root, dirs, files in os.walk(scan_dir):
            # Skip __pycache__
            dirs[:] = [d for d in dirs if not d.startswith('__')]
            for file in files:
                if any(file.endswith(ext) for ext in target_extensions):
                    filepath = Path(root) / file
                    result = scan_file(filepath)
                    if result:
                        file_issues[str(filepath)] = result
                        total_issues += len(result)

    print(f"STABILITY SCOUT REPORT")
    print(f"Total issues found: {total_issues}")
    print(f"Files with problems: {len(file_issues)}")
    print("-" * 60)

    for filepath, issues in sorted(file_issues.items()):
        print(f"\n{filepath}:")
        for issue in issues:
            print(f"  {issue}")

    # Save report
    with open('stability_scout_report.txt', 'w') as f:
        f.write(f"Total issues: {total_issues}\n")
        f.write(f"Files affected: {len(file_issues)}\n\n")
        for filepath, issues in sorted(file_issues.items()):
            f.write(f"{filepath}:\n")
            for issue in issues:
                f.write(f"  {issue}\n")
            f.write("\n")

    print(f"\nReport saved to stability_scout_report.txt")

if __name__ == '__main__':
    main()