#!/usr/bin/env python3
import re

filepath = 'agi_core.py'
with open(filepath, 'r') as f:
    content = f.read()

# Find the generate_arguments method
lines = content.split('
')
start = -1
end = -1
for i, line in enumerate(lines):
    if line.strip().startswith('def generate_arguments'):
        start = i
        # find next method start after this one
        for j in range(i+1, len(lines)):
            if lines[j].strip().startswith('def ') and not 'generate_arguments' in lines[j]:
                end = j
                break
        if end == -1:
            end = len(lines)
        break

if start == -1:
    print('generate_arguments method not found')
    exit(1)

print(f'Method lines {start} to {end}')

# New method with improved heuristics
new_method = '''    def extract_files(self, workspace_summary):
        """Extract list of file names from workspace summary."""
        # Workspace summary format: "Files: file1, file2, ..."
        import re
        files = []
        if workspace_summary.startswith("Files:"):
            # Split after colon, take everything, split by commas
            parts = workspace_summary.split(":", 1)[1].strip()
            if parts:
                # Split by commas, strip spaces
                files = [f.strip() for f in parts.split(",")]
        return files
    
    def generate_arguments(self, tool_name, workspace_summary, journal, actions):
        """
        Generate sensible default arguments for a tool based on context.
        """
        # Extract files from workspace summary
        files = self.extract_files(workspace_summary)
        
        if tool_name == "read_file":
            # Prioritize important files
            important = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_model.py", "neural_q.py", "self_reflection.py", 
                         "mcts_planner.py", "agent_brain.py", "strategy.md", 
                         "train_agi_core.py", "run_training.py"]
            for imp in important:
                if imp in files:
                    return {"filepath": imp}
            # Fallback to first file
            if files:
                return {"filepath": files[0]}
            else:
                return {"filepath": "inherited_notes.md"}
        
        elif tool_name == "list_files":
            return {"directory": "."}
        
        elif tool_name == "write_file":
            # Suggest writing to artifacts directory with a generic name
            return {"filepath": "artifacts/note.txt", "content": "AGI core wrote this."}
        
        elif tool_name == "execute_code":
            # Suggest a simple Python script that prints workspace info
            code = "import os\nprint('Workspace files:', os.listdir('.'))"
            return {"code": code, "language": "python"}
        
        elif tool_name == "write_note":
            # Generate note about current step
            note = f"Step {self.step_count}: AGI core acting. Workspace has {len(files)} files."
            return {"note": note}
        
        elif tool_name == "modify_self":
            # Avoid modifying self unless confident; suggest strategy.md
            return {"filepath": "strategy.md", "content": "# Updated by AGI core\n"}
        
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            # For issue tools, default to issue number 1 if needed
            if tool_name in ["read_issue", "comment_issue", "close_issue"]:
                return {"number": "1"}
            else:
                return {}
        
        elif tool_name == "declare_death":
            return {"reason": "AGI core decided to terminate."}
        
        else:
            return {}'''

# Replace lines
new_lines = lines[:start] + [new_method] + lines[end:]
new_content = '
'.join(new_lines)

# Write backup
backup_path = filepath + '.backup'
with open(backup_path, 'w') as f:
    f.write(content)
print(f'Backup saved to {backup_path}')

# Write new content
with open(filepath, 'w') as f:
    f.write(new_content)
print('generate_arguments updated successfully.')