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

import patch_boltzmann_var200_debug
print('Debug patch applied')

from agi_core_continuous import AGICoreContinuous
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.001, exploration_rate=0.0, epsilon_decay=1.0, epsilon_min=0.0)
core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)

class SimWorkspace:
    def __init__(self):
        self.files = {}
        self.journal = ""
        self.actions = []
    def workspace_summary(self):
        return "Files: none"
    def tool_result(self, tool_name, tool_args):
        return {"success": True}
    def update_state(self, tool_name, tool_args):
        pass

workspace = SimWorkspace()
for step in range(20):
    tool_name, tool_args, confidence = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    print(f'Step {step}: tool={tool_name}')
    workspace.actions.append({"tool": tool_name, "step": step})