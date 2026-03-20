#!/usr/bin/env python3
import re

with open('train_continuous_new_fixed.py', 'r') as f:
    content = f.read()

# Replace exploration_rate=0.5 with 0.2
content = re.sub(r'exploration_rate=0\.5', 'exploration_rate=0.2', content)

with open('train_continuous_new_fixed.py', 'w') as f:
    f.write(content)

print("Updated exploration rate.")