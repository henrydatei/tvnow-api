import dataclasses

@dataclasses.dataclass
class Download():
    downloadable: bool
    downloadAvailabilityDays: int
    downloadUsageHours: int