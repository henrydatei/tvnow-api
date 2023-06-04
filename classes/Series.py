import dataclasses
from typing import List

from classes.Season import Season

@dataclasses.dataclass
class Series():
    id: int
    title: str
    seasons: List[Season]
    imageUrl: str
    