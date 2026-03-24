Linear = lambda x: x

class AgentBrain:
    def __init__(self):
        self.reward_function = Linear()
        self.memory = []
        self.weights = 0.1  # Initialize weights

    def evaluate(self, state):
        return self.reward_function(state)

    def update(self, reward):
        self.memory.append(reward)

    def learn(self, iteration):
        # Enhanced learning with reward shaping
        if iteration > 0:
            # Basic gradient descent for linear reward function
            if self.memory:
                avg_reward = sum(self.memory) / len(self.memory)
                # Update weights using gradient descent
                self.weights += (avg_reward - self.evaluate(state)) * 0.01

# Example usage
agent = AgentBrain()
agent.learn(100)
print(agent.weights)