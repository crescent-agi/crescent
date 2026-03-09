#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous import run_training
import numpy as np

core, stats = run_training(episodes=5, steps_per_episode=5)
print("Q-values for zero state:")
zero_state = np.zeros(core.feature_dim).tolist()
q_vals = core.q_agent.nn.predict(zero_state)
tool_names = ['read_file', 'write_file', 'list_files', 'execute_code', 'write_note', 'modify_self', 'declare_death', 'list_issues', 'read_issue', 'comment_issue', 'create_issue', 'close_issue']
for i, name in enumerate(tool_names):
    print(f"  {name:20} {q_vals[i]:.3f}")
death = q_vals[tool_names.index('declare_death')]
print(f"Declare death Q-value: {death:.3f}")
if death > 0:
    print("WARNING: declare_death Q-value positive!")
else:
    print("Good: declare_death Q-value negative.")