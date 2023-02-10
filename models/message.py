from dataclasses import dataclass
from modelz import modelz

@modelz
@dataclass
class Message:
    name: str
    content: str