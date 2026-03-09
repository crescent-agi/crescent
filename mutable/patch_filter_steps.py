#!/usr/bin/env python3
import sys
import re

with open('agi_core_continuous.py', 'r') as f:
    content = f.read()

# Replace step count threshold from 20 to 100
content = content.replace('if self.step_count < 20 and action_idx == 6:',
                          'if self.step_count < 100 and action_idx == 6:')

with open('agi_core_continuous.py', 'w') as f:
    f.write(content)

print('Filter steps updated to 100.')