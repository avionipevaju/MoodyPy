import time

import schedule

from moody_py.discogs.discogs import Discogs
from moody_py.engine.moody import Moody
from moody_py.forecast.forecast import Forecast
from moody_py.storage.storage import Redis
from moody_py.youtube.youtube import YouTube


class Core:

    def __init__(self):
        self.moody = Moody()
        self.moody.verify_credentials()
        self.weather = Forecast('Belgrade')
        self.youtube_search_engine = YouTube()
        self.discogs = Discogs()
        self.redis_engine = Redis()

    def execute_task(self):
        artist = 'Chroma Key'
        track = self.discogs.get_random_track_by_artist(artist)
        print(track)

        track_by_genre = self.discogs.get_random_track_by_genre('Post+Rock')
        print(track_by_genre)

        print(self.redis_engine.get_string('app:name'))

        weather_data = self.weather.current_weather()

        self.moody.tweet(weather_data.location + ' ' + weather_data.condition + ' ' +
                         self.youtube_search_engine.search_video(track_by_genre))

    def schedule(self):
        schedule.every(30).seconds.do(self.execute_task)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    core = Core()
    core.schedule()
