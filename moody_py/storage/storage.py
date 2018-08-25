import logging

import redis


class Redis:
    """
    Enables connection to Redis data storage and provides basic operation on it
    """

    YAHOO_WEATHER_CODE = 'yahoo:weather:code:{}'
    TIME_OF_DAY_CONTENT = 'time:content:{}'

    def __init__(self):
        self.redis_engine = redis.StrictRedis(host='localhost', port=6379, db=0)

    def get_string(self, key):
        """
        Gets the string for a given key
        :param key: Key to search by
        :return: String value for a given key or None if it doesn't exist
        """
        return self.redis_engine.get(key)

    def get_list(self, key):
        """
        Gets the list for a given key
        :param key: Key to search by
        :return: List of values for a given key or None if the list doesn't exist
        """
        redis_list = self.redis_engine.lrange(key, 0, -1)
        if redis_list is None:
            logging.error('No genres for code: %s', key)
            raise Exception('Genre list is None')
        return redis_list

    def get_genre_list(self, weather_data):
        """

        :param weather_data:
        :return:
        """
        return self.get_list(self._assemble_search_key(self.YAHOO_WEATHER_CODE, weather_data.condition_code))

    def get_time_of_day_content_list(self, weather_data):
        """

        :param weather_data:
        :return:
        """
        return self.get_list(self._assemble_search_key(self.TIME_OF_DAY_CONTENT, weather_data.time_of_day))

    @staticmethod
    def _assemble_search_key(base, key):
        return base.format(key)
