import dataclasses
from typing import List, Optional

from classes.Breakpoint import Breakpoint
from classes.Download import Download

@dataclasses.dataclass
class Video():
    id: int
    headline: str
    subHeadline: str
    episode: int
    season: int
    fsk: Optional[str]
    fskRaw: int
    genres: List[str]
    missedType: int
    station: str
    formatId: int
    formatTitle: str
    type: str
    firstBroadcastAt: str
    alternateBroadcastDateText: str
    articleShort: str
    broadcastStartDateFormatted: str
    duration: str
    aspectRatio: str
    isDontCall: bool
    isProductPlacement: bool
    productPlacementType: bool
    isAirPlayEnabled: bool
    cornerLogo: str
    isStrictDrm1080p: bool
    timeType: int
    blockadeText: str
    isLiveStream: bool
    isDrm: bool
    free: bool
    productionYear: int
    isPriceProvided: bool
    progress: int
    subHeadlineHighlight: str
    isFree: bool
    eshBreakpoint: int
    breakpoint: Breakpoint
    forceAds: bool
    kids: bool
    formatType: str
    download: Download
    onlyPreroll: bool
    downloadable: bool
    refplanningId: int
    title: str
    broadcastStartDate: str
    formatImageUrl: str