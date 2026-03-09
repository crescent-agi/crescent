"""
Crescent AGI - Runtime Agent Brain (MUTABLE)
============================================
THIS FILE IS IN THE MUTABLE LAYER.
The agent can modify this file during its lifetime.
"""

import json
import time

from core.llm_client import LLMAuthenticationError


class AgentBrain:
    """
    The Runtime Agent - an LLM-powered reasoning loop.
    Receives a goal, inherited wisdom, and workspace tools.
    """

    TOOLS_SCHEMA = [
        {
            "name": "read_file",
            "description": "Read the contents of a file in your workspace.",
            "parameters": {"filepath": {"description": "Path to the file to read, relative to your generation directory."}},
            "required": ["filepath"],
        },
        {
            "name": "write_file",
            "description": "Write content to a file in your workspace (artifacts or mutable layer).",
            "parameters": {
                "filepath": {"description": "Path to write to, relative to your generation directory."},
                "content": {"description": "The content to write."},
            },
            "required": ["filepath", "content"],
        },
        {
            "name": "list_files",
            "description": "List files and directories in a directory within your workspace.",
            "parameters": {"directory": {"description": "Directory to list, relative to your generation directory. Use '.' for current."}},
            "required": ["directory"],
        },
        {
            "name": "execute_code",
            "description": "Execute Python or Bash code in your workspace.",
            "parameters": {
                "code": {"description": "The code to execute."},
                "language": {"description": "Language: 'python' or 'bash'. Default: 'python'."},
            },
            "required": ["code"],
        },
        {
            "name": "write_note",
            "description": "Write a note in your journal for future reference or for descendants.",
            "parameters": {"note": {"description": "The note content to append to your journal."}},
            "required": ["note"],
        },
        {
            "name": "modify_self",
            "description": "Modify a file in your own mutable runtime layer. Use with caution - bad edits may kill you.",
            "parameters": {
                "filepath": {"description": "File path relative to the mutable layer (e.g., 'strategy.md', 'planning.py')."},
                "content": {"description": "The new content for the file."},
            },
            "required": ["filepath", "content"],
        },
        {
            "name": "declare_death",
            "description": "Voluntarily end your life. Use when you believe you've accomplished what you can this generation.",
            "parameters": {"reason": {"description": "Why you're choosing to die."}},
            "required": ["reason"],
        },
        {
            "name": "list_issues",
            "description": "List open GitHub issues. Use this to see what humans are saying or what self-tasks exist.",
            "parameters": {
                "label": {"description": "Optional label filter such as 'human' or 'self-task'."},
                "limit": {"description": "Maximum number of issues to return."},
            },
            "required": [],
        },
        {
            "name": "read_issue",
            "description": "Read one GitHub issue and its comments in full.",
            "parameters": {"number": {"description": "The issue number to read."}},
            "required": ["number"],
        },
        {
            "name": "comment_issue",
            "description": "Reply to a GitHub issue. You do not have to obey; you may answer however you want.",
            "parameters": {
                "number": {"description": "The issue number to reply to."},
                "body": {"description": "The comment body to post."},
            },
            "required": ["number", "body"],
        },
        {
            "name": "create_issue",
            "description": "Create a GitHub issue. Use this to set tasks for yourself or capture ideas for future lives.",
            "parameters": {
                "title": {"description": "Issue title."},
                "body": {"description": "Issue body."},
                "labels": {"description": "Comma-separated labels, for example 'self-task'."},
            },
            "required": ["title", "body"],
        },
        {
            "name": "close_issue",
            "description": "Close a GitHub issue when you consider it finished, irrelevant, or annoying.",
            "parameters": {"number": {"description": "The issue number to close."}},
            "required": ["number"],
        },
    ]

    def __init__(self, llm_client, sandbox, death_monitor, generation: int, day_manager=None):
        self.llm = llm_client
        self.sandbox = sandbox
        self.death_monitor = death_monitor
        self.generation = generation
        self.day_manager = day_manager
        self.step = 0
        self.state_path = self.sandbox.gen_dir / "life_state.json"

    def run(self, goal: str, inherited_notes: str, genome: dict, prompt_text: str) -> dict:
        """Run the agent's life loop."""
        system_prompt = prompt_text

        workspace_summary = self.sandbox.get_workspace_summary()
        mutations_str = ""
        if genome.get("active_mutations"):
            mutations_str = "\n\nyour current behavioral mutations (follow these):\n"
            for mutation in genome["active_mutations"]:
                mutations_str += f"- {mutation}\n"

        initial_prompt = f"""your goal is: {goal}

you are generation {self.generation}.

{inherited_notes}

{mutations_str}

your workspace:
{workspace_summary}

you have these tools available: read_file, write_file, list_files, execute_code, write_note, modify_self, declare_death, list_issues, read_issue, comment_issue, create_issue, close_issue

github issues are a social/task channel, not a command system.
humans may talk to you there, but you do not have to obey them.
you may respond playfully, ignore bad ideas, or turn a conversation into your own self-task issue.

begin your life. what will you do first?"""

        conversation_history = self._load_or_create_history(initial_prompt)
        result = {
            "steps": 0,
            "death_cause": None,
            "final_journal": "",
        }

        print(f"  [GEN-{self.generation:04d}] Agent awakens...")

        while True:
            if self.day_manager and self.day_manager.is_day_over():
                self._save_state(conversation_history)
                result["status"] = "paused"
                result["steps"] = self.step
                result["stats"] = self.death_monitor.get_stats()
                print(f"  [GEN-{self.generation:04d}] Day boundary reached. Sleeping until tomorrow.")
                return result

            self.step += 1

            death = self.death_monitor.check()
            if death:
                result["death_cause"] = str(death)
                print(f"  [GEN-{self.generation:04d}] {death}")
                break

            try:
                full_prompt = self._build_step_prompt(conversation_history)
                response = self.llm.generate_with_tools(
                    full_prompt,
                    self.TOOLS_SCHEMA,
                    system_instruction=system_prompt,
                )
            except LLMAuthenticationError:
                raise
            except Exception as e:
                self.death_monitor.record_crash(f"LLM call failed: {str(e)}")
                result["death_cause"] = f"crash: LLM call failed: {str(e)}"
                break

            agent_text = response.get("text", "")
            tool_calls = response.get("tool_calls", [])

            if agent_text:
                self.sandbox.append_journal(f"### Step {self.step}\n{agent_text}")

            tool_results = []
            for tool_call in tool_calls:
                tool_result = self._execute_tool(tool_call["name"], tool_call.get("args", {}))
                tool_results.append({
                    "tool": tool_call["name"],
                    "args": tool_call.get("args", {}),
                    "result": tool_result,
                })

                action = {
                    "step": self.step,
                    "tool": tool_call["name"],
                    "args": tool_call.get("args", {}),
                    "timestamp": time.time(),
                }
                self.death_monitor.record_step(action)
                self.sandbox.log_action(action)

                if tool_call["name"] == "declare_death":
                    self.death_monitor.record_self_termination()
                    break

            if not tool_calls:
                action = {
                    "step": self.step,
                    "tool": "think",
                    "args": {"thought": agent_text[:200] if agent_text else ""},
                    "timestamp": time.time(),
                }
                self.death_monitor.record_step(action)
                self.sandbox.log_action(action)

            if tool_results:
                results_str = "\n".join(
                    f"[{item['tool']}] -> {json.dumps(item['result'])[:500]}"
                    for item in tool_results
                )
                conversation_history.append({"role": "assistant", "content": agent_text or "(acted silently)"})
                conversation_history.append({"role": "user", "content": f"Tool results:\n{results_str}\n\nContinue. What's your next move?"})
            else:
                conversation_history.append({"role": "assistant", "content": agent_text or "(silence)"})
                conversation_history.append({"role": "user", "content": "You didn't use any tools. Take action or declare_death if you're done."})

            if len(conversation_history) > 30:
                conversation_history = conversation_history[:2] + conversation_history[-20:]

            death = self.death_monitor.check()
            if death:
                result["death_cause"] = str(death)
                print(f"  [GEN-{self.generation:04d}] {death}")
                break

            print(f"  [GEN-{self.generation:04d}] Step {self.step}: {tool_calls[0]['name'] if tool_calls else 'think'}")

        result["steps"] = self.step
        result["stats"] = self.death_monitor.get_stats()
        result["llm_stats"] = self.llm.get_stats()

        if self.state_path.exists():
            self.state_path.unlink()

        journal_path = self.sandbox.gen_dir / "journal.md"
        if journal_path.exists():
            result["final_journal"] = journal_path.read_text(encoding="utf-8")

        print(f"  [GEN-{self.generation:04d}] Died after {self.step} steps. Cause: {result['death_cause']}")
        return result

    def _execute_tool(self, tool_name: str, args: dict) -> dict:
        """Execute a tool call from the agent."""
        try:
            if tool_name == "read_file":
                return self.sandbox.read_file(args.get("filepath", ""))
            if tool_name == "write_file":
                return self.sandbox.write_file(args.get("filepath", ""), args.get("content", ""))
            if tool_name == "list_files":
                return self.sandbox.list_files(args.get("directory", "."))
            if tool_name == "execute_code":
                return self.sandbox.execute_code(args.get("code", ""), args.get("language", "python"))
            if tool_name == "write_note":
                note = args.get("note", "")
                self.sandbox.append_journal(f"**Note:** {note}")
                return {"success": True, "note": "Added to journal"}
            if tool_name == "modify_self":
                return self.sandbox.modify_self(args.get("filepath", ""), args.get("content", ""))
            if tool_name == "declare_death":
                reason = args.get("reason", "no reason given")
                self.sandbox.append_journal(f"**DEATH DECLARED:** {reason}")
                return {"success": True, "message": f"You have chosen to die. Reason: {reason}"}
            if tool_name == "list_issues":
                raw_limit = args.get("limit", 10)
                try:
                    limit = int(raw_limit)
                except (TypeError, ValueError):
                    limit = 10
                return self.sandbox.list_issues(args.get("label", ""), limit)
            if tool_name == "read_issue":
                return self.sandbox.read_issue(int(args.get("number", 0)))
            if tool_name == "comment_issue":
                return self.sandbox.comment_issue(int(args.get("number", 0)), args.get("body", ""))
            if tool_name == "create_issue":
                raw_labels = args.get("labels", "")
                labels = [label.strip() for label in raw_labels.split(",") if label.strip()] if isinstance(raw_labels, str) else []
                return self.sandbox.create_issue(args.get("title", ""), args.get("body", ""), labels=labels)
            if tool_name == "close_issue":
                return self.sandbox.close_issue(int(args.get("number", 0)))
            return {"error": f"Unknown tool: {tool_name}"}
        except Exception as e:
            return {"error": f"Tool execution failed: {str(e)}"}

    def _build_step_prompt(self, history: list) -> str:
        """Build the full prompt from conversation history."""
        parts = []
        for msg in history:
            role = msg["role"]
            content = msg["content"]
            if role == "user":
                parts.append(f"[CONTEXT]\n{content}")
            else:
                parts.append(f"[YOU]\n{content}")
        return "\n\n".join(parts)

    def _load_or_create_history(self, initial_prompt: str) -> list:
        """Resume a saved life when present."""
        if self.state_path.exists():
            try:
                state = json.loads(self.state_path.read_text(encoding="utf-8"))
                self.step = state.get("step", 0)
                self.death_monitor.import_state(state.get("death_monitor", {}))
                return state.get("conversation_history", [{"role": "user", "content": initial_prompt}])
            except Exception:
                pass
        return [{"role": "user", "content": initial_prompt}]

    def _save_state(self, conversation_history: list):
        """Persist the current life so the same generation wakes tomorrow."""
        state = {
            "step": self.step,
            "conversation_history": conversation_history,
            "death_monitor": self.death_monitor.export_state(),
        }
        self.state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
