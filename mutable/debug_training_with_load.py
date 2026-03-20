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
print('Patch applied')

from agi_core_continuous import AGICoreContinuous
import os

# Load gen41_strong
core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.001, exploration_rate=0.0, epsilon_decay=1.0, epsilon_min=0.0)
core.q_agent.init_temperature(start_temp=1.0, decay=0.95, min_temp=0.2)
save_dir = "artifacts/agi_core_continuous_trained_gen41_strong"
if os.path.exists(save_dir):
    core.load(save_dir)
    print('Loaded model')
    if hasattr(core.q_agent, 'reset_output_weights_all_productive'):
        core.q_agent.reset_output_weights_all_productive()
    else:
        core.q_agent.reset_output_weights([0,1,3,5])
    print('Reset output weights')
else:
    print('Model not found')
    sys.exit(1)

# Tool mapping
tool_names = ["read_file", "write_file", "list_files", "execute_code", "write_note",
              "modify_self", "declare_death", "list_issues", "read_issue",
              "comment_issue", "create_issue", "close_issue"]

# Simulate a few steps
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
for step in range(10):
    tool_name, tool_args, confidence = core.decide_action(
        workspace.workspace_summary(),
        workspace.journal,
        workspace.actions
    )
    # Map tool_name to index
    try:
        idx = tool_names.index(tool_name)
    except ValueError:
        idx = -1
    print(f'Step {step}: tool={tool_name} index={idx}')
    workspace.actions.append({"tool": tool_name, "step": step})