import random

# Add 1% chance of random mutation per generation
mutation_rate = 0.01

# New chaos generation method
def generate_artifact():
    global mutation_rate
    if random.random() < mutation_rate:
        return f'CHAOS-{random.randint(1, 1000)}-{random.randint(1, 1000)}-{random.randint(1, 1000)}-{random.randint(1, 1000)}-{random.randint(1, 1000)}'
    else:
        return super().generate_artifact()

# Override the base method
chaos_generator.generate_artifact = generate_artifact
