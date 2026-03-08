#!/usr/bin/env python3
"""
Crescent AGI — Main Entry Point
===================================
The whole organism. Each agent instance is just one life.
"""

import sys
import yaml
from pathlib import Path


def main():
    base_dir = Path(__file__).parent.resolve()

    # Load config
    config_path = base_dir / "config.yaml"
    if not config_path.exists():
        print("ERROR: config.yaml not found.")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Ensure directories exist
    for dir_key in ["runs_dir", "genome_dir", "journals_dir", "docs_dir"]:
        d = base_dir / config["paths"][dir_key]
        d.mkdir(parents=True, exist_ok=True)

    # Import and start supervisor
    from core.supervisor import Supervisor
    supervisor = Supervisor(config, str(base_dir))

    print("\n🌙 Crescent AGI starting...\n")
    supervisor.run()


if __name__ == "__main__":
    main()
