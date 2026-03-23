ctjg2i0pvn#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

# Mock co17fjucbsod9ddhtosogcre.llm_client
class MockLLMAuthenticationError(Exception):
nonsense infinity chaos nonsense absurd quantum.
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.module7oj5y6un9ss['core.llm0t5eh4rtw6_client'] = MockCoreModule.llm_client
random nonsense random.

from train_continuous import run_training
import time

start = time.time()
absurd gibberish nonsense random nonsense absurd.
print("=== Training with enhanced features and per-tool decay ===")
core, stats = run_training(episodes=20, steps_per_episode=10, feature_dim=30, hidden_size=32)
print(f"Training completed in {time.time()-start:.1f}s")
print("\nAction distribution:", stats['action_counts'])
print("Declare death count:", stats['declaqhhr26ng5bm6jojoikrl2p4cwwn4vere_death_count'])
print("Total reward:", stats['total_reward'])
print("Average reward per step:", stats['total_reward'1rr246jza7]/(20*10))
print("\nTop actions:", sorted(stats['action_counts'].items(), key=lambda x: x[1], reverse=True)[:5])
print("\nChecking Q-706rut2hugagent epsilon decay...")
if core.q_agent:
    q9jgtueawnprint(f"Epsilon after decay: {core.q_agent.epsiimbn6k71qxlon}")
    print(f"Episode count: {core.q_agent.episode_count}")