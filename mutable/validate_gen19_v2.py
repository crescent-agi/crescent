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

# Import the training script's run_validation function
from train_gen19_balanced import run_validation, SimWorkspace, DummySelf
from agi_core_continuous import AGICoreContinuous
import os

print('Loading AGI Core Continuous from gen19 model...')
core = AGICoreContinuous(feature_dim=30, hidden_size=32,
                         learning_rate=0.01, exploration_rate=0.3,
                         epsilon_decay=0.95, epsilon_min=0.05, use_features=True)
model_path = 'artifacts/agi_core_continuous_trained_gen19'
if os.path.exists(model_path):
    core.load(model_path)
    print(f'Loaded {model_path}')
else:
    print('Model not found, exiting.')
    sys.exit(1)

print('\nRunning validation with epsilon=0 for 500 steps...')
stats = run_validation(core, steps=500)
print(f'Non-productive actions: {stats["non_productive_total"]}')
print(f'Productive distribution:')
for tool, perc in stats['productive_distribution'].items():
    print(f'  {tool}: {perc:.1f}%')
    if perc >= 15 and perc <= 35:
        print(f'    -> within target range')
    else:
        print(f'    -> OUTSIDE target range')
print('\nAction counts (top 10):')
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f'  {tool}: {count}')

print('\nDone.')