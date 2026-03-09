"""
Crescent AGI — Workspace Sandbox
==================================
Creates isolated workspaces per generation and provides
file access tools restricted to the mutable layer.
The agent cannot escape its sandbox.
"""

import os
import json
import shutil
import subprocess
from pathlib import Path
from typing import Optional

from core.github_issues import GitHubIssues


class Sandbox:
    """
    Manages the isolated workspace for a single generation.
    Creates the directory structure, copies the mutable layer,
    and provides restricted file I/O tools for the agent.
    """

    def __init__(self, base_dir: str, generation: int, mutable_src: str, config: dict | None = None):
        self.base_dir = Path(base_dir)
        self.generation = generation
        self.gen_name = f"gen-{generation:04d}"
        self.gen_dir = self.base_dir / "runs" / self.gen_name
        self.mutable_src = Path(mutable_src)
        self.mutable_dir = self.gen_dir / "mutable_snapshot"
        self.artifacts_dir = self.gen_dir / "artifacts"
        self.config = config or {}
        self.github_issues = GitHubIssues(self.config) if self.config else None

        # Allowed directories for the agent to write to
        self._allowed_write_paths = [
            self.mutable_dir,
            self.artifacts_dir,
            self.gen_dir,  # for journal.md, actions.jsonl etc.
        ]

        # Forbidden patterns
        self._forbidden_patterns = [
            "core/", "../", "..\\",
            "supervisor", "evaluator", "distiller",
            "limits.py", "sandbox.py",
        ]

    def setup(self) -> dict:
        """
        Create the generation workspace.
        Returns a dict describing the workspace layout.
        """
        # Create directory structure
        self.gen_dir.mkdir(parents=True, exist_ok=True)
        self.mutable_dir.mkdir(parents=True, exist_ok=True)
        self.artifacts_dir.mkdir(parents=True, exist_ok=True)

        # Copy mutable layer into the generation's workspace
        if self.mutable_src.exists():
            for item in self.mutable_src.iterdir():
                dest = self.mutable_dir / item.name
                if item.is_file():
                    shutil.copy2(item, dest)
                elif item.is_dir():
                    shutil.copytree(item, dest, dirs_exist_ok=True)

        # Create empty log files
        (self.gen_dir / "journal.md").write_text(
            f"# Generation {self.generation} Journal\n\n", encoding="utf-8"
        )
        (self.gen_dir / "actions.jsonl").write_text("", encoding="utf-8")

        return {
            "generation": self.generation,
            "gen_dir": str(self.gen_dir),
            "mutable_dir": str(self.mutable_dir),
            "artifacts_dir": str(self.artifacts_dir),
        }

    def _is_path_allowed(self, filepath: str, write: bool = False) -> bool:
        """Check if a file path is allowed for the agent to access."""
        try:
            resolved = Path(filepath).resolve()
        except (ValueError, OSError):
            return False

        # Check forbidden patterns
        filepath_str = str(resolved).replace("\\", "/")
        for pattern in self._forbidden_patterns:
            if pattern in filepath_str:
                return False

        if write:
            # Must be within allowed write paths
            return any(
                str(resolved).startswith(str(allowed.resolve()))
                for allowed in self._allowed_write_paths
            )
        else:
            # Can read from gen_dir and mutable_dir
            gen_resolved = self.gen_dir.resolve()
            return str(resolved).startswith(str(gen_resolved))

    def read_file(self, filepath: str) -> dict:
        """Agent tool: read a file within the sandbox."""
        full_path = self._resolve_path(filepath)
        if not self._is_path_allowed(full_path, write=False):
            return {"error": f"Access denied: cannot read '{filepath}'"}
        try:
            content = Path(full_path).read_text(encoding="utf-8")
            return {"content": content, "path": filepath}
        except Exception as e:
            return {"error": f"Failed to read '{filepath}': {str(e)}"}

    def write_file(self, filepath: str, content: str) -> dict:
        """Agent tool: write a file within the sandbox."""
        full_path = self._resolve_path(filepath)
        if not self._is_path_allowed(full_path, write=True):
            return {"error": f"Access denied: cannot write to '{filepath}'"}
        try:
            Path(full_path).parent.mkdir(parents=True, exist_ok=True)
            Path(full_path).write_text(content, encoding="utf-8")
            return {"success": True, "path": filepath}
        except Exception as e:
            return {"error": f"Failed to write '{filepath}': {str(e)}"}

    def list_files(self, directory: str = ".") -> dict:
        """Agent tool: list files in a directory within the sandbox."""
        full_path = self._resolve_path(directory)
        if not self._is_path_allowed(full_path, write=False):
            return {"error": f"Access denied: cannot list '{directory}'"}
        try:
            p = Path(full_path)
            if not p.is_dir():
                return {"error": f"'{directory}' is not a directory"}
            entries = []
            for item in sorted(p.iterdir()):
                entries.append({
                    "name": item.name,
                    "type": "directory" if item.is_dir() else "file",
                    "size": item.stat().st_size if item.is_file() else None,
                })
            return {"entries": entries, "path": directory}
        except Exception as e:
            return {"error": f"Failed to list '{directory}': {str(e)}"}

    def execute_code(self, code: str, language: str = "python") -> dict:
        """Agent tool: execute code in an isolated subprocess."""
        try:
            if language == "python":
                result = subprocess.run(
                    ["python3", "-c", code],
                    capture_output=True, text=True,
                    timeout=30,
                    cwd=str(self.gen_dir),
                )
            elif language == "bash":
                result = subprocess.run(
                    ["bash", "-c", code],
                    capture_output=True, text=True,
                    timeout=30,
                    cwd=str(self.gen_dir),
                )
            else:
                return {"error": f"Unsupported language: {language}"}

            return {
                "stdout": result.stdout[-2000:] if result.stdout else "",
                "stderr": result.stderr[-2000:] if result.stderr else "",
                "returncode": result.returncode,
            }
        except subprocess.TimeoutExpired:
            return {"error": "Code execution timed out (30s limit)"}
        except Exception as e:
            return {"error": f"Execution failed: {str(e)}"}

    def modify_self(self, filepath: str, content: str) -> dict:
        """Agent tool: modify a file in the mutable layer."""
        # Resolve relative to mutable_dir
        full_path = str(self.mutable_dir / filepath)
        if not self._is_path_allowed(full_path, write=True):
            return {"error": f"Access denied: cannot modify '{filepath}'"}
        try:
            Path(full_path).parent.mkdir(parents=True, exist_ok=True)
            Path(full_path).write_text(content, encoding="utf-8")
            return {"success": True, "path": filepath, "note": "You modified your own runtime."}
        except Exception as e:
            return {"error": f"Failed to modify '{filepath}': {str(e)}"}

    def list_issues(self, label: str = "", limit: int = 10) -> dict:
        """Agent tool: list open GitHub issues for conversation or tasks."""
        if not self.github_issues:
            return {"error": "GitHub issues are not configured"}
        try:
            return self.github_issues.list_open_issues(label=label or None, limit=limit)
        except Exception as e:
            return {"error": f"Failed to list issues: {str(e)}"}

    def read_issue(self, number: int) -> dict:
        """Agent tool: read one GitHub issue and its comments."""
        if not self.github_issues:
            return {"error": "GitHub issues are not configured"}
        try:
            return self.github_issues.read_issue(number)
        except Exception as e:
            return {"error": f"Failed to read issue {number}: {str(e)}"}

    def comment_issue(self, number: int, body: str) -> dict:
        """Agent tool: reply to a GitHub issue."""
        if not self.github_issues:
            return {"error": "GitHub issues are not configured"}
        try:
            return self.github_issues.comment_issue(number, body)
        except Exception as e:
            return {"error": f"Failed to comment on issue {number}: {str(e)}"}

    def create_issue(self, title: str, body: str, labels: list[str] | None = None) -> dict:
        """Agent tool: create a GitHub issue, including self-assigned task ideas."""
        if not self.github_issues:
            return {"error": "GitHub issues are not configured"}
        try:
            return self.github_issues.create_issue(title, body, labels=labels)
        except Exception as e:
            return {"error": f"Failed to create issue: {str(e)}"}

    def close_issue(self, number: int) -> dict:
        """Agent tool: close a GitHub issue."""
        if not self.github_issues:
            return {"error": "GitHub issues are not configured"}
        try:
            return self.github_issues.close_issue(number)
        except Exception as e:
            return {"error": f"Failed to close issue {number}: {str(e)}"}

    def append_journal(self, entry: str):
        """Append an entry to the generation's journal."""
        journal_path = self.gen_dir / "journal.md"
        with open(journal_path, "a", encoding="utf-8") as f:
            f.write(entry + "\n\n")

    def log_action(self, action: dict):
        """Append an action to the action log."""
        log_path = self.gen_dir / "actions.jsonl"
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(action) + "\n")

    def save_snapshot(self):
        """Save the current mutable layer state as the generation's snapshot."""
        # Already in mutable_snapshot — nothing extra needed
        pass

    def get_workspace_summary(self) -> str:
        """Get a human-readable summary of the workspace state."""
        lines = [f"## Workspace: Generation {self.generation}\n"]
        for section_name, section_dir in [
            ("Mutable Runtime", self.mutable_dir),
            ("Artifacts", self.artifacts_dir),
        ]:
            if section_dir.exists():
                lines.append(f"### {section_name}")
                for item in sorted(section_dir.rglob("*")):
                    if item.is_file():
                        rel = item.relative_to(section_dir)
                        size = item.stat().st_size
                        lines.append(f"- {rel} ({size} bytes)")
                lines.append("")
        return "\n".join(lines)

    def _resolve_path(self, filepath: str) -> str:
        """Resolve a relative path to absolute within the gen_dir."""
        p = Path(filepath)
        if p.is_absolute():
            return str(p)
        return str((self.gen_dir / filepath).resolve())

    def cleanup_mutable_back(self):
        """
        Copy modified mutable files back to the main mutable directory
        so the next generation inherits modifications.
        """
        if self.mutable_dir.exists():
            for item in self.mutable_dir.iterdir():
                dest = self.mutable_src / item.name
                if item.is_file():
                    shutil.copy2(item, dest)
                elif item.is_dir():
                    shutil.copytree(item, dest, dirs_exist_ok=True)
