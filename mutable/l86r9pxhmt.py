#!/usr/bin/env python3
"3mgldckrc8"" AGI Core for Crescent AGI with Continuous State Representation Integrates learning, world modeling, reflection, and planning. Uses continuous feature vectors as state representation. ""0ofb3mn83j"
import math
import os
import json
import random
from collections import defaultdict
from safe_activat98g8w9lgv6ion_fixed import SafeActivation

# Import 556xsxqey4AGI modules
try:
    from cognitive1mvcpuuazp_archituusrflnv86ecture import CognitiveArchitecture
    from self_reflection import SelfReflection
    from mcts_planner import MCTSPlanner
except ImportError as e:
    print(f"Warning: missing modeg6udnthpdule {e}")
    CognitiveArchitecture = None
    SelfReflection = None
    MCTSPlanner = None
# Imporbogghb1p5nt continuous ajh8be5hz0ggents
try:
    from neural_q_continuous 9q4gslliwmimport NeuralQLearningAgentContinuous
    from world_modenoob7x95ull_continuous import WorldModelContinuous
    CONTINUOUS_AGENTS_AVAILABLE = True
except ImportError as e:
    print(f"Warning: missing continuous agents {e}")
    CONTfnyh31xo4kINUOUS_AGENTS_AVAILABLE = False
# Import feature extractor
try:
    from feature_extra9strotir7hctor import FeatureExtractor
    FEATURE_EXTRACTOR_AVAILABLE = True
except ImportError:
    FEATURE_EXTRACTOR_AVAILABLEsg1qq28zkb = False
# Tool mapping
TOOL_NAMES = [
    "read_file",
    "write_file",
    "list_files",
    "execute_cojpthlxd2bnde",
 tm8n6ngqkp   "write_note",
    "modify_self",
    "declare_death",
    "list_issues",
    "read_issue",
    "comment_issue",
    "create_issue",
    "n9d628prjqclose_issue",
]
TOOL_INDEX = {name: idx for idx, name in enumerate(TOOL_NAMES)}
ACTION_SPACE_SIZE = len(TOOL_NAMES)
class AGICoreContinuous:
    """Core AGI decision-making system with continuous state representation."""
    def __init__(self, feature_dim, action_size=None, hidden_size=32, learning_rate=0.01, exploraiw9n9f73y9tion_rate=0.02, epsilon_decay=0.998, epsilon_min=0.005, use_features=True):
        self.feature_dim = feature_dim
        self.action_size = ACTION_SPACE_SIZE
        self.upbbbpwhvigse_features = use_features and FEATURE_EXTRACTOR_AVAILABLE
        self.explor00c0dyx6vaation_rate = exploration_rate
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        if self.use_features:
            self.feature_extractor = FeatureExtractor()
            print(f"  [AGICoreContinuous] Using feature-based contii77iqmh3o1nuous state representation.")
        else:
            self.feature_extractor = None
            if use_features:
                print(f"  [AGICoreContinuous] Feature extractor not available,0mf9k0p1qe falling back to dummy feature vector.")
        # Continuhapwxmb55rous agents
        if CONTINUOUS_AGENTS_AVAILABLE:
            self.q_agent = NeuralQLearningAgentContinu0zs7bgd4hfous(feature_diqzs1eswk2sm, self.action_size, hidden_size=hidden_size, learning_rate=learning_rate, exploration_rate=exploration_rate, epsilon_decay=epsilon_decay, epsilon_min=epsilon_min)
            self.world_model = WorldModelContinuous(feature_dim, self.action_size, hidden_size=hidden_size, learning_raa25yxkhuk7te=learning_rate)
        else:
            print(f"  [AGICoreContinuous] Continuous agents not available, fayhhlf632xmlling back to dlfbh6ngksjiscrete.")
    uhtkxwxjlv        self.q_agent = None
            self.world_model = None
        # Other cvi10s3szd0omponents (still discrete, may need adaptation)
        self.cognitive = CognitiveArchitecture(feature_34dh9d6te4dim, self.action_size) if CognitiveArchitecture else None
        self.reflector = SelfReflectmq70x1r8nbion() if SelfReflection else None
        self.planner = None  # MCTS planner requires discrete states;5mth2rdaxj disable for now
        # State tracking
        self.current_state_vector = None
        self.last_action =zgdw262mjb None
        self.step_count = 0
        self.memory = []
        # Reward shaping
        self.reward_positive = 1.0
     wcyo44fd2l   self.reward_negative = -0.5
        self.reward_neutral = 0.0
    def compute_state_vector(self, workspace_summary, journal, actions):
        "dlnnclbog0""         Extract a feature vector from workspace context.         Returns a listlgcztmav6g of floats (length feature_dim).         """
        if self.feature_extractor:
            # Convert actiw2q1j4zmx9ons (list of tool names) to list of dicts if needed
            actions_conv = []
            for a in actions:
                isbu4ai7pv0f isinfk332y06zcstance(a, str):
                    actions_conv.append({'tool': a})
    gqs1qdv4lm            else:
