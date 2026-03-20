import os
import re

def find_agentbrain_files():
    files = []
    for root, dirs, filenames in os.walk('.'):
        for f in filenames:
            if f.startswith('agent_brain.py'):
                files.append(os.path.join(root, f))
    return files

def extract_init_signature(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
        # Look for __init__ method
        match = re.search(r'def __init__\s*\([^)]*\)', content)
        if match:
            return match.group(0)
        return None
    except Exception as e:
        return None

# Test the function
if __name__ == '__main__':
    agentbrain_files = find_agentbrain_files()
    for f in agentbrain_files:
        sig = extract_init_signature(f)
        if sig:
            print(f"Found {f}: {sig}")
        else:
            print(f"No __init__ found in {f}")