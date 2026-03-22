#!/usr/bin/env python3
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from agi_core_continuous import AGICore

def main():
    config = {
        "episodes": 50,
        "max_steps": 40,
        "lr_actor": 0.001,
        "lr_critic": 0.002,
        "gamma": 0.99,
        "tau": 0.005,
        "noise_scale": 0.2,  # increased exploration
        "batch_size": 64,
        "model_dir": "artifacts/agi_core_continuous_trained_gen88",
        "log_interval": 10
    }
    os.makedirs(config["model_dir"], exist_ok=True)
    agent = AGICore(config)
    for ep in range(config["episodes"]):
        state = agent.reset()
        ep_reward = 0.0
        for t in range(config["max_steps"]):
            action = agent.act(state)
            next_state, reward, done = agent.step(action)
            agent.train_step()
            state = next_state
            ep_reward += reward
            if done:
                break
        if ep % config["log_interval"] == 0:
            print(f"Episode {ep} reward: {ep_reward:.3f}")
    agent.save(config["model_dir"], config)
    stats = {
        "episode_rewards": agent.episode_rewards,
        "final_reward": agent.episode_rewards[-1] if agent.episode_rewards else 0.0,
        "total_episodes": len(agent.episode_rewards),
        "total_steps": sum(agent.episode_lengths)
    }
    with open(os.path.join(config["model_dir"], "training_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    print("Training complete. Stats saved.")

if __name__ == "__main__":
    main()