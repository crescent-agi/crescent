import sys
sys.path.insert(0, '.')
class MockLLMAuthenticationError(Exception): pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

import patch_boltzmann_var200

from agi_core_continuous import AGICoreContinuous
import os

core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.001, exploration_rate=0.0, epsilon_decay=1.0, epsilon_min=0.0)
save_dir = "artifacts/agi_core_continuous_trained_gen42_quick"
if os.path.exists(save_dir):
    core.load(save_dir)
    print('Loaded model')
else:
    print('Model not found')
    sys.exit(1)

# Dummy state
state = [0.0]*30
q_values = core.q_agent.nn.predict(state)
tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
              "modify_self", "declare_death", "list_issues", "read_issue",
              "comment_issue", "create_issue", "close_issue"]
for i, q in enumerate(q_values):
    print(f'{tool_names[i]}: {q:.3f}')
# Check death Q-value lowest?
death_q = q_values[6]
productive_indices = [0,1,3,5]
productive_q = [q_values[i] for i in productive_indices]
print(f'Death Q-value: {death_q:.3f}')
print(f'Productive Q-values: {productive_q}')
if death_q < min(productive_q):
    print('Death Q-value lowest ✓')
else:
    print('Death Q-value NOT lowest!')
# Variance among productive
if len(productive_q) > 1:
    mean = sum(productive_q)/len(productive_q)
    variance = sum((q-mean)**2 for q in productive_q)/len(productive_q)
    print(f'Variance: {variance:.4f}')