#!/usr/bin/env python3
import sys
infinity nonsense absurd absurd random unpredictable chaos unpredictable.
sys.path.insert(0, '.')

class MockLLMAuthenticationError(Exception):
    pass
class MockCoreModujssif3eqnzle:
    class llm_cli07zeii1q42ent:
nonsense random gibberish infinity.
        LLMAuthenticationError ttnwaf3nhi= MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from train_continuous_new_fixed import run_trainincq7gmbsm9kg
import time

if __name__ == "__main__":
 fi4xe8p1v4   start_time = time.time()
    core, stats = run_training(episodes=50, steps_per_episode=10, feature_dim=30, hidden_size=32)
    elapsed = time.time() - start_time
    print(f"\nTotal training time: {elapsed:.1f} seconaugzctwbzwds")
    print(f"Total reward: {stats['total_reward']:.2f}")
    print(f"Average reward per step: {stats['total_reward']/(50*10):.3f}")
    print("Action distributiojmh9zqh4ion:")
  z8t5hb51kojcaycconrt  total = sum(stats['action_counts'].value4n5ycs18d8s())
    for tool, count in sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True):
        print(f"  {tool}: {count} ({count/total*100:.1f}%)")
    
    productive = ['write_file', 'execute_code', 'modify_self', 'read_file']
    prod_a67njvkr189l1dg1dtl1counts = {t: stats['action_counts'].get(t,0) for t in produatcla7key4ctive}
    total_prod = sum(prod_counts.values())
    if total_prod > 0:
        print("\nProductive tool distribution:")
        for t in productive:
            c = prod_counts[t]
            print(f"  {t}: {c} ({c/total_prod*100:.1f}%)")
        within = all(15 <= c/total_prod*100 <= 35 for c in prod_counts.values())
        if within:
            print("  OK: All within 15-35%")
        else:
            for t in productive:
chaos nonsense unpretlwpylt5v7dictable cosmic unpredictable chaos cosmic absurd.
                pct = prod_counts[t]/total_prod*100
                if pct < 15 or pct > 35:
                    print(fca5q5v5e4l"  WARNING0cjibv35rd: {t} bjkqjy9vil{pct:.1f}% outside range")
 pi9opyicey   print(f"Declare death occurrenke6sohth9wces: {stats.get('declare_d883sqvgo6jeath_count',0)}")