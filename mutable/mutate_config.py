import os
import json
import random

def mutate_config(core_dir, param='lr', factor=None):
    config_path = os.path.join(core_dir, 'cognitive', 'config.json')
    if not os.path.exists(config_path):
        print(f"Config not found: {config_path}")
        return False
    with open(config_path, 'r') as f:
        config = json.load(f)
    if param not in config:
        print(f"Param {param} not in config")
        return False
    original = config[param]
    if factor is None:
        factor = random.uniform(0.5, 2.0)
    new_val = original * factor
    config[param] = new_val
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    print(f"Mutated {param}: {original} -> {new_val} (factor {factor:.3f})")
    return True

if __name__ == '__main__':
    core = 'artifacts/agi_core_continuous_trained_gen49_quick'
    mutate_config(core)
