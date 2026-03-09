#!/usr/bin/env python3
"""
AGI Core for Crescent AGI with Continuous State Representation
Integrates learning, world modeling, reflection, and planning.
Uses continuous feature vectors as state representation.
"""

import sys
import os
import json
import random
from collections import defaultdict

# Import AGI modules
try:
    from cognitive_architecture import CognitiveArchitecture
    from self_reflection import SelfReflection
    from mcts_planner import MCTSPlanner
except ImportError as e:
    print(f"Warning: missing module {e}")
    CognitiveArchitecture = None
    SelfReflection = None
    MCTSPlanner = None

# Import continuous agents
try:
    from neural_q_continuous import NeuralQLearningAgentContinuous
    from world_model_continuous import WorldModelContinuous
    CONTINUOUS_AGENTS_AVAILABLE = True
except ImportError as e:
    print(f"Warning: missing continuous agents {e}")
    CONTINUOUS_AGENTS_AVAILABLE = False

# Import feature extractor
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


class AGICoreContinuous:
    """Core AGI decision-making system with continuous state representation."""
    
    def __init__(self, feature_dim, action_size=None, hidden_size=32, learning_rate=0.01, exploration_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005, use_features=True):
        self.feature_dim = feature_dim
        self.action_size = ACTION_SPACE_SIZE
        self.use_features = use_features and FEATURE_EXTRACTOR_AVAILABLE
        self.exploration_rate = exploration_rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        if self.use_features:
            self.feature_extractor = FeatureExtractor()
            print(f"  [AGICoreContinuous] Using feature-based continuous state representation.")
        else:
            self.feature_extractor = None
            if use_features:
                print(f"  [AGICoreContinuous] Feature extractor not available, falling back to dummy feature vector.")
        # Continuous agents
        if CONTINUOUS_AGENTS_AVAILABLE:
            self.q_agent = NeuralQLearningAgentContinuous(feature_dim, self.action_size, hidden_size=hidden_size, learning_rate=learning_rate, exploration_rate=exploration_rate, epsilon_decay=epsilon_decay, epsilon_min=epsilon_min)
            self.world_model = WorldModelContinuous(feature_dim, self.action_size, hidden_size=hidden_size, learning_rate=learning_rate)
        else:
            print(f"  [AGICoreContinuous] Continuous agents not available, falling back to discrete.")
            self.q_agent = None
            self.world_model = None
        # Other components (still discrete, may need adaptation)
        self.cognitive = CognitiveArchitecture(feature_dim, self.action_size) if CognitiveArchitecture else None
        self.reflector = SelfReflection() if SelfReflection else None
        self.planner = None  # MCTS planner requires discrete states; disable for now
        # TODO: adapt MCTS planner for continuous states
        
        # State tracking
        self.current_state_vector = None
        self.last_action = None
        self.step_count = 0
        self.memory = []
        
        # Reward shaping
        self.reward_positive = 1.0
        self.reward_negative = -0.5
        self.reward_neutral = 0.0
    
    def compute_state_vector(self, workspace_summary, journal, actions):
        """
        Extract a feature vector from workspace context.
        Returns a list of floats (length feature_dim).
        """
        if self.feature_extractor:
            features = self.feature_extractor.extract(workspace_summary, journal, actions)
            # Ensure length matches feature_dim (should be 15)
            if len(features) != self.feature_dim:
                # Pad or truncate
                if len(features) < self.feature_dim:
                    features = features + [0.0] * (self.feature_dim - len(features))
                else:
                    features = features[:self.feature_dim]
            return features
        else:
            # Dummy feature vector based on hash
            context = f"{workspace_summary[:500]}|{journal[:500]}|{actions[-10:]}"
            import hashlib
            hash_int = int(hashlib.sha256(context.encode()).hexdigest(), 16)
            # Generate deterministic pseudo-random vector
            random.seed(hash_int)
            return [random.random() for _ in range(self.feature_dim)]
    
    def decide_action(self, workspace_summary, journal, actions, available_tools=None):
        """
        Decide which action to take next.
        Returns (tool_name, tool_args, confidence).
        """
        # Compute current state vector
        state_vec = self.compute_state_vector(workspace_summary, journal, actions)
        self.current_state_vector = state_vec
        
        # Choose action index using continuous Q-agent or fallback
        action_idx = None
        confidence = 0.5
        
        if self.q_agent:
            # Use continuous Q-agent's epsilon-greedy policy
            action_idx = self.q_agent.choose_action(state_vec)
            confidence = 0.7
        elif self.cognitive:
            # Use cognitive architecture (discrete)
            # Map state vector to discrete index via simple hash
            state_idx = hash(str(state_vec)) % self.cognitive.state_size
            available = available_tools or TOOL_NAMES
            tool = self.cognitive.decide_action(state_idx, available)
            action_idx = TOOL_INDEX.get(tool, 0)
            confidence = 0.6
        else:
            # Fallback: random
            # Filter declare_death during random fallback
            for _ in range(10):
                action_idx = random.randrange(self.action_size)
                if action_idx != 6:  # declare_death
                    break
            confidence = 0.1
        
        # Map action index to tool name
        if self.step_count < 100 and action_idx == 6:
            # Choose a different action
            if self.q_agent:
                q_vals = self.q_agent.nn.predict(state_vec)
                sorted_indices = sorted(range(len(q_vals)), key=lambda i: q_vals[i], reverse=True)
                for idx in sorted_indices:
                    if idx != 6:
                        action_idx = idx
                        break
            else:
                # random fallback: pick any non-death action
                for _ in range(10):
                    candidate = random.randrange(self.action_size)
                    if candidate != 6:
                        action_idx = candidate
                        break
        
        tool_name = TOOL_NAMES[action_idx] if 0 <= action_idx < len(TOOL_NAMES) else TOOL_NAMES[0]
        tool_args = self.generate_arguments(tool_name, workspace_summary, journal, actions)
        
        self.last_action = (tool_name, action_idx)
        return tool_name, tool_args, confidence
    
    def extract_files(self, workspace_summary):
        """Extract list of file names from workspace summary."""
        import re
        files = []
        if workspace_summary.startswith("Files:"):
            parts = workspace_summary.split(":", 1)[1].strip()
            if parts:
                files = [f.strip() for f in parts.split(",")]
        return files
    
    def generate_arguments(self, tool_name, workspace_summary, journal, actions):
        """
        Generate sensible default arguments for a tool based on context.
        (Same as original AGICore)
        """
        files = self.extract_files(workspace_summary)
        
        if tool_name == "read_file":
            important = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_model.py", "neural_q.py", "self_reflection.py", 
                         "mcts_planner.py", "agent_brain.py", "strategy.md", 
                         "train_agi_core.py", "run_training.py"]
            for imp in important:
                if imp in files:
                    return {"filepath": imp}
            if files:
                return {"filepath": files[0]}
            else:
                return {"filepath": "inherited_notes.md"}
        
        elif tool_name == "list_files":
            return {"directory": "."}
        
        elif tool_name == "write_file":
            import random
            choice = random.random()
            if choice < 0.3:
                return {"filepath": "artifacts/test.py", "content": "# AGI Core generated this file\\nprint('Hello from AGI')"}
            elif choice < 0.6:
                return {"filepath": "agent_brain.py", "content": "# Modified by AGI Core\\n"}
            else:
                return {"filepath": "artifacts/note.txt", "content": "AGI core wrote this."}
        
        elif tool_name == "execute_code":
            code = "import os\nprint('Workspace files:', os.listdir('.'))"
            return {"code": code, "language": "python"}
        
        elif tool_name == "write_note":
            note = f"Step {self.step_count}: AGI core acting. Workspace has {len(files)} files."
            return {"note": note}
        
        elif tool_name == "modify_self":
            return {"filepath": "strategy.md", "content": "# Updated by AGI core\n"}
        
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
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
        if self.current_state_vector is None or self.last_action is None:
            # Record reward for feature trend
            if self.feature_extractor:
                self.feature_extractor.add_reward(reward)
            return
        _, action_idx = self.last_action
        next_state_vec = self.compute_state_vector(next_workspace_summary, next_journal, next_actions)
        
        # Update Q-agent (continuous)
        if self.q_agent:
            self.q_agent.learn(self.current_state_vector, action_idx, reward, next_state_vec, done=False)
        
        # Update world model (continuous)
        if self.world_model:
            self.world_model.learn_transition(self.current_state_vector, action_idx, next_state_vec)
        
        # Update cognitive architecture (discrete) - optional
        if self.cognitive:
            # Map vectors to discrete indices
            state_idx = hash(str(self.current_state_vector)) % self.cognitive.state_size
            next_state_idx = hash(str(next_state_vec)) % self.cognitive.state_size
            self.cognitive.learn_from_experience(state_idx, action_idx, reward, next_state_idx, done=False)
        
        # Record memory
        self.memory.append((self.current_state_vector, action_idx, reward, next_state_vec))
        self.step_count += 1
    
    def reflect(self):
        """Invoke self-reflection."""
        if self.reflector:
            return self.reflector.generate_advice()
        return {"advice": ["No reflection module available."]}
    
    def save(self, directory="artifacts/agi_core_continuous"):
        """Save all models."""
        os.makedirs(directory, exist_ok=True)
        if self.cognitive:
            self.cognitive.save(os.path.join(directory, "cognitive"))
        if self.q_agent:
            self.q_agent.save(os.path.join(directory, "q_agent.pkl"))
        if self.world_model:
            self.world_model.save(os.path.join(directory, "world_model.pkl"))
        with open(os.path.join(directory, "memory.json"), "w") as f:
            # JSON cannot serialize tuples with lists; convert to list of lists
            mem_serializable = []
            for state_vec, action, reward, next_vec in self.memory:
                mem_serializable.append([state_vec, action, reward, next_vec])
            json.dump(mem_serializable, f)
        print(f"AGI Core Continuous saved to {directory}")
    
    def load(self, directory="artifacts/agi_core_continuous"):
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
                mem_serializable = json.load(f)
                self.memory = [(state_vec, action, reward, next_vec) for state_vec, action, reward, next_vec in mem_serializable]
        print(f"AGI Core Continuous loaded from {directory}")


# Example usage
if __name__ == "__main__":
    core = AGICoreContinuous(feature_dim=15, use_features=True)
    print("AGI Core Continuous initialized.")
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