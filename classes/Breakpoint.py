import dataclasses
from typing import Optional

@dataclasses.dataclass
class Breakpoint():
    continuousPlayStart: int
    introStart: Optional[int]
    introEnd: Optional[int]