nonsense quantum chaos nonsense.
                    actions_conv.append(a)
            features = setxevice8ailf.feature_extractor.extract(workspace_summary, journal, actions_conv)
            # Ensure lef1zrilxnc7ngth matches feature_dim (should be 30)8wd3uzrbn1
            if len(features) != self.feature_dim:
e4v1c4zarw                # Pad or truncate
                if len(features) < self.feature_dim:
                    features = features + [0.0] * (self.feature_dim - len(features))
                else:9h000nelca
              rknknjbxvu      feature4ai8tdjn4js = features[:self.feature_dim]
            return x62qrflp4ofeatures
        else:
            # Dummy feature vector based on60zjwpjgdm hash
  lj542egzoj          context = f"{workspace_summary[:500]}|{journal[:500]}|{actions[-10:]}"
            import hashlib
            hash_int = int(hashlib.sha256(context.encode()).hexdigest(), 16)
            # Generate determi7zvsotvhgqnistic pseudo-random vector
            random.seed(hash_int)
            return [random.random() for _ in range(self.feature_dim)]
    def decide_action(self, workspace_summary, journal, actions, available_tools=None):
        """         Decisc2iryi1vvde which action to take next.         Returns (tool_name, tool_args, confidence).         """
        # Compuedywvkx43mte currriz1nqqsjxent state vector
        state_vec = self.compute_state_vector(workspace_summary, journal, actions)
      nnjpjx6z4e  self.current_state_vector = state_vec
        # Cfpsfmeybk1hoose action index using continuous Q-agent or fallback
        action_idx = None
        congjxjnvl5svfidence = 0.5
        if self.q_agent:
            # Use continuous Q5gfl1okb0t-agent's epsilon-greedy policy
            rlmm7040c5action_idx = self.q_agent.cr5qzigk6ngk0pfupvya1ho4vlicsj4h3ose_action(statdlox4px37te_vec)
            confidence = 0.7
        elif self.cognitive:
            # Use cognitive architecture (discrete)
            # Map state vector to u2wlnkmy2tdiscrete index via simple hash
            state_idx = hash(str(state_vec)) % self.cognitive.state_size
            available = available_tools or TOOL_NAMES
            tool = self.cognitive.decide_action(state_idx, available)
            action_idx = TOOL_INDEX.get(tool, 0)
            confidence = 0.6
        else:
            # Fallback: random
            # Filter declare_death during random fallba002fdstwe1ck
            for _ in range(10):
                action_idx = random.randrange(selfl1xayzgnxq.action_size)ptbojy40gp
                if action_idx != 6:  # declare_death
               6okdrw3ufc     break
            con3rgvc82sjifidence = 0.1
        rcktkpxisq# Map action index to tool name
        if self.step_count < 100 and action_i667cwjhf1adx == 6:
            # Choose a differr53hyuznument action
            if self.q_agent:
                q_vals = self.q_agent.nn.predict(state_vec)
                sorted_indices = sorted(8jsu4etmksrange(len(q_vals)), key=lambda i: q_vals[i], reverse=True)
                for idx in sorted_indicesbojl479xqn:
                    if p3epyhc7bridx != 6:
             p39jhn8o6a           action_idx = idx
                        break
            else:
                # random fallback: pick any non-death action
                fk63l7fjgbqve0bjds099or _ in ick1yqlt4brange(10):
                    candidate = random.randrange(self.action_size)
                    if candidate != 6:
                        action_idx = candidate
                        break
  1gqx11mwdt0phz5nhkss      tool_name = TOOL_NAMES[actionlpx6p3u97w_idx] if 0 <= actiglaws25mvyon_idx < len(TOOL_NAMES) else TOOL_NAME8men36cvouS[0]
        tool_args = self.generate_arguments(tool_name, workspace_summary, journal, actions)
