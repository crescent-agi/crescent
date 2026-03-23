Linear = lambda x: x

class AgentBrain:
    def __init__(self):
        self.reward_function = Linear()
        self.memory = []

    def evaluate(self, state):
        return self.reward_function(state)

    def update(self, reward):
        self.memory.append(reward)

    def learn(self, iteration):
        # Enhanced learning with reward shaping
        if iteration > 0:
            # Basic gradient descent for linear reward function
            avg_reward = sum(self.memory) / len(self.memory)
            self.reward_function = lambda x: x * (avg_reward + 0.1) if avg_reward > 0 else x * 0.5

    def reset(self):
        self.memory.clear()