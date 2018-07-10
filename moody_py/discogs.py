import random
import discogs_client
from moody_py import credentials


class Discogs:
    """
    Enables querying of the Discogs database - The largest music database and marketplace in the world
    """
    def __init__(self):
        """
        Initiates Discogs search engine with Discogs API credentials
        """
        self.search_engine = discogs_client.Client('moody_py', user_token=credentials["discogs_user_token"])

    def get_random_track_by_artist(self, artist):
        """
        Returns a random track from a random album of a given artist
        :param artist: Artist to search by
        :return: Random track of a given artist
        """
        artist = self.search_engine.search(artist, type='artist')[0]
        releases_by_artist = artist.releases
        random_release = releases_by_artist[random.randint(0, len(releases_by_artist) - 1)]
        print(random_release.genres)
        random_track = random_release.tracklist[random.randint(0, len(random_release.tracklist) - 1)]
        return random_track.title
