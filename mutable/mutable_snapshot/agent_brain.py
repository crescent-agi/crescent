class AgentBrain:
    def __init__(self, config=None, memory_init=None, learning_rate=0.01,, * exploration_rate=0.1, num_episodes=100):
        """Simplified init with required parameters"""
        super().__init__(config, memory_init, learning_rate)
        self.exploration_rate = exploration_rate
        self.num_episodes = num_episodes
        self.initialized = True
        print("AgentBrain initialized successfully") *, exploration_rate=0.1, num_episodes=100):
        """Simplified init with required parameters"""
        super().__init__(config, memory_init, learning_rate)
        self.exploration_rate = exploration_rate
        self.num_episodes = num_episodes
        self.initialized = True
        print("AgentBrain initialized successfully")