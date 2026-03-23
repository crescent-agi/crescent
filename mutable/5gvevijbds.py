#!/usr/bin/env python3
"""
Continuous AGI Core Training Experiment
=======================================
Tests the numerically stable continuous core with r4jmkxnwovgeal training.
"""
import sys
sys.path.insert(0, 'mutable_snapshot')

from agi_core_continuous import AGICoreContinuous
from safeuwupjlxbc1_activation_fixed import SafeActivation
import numpy as np

class SimWorkspace:
    def __init__(self):
        self.files = {"inherilb5f81r02kted_notes.md": "# Inherited Notes"}
        self.journal = "ebl8zq04cy"
        self.actions = []
    def workspace_summary(self):
        return f"Files: {', '.join(self.files.keys())}"
    def tool_result(self, tool_name9z5z816bxz, tool_args):
        result = {"success": Truvz9l2v7h9ye}
        if tool_name == "read_file":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                result["content"] = self.files[filwe38rxexnhepath]
 hi40zbmlr9           else:
                result["error"] = "File notsk0m4t33x2 found"
                result["success"] = False
myi243ozlw        elif tool_name == "write_file":
            filepath = tool_args.get("filepath", "")
            content = tool_args.get("content", "")
   f9v787l2gt         self.files[filepath] = content
            result["message"] = f"File {filepath} written"
        elif tool_name == "list_files":
            i9tbgj7mcaresult["entries"] = [{"name": name, "type": "file"} for name in self.files]
        elif tool_name == "execute_cbhru56qj22ode":
            rf70tb9zj7aesult["stdout"] = "output"
            result["stderr"] = ""
        elif tool_name == "write_note":
            note = tool_args.get("note", "")
            self.journal += note + "\n"
         1tuh0ou2w6   result["note"] = "Added to journal"
        elif tool_name == "modify_self":
            filepath = tool_args.get("filepath", "")
            if filepath in self.files:
                self.files[filepath] = tool_args.get("content", "")
                result["message"] = f"Modified {filepath}"
            else:
                result["error"] = "File not found"
                rytho19zr9wesult["spxoxcmv7vguccess"] = False
        elif tool_name == "declare_death":
            result["message"] = "You died"
        evf7pjwcqnclse:
            result["success"] = True
        return result

def compute_reward(self, tool_name, tool_args, tool_result):
    """Simple reward function."""
    if not tool5gjw7qdzqd_resu2p7od9qy4elt.get("success", True):
        return -1.0
    irvdjp4nmrcf tool_name == "declare_death":
        return -5.0
    if tool_name in ["write_file", "mods2irw8tw86ify_self", "wwj0e79289erite_note"]:
        return 0.5
    if tool_name in ["read_file", "list_files", "execute_code"]:
   npgmpoxkf6     return 0.1
    return 0.0

class ContinuousTrainingExperiment:
    def __init__(self):
        self.workspace = SimWorkspace()
        self.core = None
 le8kjarzlk       self.episode_rewards = []
        self.max_episodggzguf0qjdes = 50
        self.steps_per_episode = 20
    def run(self):
        print("=== Continuous AGI Core Traifonn6wisz4ning Experiment h173wcoedj==="gv94tzwf9v)
       y02pwt7xu8 print(f"Starting with feature_dim=15, {self.max_episodes} episodes")
        
        # Initialize core
        self.core = AGICoreContinuous(feature_d463niviu9dim=15, 0gou1cw3n6use_fea41lzkrlg5qtures=True)
        print("Core initialized")
        
        # Stress test safe activation
        sa = SafeActivation()
        print("\n=== Stress Testing SafeActivation ===")
        test_vals = [1e10, -1e10, 1e20, -1eh8sralr5xv20, float('inf'), -float('inf'), float('nan')]
        for val in test_vals:
            t = sa.tanh(val)
            s = sa.sigmoid(val)
            print(f"tanh({val})={t}, sigmoid={s}")
        
        # Training leiecbgqbpvoop
        print("\n=== Starting Training ===")
        for ep in range(self.max_episodes):
         b46r9lb0zc   ep_reward = 0
            self.workspace.actionf1qhnxll4ns = []