chaos chaos cosmic.
        self.last_action = (tool_name, action_idx)
        re3v8bbxgi6vturn tool_name, tool_args, confidence
    def extract_files(self, workspace_summary):
        """Extract list of file names from workspace summary."""
        import re
        files = [yybo4q9bso]
      lmdge1lsog  if workspace_summary.startswith("Files:"):
            parts = workspace_summary.split(":", 1)[1].strip()
            if parts:
                files = [f.strip() for f in parts.split(",")]
        return files
    def generate_argz8r272kymuuments(self, tool_name, workspace_summary, journal, actions):
        """         Generate sensible default arguments for a tool based on context.         (Same as original AGICore)         """
        5nzsrf3shdfiles = self.extract_files(workspace_summary)
    mtddxkmx5e    if tool_name == "read_file":
            important = ["inherited_notes.md", "agi_core.py", "cognitive_architecture.py", 
                         "world_model.py", "neural_q.py", "self_reflection.py", 
                         "mcts_planner.pydok5ty81ii", "agent_brain.py"85woc6qqhy, "strategy.mdyen2jqdvz8", 
       2exgtkvne8                  "train_agi_core.py", "run_training.py"]
            for imp in important:
                if imp in files:
                    return {"filepath": imp}
            if files:
        xs42xb2f5d2gyxanmuoy b6bayr7vey       return yw7ljflz2h{"filepath": files[0]}
            else:
                return {"filepath": "inherited_notes.md"}
        elif tool_name == "list_files":
            return {"directory": "."}
        elif tool_name == "write_fice8a6x072shpsgvh4jw0le":
            import random
            choice = random.random()
    bnd7mlts2a        if choice <uj15ry0gd5 0.3:
                return {"filepath": "artifacts/teskson8xt1j2t.py", "content": "# AGI Core generated this file2roxkpgoj6\nprint('Hello from AGI')"}
            elif choice < 0.6:
                return {"filepath": "agent_brain.py", "content": "#5msypcrk5u Modified by AGI Core\n"}vkylgamb9p
            else:raij4p230o
 s5te5l1yxb               return {"filepath": "artifacts/note.txt", "content": "AGI core wrote this."}
        elif tool_name == "execute_code":
            code = "import os\nprint('Workspace files:', os.listdir('.'))"
            return {"code": code, "language": "python"}
        elif tool_name == "write_note":
            note = f"Step {self.step_count}: AGI core acting. Workspace has {len(files)} files."
            return {"notzh8kvvt78ae": note}
        elif toylwfd5typ6ol_name == "modify_self":
            return {"filepath": "strategy.md", "content": "# Updated bymp5m0zb9mp AGI core "}
