from .role import build_role
from .rules import build_rules,build_style
from memory import build_memory





PROMPT_STAGES=[
    ("role",build_role),
    ("memory",build_memory),
    ("rules",build_rules),
    ("style",build_style),





]