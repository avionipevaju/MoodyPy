import redis


class Redis:
    """
    Enables connection to Redis data storage and provides basic operation on it
    """

    def __init__(self):
        self.redis_engine = redis.StrictRedis(host='localhost', port=6379, db=0)

    def get_string(self, key):
        """
        Gets the string for a given key
        :param key: Key to search by
        :return: String value of a given key or None if it doesn't exist
        """
        return self.redis_engine.get(key)
