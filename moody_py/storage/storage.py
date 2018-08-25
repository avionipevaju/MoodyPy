import redis


class Redis:
    """
    Enables connection to Redis data storage and provides basic operation on it
    """

    YAHOO_WEATHER_CODE = "yahoo:weather:code:"

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
        return self.redis_engine.lrange(self._assemble_search_key(key), 0, -1)

    def _assemble_search_key(self, key):
        return self.YAHOO_WEATHER_CODE + key
