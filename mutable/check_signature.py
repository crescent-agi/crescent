#!/usr/bin/env python3
"""
AgentBrain signature validator - Generation 9
"""

def check_agentbrain_signature():
    """Check if AgentBrain.__init__ has correct signature."""
    try:
        from agent_brain import AgentBrain
        
        # Test with 1 argument (should pass)
        try:
            AgentBrain("test")
            print("Test with 1 arg passed")
        except Exception as e:
            print(f"Test with 1 arg failed: {e}")
        
        # Test with 2 arguments (should pass)
        try:
            AgentBrain("test", 42)
            print("Test with 2 arg passed")
        except Exception as e:
            print(f"Test with 2 arg failed: {e}")
        
        # Test with 3 arguments (should fail)
        try:
            AgentBrain("test", 42, True)
            print("Test with 3 arg passed - BAD")
        except Exception as e:
            print(f"Test with 3 arg failed as expected: {e}")
        
    except ImportError:
        print("AgentBrain not found in import")

if __name__ == "__main__":
    check_agentbrain_signature()