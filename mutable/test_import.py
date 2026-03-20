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

# Monkey-patch neural_q_continuous import to use our Double DQN class
import neural_q_continuous_double
sys.modules['neural_q_continuous'] = neural_q_continuous_double

# Apply weight clipping patch
import patch_weight_clipping
# Apply strong Q-value regularization patch (for choose_action)
import patch_qreg_v3
# Apply variance penalty patch (overrides learn)
import patch_variance_penalty

from agi_core_continuous import AGICoreContinuous
print("Import successful")