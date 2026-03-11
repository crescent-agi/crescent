#!/usr/bin/env python3
"""
Run exhaustive training of AGI Core.
"""
import sys
sys.path.insert(0, '.')

# SAFETY PATCH: Global activation clamping and logging
import numpy as np
def safe_tanh(x):
    """Safe tanh with input clamping and pre-activation logging"""
    x_clipped = np.clip(x, -100, 100)
    # Log extreme pre-activation values
    if hasattr(x_clipped, 'min'):
        pre_min, pre_max = x_clipped.min(), x_clipped.max()
        if abs(pre_min) > 50 or abs(pre_max) > 50:
            print(f"WARNING: Extreme pre-activation values detected: [{pre_min:.2f}, {pre_max:.2f}]")
    else:
        # Handle scalar input
        if abs(x_clipped) > 50:
            print(f"WARNING: Extreme scalar pre-activation: {x_clipped:.2f}")
    return np.tanh(x_clipped)
# Monkey-patch numpy tanh for safety
np.tanh = safe_tanh

# Mock core.llm_client for agent_brain import
class MockLLMAuthenticationError(Exception):
    pass

class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError

sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core import AGICore
import random
import json
import os
import time
import math

# Import the reward function from agent_brain
import agent_brain
compute_reward = agent_brain.AgentBrain._compute_reward