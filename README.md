# GenPark Agent Runtime Hotpatch Sandbox Injector Skill

Dynamic in-memory method replacement and self-adaptation engine with deterministic rollback checkpoints.

Explore more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
sequenceDiagram
    participant Agent as Autonomous Agent
    participant Target as Target Class / Instance
    participant Patcher as RuntimeHotpatcher

    Agent->>Patcher: apply_patch(Target, "func", new_func)
    Patcher->>Patcher: Save original method in rollback stack
    Patcher->>Target: setattr(Target, "func", bound_method)
    Target-->>Agent: New behavior active

    Agent->>Patcher: rollback_last_patch()
    Patcher->>Target: setattr(Target, "func", original_method)
    Target-->>Agent: Original behavior restored
```

## Features
- Dynamic runtime method binding with standard library `types.MethodType`.
- Stack-based rollback mechanism for risk-free self-adaptation.
- Zero external dependencies.
