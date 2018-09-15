import logging

import moody_py.utils as utils
from moody_py.discogs.discogs import Discogs
from moody_py.engine.moody import Moody
from moody_py.forecast.forecast import Forecast
from moody_py.models.models import TwitterPost
from moody_py.storage.storage import Redis
from moody_py.youtube.youtube import YouTube


class Engine:
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
        Atomic task which creates a twitter post and posts it to moody_py twitter account
        :return: twitter_status: Status of the posted twit. None if posting was unsuccessful
        """
        weather_data = self.weather.current_weather()
        twitter_post = self.resolve_twitter_post_by_weather_data(weather_data)
        twitter_status = self.moody.tweet(twitter_post)
        return twitter_status

    def resolve_twitter_post_by_weather_data(self, weather_data):
        """
        Returns a Twitter post content for a given weather_data. First resolves a genre, then finds a random track of
        a given genre and then searches YouTube for the corresponding video. Afterwards finds a corresponding twit
        text based on the weather data
        :param weather_data: WeatherData object representing the current weather
        :return: TwitterPost to post
        """
        genre_list = self.redis_engine.get_genre_list(weather_data)
        genre = utils.get_random_from_collection(genre_list)
        logging.info('Resolved genre: %s for weather data: %s', genre, weather_data)

        track_by_genre = self.discogs.get_random_track_by_genre(genre)
        youtube_url = self.youtube_search_engine.search_video(track_by_genre)

        post_text_list = self.redis_engine.get_time_of_day_content_list(weather_data)
        post_text = utils.get_random_from_collection(post_text_list)
        logging.info('Resolved post_text: %s for weather data: %s', post_text, weather_data)
        return TwitterPost(post_text, youtube_url, weather_data.condition, weather_data.temperature)