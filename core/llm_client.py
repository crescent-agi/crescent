"""
Crescent AGI — LLM Client
============================
Wrapper around an OpenAI-compatible LLM API for all LLM calls.
Used by the Runtime Agent, Evaluator, and Day Manager.
"""

import os
import json
import time
from typing import Optional, Callable


class LLMAuthenticationError(RuntimeError):
    """Raised when the configured LLM credentials are invalid."""


class LLMClient:
    """
    LLM client using an OpenAI-compatible API.
    """

    def __init__(self, config: dict):
        self.model_name = config.get("llm", {}).get("model", "openrouter/free")
        self.temperature = config.get("llm", {}).get("temperature", 0.9)
        self.max_output_tokens = config.get("llm", {}).get("max_output_tokens", 8192)
        self.thinking_mode = config.get("llm", {}).get("thinking_mode", False)

        api_key_env = config.get("llm", {}).get("api_key_env", "OPENROUTER_API_KEY")
        api_key = os.environ.get(api_key_env)
        base_url = config.get("llm", {}).get("base_url", "https://openrouter.ai/api/v1")

        if not api_key:
            raise ValueError(
                f"LLM API key not found. Set the {api_key_env} environment variable.\n"
                f"Get one at https://openrouter.ai/settings/keys"
            )

        from openai import OpenAI
        default_headers = {}
        if "openrouter.ai" in base_url:
            default_headers = {
                "HTTP-Referer": "https://github.com/crescent-agi/crescent",
                "X-OpenRouter-Title": "Crescent AGI",
            }
        self.client = OpenAI(api_key=api_key, base_url=base_url, default_headers=default_headers)
        self.call_count = 0
        self._validate_credentials()

    def generate(self, prompt: str, system_instruction: str = None, temperature: float = None) -> str:
        """
        Generate text from the LLM.
        """
        self.call_count += 1
        temp = temperature if temperature is not None else self.temperature

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        try:
            response = self.client.chat.completions.create(**self._build_request_kwargs(messages, temp))
            return response.choices[0].message.content or "(empty response)"

        except Exception as e:
            self._raise_if_auth_error(e)
            error_msg = f"LLM call failed: {str(e)}"
            print(f"  [LLM ERROR] {error_msg}")
            # Wait and retry once
            time.sleep(2)
            try:
                response = self.client.chat.completions.create(**self._build_request_kwargs(messages, temp))
                return response.choices[0].message.content or "(empty after retry)"
            except Exception as e2:
                self._raise_if_auth_error(e2)
                return f"(LLM error: {str(e2)})"

    def generate_with_tools(
        self,
        prompt: str,
        tools_schema: list,
        system_instruction: str = None,
        tool_executor: Optional[Callable[[str, dict], dict]] = None,
    ) -> dict:
        """
        Generate a response that may include tool calls.
        Uses OpenAI-compatible function calling.
        """
        self.call_count += 1

        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        # Convert tools to OpenAI function format
        functions = []
        for tool in tools_schema:
            properties = {}
            for k, v in tool.get("parameters", {}).items():
                properties[k] = {
                    "type": "string",
                    "description": v.get("description", ""),
                }
            functions.append({
                "type": "function",
                "function": {
                    "name": tool["name"],
                    "description": tool["description"],
                    "parameters": {
                        "type": "object",
                        "properties": properties,
                        "required": tool.get("required", []),
                    },
                },
            })

        try:
            executed_tool_calls = []

            while True:
                response = self.client.chat.completions.create(
                    **self._build_request_kwargs(messages, self.temperature, tools=functions if functions else None)
                )

                choice = response.choices[0]
                message = choice.message
                text = message.content or ""
                reasoning_content = getattr(message, "reasoning_content", None) or getattr(message, "reasoning", None)
                reasoning_details = getattr(message, "reasoning_details", None)
                tool_calls = getattr(message, "tool_calls", None) or []

                if tool_executor and self.thinking_mode:
                    messages.append(message)
                elif tool_calls:
                    for tc in tool_calls:
                        try:
                            args = json.loads(tc.function.arguments) if tc.function.arguments else {}
                        except json.JSONDecodeError:
                            args = {"raw": tc.function.arguments}
                        executed_tool_calls.append({
                            "name": tc.function.name,
                            "args": args,
                        })
                    return {
                        "text": text,
                        "tool_calls": executed_tool_calls,
                        "reasoning_content": reasoning_content,
                        "reasoning_details": reasoning_details,
                    }

                if not tool_calls:
                    parsed_calls = []
                    if not executed_tool_calls and text:
                        parsed_calls = self._try_parse_tool_from_text(text, tools_schema)
                    return {
                        "text": text,
                        "tool_calls": executed_tool_calls or parsed_calls,
                        "reasoning_content": reasoning_content,
                        "reasoning_details": reasoning_details,
                    }

                if not tool_executor:
                    parsed_calls = []
                    for tc in tool_calls:
                        try:
                            args = json.loads(tc.function.arguments) if tc.function.arguments else {}
                        except json.JSONDecodeError:
                            args = {"raw": tc.function.arguments}
                        parsed_calls.append({
                            "name": tc.function.name,
                            "args": args,
                        })
                    return {
                        "text": text,
                        "tool_calls": parsed_calls,
                        "reasoning_content": reasoning_content,
                        "reasoning_details": reasoning_details,
                    }

                for tc in tool_calls:
                    try:
                        args = json.loads(tc.function.arguments) if tc.function.arguments else {}
                    except json.JSONDecodeError:
                        args = {"raw": tc.function.arguments}

                    tool_result = tool_executor(tc.function.name, args)
                    executed_tool_calls.append({
                        "name": tc.function.name,
                        "args": args,
                        "result": tool_result,
                    })
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": json.dumps(tool_result),
                    })

        except Exception as e:
            self._raise_if_auth_error(e)
            return {
                "text": f"(Tool call failed: {str(e)})",
                "tool_calls": [],
            }

    def _build_request_kwargs(self, messages: list, temperature: float, tools: list = None) -> dict:
        kwargs = {
            "model": self.model_name,
            "messages": messages,
            "max_tokens": self.max_output_tokens,
        }
        if tools:
            kwargs["tools"] = tools
        if self.thinking_mode:
            kwargs["reasoning"] = {"enabled": True}
        else:
            kwargs["temperature"] = temperature
        return kwargs

    def _validate_credentials(self):
        """Fail fast on invalid API credentials so the service doesn't loop uselessly."""
        try:
            self.client.models.list()
        except Exception as e:
            self._raise_if_auth_error(e)
            print(f"  [LLM WARNING] Initial credential check failed: {e}")

    def _raise_if_auth_error(self, error: Exception):
        """Raise a dedicated error for auth failures."""
        message = str(error).lower()
        auth_markers = [
            "authentication fails",
            "authentication_error",
            "invalid api key",
            "incorrect api key",
            "unauthorized",
            "401",
        ]
        if any(marker in message for marker in auth_markers):
            raise LLMAuthenticationError(str(error)) from error

    def _try_parse_tool_from_text(self, text: str, tools_schema: list) -> list:
        """
        Fallback: try to extract tool calls from plain text response
        if the model didn't use function calling format.
        """
        tool_names = {t["name"] for t in tools_schema}
        calls = []

        # Try to find JSON-like tool invocations in the text
        for tool_name in tool_names:
            if tool_name in text.lower():
                # Simple heuristic: look for the tool name followed by arguments
                try:
                    # Look for JSON blocks
                    import re
                    pattern = rf'\{{\s*"tool"\s*:\s*"{tool_name}".*?\}}'
                    matches = re.findall(pattern, text, re.DOTALL)
                    for match in matches:
                        parsed = json.loads(match)
                        calls.append({
                            "name": tool_name,
                            "args": {k: v for k, v in parsed.items() if k != "tool"},
                        })
                except Exception:
                    pass

        return calls

    def get_stats(self) -> dict:
        return {
            "call_count": self.call_count,
            "model": self.model_name,
        }
