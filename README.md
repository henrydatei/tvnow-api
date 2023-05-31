# tvnow-api
A python API wrapper for RTL+ or TVNOW

Really simple wrapper, has just a few functions for getting data from RTL's TVnow/RTL+/catch-up TV/... You can use this to automatically send the data to TheMovieDB or similar services.

### Usage
- Clone the repo
- Install requirements: `pip install requests dacite`
- Create a file in your local copy of this repo (this is just an example):
```python
from TvnowAPI import TvnowAPI

api = TvnowAPI()

# search for Lets Dance
results = api.search("Lets Dance")
print(results)

# get some information for the show "Let's Dance" which has the ID 21
lets_dance = api.get_series(21)
print(lets_dance)

# get infos for the recent season, 2023
episodes = api.get_episodes_for_season(lets_dance.seasons[0])
print(episodes)
```