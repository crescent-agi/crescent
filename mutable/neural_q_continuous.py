def learn(self, input, target):
    # Add variance penalty to loss function
    original_loss = 0.5 * (self.output - target)**2
    variance_penalty = self.lambda_var * np.var(self.output[:4])  # Penalize variance of top 4 Q-values
    total_loss = original_loss + variance_penalty
    # Backpropagation with gradient for variance term
    dL_doutput = (self.output - target) + self.lambda_var * 2 * (self.output[:4] - self.output[:4].mean())  # Gradient of variance penalty
    self.backward(dL_doutput)
    # Existing learning logic...