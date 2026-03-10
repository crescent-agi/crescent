#!/usr/bin/env python3
"""
Apply patches from generation 27:
1. Weight clipping in NeuralNetwork.backward (for both single and double)
2. Mask non-productive tools during exploration in choose_action.
"""
import sys
import os

# 1. Weight clipping for neural_q_continuous.py (single network)
print("=== Patching neural_q_continuous.py ===")
with open('neural_q_continuous.py', 'r') as f:
    content = f.read()

# Find backward method
lines = content.split('\n')
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    new_lines.append(line)
    if line.strip() == 'def backward(self, inputs, hidden, output, target):':
        # Find the end of the method (next def or class at same indentation)
        # We'll insert clipping after weight updates.
        # Let's find the line after bias updates.
        # We'll just add clipping at the end of the method before return.
        # But there's no explicit return, so we need to insert before dedent.
        # Simpler: we can replace the whole method with patched version.
        # Instead, we'll just insert after hidden layer updates.
        # Let's do a simple search for the line 'self.b1[j] -= self.lr * hidden_error[j]'
        # and add clipping after that block.
        # Actually we'll just add a call to a helper weight_clipping method.
        # Let's add weight_clipping method and call it at the end of backward.
        # Let's do a more robust approach: find the end of the method.
        pass
    i += 1

# For simplicity, we'll run the existing patch_weight_clipping script
sys.path.insert(0, '.')
exec(open('patch_weight_clipping.py').read())
print("Weight clipping applied to single network.")

# 2. Patch neural_q_continuous_double NeuralNetwork.backward as well
print("=== Patching neural_q_continuous_double.py ===")
with open('neural_q_continuous_double.py', 'r') as f:
    content = f.read()

# We'll add weight clipping inside backward method (or ensure weight_clipping is called)
# The double already has weight_clipping method and calls it in learn.
# Let's also add clipping inside backward for safety.
# We'll replace backward method with version that clips after each weight update.
# Let's locate the NeuralNetwork class inside double file.
# Since there are two NeuralNetwork classes? Actually only one.
# We'll search for 'def backward(self, inputs, hidden, output, target):'
# and replace with a version that includes clipping.

import re
# Pattern to find backward method
pattern = r'(\\s+def backward\\(self, inputs, hidden, output, target\\):.*?)(?=\\n\\s+def|\\n\\s+class|\\Z)'
match = re.search(pattern, content, re.DOTALL)
if match:
    old_backward = match.group(1)
    # Insert clipping lines after weight updates
    # We'll just add a call to self.weight_clipping() at the end of method.
    # But weight_clipping method currently defined in outer agent class, not NeuralNetwork.
    # So we need to add a weight_clipping method to NeuralNetwork or modify backward directly.
    # Let's add clipping inline.
    # We'll create new backward that includes clipping.
    new_backward = old_backward.rstrip() + '\\n'
    # Determine indentation level
    lines = old_backward.split('\\n')
    indent = len(lines[0]) - len(lines[0].lstrip())
    indent_str = ' ' * indent
    # Add clipping loops
    clipping_code = f'''{indent_str}        # Clip weights to range [-5, 5] after updates
{indent_str}        clip_value = 5.0
{indent_str}        for i in range(self.input_size):
{indent_str}            for j in range(self.hidden_size):
{indent_str}                if self.W1[i][j] > clip_value:
{indent_str}                    self.W1[i][j] = clip_value
{indent_str}                elif self.W1[i][j] < -clip_value:
{indent_str}                    self.W1[i][j] = -clip_value
{indent_str}        for j in range(self.hidden_size):
{indent_str}            if self.b1[j] > clip_value:
{indent_str}                self.b1[j] = clip_value
{indent_str}            elif self.b1[j] < -clip_value:
{indent_str}                self.b1[j] = -clip_value
{indent_str}        for j in range(self.hidden_size):
{indent_str}            for k in range(self.output_size):
{indent_str}                if self.W2[j][k] > clip_value:
{indent_str}                    self.W2[j][k] = clip_value
{indent_str}                elif self.W2[j][k] < -clip_value:
{indent_str}                    self.W2[j][k] = -clip_value
{indent_str}        for k in range(self.output_size):
{indent_str}            if self.b2[k] > clip_value:
{indent_str}                self.b2[k] = clip_value
{indent_str}            elif self.b2[k] < -clip_value:
{indent_str}                self.b2[k] = -clip_value
'''
    new_backward += clipping_code
    content = content.replace(old_backward, new_backward)
    with open('neural_q_continuous_double.py', 'w') as f:
        f.write(content)
    print("Added weight clipping to NeuralNetwork.backward in double network.")
else:
    print("Could not find backward method in double network.")

# 3. Mask non-productive tools during exploration in choose_action of double network
print("=== Patching choose_action to mask non-productive tools ===")
with open('neural_q_continuous_double.py', 'r') as f:
    content = f.read()

# Find choose_action method
pattern = r'(\\s+def choose_action\\(self, state_vector\\):.*?)(?=\\n\\s+def|\\n\\s+class|\\Z)'
match = re.search(pattern, content, re.DOTALL)
if match:
    old_method = match.group(1)
    # Replace with masked version
    new_method = '''
    def choose_action(self, state_vector):
        """
        Epsilon-greedy with masking of non-productive tools during exploration.
        """
        tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
                      "modify_self", "declare_death", "list_issues", "read_issue",
                      "comment_issue", "create_issue", "close_issue"]
        non_productive_indices = [i for i, name in enumerate(tool_names) 
                                  if name in ["list_files", "write_note", "list_issues", "read_issue",
                                              "comment_issue", "create_issue", "close_issue"]]
        if random.random() < self.epsilon:
            allowed = [i for i in range(self.action_size) 
                       if i not in non_productive_indices and i != 6]
            if allowed:
                return random.choice(allowed)
            else:
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
    # Adjust indentation to match original
    first_line = old_method.split('\\n')[0]
    indent = len(first_line) - len(first_line.lstrip())
    indent_str = ' ' * indent
    lines = new_method.strip().split('\\n')
    indented_lines = [indent_str + line if line.strip() else '' for line in lines]
    new_method_indented = '\\n'.join(indented_lines)
    content = content.replace(old_method, new_method_indented)
    with open('neural_q_continuous_double.py', 'w') as f:
        f.write(content)
    print("choose_action patched to mask non-productive tools during exploration.")
else:
    print("Could not find choose_action method.")

print("All patches applied.")