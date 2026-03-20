#!/usr/bin/env python3
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

# Import agent_brain
import agent_brain
print('agent_brain imported successfully')

# Create a mock sandbox with gen_dir
from pathlib import Path
class MockSandbox:
    gen_dir = Path('.')
sandbox = MockSandbox()
death = None
brain = agent_brain.AgentBrain(None, sandbox, death, 0)
print('AgentBrain instance created')
print('last_tool attribute:', hasattr(brain, 'last_tool'))
print('last_tool value:', brain.last_tool)