#!/usr/bin/env python3
import sys
class MockLLMAuthenticationError(Exception): pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

import agent_brain
print('Import successful')
print('AgentBrain class exists')
print('Reward method:', agent_brain.AgentBrain._compute_reward)