import os

# List all Python files in the workspace
python_files = [f for f in os.listdir('.') if f.endswith('.py')]
print(f"Found {len(python_files)} Python files:")
for file in python_files:
    print(f"- {file}")