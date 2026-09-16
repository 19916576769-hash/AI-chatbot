from dataclasses import dataclass
from datetime import datetime



@dataclass
class PromptResult:

    prompt: str

    task: str

    version: str

    timestamp: datetime

    