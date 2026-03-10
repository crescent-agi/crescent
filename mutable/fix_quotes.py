import sys

with open('agi_core_continuous.py', 'r') as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i]
    # Check if line contains an odd number of double quotes (excluding escaped quotes)
    # Simple detection: count quotes, ignoring escaped quotes? We'll just merge if line ends with unclosed quote
    if line.count('"') % 2 == 1:
        # Look ahead for the closing quote
        j = i + 1
        merged = line.rstrip('\n')
        while j < len(lines):
            merged += ' ' + lines[j].rstrip('\n')
            if lines[j].count('"') % 2 == 1:
                # closing quote found
                break
            j += 1
        # Replace lines i..j with merged line
        lines[i] = merged + '\n'
        for k in range(i+1, j+1):
            lines[k] = ''
        i = j
    else:
        i += 1

# Remove empty lines
lines = [line for line in lines if line.strip() != '']

with open('agi_core_continuous.py', 'w') as f:
    f.writelines(lines)
print("Fixed quotes.")