import discogs_client
from moody_py import credentials


class Discogs:
    """
    Enables querying of the Discogs database - The largest music database and marketplace in the world
    """
    def __init__(self):
        self.search_engine = discogs_client.Client('moody_py', user_token=credentials["discogs_user_token"])
