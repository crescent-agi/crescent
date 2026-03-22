import os
import json
import random
import glob

def mutate_config():
    # Find all config.json files under artifacts
    config_paths = []
    for root, dirs, files in os.walk('artifacts'):
        if 'config.json' in files:
            config_paths.append(os.path.join(root, 'config.json'))
    
    if not config_paths:
        print("No config.json files found in artifacts.")
        return
    
    # Pick one randomly
    path = random.choice(config_paths)
    print(f"Selected config: {path}")
    
    # Load config
    with open(path, 'r') as f:
        config = json.load(f)
    
    # Choose a numeric hyperparameter to mutate
    numeric_keys = [k for k, v in config.items() if isinstance(v, (int, float))]
    if not numeric_keys:
        print("No numeric hyperparameters found.")
        return
    
    key = random.choice(numeric_keys)
    old_val = config[key]
    
    # Decide mutation: small random factor
    if isinstance(old_val, int):
        change = random.choice([-1, 1])
        new_val = max(1, old_val + change)
    else:  # float
        factor = random.uniform(0.9, 1.1)
        new_val = old_val * factor
    
    config[key] = new_val
    
    # Write back
    with open(path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"Mutated {key}: {old_val} -> {new_val}")

if __name__ == '__main__':
    mutate_config()