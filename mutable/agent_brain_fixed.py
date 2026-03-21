class AgentBrain:
    def __init__(self, *args, **kwargs):
        """Simplified initialization with required parameters"""
        super().__init__(*args, **kwargs)
        self.initialized = True
        if __name__ == '__main__':
            print('AgentBrain initialized successfully')