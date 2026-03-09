"""
Pure Python Q-learning Agent (no numpy)
=======================================
Lightweight reinforcement learning for AGI.
"""

import random
import pickle
import math

class PureQLearningAgent:
    def __init__(self, state_space_size, action_space_size, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.state_space_size = state_space_size
        self.action_space_size = action_space_size
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_rate
        # Q-table as list of lists
        self.q_table = [[0.0] * action_space_size for _ in range(state_space_size)]
        self.history = []
    
    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randrange(self.action_space_size)
        else:
            q_vals = self.q_table[state]
            max_q = max(q_vals)
            # If multiple actions have same max, pick random among them
            best_actions = [i for i, q in enumerate(q_vals) if q == max_q]
            return random.choice(best_actions)
    
    def learn(self, state, action, reward, next_state, done):
        current_q = self.q_table[state][action]
        max_next_q = max(self.q_table[next_state]) if not done else 0.0
        target = reward + self.gamma * max_next_q
        self.q_table[state][action] += self.lr * (target - current_q)
        self.history.append((state, action, reward, next_state, done))
    
    def save(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump({
                'q_table': self.q_table,
                'lr': self.lr,
                'gamma': self.gamma,
                'epsilon': self.epsilon,
                'history': self.history
            }, f)
    
    def load(self, filepath):
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
        self.q_table = data['q_table']
        self.lr = data['lr']
        self.gamma = data['gamma']
        self.epsilon = data['epsilon']
        self.history = data['history']


def test():
    agent = PureQLearningAgent(5, 3)
    # Teach agent that action 2 in state 0 is best
    for _ in range(100):
        state = 0
        action = agent.choose_action(state)
        reward = 1 if action == 2 else 0
        next_state = (state + 1) % 5
        agent.learn(state, action, reward, next_state, done=False)
    print("Q-table state 0:", agent.q_table[0])
    best = max(range(len(agent.q_table[0])), key=lambda i: agent.q_table[0][i])
    print(f"Best action: {best}")
    assert best == 2, "Agent didn't learn"
    print("Test passed!")


if __name__ == "__main__":
    test()