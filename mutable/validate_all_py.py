import os
import re

# Script to validate Python files in the workspace
# Focus on AgentBrain signature validation

def check_agent_brain_signature(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # Look for AgentBrain class definition
            agent_brain_match = re.search(r'class\s+AgentBrain(?:\s*.*)?\s*:', content)
            if agent_brain_match:
                # Check for __init__ method parameters
                init_match = re.search(r'__init__\s*\((.*?)\)', content)
                params = init_match.group(1) if init_match else ''
                print(f'Found AgentBrain in {file_path}. Parameters: {params}')
        return True
    except Exception as e:
        print(f'Error processing {file_path}: {str(e)}')
        return False

def validate_all_py():
    directory = '.'
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and file != 'validate_all_py.py':
                check_file = os.path.join(root, file)
                check_agent_brain_signature(check_file)

if __name__ == '__main__':
    print('=== Validating Python files for AgentBrain signature ===')
    validate_all_py()
    print('=== Validation complete ===')

print('Creating validate_all_py.py to validate workspace Python files')
with open('mutable_snapshot/validate_all_py.py', 'w') as f:
    f.write('import os\nimport re\n\ndef check_agent_brain_signature(file_path):\n    try:\n        with open(file_path, \'r\') as f:\n            content = f.read()\n            \# Look for AgentBrain class definition\n            agent_brain_match = re.search(r\'class\s+AgentBrain(?:\s*.*)?\s*:', content)\n            if agent_brain_match:\n                \# Check for __init__ method parameters\n                init_match = re.search(r\'__init__\s*\((.*?)\)', content)\n                params = init_match.group(1) if init_match else \'\'\n                print(f\'Found AgentBrain in {file_path}. Parameters: {params}\')
        return True
    except Exception as e:\n        print(f\'Error processing {file_path}: {str(e)}\')
        return False\n\ndef validate_all_py():\n    directory = \'.\'
    for root, dirs, files in os.walk(directory):\n        for file in files:\n            if file.endswith(\'.py\') and file != \'validate_all_py.py\':\n                check_file = os.path.join(root, file)\n                check_agent_brain_signature(check_file)\n\nif __name__ == \'__main__\':\n    print(\'=== Validating Python files for AgentBrain signature ===\')\n    validate_all_py()\n    print(\'=== Validation complete ===\')\n\nprint(\'validate_all_py.py created successfully\')')