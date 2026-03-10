#!/usr/bin/env python3
"""
Patch neural_q_continuous_double choose_action to allow death during exploration.
"""
import re

with open('neural_q_continuous_double.py', 'r') as f:
    content = f.read()

# Find choose_action method
pattern = r'(\\s+def choose_action\\(self, state_vector\\):.*?)(?=\\n\\s+def|\\n\\s+class|\\Z)'
match = re.search(pattern, content, re.DOTALL)
if not match:
    print("choose_action method not found")
    sys.exit(1)

old_method = match.group(1)
print("Found choose_action method, length:", len(old_method))

# Replace the random exploration block
lines = old_method.split('\\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if 'if random.random() < self.epsilon:' in line:
        # Keep the epsilon check line
        new_lines.append(line)
        i += 1
        # Find the block inside
        # Determine indentation of block
        indent = len(line) - len(line.lstrip())
        indent_str = ' ' * indent
        # Replace the next lines up to the else block
        # We'll replace the whole block with our own
        # Remove existing lines until we reach the 'else:' line at same indentation
        while i < len(lines) and (lines[i].strip() == '' or len(lines[i]) - len(lines[i].lstrip()) > indent):
            i += 1
        # Now we are at the line with same indent as 'if' that is not part of the block
        # That line should be 'else:'.
        # We'll reconstruct the block.
        new_lines.append(indent_str + '    # Random exploration: allow death (no filtering)')
        new_lines.append(indent_str + '    return random.randrange(self.action_size)')
        # Keep the else block as is, we will add later
        # Need to capture the else block and re-add.
        # Let's collect the rest of the method after else
        else_block = []
        while i < len(lines):
            else_block.append(lines[i])
            i += 1
        # Insert else block
        new_lines.extend(else_block)
        break
    else:
        new_lines.append(line)
        i += 1

if len(new_lines) == len(lines):
    print("Did not find epsilon line, maybe method already patched?")
    # fallback: replace whole method with patched version
    # Let's craft new method
    new_method = '''
    def choose_action(self, state_vector):
        """
        Epsilon-greedy action selection.
        state_vector: list of floats (length feature_dim)
        """
        if random.random() < self.epsilon:
            # Random exploration: allow death (no filtering)
            return random.randrange(self.action_size)
        else:
            q_values = self.nn.predict(state_vector)
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            if len(best_actions) > 1 and 6 in best_actions:
                best_actions.remove(6)
            if best_actions == [6]:
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actions)
'''
    # Determine indentation
    first_line = old_method.split('\\n')[0]
    indent = len(first_line) - len(first_line.lstrip())
    indent_str = ' ' * indent
    lines_new = new_method.strip().split('\\n')
    indented = [indent_str + line if line.strip() else '' for line in lines_new]
    new_method_indented = '\\n'.join(indented)
    content = content.replace(old_method, new_method_indented)
else:
    new_method = '\\n'.join(new_lines)
    # Ensure we haven't messed up indentation
    # Replace old method with new method
    content = content.replace(old_method, new_method)

with open('neural_q_continuous_double.py', 'w') as f:
    f.write(content)

print("Patched choose_action to allow death during exploration.")