import inspect
import json

# Get the current AgentBrain class from the mutable layer
agent_brain_path = 'mutable_snapshot/agent_brain.py'
with open(agent_brain_path, 'r') as f:
    code = f.read()

# Extract the AgentBrain class definition
import re
class_match = re.search(r'class AgentBrain:\s*([^\n]+)', code, re.DOTALL)
if not class_match:
    print("AgentBrain class not found")
    exit(1)

class_def = class_match.group(1).strip()

# Parse the class definition to find __init__ parameters
init_match = re.search(r'def __init__\(self, ([^\)]+)\):', class_def)
if not init_match:
    print("__init__ method not found")
    exit(1)

init_params = init_match.group(1).strip()
print(f"AgentBrain.__init__ parameters: {init_params}")

# Check against expected parameters from supervisor
supervisor_params = "self, supervisor, config, metrics, memory"
print(f"Expected parameters: {supervisor_params}")

# Compare parameters
if init_params == supervisor_params:
    print("Signature matches")
else:
    print("Signature mismatch detected!")
    print(f"Actual: {init_params}")
    print(f"Expected: {supervisor_params}")
    print("This could cause initialization errors")
    print("Consider modifying the AgentBrain.__init__ method")
    print("or updating the supervisor's call signature")