import dataclasses
import requests
from typing import List
import dacite

from classes.Season import Season
from classes.Series import Series
from classes.Episode import Episode

@dataclasses.dataclass
class TvnowAPI():
    
    def __post_init__(self):
        self.headers = {
            "user-agent": "RTLplus/5.2.3 (com.rtlinteractive.tvnow; build:202303231827; iOS 15.1.0) Alamofire/5.4.4",
            "accept": "*/*",
            "content-type": "application/json",
            "X-Bff-Api-Version": "2",
            "X-Client-Version": "202303231827",
            "X-Transformscope": "ios",
            "X-Pay-Type": "free",
            "Accept-Language": "de-DE;q=1.0",
            "Accept-Encoding": "gzip, deflate",
            "Transformscope": "ios",
            "X-Device-Type": "tablet"
        }
        self.host = 'https://app.tvnow.de'
    
    def get_series(self, series_id: int) -> Series:
        r = requests.get(self.host + '/page/format/' + str(series_id), headers=self.headers)
        r.raise_for_status()
        s = Series(id=series_id, title=r.json()['title'], seasons=[])
        for module in r.json()['modules']:
            if module['label'] == 'Navigation Module':
                if module['navigation']['navigationType'] == 'season':
                    for season in module['navigation']['seasonItems']:
                        s.seasons.append(Season(id=season['id'], belongs_to=series_id, navigation_type='season'))
                elif module['navigation']['navigationType'] == 'annual':
                    for season in module['navigation']['annualItems']:
                        s.seasons.append(Season(id=season['year'], belongs_to=series_id, navigation_type='annual'))
                    
        return s
    
    def get_episodes_for_season(self, season: Season) -> List[Episode]:
        if season.navigation_type == 'season':
            params = {"season": season.id}
            r = requests.get(self.host + '/module/teaserrow/format/episode/' + str(season.belongs_to), headers=self.headers, params=params)
            r.raise_for_status()
            return [dacite.from_dict(data_class=Episode, data=episode) for episode in r.json()['items']]
        elif season.navigation_type == 'annual':
            episodes = []
            for month in range(1, 13):
                params = {"year": season.id, "month": month}
                r = requests.get(self.host + '/module/teaserrow/format/episode/' + str(season.belongs_to), headers=self.headers, params=params)
                r.raise_for_status()
                if 'items' in r.json():
                    partial_episodes = [dacite.from_dict(data_class=Episode, data=episode) for episode in r.json()['items']]
                    partial_episodes.reverse()
                    episodes.extend(partial_episodes)
            return episodes
    
    def search(self, query: str) -> List[Series]:
        r = requests.get(self.host + '/search/' + query, headers=self.headers)
        r.raise_for_status()
        return [self.get_series(series['id']) for series in r.json()['items']]
            