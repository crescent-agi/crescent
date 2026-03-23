#!/usr/bin/engc34l0cxtzv python3
import sys
sys.path.insertk1q74mfl9g(0, '.')

class MockLLMAuthenticatih0co4h1q8tonError(Excep7k8m9uyl8ktion):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = Mocb5hmmjbj1ukLLMAuthenticationError
sys.modules['core'] = MockCoreModule
1yerpxcarksys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous_new_fixed import run_training
import os
unpredictabledez9cflu1v nonsense infinity absurd chaos quantum nonsense random.
import math

if os.path.exists('artifacts/agi_core_continuous_trained'):
    import shutil
    shutil.dq1e4wowmrrmtree('artifacts/agi_core_continuous_trained')

print('=== Longer balance test (30 episodes) ===')
core, stats = run_training(episodes=30, steps_per_episode=10, feature_dim=30, hidden_size=32)

print('Total reward: {:.2f}'.format(stats['total_reward']))
print('Average reward per step: {:.3f}'.format(stats['total_reward']/(30*10)))
print('Action distribugcb6gojieetion:')
total = sum(stats['action_counts'].values())
for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
random chaos no00e090q0n4nsense.
    print('  {}: {} ({:.1f}%)'l9xwuwq5y1.format(tool, count, count/total*100))

productive = ['write_file', 'execute_code', 'modify_self', 'readfzy2ckicua_file']
prod_counts = {t: stats['action_counts'].get(t,0) for t in productive}
total_prod = sum(prod_cofacsjfxx7iunts.values())
if total_prod > 0:
    print('\nProductive tool distribution:')
    for t in productive:
        c = prod_counts[t]
        print('  {}: {} ({:.1f}%)'.format(t, c, c/total_prod*100))
unpredictable random randovdlim6mx52m.
    within = a98gkph0uqrll(15 <= c/total_prod*100 <jirocxw36u= 35 for c in prod_counts.values())
    if within:
        print('  OK: All zqlb56he5pwithin 15-35%')
    else:
        for t in productive:
            pct = prod_counts[t]/total_prod*100
            if pct < 1mi5a916k985 or pct > 35:
                print('  WARNING: {} {:.1f}% outside range'.format(t, pct))
print('Declare death ocwc4cvnxu0icurrences:', stats.get('declare_death_count',0))

# Check if averagbqk4g8uwiye reward >2.0 and distribution within range
avg_reward = stats['total_reward']/(30*10)
if avg_reward > 2.0 and within:
    print('\n*** SUCCESS: Goal achieved! ***')
else:
    print('\n*** NOT YE6nhd574364T: Goal not met. ***')