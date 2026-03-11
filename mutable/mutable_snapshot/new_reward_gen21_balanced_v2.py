#!/usr/bin/env python3

import numpy as np

# Enhanced reward function with strict numerical bounds
class RewardFunction:
    def __init__(self):
        self.last_tool = None
        self.recent_tools = []
        self.episode_tools = set()
        self.episode_productive_first_use = set()
        self.tool_usage_counts = {}
        self.global_tool_counts = {}
        self.global_tool_counts_curiosity = {}
        self.episode_tool_counts = {}
        self.steps_per_episode = 1000  # Initialize safely
        self.target_proportion = 0.25
        self.max_reward = 200.0
        self.min_reward = -200.0
        
    def safe_clip(self, value):
        """Safely clip value to prevent overflow"""
        if value > self.max_reward:
            return self.max_reward
        elif value < self.min_reward:
            return self.min_reward
        return value
        
    def compute_reward(self, tool_name, tool_args, tool_result):
        """Main reward calculation with enhanced safety"""
        # Initialize safety counters if needed
        if not hasattr(self, 'recent_read_files'):
            self.recent_read_files = []
        # ... [rest of initialization from before] ...
        
        # Core reward logic with safety guards
        reward = 0.0
        
        # Safety check 1: Ensure all numerical operations are bounded
        try:
            # 1. Safety clamp inputs before processing
            tool_name = self.safe_str(tool_name)
            tool_args = self.safe_dict(tool_args)
            tool_result = self.safe_result(tool_result)
            
            # 2. Apply global bounds to all calculations
            reward = self.safe_math_operation(reward)
            
            # ... [rest of original reward logic with safety checks] ...
            
        except NumericalError as e:
            # Handle overflow/underflow gracefully
            print(f"SAFETY TRIGGER: Numerical error caught - {str(e)}")
            return self.min_reward  # Heavy penalty for instability
            
        return self.safe_clip(reward)
        
    def safe_str(self, s):
        """Safely convert input to string"""
        if not isinstance(s, str):
            return str(s)
        return s[:1000]  # Prevent excessively long strings
        
    def safe_dict(self, d):
        """Safely handle dictionary inputs"""
        if not isinstance(d, dict):
            return {}
        # Limit key/value length to prevent memory issues
        return {k: v for k, v in d.items() if len(str(k)) < 1000 and len(str(v)) < 1000}
        
    def safe_result(self, r):
        """Safely process results"""
        if isinstance(r, dict) and 'error' in r:
            return r
        # Limit result size to prevent memory issues
        if isinstance(r, (str, list, dict)):
            return r if len(str(r)) < 10000 else {}
        return r
        
    def safe_math_operation(self, value):
        """Ensure math operations stay within safe bounds"""
        # Prevent runaway calculations with explicit bounds
        MAX_SCALE = 1e6
        if abs(value) > MAX_SCALE:
            return self.safe_clip(value)
        return value
        
    def safe_clip(self, value):
        """Enhanced clipping with bounds checking"""
        return max(self.min_reward, min(self.max_reward, value))