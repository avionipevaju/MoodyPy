import logging
import time

import schedule

import moody_py.utils as utils
from moody_py.discogs.discogs import Discogs
from moody_py.engine.moody import Moody
from moody_py.forecast.forecast import Forecast
from moody_py.storage.storage import Redis
from moody_py.youtube.youtube import YouTube
from moody_py.models.models import Content


class Core:
    """
    Moody_py core functionality. Genre resolving according to current weather. Artist and song resolving according to
    a specific genre. YouTube search. Content posting to moody_py twitter account. Task scheduling.
    """

    LOCATION = 'Belgrade'

    def __init__(self):
        self.moody = Moody()
        self.moody.verify_credentials()
        self.weather = Forecast(self.LOCATION)
        self.youtube_search_engine = YouTube()
        self.discogs = Discogs()
        self.redis_engine = Redis()

    def execute_task(self):
        """
        Atomic task which collects the current weather data, resolves the genre, artist and song accordingly and
        then performs a YouTube search with the resolved data. YouTube search result is posted to moody_py
        twitter account
        :return:
        """
        weather_data = self.weather.current_weather()
        content = self.resolve_content_by_weather_data(weather_data)
        track_by_genre = self.discogs.get_random_track_by_genre(content.genre)
        youtube_url = self.youtube_search_engine.search_video(track_by_genre)
        self.moody.tweet("{} {}".format(content.content, youtube_url))

    def resolve_content_by_weather_data(self, weather_data):
        """
        Returns a genre for a given weather_data
        :param weather_data: WeatherData object representing the current weather
        :return: String represented genre
        """
        genre_list = self.redis_engine.get_genre_list(weather_data)
        genre = utils.get_random_from_collection(genre_list)
        content_list = self.redis_engine.get_time_of_day_content_list(weather_data)
        content = utils.get_random_from_collection(content_list)
        logging.info('Resolved genre: %s for weather data: %s', genre, weather_data)
        return Content(genre, content)

    def schedule(self):
        """
        Schedules moody_py task to execute periodically.
        :return:
        """
        schedule.every(30).seconds.do(self.execute_task)
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    core = Core()
    #core.schedule()
    core.execute_task()
