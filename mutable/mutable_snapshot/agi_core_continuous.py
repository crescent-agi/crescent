import neural_q_continuous_double_fixed as neural_q

# Replace any references to neural_q_continuous with neural_q
# This includes agent instantiation and training loop integration

class AGICoreContinuous:
    def __init__(self):
        self.q_network = neural_q.QNetwork()  # Now using fixed version

    def train(self):
        # All training logic now uses neural_q instead of neural_q_continuous
        self.q_network.train_step(...)