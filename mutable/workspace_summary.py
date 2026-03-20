#!/usr/bin/env python3

from tools import list_files

def generate_summary(directory=''.):
    print(f"Workspace contents of '{directory}':")
    for item in list_files(directory):
        print(f"- {item}")

if __name__ == "__main__":
    generate_summary().'):
    print(f"Workspace contents of '{directory}':")
    for item in list_files(directory):
        print(f"- {item}")

if __name__ == "__main__":
    generate_summary()