import sys

# Tiny helper to check if we're alive
print(f'Generation {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} agent is awake')

# Start by modifying our own brain
print('Modifying agent_brain.py to add a debug flag')
with open('mutable_snapshot/agent_brain.py.backup_final', 'r') as f:
    content = f.read()
content = content.replace('DEBUG_MODE = False', 'DEBUG_MODE = True')
with open('mutable_snapshot/agent_brain.py.backup_final', 'w') as f:
    f.write(content