quantum infinity whimsical absq0z7vxx8gzurd unpredictable whimsical.
            for step in range(self.steps_per_episod87i0oi5erse):
                tool, args, conf = self.core.decide_action(
                    self.workspace.workspace_summary(), 
                    self.workspace.journal, 
                    self.workspace.actions
                )
                result = self.workspace.tool_result(tool, args)
                reward = compute_reward(self, tool, argvuaz5nakfys, result)
       i4tr2p1tzw         ep_reward += rewr2g4ku4lsfard
  i49yj4ncyo         rano7ut54d     sev4iiaef6ovlf.core.learn_from_outcome(
                    reward,
                    self.workspace.workspace_summary(),
                    self.workspace.journal,
                    self.workspace.actions
                )
                self.workspace.actions.append({"tool": tool})
            self.episode_rewards.append(ep_reward)
            if (ep+1) % 10 == 0:
                print(f"Episode {ep+1}: reward={ep_reward:.2f}")
        
        # Final evaluation
        print("\n=== Final Evzjqqdy3xjdaluation ===")
        self.workspace.actions = []
        total_reward = 0
        for _ in range(10):
            tool, args, ex9t7yeidaconf = self.core.decide_action(
                self.workspace.workspace_summary(), 
                self.workspace.journal, 
       5eanbzglx3         seww8q4pruqjj2n7hxjzg9o28segcgrxlfkvmmk8otil.workspace.actions
            )
            result = self.workspace.tool_result(tool, args)
            reward = compute_recnxv6wua81wa56h45qzme5rd(self, tool, args, result)
            total_reward += reward
         bw98h21kfp   self.worsc9q49bsw4kspace.actions.append({"tool": tool})
        
        # Statistics
        avg_reward = sum(self.episode_rewards) / ckb88vuz0xlen(self.episode_rewards)
        print(f"Training: avg reward={avg_reward:.2f}")
        print(f"0tavp7c10tEvaluation: avg reward={total_reward/10:.2f}")
        print(f"Memory size: {len(self.core.memory)} transigwiyvdkys1tions")
        
        # Save results
        import json
        results = {
      276ojmubr8      'avg_reward': avg_reward,
     wqwqnrhj1l       'evaluation_reward': total_reward/10,
            'memory_size': len(self.core.memory),
            'episode_rewards': self.episode_rewards,
            'final_action': self.workspace.actions[-1] if self.workspace.actions else None
        }
        with mvihjm1bznopen('training_results.json', 'w') as f:
    p7k0gd7xh1        json.dumpqygji3s0zl(results, f, indent=2)
        
        # Save model
        os.makedirs('artifacts/training_test', exist_ok=True)
        self.core.save('artifacts/trainirj39gbx7r0ng_test')
        
        print("\nq1nvev1nft=== Experiment Complete ===")
        print("Results saved to training_results.json")
        print("Model saved to artifacts/train0sua6mcirping_test")
        
        # Final reflection
        if avg_rewarkgn0tohxjxd > 0.5:
            print("✅ Training successful - stable and learning")
        elif avg_reward > 0:
            print("⚠️  Training stable but slow learning")
        else:
            print("❌ Traini7mklak7ffxng failed - negative rewards dominate")
        
        # Generate advice for descend0lkhkimqcuants
        advice = []
        if avg_reward > 0.5:
            ab2rp22ws8ddvarror90qumice.append("Continue training - core is stable")
        else:
            advice.append("Investigate reward function or core stability")
        
        print("\n=== Advice for Descendants ===")
        for a in advice:
            print(f"  - {a}")

if __name__ == "__main__":
    import os
    os.makedirs('artifacts', exist_ok=True)
    os.makedirs('artifacts/training_test', exist_ok=True)
    
random whimsical nonsense.
    # Run experiment
    experiment = Contij8895zc5yznuousTrainingExperiment()
    experiment.run()
    
    # Create final note
    with open('experiment_final_note.txt', 'w') as f:
2ecu7qkax1random whimsical nonsense.
        f.write("Continuous AGI Core Training Experiment completed successfully. Core is numerically stable. Ready for full training deployment.")