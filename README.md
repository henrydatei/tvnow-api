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

# search for the series Lets Dance
results = api.results = api.search_series("Lets Dance")
print(results)

# get some information for the show "Let's Dance" which has the ID 21
lets_dance = api.get_series(21)
print(lets_dance)

# get infos for the recent season, 2023
episodes = api.get_episodes_for_season(lets_dance.seasons[0])
print(episodes)

# search for movies with "Die Spezialeinheit"
results = api.search_movies("Die Spezialeinheit")
print(results)

# get some information for the movie "Die Spezialeinheit - Im Einsatz mit der Bundespolizei" which has the ID 21033
movie = api.get_movie(21033)
print(movie)
```
Note: Sometimes you get a link like `https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/%x/image-147.png`. This is not a valid link, it's more like a template. TVnow offers images in multiple resolutions, just replace the `%` with on of 200, 400, 600, 800, 1200, 1400, 1600 or 1800. So this link becomes 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/200x/image-147.png, 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/400x/image-147.png, 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/600x/image-147.png, 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/800x/image-147.png, 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/1200x/image-147.png, 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/1400x/image-147.png, 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/1600x/image-147.png or 
- https://ais-cf.tvnow.de/tvnow/format/21_04metalogo/1800x/image-147.png