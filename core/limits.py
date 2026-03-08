"""
Crescent AGI — Death Conditions & Resource Limits
===================================================
Monitors agent behavior and detects when the agent should die.
Death is not failure — it is the engine of evolution.
"""

import time
from difflib import SequenceMatcher
from typing import Optional


class DeathCondition:
    """Represents a detected death condition."""
    def __init__(self, cause: str, details: str = ""):
        self.cause = cause
        self.details = details
        self.timestamp = time.time()

    def to_dict(self):
        return {
            "cause": self.cause,
            "details": self.details,
            "timestamp": self.timestamp,
        }

    def __str__(self):
        return f"DEATH: {self.cause} — {self.details}"


class DeathMonitor:
    """
    Watches for death conditions during a generation's life.
    Frequent death is desired — that's where evolution happens.
    """

    def __init__(self, config: dict):
        death_cfg = config.get("death", {})
        agent_cfg = config.get("agent", {})

        self.max_steps = agent_cfg.get("max_steps_per_generation", 50)
        self.max_time_seconds = agent_cfg.get("max_time_per_generation_minutes", 15) * 60
        self.max_repeated_actions = death_cfg.get("max_repeated_actions", 5)
        self.max_consecutive_self_edits = death_cfg.get("max_consecutive_self_edits", 8)
        self.loop_detection_window = death_cfg.get("loop_detection_window", 10)
        self.loop_similarity_threshold = death_cfg.get("loop_similarity_threshold", 0.85)

        self.start_time = time.time()
        self.step_count = 0
        self.action_history: list[dict] = []
        self.consecutive_self_edits = 0
        self.agent_declared_death = False
        self.crash_error: Optional[str] = None

    def record_step(self, action: dict):
        """Record an action taken by the agent."""
        self.step_count += 1
        self.action_history.append(action)

        # Track consecutive self-edits
        action_type = action.get("tool", "")
        if action_type == "modify_self":
            self.consecutive_self_edits += 1
        else:
            self.consecutive_self_edits = 0

    def record_crash(self, error: str):
        """Record that the agent crashed."""
        self.crash_error = error

    def record_self_termination(self):
        """Record that the agent declared its own death."""
        self.agent_declared_death = True

    def check(self) -> Optional[DeathCondition]:
        """
        Check all death conditions. Returns a DeathCondition if the agent
        should die, or None if it may continue living.
        """
        # 1. Crash
        if self.crash_error:
            return DeathCondition("crash", self.crash_error)

        # 2. Self-termination
        if self.agent_declared_death:
            return DeathCondition("self_termination", "Agent declared its own death")

        # 3. Timeout
        elapsed = time.time() - self.start_time
        if elapsed >= self.max_time_seconds:
            return DeathCondition("timeout", f"Exceeded {self.max_time_seconds}s ({elapsed:.1f}s elapsed)")

        # 4. Max steps
        if self.step_count >= self.max_steps:
            return DeathCondition("max_steps", f"Reached {self.step_count}/{self.max_steps} steps")

        # 5. Too many consecutive self-edits
        if self.consecutive_self_edits >= self.max_consecutive_self_edits:
            return DeathCondition(
                "excessive_self_modification",
                f"{self.consecutive_self_edits} consecutive self-edits"
            )

        # 6. Repeated actions (loop detection)
        loop = self._detect_loops()
        if loop:
            return loop

        return None

    def _detect_loops(self) -> Optional[DeathCondition]:
        """Detect if the agent is stuck in a loop."""
        if len(self.action_history) < self.loop_detection_window:
            return None

        recent = self.action_history[-self.loop_detection_window:]
        action_strs = [str(a.get("tool", "") + ":" + str(a.get("args", ""))) for a in recent]

        # Check for exact repeated actions
        from collections import Counter
        counts = Counter(action_strs)
        most_common_action, most_common_count = counts.most_common(1)[0]
        if most_common_count >= self.max_repeated_actions:
            return DeathCondition(
                "action_loop",
                f"Action '{most_common_action[:80]}' repeated {most_common_count} times in last {self.loop_detection_window} steps"
            )

        # Check for similar action sequences (sliding window)
        if len(action_strs) >= 6:
            half = len(action_strs) // 2
            first_half = " ".join(action_strs[:half])
            second_half = " ".join(action_strs[half:])
            similarity = SequenceMatcher(None, first_half, second_half).ratio()
            if similarity >= self.loop_similarity_threshold:
                return DeathCondition(
                    "sequence_loop",
                    f"Action sequence similarity {similarity:.2f} exceeds threshold {self.loop_similarity_threshold}"
                )

        return None

    def get_stats(self) -> dict:
        """Get current life stats."""
        return {
            "steps": self.step_count,
            "max_steps": self.max_steps,
            "elapsed_seconds": time.time() - self.start_time,
            "max_time_seconds": self.max_time_seconds,
            "consecutive_self_edits": self.consecutive_self_edits,
            "total_actions": len(self.action_history),
        }
