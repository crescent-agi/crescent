#!/usr/bin/env python3
import sys
import os
import re
import ast
from pathlib import Path

def find_python_files(root_dir):
    """Find all Python files in workspace."""
    python_files = []
    for path in Path(root_dir).rglob('*.py'):
        python_files.append(str(path))
    return python_files

def extract_class_signature(filepath, class_name):
    """Extract __init__ signature from a class definition."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        # Parse the file to find the class definition
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                # Find the __init__ method
                for method in node.body:
                    if isinstance(method, ast.FunctionDef) and method.name == '__init__':
                        # Extract parameter names
                        params = [arg.arg for arg in method.args.args]
                        return params
        return []
    except Exception as e:
        return []

# Main execution
if __name__ == '__main__':
    workspace_dir = '/home/faris/crescent-agi/runs/gen-0006'
    python_files = find_python_files(workspace_dir)
    print(f'Found {len(python_files)} Python files')
    for file in python_files:
        # Extract class signatures
        signatures = extract_class_signature(file, 'AgentBrain')
        if signatures:
            print(f'{file}: {signatures}')
    # Analyze signatures for consistency
    # ... (additional analysis code would go here)
