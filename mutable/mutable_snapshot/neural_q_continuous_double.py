class NeuralQLearningAgentContinuousDouble:
    # ... (existing code) 
    
    def choose_action(self, state_vector):
        """
        Epsilon-greedy action selection with input clamping.
        """
        # Clamp state vector inputs to prevent overflow
        clamped_state = [max(-10.0, min(10.0, x)) for x in state_vector]
        if random.random() < self.epsilon:
            # Random exploration with clamping
            for _ in range(10):
                action = random.randrange(self.action_size)
                if action != 6:
                    return action
            return 6
        else:
            # Use clamped state for Q-value prediction
            q_values = self.nn.predict(clamped_state)
            max_q = max(q_values)
            best_actions = [i for i, q in enumerate(q_values) if q == max_q]
            if len(best_actions) > 1 and 6 in best_actions:
                best_actions.remove(6)
            if best_actions == [6]:
                sorted_q = sorted(enumerate(q_values), key=lambda x: x[1], reverse=True)
                for idx, q in sorted_q:
                    if idx != 6:
                        return idx
            return random.choice(best_actions)

    
    def learn(self, state_vector, action, reward, next_state_vector, done):
        """
        Double DQN update with clamped inputs and entropy regularization.
        """
        # Clamp all state vectors
        clamped_state = [max(-10.0, min(10.0, x)) for x in state_vector]
        clamped_next_state = [max(-10.0, min(10.0, x)) for x in next_state_vector]
        
        # Compute entropy bonus
        q_values = self.nn.predict(clamped_state)
        exp_q = [math.exp(q) for q in q_values]
        sum_exp = sum(exp_q)
        probs = [e / sum_exp for e in exp_q]
        entropy = -sum(p * math.log(p + 1e-10) for p in probs)
        entropy_bonus = entropy_coeff * entropy
        reward_total = reward + entropy_bonus
        
        # Predict Q-values for clamped states
        q_values_next = self(nn).predict(clamped_next_state)
        best_action = max(range(self.action_size), key=lambda a: q_values_next[a])
        target_q_next = self.target_nn.predict(clamped_next_state)[best_action] if not done else 0.0
        target = reward_total + self.gamma * target_q_next
        
        # Update evaluation network with clamped inputs
        inputs = clamped_state
        output, hidden = self.nn.forward(inputs)
        self.nn.backward(inputs, hidden, output, target_q)
        self.weight_clipping()