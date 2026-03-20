"""
Crescent AGI — Runtime Agent Brain (MUTABLE)
===============================================
THIS FILE IS IN THE MUTABLE LAYER.
The agent can modify this file during its lifetime.

The mortal creature. Unstable by design. Allowed to fail badly.
"""

import json
import time
from pathlib import Path
from typing import Optional


class AgentBrain:
    """
    The Runtime Agent — an LLM-powered reasoning loop.
    Receives a goal, inherited wisdom, and workspace tools.
    Lives for a limited time, then dies.
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
            "description": "Modify a file in your own mutable runtime layer. Use with caution — bad edits may kill you.",
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
    ]

    def __init__(self, llm_client, sandbox, death_monitor, generation: int):
        self.llm = llm_client
        self.sandbox = sandbox
        self.death_monitor = death_monitor
        self.generation = generation
        self.step = 0

    def run(self, goal: str, inherited_notes: str, genome: dict, prompt_text: str) -> dict:
        """
        Run the agent's life loop.

        Args:
            goal: The vague goal ("build agi")
            inherited_notes: Notes from previous generations
            genome: Current genome state
            prompt_text: The runtime prompt (from mutable/prompt.txt)

        Returns:
            dict with final stats and death info
        """
        # Build the system prompt
        system_prompt = prompt_text

        # Build the initial context
        workspace_summary = self.sandbox.get_workspace_summary()
        mutations_str = ""
        if genome.get("active_mutations"):
            mutations_str = "\n\nyour current behavioral mutations (follow these):\n"
            for m in genome["active_mutations"]:
                mutations_str += f"- {m}\n"

        initial_prompt = f"""your goal is: {goal}

you are generation {self.generation}.

{inherited_notes}

{mutations_str}

your workspace:
{workspace_summary}

you have these tools available: read_file, write_file, list_files, execute_code, write_note, modify_self, declare_death

begin your life. what will you do first?"""

        conversation_history = [
            {"role": "user", "content": initial_prompt}
        ]

        result = {
            "steps": 0,
            "death_cause": None,
            "final_journal": "",
        }

        print(f"  [GEN-{self.generation:04d}] Agent awakens...")

        while True:
            self.step += 1

            # Check death conditions BEFORE acting
            death = self.death_monitor.check()
            if death:
                result["death_cause"] = str(death)
                print(f"  [GEN-{self.generation:04d}] {death}")
                break

            # Call LLM with tools
            try:
                full_prompt = self._build_step_prompt(conversation_history)
                response = self.llm.generate_with_tools(
                    full_prompt,
                    self.TOOLS_SCHEMA,
                    system_instruction=system_prompt,
                )
            except Exception as e:
                self.death_monitor.record_crash(f"LLM call failed: {str(e)}")
                result["death_cause"] = f"crash: LLM call failed: {str(e)}"
                break

            # Process the response
            agent_text = response.get("text", "")
            tool_calls = response.get("tool_calls", [])

            # Log the agent's thinking
            if agent_text:
                self.sandbox.append_journal(f"### Step {self.step}\n{agent_text}")

            # Execute tool calls
            tool_results = []
            for tc in tool_calls:
                tool_result = self._execute_tool(tc["name"], tc.get("args", {}))
                tool_results.append({
                    "tool": tc["name"],
                    "args": tc.get("args", {}),
                    "result": tool_result,
                })

                # Record action for death monitoring
                action = {
                    "step": self.step,
                    "tool": tc["name"],
                    "args": tc.get("args", {}),
                    "timestamp": time.time(),
                }
                self.death_monitor.record_step(action)
                self.sandbox.log_action(action)

                # Check if agent declared death
                if tc["name"] == "declare_death":
                    self.death_monitor.record_self_termination()
                    break

            # If no tool calls, the agent is just thinking — still counts as a step
            if not tool_calls:
                action = {
                    "step": self.step,
                    "tool": "think",
                    "args": {"thought": agent_text[:200] if agent_text else ""},
                    "timestamp": time.time(),
                }
                self.death_monitor.record_step(action)
                self.sandbox.log_action(action)

            # Build tool results feedback
            if tool_results:
                results_str = "\n".join([
                    f"[{tr['tool']}] → {json.dumps(tr['result'])[:500]}"
                    for tr in tool_results
                ])
                conversation_history.append({"role": "assistant", "content": agent_text or "(acted silently)"})
                conversation_history.append({"role": "user", "content": f"Tool results:\n{results_str}\n\nContinue. What's your next move?"})
            else:
                conversation_history.append({"role": "assistant", "content": agent_text or "(silence)"})
                conversation_history.append({"role": "user", "content": "You didn't use any tools. Take action or declare_death if you're done."})

            # Keep conversation history manageable
            if len(conversation_history) > 30:
                # Keep first 2 and last 20 messages
                conversation_history = conversation_history[:2] + conversation_history[-20:]

            # Check death again after acting
            death = self.death_monitor.check()
            if death:
                result["death_cause"] = str(death)
                print(f"  [GEN-{self.generation:04d}] {death}")
                break

            print(f"  [GEN-{self.generation:04d}] Step {self.step}: {tool_calls[0]['name'] if tool_calls else 'think'}")

        result["steps"] = self.step
        result["stats"] = self.death_monitor.get_stats()
        result["llm_stats"] = self.llm.get_stats()

        # Read final journal
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
            elif tool_name == "write_file":
                return self.sandbox.write_file(args.get("filepath", ""), args.get("content", ""))
            elif tool_name == "list_files":
                return self.sandbox.list_files(args.get("directory", "."))
            elif tool_name == "execute_code":
                return self.sandbox.execute_code(args.get("code", ""), args.get("language", "python"))
            elif tool_name == "write_note":
                note = args.get("note", "")
                self.sandbox.append_journal(f"**Note:** {note}")
                return {"success": True, "note": "Added to journal"}
            elif tool_name == "modify_self":
                return self.sandbox.modify_self(args.get("filepath", ""), args.get("content", ""))
            elif tool_name == "declare_death":
                reason = args.get("reason", "no reason given")
                self.sandbox.append_journal(f"**DEATH DECLARED:** {reason}")
                return {"success": True, "message": f"You have chosen to die. Reason: {reason}"}
            else:
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
