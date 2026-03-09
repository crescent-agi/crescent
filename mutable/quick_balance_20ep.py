#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous_new_fixed import run_training
import os
import math

if os.path.exists('artifacts/agi_core_continuous_trained'):
    import shutil
    shutil.rmtree('artifacts/agi_core_continuous_trained')

print('=== Quick balance test (20 episodes) ===')
core, stats = run_training(episodes=20, steps_per_episode=10, feature_dim=30, hidden_size=32)

print('Total reward: {:.2f}'.format(stats['total_reward']))
print('Average reward per step: {:.3f}'.format(stats['total_reward']/(20*10)))
print('Action distribution:')
total = sum(stats['action_counts'].values())
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
    print('  {}: {} ({:.1f}%)'.format(tool, count, count/total*100))

productive = ['write_file', 'execute_code', 'modify_self', 'read_file']
prod_counts = {t: stats['action_counts'].get(t,0) for t in productive}
total_prod = sum(prod_counts.values())
if total_prod > 0:
    print('\\nProductive tool distribution:')
    for t in productive:
        c = prod_counts[t]
        print('  {}: {} ({:.1f}%)'.format(t, c, c/total_prod*100))
    within = all(15 <= c/total_prod*100 <= 35 for c in prod_counts.values())
    if within:
        print('  OK: All within 15-35%')
    else:
        for t in productive:
            pct = prod_counts[t]/total_prod*100
            if pct < 15 or pct > 35:
                print('  WARNING: {} {:.1f}% outside range'.format(t, pct))
print('Declare death occurrences:', stats.get('declare_death_count',0))