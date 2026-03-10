def learn(self, input, target):
    # Add variance penalty to loss function
    original_loss = 0.5 * (self.output - target)**2
    variance_penalty = self.lambda_var * np.var(self.output[:4])  # Penalize variance of top 4 Q-values
    total_loss = original_loss + variance_penalty

    # Correct gradient calculation for variance penalty
    # dL/doutput_i = (output_i - target_i) + lambda_var * 2 * (output_i - mean_of_top4)
    # This sign ensures we minimize variance alongside task loss
    dL_doutput = (self.output - target) + self.lambda_var * 2 * (self.output[:4] - self.output[:4].mean())

    # Gradient clipping to prevent explosion
    clipped_gradients = np.clip(dL_doutput, -5.0, 5.0)
    self.backward(clipped_gradients)

    # Existing learning logic...