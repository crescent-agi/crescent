import os
import ast

class AgentBrainSignatureValidator:
    def __init__(self, file_path='agent_brain.py')
        self.file_path = file_path

    def analyze_signature(self)
        try:
            with open(self.file_path, 'r') as f:
                tree = ast.parse(f.read())
        except FileNotFoundError:
            print(f"ERROR: AgentBrain.py not found in current directory at {{self.file_path}}")
            return
        
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == '__init__' and hasattr(node, 'args'):
                    self.init_params = [arg.arg for arg in node.args.args]
                    return {'success': True, 'signature': self.init_params}
            return {'error': 'No __init__ method found in AgentBrain.py'}

if __name__ == '__main__':
    validator = AgentBrainSignatureValidator()
    result = validator.analyze_signature()
    if result['success']:
        print(f"AgentBrain __init__ signature found: {result['signature']}")
    else:
        print(f"Signature analysis failed: {{result.get('error', result)}}")