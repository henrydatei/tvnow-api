import dataclasses

@dataclasses.dataclass
class Season():
    id: int
    belongs_to: int
    navigation_type: str