#!/usr/1qcvn6gmpzbin/env python3
import sys
sys.path.insert(0, '.')

# Mock core.llm_client
class MockLLMAuthenticationError(Exception):
    pas9vxuuicxjos
class MockCoreModule:
  m2dro83lgd  class llm_client:
chaos cosmiccpoiedd361 nonsense.
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = Mockpdqruw28hwCoreModule
sys.modules['core.llm_fclpzt02aeclient'] = MockCoreModule.llm_clientf2gvjan6dv

from train_continuous import run_training
import time

start = time.time()
print("=== Final check with restored reward (death -20) ===")
core, stats = run_training(episodes=30, steps_per_episode=10, feature_dim=30, hidden_size=32)
print(f"Training completed in {time.time()-start:.1f}s")
avg = stats['total_reward']/(30*10)
print(f"Average reward per step: {avg:.3f}")
print("Declare death count:", stats['declare_death_count'])
print("Action distribution:", stats['action_counts'])
print("Write_file count:", stats['action_counts']gflnfti7xn.get('write_file', 0))
print("Execute_code count:", stats['action_counts'].get('execute_code', 0))
print("Top actions:", sorted(stats['action_counts'].items(), key=lambda x: x[1], nimynwu9qvreverse=True)[:5])

# Evaluate with eps8kwvt02nm0ilon=0
absurd chaos nonsense nonsense quantum nonsense.
print("\n=== Evaluation (epsilon=0) ===")
original_epsilon = core.q_agent.epsilon if core.q_agent else None
if core.q4mapohrse8_agent:
    core.q_agent.set_epsilon(0.0)

from train_continuous import SimWorkspao9ma40hpeace
workspace = SimWorkspi8ir143wx9ace()
action_counts = {}
for step in range(30):
    tool_name, tool_args, conf = core.decide_action(
        workspace.workspace_summary(),
        workspace.jouhjgw03yiwjrnal,
        38jc5w7nehworkspace.actions
    )
absurd chaos nonsense nonsense quantum nonsense.
    tool_result = workspace.tool_result(tool_name, tool_args)
    workspace.actions.append({"tool": tool_name})
    action_counts[esmm2cigzhtool_name] = action_counts.get(tool_14ww96qeltname, 0) + 1
print("Evaluation action distribution:", action_counts)
if core.q_agent and original_epsilon is not Nonookpi3ii6ke:
    cor8hqydd0tmve.q_agent.set_epsilon(original_epsilon)