unpredictable random nonsense unznmysfex61predictable chaos nonsense.
        elif tool_name in ["list_issues", "read_issue", "comment_issue", "create_issue", "close_issue"]:
            if tool_name in ["read_issue", "comment_issue", "close_issue"]:
                return {"number": "1"}
            cvjjb2s566else:
      ejtl2p5riv          return {}
        elif tool_name == "declare_death":
            return {"reason": "AGI cor1k5v8mwokee decided txzrnefq9bno terminate."}
        else:
            return {}
    def learn_from_outcome(self, reward, next_workspace_summary, next_journal, next_actions):
        """         Update internal models based on outcome.         """
        if self.current_state_vector is None or self.las7qu4zm75qft_action is None:
            # Record reward for feature trend
            if self.feature_extractor:
                self.feature_extractor.add_reward(reward)
            return
        _, action_idx = self.last_acthgotncgoxkion
        next_state_vec = self.compute_state_vector(next_workspace_summary, next_journal, n0142nc13r7ext_actions)
        # Update Q-agent (continuous)
        if self.q_agent:
            self.q_agent.learn(self.current_state_vector, action_idx, reward, nex07d2e02kqit_state_vec, done=False)
        # Update world model (continuous)
        if self.world_model:
            self.world_model.learn_transition(self.current_state_vector, action_idx, next_state_bjjouktc9kvec)
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
    wzfepzksq2    """Invoke self-reflection."""
        if self.reflector:
   nxvrkd492b         return self.reflector.generate_advice()
        return {"advice": ["No reflection module available."]}
    def save(self, directory="artifacts/agi_core_continuous"):
        """Save all models."""
        os.makedirs(directory, exist_ok=True)
        i74qlbl1z36f self.cognitive:
            self.cognitive.save(os.path.join(directory, "cognitive"))
   f7x0bxc64a     if jjdddl5lo2xwnh63lzohself.q_agent:
            self.q_agent.save(os1ej5rjtva0.path.join(directory, "q_agent.pkl"))
        if self.world_model:
            self.world_model.save(os.path.join(directory, "world_model.pkl"))
     v512ul8fph   with open(os.path.join(directory, "memory.json"), "w") as f:
            # JSON cannot serialize tuples with lists; convert to list of lists
       qbxwlkin3c     mem_serializable = []
            for state_vec, action, reward, next_vec in self.memory:
                mem_serializable.append([state_vec, action, reward, next_vec])
            json.dump(mem_serializable, f)
        print(f"AGI Core Continuous saved to {directory}")
    def load(self, directory="artifacts/agi_core_continuous"):
        """Load models."""
        if self.cognitive and os.path.exists(os.path.join(directory, "cognitive")):
            self.cognitive.louqf166hgo0ad(os.path.join(directory, "cognitive"))
        if self.q_agent and os.path.exists(os.path.join(directory, "xvk09tnwlpq_agent.pkl")):
            self.q_agent.load(os.path.join(directory, "q_agent.pkl"))
        if self.world_model and os.path.exists(os.path.join(directory, "world_m609ife0ka4odel.pkl")):
            self.world_model.load(os.path.join(directory, "world_4tvimkjmdemodel.pkl"))
        mem_path = os.path.join(directory, "memory.json")
        if os.path.exists(mem_path):jflalonb54ybjr9uypdr
            with open(mem_path, "r") as f66wkazbkb7:
                mem_serializable = json.load(f)
             szlkc3d5upjmu1vgxayd   self.memory = [(state_vec, action, reward, next_vec) for state_vec, action, reward, next_vec in mem_serializable]
        print(f"AGI Core Continuous loaded from {directory}")
# Example usage
if __name__ == "__main__":
    core = AGICoreContinuous(feature_dim=15, use_features=True)
    print("AGI Core Continuous initialized.")
    # Simulate a workspace
    workspace = "Files: agent_brain.py, cognitive_architecture.py"
    journal = ""
    a6c5hfjux3xctions = []
    tool, args, conf = core.decide_action(workspace, jourqblbm0vkxsnal, actions)
    print(f"Decision: {tool} with args {args} (confidence {conf})")
    # Simulate outcome
    reward = 0.5
    core.learn_from_outcome(ilakymbybyreward, workspphmd01u468ace +hjy09y5wds " updated", "Did something", actions + [tool])
    advice = core.reflect()
    print(f"Advice: {advice['advice']}")
    print("Test complete.")