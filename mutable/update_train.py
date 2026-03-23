#!/usr/bin/env python3
import re

with open('mutable_snapshot/train_continuous_new_fixed.py', 'r') as f:
    content = f.read()

# Replace exploration_rate=0.3, epsilon_decay=0.95
new_content = re.sub(r'exploration_rate=0\.3, epsilon_decay=0\.95', 'exploration_rate=0.2, epsilon_decay=0.9', content)
# Also replace epsilon_decay maybe elsewhere? Not needed.

with open('mutable_snapshot/train_continuous_new_fixed.py', 'w') as f:
    f.write(new_content)
print("Updated train script exploration parameters.")