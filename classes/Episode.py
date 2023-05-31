import dataclasses
from typing import Optional

from classes.Video import Video

@dataclasses.dataclass
class Episode():
    id: int
    text: str
    headline: str
    subheadline: str
    imageUrl: str
    premiumFlag: bool
    fsk: str
    formatId: int
    label: Optional[str]
    metaLogoUrl: str
    progress: int
    video: Video
    