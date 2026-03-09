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
import time

if __name__ == "__main__":
    start_time = time.time()
    core, stats = run_training(episodes=50, steps_per_episode=10, feature_dim=30, hidden_size=32)
    elapsed = time.time() - start_time
    print(f"\\nTotal training time: {elapsed:.1f} seconds")
    print(f"Total reward: {stats['total_reward']:.2f}")
    print(f"Average reward per step: {stats['total_reward']/(50*10):.3f}")
    print("Action distribution:")
    total = sum(stats['action_counts'].values())
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {tool}: {count} ({count/total*100:.1f}%)")
    
    productive = ['write_file', 'execute_code', 'modify_self', 'read_file']
    prod_counts = {t: stats['action_counts'].get(t,0) for t in productive}
    total_prod = sum(prod_counts.values())
    if total_prod > 0:
        print("\\nProductive tool distribution:")
        for t in productive:
            c = prod_counts[t]
            print(f"  {t}: {c} ({c/total_prod*100:.1f}%)")
        within = all(15 <= c/total_prod*100 <= 35 for c in prod_counts.values())
        if within:
            print("  OK: All within 15-35%")
        else:
            for t in productive:
                pct = prod_counts[t]/total_prod*100
                if pct < 15 or pct > 35:
                    print(f"  WARNING: {t} {pct:.1f}% outside range")
    print(f"Declare death occurrences: {stats.get('declare_death_count',0)}")