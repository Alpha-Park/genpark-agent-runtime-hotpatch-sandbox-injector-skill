"""
MCP Server for Agent Runtime Hotpatch Sandbox Injector Skill
"""

import json
import sys
from client import RuntimeHotpatcher

patcher = RuntimeHotpatcher()

def handle_call(name: str, args: dict) -> dict:
    if name == "rollback":
        ok = patcher.rollback_last_patch()
        return {"rolled_back": ok, "remaining_patches": len(patcher.patch_history)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
