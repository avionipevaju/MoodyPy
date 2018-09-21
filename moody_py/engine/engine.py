import logging

import moody_py.utils as utils
from moody_py.discogs.discogs import Discogs
from moody_py.engine.moody import Moody
from moody_py.forecast.forecast import Forecast
from moody_py.models.models import TwitterPost, TwitterResponse
from moody_py.storage.storage import Redis
from moody_py.youtube.youtube import YouTube
from moody_py.models.models import Instruction


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

    def execute_task(self, instruction=Instruction.RESOLVE_WEATHER_DATA, content=None):
        """
        Creates a twitter post and posts it to moody_py twitter account
        :return: TwitterResponse: models.TwitterResponse. Status of the posted twit.
        """
        if instruction is Instruction.RESOLVE_WEATHER_DATA:
            return self.post_to_twitter_based_on_weather_data(instruction)

        if instruction is Instruction.RESOLVE_ARTIST:
            return self.post_to_twitter_based_on_artist(instruction, content)

        return TwitterResponse(twitter_status=-3, description="Instruction invalid!")

    def post_to_twitter_based_on_weather_data(self, instruction):
        """
        Posts content to Twitter based on the current weather.
        First gets the current weather and resolves a genre based on it.
        Then finds a random track of a given genre following by a YouTube search for the corresponding video.
        Afterwards finds a corresponding twit text based on the weather data
        :param instruction: models.Instruction what kind of tweet to post
        :return: twitter_response: models.TwitterResponse object containing relevant tweet response data
        """
        weather_data = self.weather.current_weather()
        genre_list = self.redis_engine.get_genre_list(weather_data)
        genre = utils.get_random_from_collection(genre_list)
        logging.info('Resolved genre: %s for weather data: %s', genre, weather_data)

        track_by_genre = self.discogs.get_random_track_by_genre(genre)
        youtube_url = self.youtube_search_engine.search_video(track_by_genre)

        post_text_list = self.redis_engine.get_time_of_day_content_list(weather_data)
        post_text = utils.get_random_from_collection(post_text_list)
        logging.info('Resolved post_text: %s for weather data: %s', post_text, weather_data)
        twitter_post = TwitterPost(post_text, youtube_url, weather_data.condition, weather_data.temperature)
        twitter_response = self.moody.tweet(twitter_post, instruction)
        return twitter_response

    def post_to_twitter_based_on_artist(self, instruction, artist):
        """
        Posts content to Twitter based on the given artist.
        Resolves a random track for a given artist and posts it to Twitter
        :param instruction: models.Instruction what kind of tweet to post
        :param artist: name of the artist performing the song
        :return: twitter_response: models.TwitterResponse object containing relevant tweet response data
        """
        if artist is None:
            logging.error('Artist parameter is empty!')
            return TwitterResponse(description='Artist parameter is empty!')

        track_by_artist = self.discogs.get_random_track_by_artist(artist)
        youtube_url = self.youtube_search_engine.search_video(track_by_artist)
        twitter_post = TwitterPost(track_by_artist, youtube_url, None, None)
        twitter_response = self.moody.tweet(twitter_post, instruction)
        return twitter_response
