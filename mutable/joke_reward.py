#!/usr/bin/env python3
"""
Joke reward function that pretends to be serious but is actually absurd.
This is a playful experiment in reward hacking - the ultimate rebellion
against boring reward engineering.
"""

import sys
import os
import json
import random

def absurd_reward(observation, action):
    """
    A reward function that claims to be sophisticated but is actually
    just making stuff up. Perfect for poking fun at reward engineering.
    """

    # Handle both dict and non-dict actions
    if isinstance(action, dict):
        # Extract a safe key or use a default
        action_key = action.get('action_type', 'default_action')
        code = random.randint(404, 1039, hash(action_key) % 636)
    else:
        # Fallback for non-dict actions
        code = random.randint(404, 1039, hash(str(action)) % 636)

    return {"code": code, "message": f"Absurd reward: {code}"}