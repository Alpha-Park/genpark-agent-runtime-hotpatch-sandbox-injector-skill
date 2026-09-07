"""
Demonstration of Agent Runtime Hotpatch Sandbox Injector Skill
"""

from client import RuntimeHotpatcher

class MathAgent:
    def divide(self, a, b):
        return a / b  # Vulnerable to ZeroDivisionError


def safe_divide(self, a, b):
    if b == 0:
        return 0.0  # Patched safe behavior
    return a / b


def main():
    print("=== Testing In-Memory Agent Runtime Hotpatching ===")
    hotpatcher = RuntimeHotpatcher()
    agent = MathAgent()

    # Pre-patch test
    print(f"Normal division: 10 / 2 = {agent.divide(10, 2)}")

    print("\nApplying hotpatch: replacing MathAgent.divide with safe_divide...")
    ok = hotpatcher.apply_patch(agent, "divide", safe_divide)
    assert ok is True

    # Post-patch test (safe division handles zero)
    zero_res = agent.divide(10, 0)
    print(f"Patched division with zero: 10 / 0 = {zero_res}")
    assert zero_res == 0.0

    print("\nRolling back hotpatch...")
    rolled_back = hotpatcher.rollback_last_patch()
    assert rolled_back is True

    # Confirm original behavior restored
    try:
        agent.divide(10, 0)
        print("ERROR: Expected ZeroDivisionError after rollback")
        assert False
    except ZeroDivisionError:
        print("Rollback Confirmed: ZeroDivisionError correctly raised!")

    print("\nAgent Runtime Hotpatch Sandbox Injector Verification PASS!")

if __name__ == "__main__":
    main()
