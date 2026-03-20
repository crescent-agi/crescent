"""
Monte Carlo Tree Search Planner for AGI
========================================
Pure Python implementation of MCTS using a learned world model and Q‑network.
"""

import math
import random


class MCTSNode:
    """Node in the MCTS tree."""
    def __init__(self, state, parent=None, action=None):
        self.state = state          # state index
        self.parent = parent
        self.action = action        # action taken from parent to reach this node
        self.children = {}          # dict action -> MCTSNode
        self.visits = 0
        self.total_value = 0.0
        self.untried_actions = None  # list of actions not yet expanded
    
    def is_fully_expanded(self, action_space):
        if self.untried_actions is None:
            self.untried_actions = list(range(action_space))
        return len(self.untried_actions) == 0
    
    def best_child(self, exploration_weight=1.414):
        """Select child with highest UCB score."""
        return max(self.children.values(),
                   key=lambda c: c.total_value / (c.visits + 1e-6) +
                                 exploration_weight * math.sqrt(math.log(self.visits + 1) / (c.visits + 1e-6)))
    
    def add_child(self, action, child_state):
        child = MCTSNode(child_state, parent=self, action=action)
        if self.untried_actions is None:
            self.untried_actions = list(range(action_space))
        if action in self.untried_actions:
            self.untried_actions.remove(action)
        self.children[action] = child
        return child
    
    def update(self, reward):
        self.visits += 1
        self.total_value += reward


class MCTSPlanner:
    """MCTS planner using a world model and Q‑network."""
    
    def __init__(self, world_model, q_agent, action_space_size, state_space_size,
                 max_iterations=100, max_depth=10, exploration_weight=1.414):
        self.world_model = world_model
        self.q_agent = q_agent
        self.action_space_size = action_space_size
        self.state_space_size = state_space_size
        self.max_iterations = max_iterations
        self.max_depth = max_depth
        self.exploration_weight = exploration_weight
    
    def plan(self, start_state):
        """Return best action according to MCTS."""
        root = MCTSNode(start_state)
        
        for _ in range(self.max_iterations):
            node = root
            depth = 0
            
            # Selection
            while node.is_fully_expanded(self.action_space_size) and node.children:
                node = node.best_child(self.exploration_weight)
                depth += 1
                if depth >= self.max_depth:
                    break
            
            # Expansion
            if not node.is_fully_expanded(self.action_space_size) and depth < self.max_depth:
                action = random.choice(node.untried_actions)
                # Simulate transition using world model
                next_state = self.world_model.sample_next(node.state, action)
                node = node.add_child(action, next_state)
                depth += 1
            
            # Simulation (rollout)
            rollout_reward = self._rollout(node.state, depth)
            
            # Backpropagation
            while node is not None:
                node.update(rollout_reward)
                node = node.parent
                # Discount reward for each step up the tree
                rollout_reward *= 0.9
        
        # Choose best action (most visits)
        best_action = max(root.children.keys(),
                          key=lambda a: root.children[a].visits)
        return best_action
    
    def _rollout(self, state, depth):
        """Random rollout from given state to max depth, using Q‑value as final reward."""
        total_reward = 0.0
        discount = 1.0
        current_state = state
        for step in range(self.max_depth - depth):
            # Random action
            action = random.randrange(self.action_space_size)
            # Use Q‑value as immediate reward
            q_values = self.q_agent.nn.predict(self.q_agent._one_hot(current_state))
            immediate_reward = q_values[action]
            total_reward += discount * immediate_reward
            # Transition
            current_state = self.world_model.sample_next(current_state, action)
            discount *= 0.9
            # Stop if terminal? not modeled
        return total_reward


def test():
    """Simple test with dummy world model and Q‑agent."""
    # Mock classes
    class MockWorldModel:
        def sample_next(self, state, action):
            return (state + action) % 5
    
    class MockQAgent:
        def __init__(self):
            self.nn = self
        def predict(self, one_hot):
            # return random Q-values
            import random
            return [random.random() for _ in range(3)]
        def _one_hot(self, state):
            return [0]*5
    
    wm = MockWorldModel()
    qa = MockQAgent()
    planner = MCTSPlanner(wm, qa, action_space_size=3, state_space_size=5,
                          max_iterations=50, max_depth=5)
    best_action = planner.plan(start_state=0)
    print(f"MCTS selected action: {best_action}")
    print("Test passed.")


if __name__ == "__main__":
    test()