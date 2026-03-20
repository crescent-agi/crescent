#!/usr/bin/env python3
import re

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'exploration_rate=0.2' in line:
        # Replace exploration_rate=0.2 with exploration_rate=0.3
        new_line = line.replace('exploration_rate=0.2', 'exploration_rate=0.3')
        # Also replace epsilon_decay=0.995 with epsilon_decay=0.99
        new_line = new_line.replace('epsilon_decay=0.995', 'epsilon_decay=0.99')
        # epsilon_min=0.01 -> epsilon_min=0.05
        new_line = new_line.replace('epsilon_min=0.01', 'epsilon_min=0.05')
        lines[i] = new_line
        print(f"Updated line {i+1}: {new_line.strip()}")
        break

with open('agent_brain.py', 'w') as f:
    f.writelines(lines)
print("Exploration parameters updated.")