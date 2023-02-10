from dataclasses import dataclass
from modelz import modelz

@modelz
@dataclass
class Ticket:
    id: int