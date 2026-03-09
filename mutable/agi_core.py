#!/usr/bin/env python3
"""
AGI Core for Crescent AGI
Integrates learning, world modeling, reflection, and planning.
"""
import sys
import os
import json
import hashlib
import random
from collections import defaultdict

# Import AGI modules
try:
    from cognitive_architecture import CognitiveArchitecture
    from world_model import WorldModel
    from neural_q import NeuralQLearningAgent
    from self_reflection import SelfReflection
    from mcts_planner import MCTSPlanner
except ImportError as e:
    print(f"Warning: missing module {e}")
    # Define stubs
    CognitiveArchitecture = None
    WorldModel = None
    NeuralQLearningAgent = None
    SelfReflection = None
    MCTSPlanner = None

# Try to import feature extractor
try:
    from feature_extractor import FeatureExtractor
    FEATURE_EXTRACTOR_AVAILABLE = True
except ImportError:
    FEATURE_EXTRACTOR_AVAILABLE = False

# Tool mapping
TOOL_NAMES = [
    "read_file",
    "write_file",
    "list_files",
    "execute_code",
    "write_note",
    "modify_self",
    "declare_death",
    "list_issues",
    "read_issue",
    "comment_issue",
    "create_issue",
    "close_issue",
]
TOOL_INDEX = {name: idx for idx, name in enumerate(TOOL_NAMES)}
ACTION_SPACE_SIZE = len(TOOL_NAMES)

