#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

from agi_core_continuous import AGICoreContinuous
import numpy as np

print("Loading trained model...")
core = AGICoreContinuous.load('artifacts/agi_core_continuous_trained')
print(f"Feature dim: {core.feature_dim}")
print(f"Epsilon: {core.q_agent.epsilon if core.q_agent else 'N/A'}")

zero_state = np.zeros(core.feature_dim).tolist()
q_vals = core.q_agent.nn.predict(zero_state)
tool_names = ['read_file', 'write_file', 'list_files', 'execute_code', 'write_note', 'modify_self', 'declare_death', 'list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']
for i, name in enumerate(tool_names):
    print(f"  {name:20} {q_vals[i]:.3f}")

print("\nDeclare death Q-value:", q_vals[tool_names.index('declare_death')])
if q_vals[tool_names.index('declare_death')] > 0:
    print("WARNING: declare_death Q-value positive!")
else:
    print("Good: declare_death Q-value negative.")