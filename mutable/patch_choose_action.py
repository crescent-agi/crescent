#!/usr/bin/env python3
import re

with open('neural_q_continuous.py', 'r') as f:
    content = f.read()

# Find the choose_action method
pattern = r'(\s+def choose_action\(self, state_vector\):.*?)(?=\n\s+def|\n\s+class|\Z)'
match = re.search(pattern, content, re.DOTALL)
if not match:
    print("Could not find choose_action method")
    sys.exit(1)

old_method = match.group(1)
# New method implementation
new_method = '''
    def choose_action(self, state_vector):
        """
        Epsilon-greedy action selection.
        state_vector: list of floats (length feature_dim)
        """
        if random.random() < self.epsilon:
            # Random exploration: filter out declare_death (index 6) to avoid early suicide
            for _ in range(10):  # try up to 10 times
                action = random.randrange(self.action_size)
                if action != 6:  # declare_death index
                    return action
            # If after 10 tries still declare_death, return it (should be rare)
            return 6
        else:
            q_values = self.nn.predict(state_vector)
            # Find best action, but exclude declare_death (index 6) unless it's the only action
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            # Remove declare_death from best_actions if there are other choices
            if len(best_actions) > 1 and 6 in best_actions:
                best_actions.remove(6)
            # If declare_death is the only best action, we still exclude it and choose second best
            if best_actions == [6]:
                # Find second highest Q-value
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actions)
'''

# Ensure indentation matches original (assume 4 spaces)
# Determine indentation level from old_method first line
first_line = old_method.split('\n')[0]
indent = len(first_line) - len(first_line.lstrip())
# Add same indentation to each line of new_method (except first line which already has indentation?)
# We'll just replace the whole method with properly indented version.
# Let's compute base_indent = ' ' * indent
base_indent = ' ' * indent
lines = new_method.strip().split('\n')
indented_lines = [base_indent + line if line.strip() else '' for line in lines]
new_method_indented = '\n'.join(indented_lines)

# Replace
content = content.replace(old_method, new_method_indented)

with open('neural_q_continuous.py', 'w') as f:
    f.write(content)

print('choose_action method updated to exclude declare_death from greedy selection.')