import sys
import os

# Read the corrupted file as binary
with open('new_reward_gen49.py', 'rb') as f:
    raw = f.read()
# Decode with unicode_escape to fix escaped backslashes
decoded = raw.decode('unicode_escape')
# Write back
with open('new_reward_gen49_fixed.py', 'w', encoding='utf-8') as f:
    f.write(decoded)
print("Fixed file saved as new_reward_gen49_fixed.py")
# Also replace original if you want
with open('new_reward_gen49.py', 'w', encoding='utf-8') as f:
    f.write(decoded)
print("Original file replaced.")