#!/usr/bin/env python3
import sys

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Delete lines 411-419 (0-index 410-418)
del lines[410:419]

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Removed problematic bonus block')