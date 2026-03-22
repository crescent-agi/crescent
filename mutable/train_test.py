from mutable_snapshot.neural_q_continuous import NeuralQAgent
import numpy as np

# Simple environment: state is 4-dim vector of random values
def random_state():
    return np.random.randn(4)

agent = NeuralQAgent(state_size=4, action_size=2, learning_rate=0.01)

# Run a few episodes
for episode in range(5):
    state = random_state()
    action = agent.choose_action(state, epsilon=0.1)
    next_state = random_state()
    reward = np.random.rand()
    done = np.random.rand() < 0.2  # 20% chance of done
    agent.update_q_value(state, action, reward, next_state, done)
    print(f"Episode {episode}, Action: {action}, Reward: {reward}")

print("Training test completed.")