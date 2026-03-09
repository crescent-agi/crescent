#!/usr/bin/env python3
"""
Patch neural_q_continuous choose_action to filter declare_death during random exploration.
"""
import sys

path = 'neural_q_continuous.py'
with open(path, 'r') as f:
    lines = f.readlines()

# Find choose_action method
start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def choose_action(self, state_vector):'):
        start = i
        break
if start is None:
    print('choose_action method not found')
    sys.exit(1)

# Find end of method (next line with same indentation that starts with 'def ' or end of file)
indent = len(lines[start]) - len(lines[start].lstrip())
end = None
for i in range(start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if len(lines[i]) - len(lines[i].lstrip()) == indent and lines[i].lstrip().startswith('def '):
        end = i
        break
if end is None:
    end = len(lines)

print(f'choose_action lines {start+1} to {end}')

# Replace the method body
# We'll keep the signature and docstring, but replace the body.
# Let's construct new method lines.
new_method_lines = []
new_method_lines.append('    def choose_action(self, state_vector):\n')
new_method_lines.append('        """\n')
new_method_lines.append('        Epsilon-greedy action selection.\n')
new_method_lines.append('        state_vector: list of floats (length feature_dim)\n')
new_method_lines.append('        """\n')
new_method_lines.append('        if random.random() < self.epsilon:\n')
new_method_lines.append('            # Random exploration: filter out declare_death (index 6) to avoid early suicide\n')
new_method_lines.append('            for _ in range(10):  # try up to 10 times\n')
new_method_lines.append('                action = random.randrange(self.action_size)\n')
new_method_lines.append('                if action != 6:  # declare_death index\n')
new_method_lines.append('                    return action\n')
new_method_lines.append('            # If after 10 tries still declare_death, return it (should be rare)\n')
new_method_lines.append('            return 6\n')
new_method_lines.append('        else:\n')
new_method_lines.append('            q_values = self.nn.predict(state_vector)\n')
new_method_lines.append('            max_q = max(q_values)\n')
new_method_lines.append('            best_actions = [i for i, q in enumerate(q_values) if q == max_q]\n')
new_method_lines.append('            return random.choice(best_actions)\n')

# Replace the slice
lines[start:end] = new_method_lines

with open(path, 'w') as f:
    f.writelines(lines)

print('choose_action patched to filter declare_death.')

# Also patch AGICoreContinuous decide_action random fallback (though unlikely used)
path2 = 'agi_core_continuous.py'
with open(path2, 'r') as f:
    lines2 = f.readlines()

# Find the random fallback line (approx line "action_idx = random.randrange(self.action_size)")
for i, line in enumerate(lines2):
    if 'action_idx = random.randrange(self.action_size)' in line:
        # Insert a check before that line
        indent = len(line) - len(line.lstrip())
        new_line = ' ' * indent + '# Filter declare_death during random fallback\n'
        new_line2 = ' ' * indent + 'for _ in range(10):\n'
        new_line3 = ' ' * indent + '    action_idx = random.randrange(self.action_size)\n'
        new_line4 = ' ' * indent + '    if action_idx != 6:  # declare_death\n'
        new_line5 = ' ' * indent + '        break\n'
        lines2[i] = new_line + new_line2 + new_line3 + new_line4 + new_line5
        print(f'Patched random fallback at line {i+1}')
        break

with open(path2, 'w') as f:
    f.writelines(lines2)

print('AGICoreContinuous random fallback patched.')