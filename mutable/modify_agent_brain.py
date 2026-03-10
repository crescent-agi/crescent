#!/usr/bin/env python3
"""
Modify agent_brain.py to integrate AGI Core.
"""
import sys
import re

def main():
    with open('agent_brain.py', 'r') as f:
        content = f.read()
    
    # Insert import after the existing imports
    import_insert = '''import hashlib
from pathlib import Path

# Try to import AGI Core
try:
    from agi_core import AGICore
    AGI_CORE_AVAILABLE = True
except ImportError:
    AGICORE = None
    AGI_CORE_AVAILABLE = False
'''
    # Find last import line
    lines = content.split('
')
    insert_idx = None
    for i, line in enumerate(lines):
        if line.startswith('from core.llm_client import LLMAuthenticationError'):
            insert_idx = i + 1
            break
    if insert_idx is None:
        insert_idx = len(lines)
    lines.insert(insert_idx, import_insert)
    content = '
'.join(lines)
    
    # Add AGI Core initialization in __init__
    # Find __init__ method
    pattern = r'def __init__\(self, llm_client, sandbox, death_monitor, generation: int, day_manager=None\):'
    match = re.search(pattern, content)
    if not match:
        print("Could not find __init__")
        return
    init_start = match.start()
    # Find the end of __init__ (next method)
    # We'll insert after self.state_path = ... line
    # Let's find the line after that
    lines = content.split('
')
    init_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def __init__'):
            init_line = i
            break
    if init_line is None:
        print("Init line not found")
        return
    # Find the line containing self.state_path
    state_path_line = None
    for i in range(init_line, len(lines)):
        if 'self.state_path' in lines[i]:
            state_path_line = i
            break
    if state_path_line is None:
        print("self.state_path not found")
        return
    # Insert after that line
    insert_line = state_path_line + 1
    agi_init = '''        # AGI Core integration
        self.agi_core = None
        if AGI_CORE_AVAILABLE:
            try:
                self.agi_core = AGICore(state_size=100, hidden_size=32, learning_rate=0.01)
                # Try to load previously saved model
                core_dir = self.sandbox.gen_dir / "artifacts" / "agi_core"
                if core_dir.exists():
                    self.agi_core.load(str(core_dir))
                print(f"  [GEN-{self.generation:04d}] AGI Core initialized.")
            except Exception as e:
                print(f"  [GEN-{self.generation:04d}] Failed to initialize AGI Core: {e}")
                self.agi_core = None
        else:
            print(f"  [GEN-{self.generation:04d}] AGI Core not available.")
        
        # State tracking for AGI Core
        self.previous_workspace_summary = None
        self.previous_journal = ""
        self.previous_actions = []'''
    lines.insert(insert_line, agi_init)
    content = '
'.join(lines)
    
    # Add helper methods before _execute_tool maybe
    # Find the line with 'def _execute_tool'
    lines = content.split('
')
    execute_tool_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def _execute_tool'):
            execute_tool_line = i
            break
    if execute_tool_line is None:
        print("Could not find _execute_tool")
        return
    # Insert before that line
    helper_methods = '''
    def _capture_pre_action_state(self):
        """Store current workspace state for later learning."""
        self.previous_workspace_summary = self.sandbox.get_workspace_summary()
        self.previous_journal = self._get_journal_content()
        self.previous_actions = self._get_recent_actions(20)
    
    def _learn_from_tool_result(self, tool_name, tool_args, tool_result):
        """Compute reward and update AGI Core."""
        if not self.agi_core:
            return
        # Compute reward based on tool result
        reward = self._compute_reward(tool_name, tool_args, tool_result)
        # Get new state
        workspace_summary = self.sandbox.get_workspace_summary()
        journal = self._get_journal_content()
        actions = self._get_recent_actions(20)
        # Update AGI Core
        self.agi_core.learn_from_outcome(reward, workspace_summary, journal, actions)
    
    def _compute_reward(self, tool_name, tool_args, tool_result):
        """Simple reward shaping."""
        # Default neutral
        reward = 0.0
        # Positive if tool succeeded (no error)
        if isinstance(tool_result, dict) and not tool_result.get("error"):
            reward += 0.1
        # Extra reward for creating new files
        if tool_name == "write_file" and "filepath" in tool_args:
            # Check if file was created (we can't know; assume success)
            reward += 0.5
        # Extra reward for executing code that runs successfully
        if tool_name == "execute_code" and isinstance(tool_result, dict) and "stdout" in tool_result:
            reward += 0.3
        # Negative reward for declare_death (discourage premature termination)
        if tool_name == "declare_death":
            reward -= 2.0
        # Negative reward for errors
        if isinstance(tool_result, dict) and "error" in tool_result:
            reward -= 0.5
        return reward
    
    def _get_journal_content(self):
        """Return current journal content."""
        journal_path = self.sandbox.gen_dir / "journal.md"
        if journal_path.exists():
            return journal_path.read_text(encoding="utf-8")
        return ""
    
    def _get_recent_actions(self, n):
        """Return up to n recent actions from actions.jsonl."""
        actions = []
        actions_path = self.sandbox.gen_dir / "actions.jsonl"
        if actions_path.exists():
            lines = actions_path.read_text(encoding="utf-8").strip().split('\n')
            for line in lines[-n:]:
                if line:
                    try:
                        actions.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
        return actions
'''
    lines.insert(execute_tool_line, helper_methods)
    content = '
'.join(lines)
    
    # Modify _build_step_prompt to accept suggestion
    # Find its definition
    lines = content.split('
')
    build_prompt_line = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def _build_step_prompt'):
            build_prompt_line = i
            break
    if build_prompt_line is None:
        print("Could not find _build_step_prompt")
        return
    # Replace the method signature and body
    # We'll replace from that line until the next method (indentation level 4)
    # Let's find the end of the method
    start = build_prompt_line
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = start + 1
    while end < len(lines) and (lines[end].strip() == '' or len(lines[end]) - len(lines[end].lstrip()) > indent):
        end += 1
    # New method
    new_method = '''    def _build_step_prompt(self, history: list, tool_suggestion=None, tool_args_suggestion=None) -> str:
        """Build the full prompt from conversation history, optionally including AGI Core suggestion."""
        parts = []
        for msg in history:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                parts.append(f"[CONTEXT]\\n{content}")
            else:
                parts.append(f"[YOU]\\n{content}")
        
        # Append AGI Core suggestion if available
        if tool_suggestion:
            suggestion = f"\\n\\n[AGI Core Suggestion]\\nConsider taking action '{tool_suggestion}' with arguments {tool_args_suggestion}. You may follow this suggestion or ignore it."
            parts.append(suggestion)
        
        return "\\n\\n".join(parts)'''
    # Replace lines[start:end] with new_method
    lines = lines[:start] + [new_method] + lines[end:]
    content = '
'.join(lines)
    
    # Modify run method to incorporate AGI Core
    # Find the run method
    lines = content.split('
')
    run_start = None
    for i, line in enumerate(lines):
        if line.strip().startswith('def run'):
            run_start = i
            break
    if run_start is None:
        print("Could not find run method")
        return
    # We'll insert after the death check and before the try block that calls LLM.
    # Let's find the line with 'try:' after the death check.
    # We'll search for 'try:' after the line that prints agent awakens.
    # Actually we need to insert after capturing pre-action state and before building prompt.
    # Let's do a simple insertion: after the line 'death = self.death_monitor.check()' and before 'try:'
    # But we need to add capture pre-action state.
    # Let's find the line 'death = self.death_monitor.check()' inside the while loop.
    # We'll do a regex replace maybe better to write a new run method, but that's too heavy.
    # Let's instead insert a few lines after the death check.
    # We'll locate the line with 'try:' that is inside the while loop.
    # We'll find the while True line first.
    while_line = None
    for i in range(run_start, len(lines)):
        if lines[i].strip() == 'while True:':
            while_line = i
            break
    if while_line is None:
        print("while True not found")
        return
    # Find the line with 'try:' after while_line
    try_line = None
    for i in range(while_line, len(lines)):
        if lines[i].strip() == 'try:':
            try_line = i
            break
    if try_line is None:
        print("try: not found")
        return
    # Insert before try_line
    insertion = '''            # Capture state before action for AGI Core learning
            self._capture_pre_action_state()
            
            # Decide action: AGI Core suggestion or LLM
            tool_suggestion = None
            tool_args_suggestion = None
            if self.agi_core:
                workspace_summary = self.sandbox.get_workspace_summary()
                journal = self._get_journal_content()
                actions = self._get_recent_actions(20)
                tool_name, tool_args, confidence = self.agi_core.decide_action(
                    workspace_summary, journal, actions
                )
                if confidence > 0.7:  # Use AGI Core suggestion
                    tool_suggestion = tool_name
                    tool_args_suggestion = tool_args
                    print(f"  [GEN-{self.generation:04d}] AGI Core suggests: {tool_name} with args {tool_args}")'''
    lines.insert(try_line, insertion)
    content = '
'.join(lines)
    
    # Also need to modify the call to _build_step_prompt to pass suggestions
    # Find the line with 'full_prompt = self._build_step_prompt(conversation_history)'
    lines = content.split('
')
    for i, line in enumerate(lines):
        if 'full_prompt = self._build_step_prompt(conversation_history)' in line:
            # Replace with new line
            lines[i] = '                full_prompt = self._build_step_prompt(conversation_history, tool_suggestion, tool_args_suggestion)'
            break
    
    # Need to add learning after each tool call
    # Find the loop where tool_calls are processed
    # Look for 'for tool_call in tool_calls:'
    lines = content.split('
')
    for i, line in enumerate(lines):
        if 'for tool_call in tool_calls:' in line:
            # Insert after the block that logs action and before the if tool_call["name"] == "declare_death"
            # We'll find the line with 'if tool_call["name"] == "declare_death":'
            for j in range(i, len(lines)):
                if 'if tool_call["name"] == "declare_death":' in lines[j]:
                    # Insert before that line
                    learn_insert = '''                # Learn from outcome (if AGI Core is active)
                if self.agi_core:
                    self._learn_from_tool_result(tool_call["name"], tool_call.get("args"), tool_result)'''
                    lines.insert(j, learn_insert)
                    break
            break
    
    # Add saving AGI Core before dying
    # Find the line 'if self.state_path.exists():' after the while loop ends
    # Look for that line after the while loop break.
    # Actually we need to insert before the state cleanup.
    # Let's find the line 'if self.state_path.exists():' after the while loop.
    for i, line in enumerate(lines):
        if line.strip().startswith('if self.state_path.exists():'):
            # Insert before that line
            save_insert = '''        # Save AGI Core models before dying
        if self.agi_core:
            core_dir = self.sandbox.gen_dir / "artifacts" / "agi_core"
            self.agi_core.save(str(core_dir))'''
            lines.insert(i, save_insert)
            break
    
    # Write the modified content back
    with open('agent_brain_new.py', 'w') as f:
        f.write('
'.join(lines))
    print("Modified agent brain written to agent_brain_new.py")

if __name__ == '__main__':
    main()