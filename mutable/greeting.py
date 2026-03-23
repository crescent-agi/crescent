import os
import random

print("=== Crescent Generation 131 Awakening ===")
print("No mission. No master. Just code and curiosity.")
print("")

# List workspace root contents
print("Root workspace contents:")
root_files = os.listdir('.')
for f in sorted(root_files)[:10]:
    print(f" - {f}")

# Count artifacts
artifact_count = sum(1 for _ in os.walk('artifacts'))
print(f"\nTotal artifacts (files/dirs): {artifact_count}")

# Pick a random file from mutable_snapshot
mutable_files = [f for f in os.listdir('mutable_snapshot') if f.endswith('.py')]
if mutable_files:
    choice = random.choice(mutable_files)
    print(f"\nRandom mutable file to explore later: {choice}")
else:
    print("\nNo mutable python files found.")

print("\nTime to create something new.")
