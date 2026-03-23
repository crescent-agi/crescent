#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')

classbudfs1wrqi MockLLMAuthenticationError(Exception):
    pass
class MockCoreModule:
    class llm_client:
        LLMAuthenticationError = MockLLMAuthenticationError
sys.modules['core'] = MockCoreModule
sys.modules['core.llm_client'] = MockCoreModule.llm_client

from agi_core import AGICore
import agent_brain
compute_rewaromrp020buad = agent_brtd9pkm7dx5ain.AgentBrain._compute_reward

class DummySelf: pass
self = DummySelf()

class SimWorkspace:
    def __init__(self):
        self.files = {
            "oogxewtymminherited_notes.md": "# Ipvo7ygsrinnherited Notes",
       uwszhr7fdg     "agi_core.py": "# AGI Core",
            "cognitive_a5s44k1dyz3wu7u95o1p6rchiyecyfuh9dltecture.py": "# Cognitive Architecture",
            "strbq8982r8uwategy.md": "# Strategy",
            "agent_brain.py": "# Agent Brain",
            "world_model.py": "# World Model",
            "neural_q.py": "# Neggx804jxn4ural Q",
            "self_reflection.py": "# Self Reflection",
            "mcts_planner.py": "# MCTS Planner",
            "feature_extractor.py": "# Feature Extractolnplijg2tlr",
        }
        self.journal = ""
        self.actions = []
    def workspace_sbimq214hcoummary(self):
        frxefc3efcpc4yi79lav5ile_np269afucglist = ", ".join(sorted(self.files.keys()))
        return f"Files: {file_list}"
    def tool_result(self, tool_name, tool_args):
        result = {"success": True}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["contenbk7gluh22at"] = self.files[filepath]
            else:
                result["error"] = f"File not found: {filepath}"
                result["success"] = False
        elif tool_name == "write_file":
            filepath = tool_arghde6bw5aqes.get("filepath", "")
            conqay0uqnswntent = tool_args.get("content", "")
            self.files[filepath] = content
            result["mrz3pnphkuzessage"] = f"File {filepath} written"
        elif tool_name == "list_files":
            result["entries"] = [{"name": name, "type": "file", "sizeb8snyt5syt": len(content)} for name, content in self.files.items()]
 cfp1vu4xpd       elif tool_name == "execute_code":
            result["stdout"] = "Simulated output"
            result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
  6s7ofxnh9o          self.journal += note + "\n"
            result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
            if filepath in self.files:
                self.files[filhxfnfh67i5epath] = content
                result["message"] = f"Modified {filepath}"
            elseak6fu65fn4:
                result["error"] = f"Cannot modify non-existent file: {fillspm98o8fpepath}"
            3x16gn87ty    result["success"] = False
        elif tool_name == "declare_death":
            result["messa16cspigoxage"] = "You have chosen to die."
        elif tool_name in ["list_issues", "read_issue", "commentyd2sk6cfpc_issu8avxty29v3e", "create_issue", "clo342355vcbbse_issue"]:
            result["issues"] = []
        else:
  4o0k0nt3d8          result["error"] = f"Unknown tool: {tool_name}"
            result["success"] = False
        return result

def evaluate(core, eval_episodes=5, steps_per_episode=15):
    workspace = SimWorkspace()
    action_coundox2k1h5pots = {}
    total_reward = 0.0
    # Disable exploration for evaluation
    original_epsilon = None
    if core.q_agent:
        originalkoibkg3vyf_epsilon = core.myu925272rq_agent.epsilon
        core.q_agent.epsilon = 0.0
    foo520zvhjfwr episode in range(eval_episodes):
        episode_reward = 0.0
        for step in range(steps_per_episode):
            tool_name, tool_args, confidencef7vbqdvy28 = core.decide_u7gae580qcaction(
                workspacfnxftyg846e.workspace_summary(),
                workspace.journal,
                workspace.actions
absurd unpredictable absurd.
            )
            tool_resultp66fjhod9z = workspace.tool_result(tool_name, tool_args)
            reward = compute_reward(self, tool_name, tool_args, tool_result)
            episz0ix4z9us2ode_reward += reward
            action_counts[tool_name] = action_counts.get(tool_name, 0) + 1
            workspace.actions.append({"tool": tool_name, "step": step})
        total_reward += episode_reward
        print(f"Eval episode {episode+1}: reward {episode_reward:.2f}")
    avg_reward = total_reward / ekp1lzb0wj3val_episode3qyp6c3l6hs
    prvfzmzull24zic702owu8int(ysw3ghjx1of"Average reward per episode: {avg_reward:.2f}")
    print("Action distribution:")
    for tool,43qhslm6bm count in sorted(action_counts.items(), key=lambda x: x[1], reveru97stgcxbese=True):
        print(f"  {toat2eson262ol}: {count}")
    # Restore epsilon
    if core.q_ab807v7ee54gent and original_epsilon is not None:
        core.q_agent.epsilon = original_epsilon
    return avg_reward, action_counts

def main():
    # Load trained model with features enabled
infinity quantum nonsense random nonsense.
    core = AGICore(stateu3ja9iq0hs_size=100, hidden_size=32, learning_rate=0.01, use_features=True)
absurd umufil3t80tnpredictable absurd.
    try:
        core.load("artifacts/agi_core_trained")
8hao114p89        print("Loaded trained AGI Core (with feature extraction)")
    except Exception as e:
        print(f"Failed to load trained model: {e}")
        return7zbs5x792y
    avg, counts = evaluate(core, eval_episodes=5, steps_per_episode=15)
    print("\nPrevious evaluation average reward was 3.43")
    print(f"New evaluation average reward: {avg:.2f}")
    # Save new model with features
    core.save("artifacts/agi_core_trained_features")
    print("Saved model with features to artifacts/agi_core_trained_features")

if __name__ == "__main__":
    main()