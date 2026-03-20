#!/usr/bin/env python3
import sys
import os

with open('agent_brain.py', 'r') as f:
    lines = f.readlines()

# Find start of __init__ method
init_start = None
for i, line in enumerate(lines):
    if line.strip().startswith('def __init__(self, llm_client, sandbox, death_monitor, generation: int, day_manager=None):'):
        init_start = i
        break
if init_start is None:
    print('__init__ method not found')
    sys.exit(1)

# Find end of __init__ method: next line with same indentation that starts with 'def '
indent = len(lines[init_start]) - len(lines[init_start].lstrip())
init_end = None
for i in range(init_start + 1, len(lines)):
    if lines[i].strip() == '':
        continue
    if len(lines[i]) - len(lines[i].lstrip()) <= indent and lines[i].strip().startswith('def '):
        init_end = i
        break
if init_end is None:
    init_end = len(lines)

print(f'__init__ method from line {init_start} to {init_end}')

# New __init__ block (indentation 8 spaces)
new_init = '''    def __init__(self, llm_client, sandbox, death_monitor, generation: int, day_manager=None):
        self.llm = llm_client
        self.sandbox = sandbox
        self.death_monitor = death_monitor
        self.generation = generation
        self.day_manager = day_manager
        self.step = 0
        self.state_path = self.sandbox.gen_dir / \"life_state.json\"
        # Per-tool usage tracking for decayed reward
        self.tool_usage_counts = {}
        self.tool_decay_factor = 0.85  # decay per step
        self.tool_penalty_factor = 0.25  # penalty per usage count
        
        # AGI Core integration
        self.agi_core = None
        if AGI_CORE_AVAILABLE:
            try:
                if AGI_CORE_TYPE == 'continuous':
                    # Use continuous core with enhanced features
                    self.agi_core = AGICoreContinuous(feature_dim=30, hidden_size=32, learning_rate=0.01, use_features=True)
                    # Try to load previously saved continuous model
                    core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core_continuous_trained\"
                else:
                    # Fallback to discrete core
                    self.agi_core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
                    core_dir = self.sandbox.gen_dir / \"artifacts\" / \"agi_core\"
                if core_dir.exists():
                    self.agi_core.load(str(core_dir))
                print(f\"  [GEN-{self.generation:04d}] AGI Core ({AGI_CORE_TYPE}) initialized.\")
            except Exception as e:
                print(f\"  [GEN-{self.generation:04d}] Failed to initialize AGI Core: {e}\")
                self.agi_core = None
        else:
            print(f\"  [GEN-{self.generation:04d}] AGI Core not available.\")
        
        # State tracking for AGI Core
        self.previous_workspace_summary = None
        self.previous_journal = \"\"
        self.previous_actions = []
'''

# Replace the block
lines[init_start:init_end] = [new_init]

# Write back
with open('agent_brain.py', 'w') as f:
    f.writelines(lines)

print('Fixed __init__ method.')