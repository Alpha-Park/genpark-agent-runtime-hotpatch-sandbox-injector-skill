"""
Agent Runtime Hotpatch Sandbox Injector Skill Client
Pure Python Standard Library implementation of dynamic runtime method replacement.
Enables autonomous agents to swap out buggy, slow, or deprecated methods in-memory,
maintaining an audit log of patches and supporting atomic rollbacks.
"""

from typing import List, Dict, Any, Tuple, Optional, Callable
import types


class HotpatchRecord:
    def __init__(self, target_obj: Any, attr_name: str, original_func: Callable, patch_func: Callable):
        self.target_obj = target_obj
        self.attr_name = attr_name
        self.original_func = original_func
        self.patch_func = patch_func


class RuntimeHotpatcher:
    def __init__(self):
        self.patch_history: List[HotpatchRecord] = []

    def apply_patch(self, target_obj: Any, attr_name: str, new_func: Callable) -> bool:
        """Replace target_obj.attr_name with new_func in-memory."""
        if not hasattr(target_obj, attr_name):
            return False
        original = getattr(target_obj, attr_name)
        record = HotpatchRecord(target_obj, attr_name, original, new_func)
        self.patch_history.append(record)

        # Bind method if target is an instance
        if not isinstance(new_func, (classmethod, staticmethod)) and not isinstance(target_obj, type):
            bound_method = types.MethodType(new_func, target_obj)
            setattr(target_obj, attr_name, bound_method)
        else:
            setattr(target_obj, attr_name, new_func)
        return True

    def rollback_last_patch(self) -> bool:
        """Revert the most recent hotpatch."""
        if not self.patch_history:
            return False
        record = self.patch_history.pop()
        setattr(record.target_obj, record.attr_name, record.original_func)
        return True