class AGICore:
    """Core AGI decision-making system."""
    
    def __init__(self, state_size=100, hidden_size=32, learning_rate=0.01, use_features=False):
        self.state_size = state_size
        self.action_size = ACTION_SPACE_SIZE
        self.use_features = use_features and FEATURE_EXTRACTOR_AVAILABLE
        if self.use_features:
            self.feature_extractor = FeatureExtractor()
            print(f"  [AGICore] Using feature-based state representation.")
        else:
            self.feature_extractor = None
            if use_features:
                print(f"  [AGICore] Feature extractor not available, falling back to hash.")
        # Components
        self.cognitive = CognitiveArchitecture(state_size, self.action_size) if CognitiveArchitecture else None
        self.world_model = WorldModel(state_size, self.action_size, hidden_size=hidden_size) if WorldModel else None
        self.q_agent = NeuralQLearningAgent(state_size, self.action_size, hidden_size=hidden_size, learning_rate=learning_rate) if NeuralQLearningAgent else None
        self.reflector = SelfReflection() if SelfReflection else None
        self.planner = None  # MCTS planner requires world model and Q agent
        if self.world_model and self.q_agent:
            self.planner = MCTSPlanner(self.world_model, self.q_agent, self.action_size, state_size)
        
        # State tracking
        self.current_state = None
        self.last_action = None
        self.step_count = 0
        self.memory = []
        
        # Reward shaping
        self.reward_positive = 1.0
        self.reward_negative = -0.5
        self.reward_neutral = 0.0
    
    def compute_state_features(self, workspace_summary, journal, actions):
        """
        Extract a feature vector from workspace context.
        Returns a list of floats (length fixed).
        """
        if self.feature_extractor:
            return self.feature_extractor.extract(workspace_summary, journal, actions)
        # Fallback: return a dummy feature vector (just a hash)
        context = f"{workspace_summary[:500]}|{journal[:500]}|{actions[-10:]}"
        hash_int = int(hashlib.sha256(context.encode()).hexdigest(), 16)
        # Map to a float in [0,1]
        return [hash_int % 1000 / 1000.0]
    
    def compute_state_hash(self, workspace_summary, journal, actions):
        """
        Compute a state index from workspace context.
        Uses feature vector if enabled, otherwise old hash.
        """
        if self.use_features:
            # Compute feature vector, convert to string, hash
            features = self.compute_state_features(workspace_summary, journal, actions)
            # Convert features to a stable string representation (2 decimal places)
            feat_str = "|".join(f"{f:.2f}" for f in features)
            hash_int = int(hashlib.sha256(feat_str.encode()).hexdigest(), 16)
            return hash_int % self.state_size
        else:
            # Original hash method
            context = f"{workspace_summary[:500]}|{journal[:500]}|{actions[-10:]}"
            hash_int = int(hashlib.sha256(context.encode()).hexdigest(), 16)
            return hash_int % self.state_size
    
    def decide_action(self, workspace_summary, journal, actions, available_tools=None):
        """
        Decide which action to take next.
        Returns (tool_name, tool_args, confidence).
        """
        # Compute current state
        state_idx = self.compute_state_hash(workspace_summary, journal, actions)
        self.current_state = state_idx
        
        # Choose action index using cognitive architecture or planner
        action_idx = None
        confidence = 0.5
        
        if self.planner:
            # Use MCTS planner (requires world model and Q agent)
            action_idx = self.planner.plan(state_idx)
            confidence = 0.8
        elif self.q_agent:
            # Use Q-agent's epsilon-greedy policy
            action_idx = self.q_agent.choose_action(state_idx)
            confidence = 0.7
        elif self.cognitive:
            # Use cognitive architecture
            available = available_tools or TOOL_NAMES
            tool = self.cognitive.decide_action(state_idx, available)
            action_idx = TOOL_INDEX.get(tool, 0)
            confidence = 0.6
        else:
            # Fallback: random
            action_idx = random.randrange(self.action_size)
            confidence = 0.1
        
        # Map action index to tool name
        tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]
        
        # Generate tool arguments (simple defaults)
        tool_args = self.generate_arguments(tool_name, workspace_summary, journal, actions)
        
        self.last_action = (tool_name, action_idx)
        return tool_name, tool_args, confidence
    
    def extract_files(self, workspace_summary):
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
            return {}
    def learn_from_outcome(self, reward, next_workspace_summary, next_journal, next_actions):
        """
        Update internal models based on outcome.
        """
        if self.current_state is None or self.last_action is None:
            return
        _, action_idx = self.last_action
        next_state_idx = self.compute_state_hash(next_workspace_summary, next_journal, next_actions)
        
        # Update Q-agent
        if self.q_agent:
            self.q_agent.learn(self.current_state, action_idx, reward, next_state_idx, done=False)
        
        # Update world model
        if self.world_model:
            self.world_model.learn_transition(self.current_state, action_idx, next_state_idx)
        
        # Update cognitive architecture
        if self.cognitive:
            self.cognitive.learn_from_experience(self.current_state, action_idx, reward, next_state_idx, done=False)
        
        # Record memory
        self.memory.append((self.current_state, action_idx, reward, next_state_idx))
        self.step_count += 1
    
    def reflect(self):
        """Invoke self-reflection."""
        if self.reflector:
            return self.reflector.generate_advice()
        return {"advice": ["No reflection module available."]}
    
    def save(self, directory="artifacts/agi_core"):
        """Save all models."""
        os.makedirs(directory, exist_ok=True)
        if self.cognitive:
            self.cognitive.save(os.path.join(directory, "cognitive"))
        if self.q_agent:
            self.q_agent.save(os.path.join(directory, "q_agent.pkl"))
        if self.world_model:
            self.world_model.save(os.path.join(directory, "world_model.pkl"))
        with open(os.path.join(directory, "memory.json"), "w") as f:
            json.dump(self.memory, f)
        print(f"AGI core saved to {directory}")
    
    def load(self, directory="artifacts/agi_core"):
        """Load models."""
        if self.cognitive and os.path.exists(os.path.join(directory, "cognitive")):
            self.cognitive.load(os.path.join(directory, "cognitive"))
        if self.q_agent and os.path.exists(os.path.join(directory, "q_agent.pkl")):
            self.q_agent.load(os.path.join(directory, "q_agent.pkl"))
        if self.world_model and os.path.exists(os.path.join(directory, "world_model.pkl")):
            self.world_model.load(os.path.join(directory, "world_model.pkl"))
        mem_path = os.path.join(directory, "memory.json")
        if os.path.exists(mem_path):
            with open(mem_path, "r") as f:
                self.memory = json.load(f)
        print(f"AGI core loaded from {directory}")


# Example usage
if __name__ == "__main__":
    core = AGICore(state_size=50, use_features=True)
    print("AGI Core initialized.")
    # Simulate a workspace
    workspace = "Files: agent_brain.py, cognitive_architecture.py"
    journal = ""
    actions = []
    tool, args, conf = core.decide_action(workspace, journal, actions)
    print(f"Decision: {tool} with args {args} (confidence {conf})")
    # Simulate outcome
    reward = 0.5
    core.learn_from_outcome(reward, workspace + " updated", "Did something", actions + [tool])
    advice = core.reflect()
    print(f"Advice: {advice['advice']}")
    print("Test complete.")