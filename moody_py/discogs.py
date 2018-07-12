import urllib2
from bs4 import BeautifulSoup
import discogs_client
from moody_py import credentials
from utils import Utils


class Discogs:
    """
    Enables querying of the Discogs database - The largest music database and marketplace in the world
    """
    def __init__(self):
        """
        Initializes Discogs search engine with Discogs API credentials
        """
        self.search_engine = discogs_client.Client('moody_py', user_token=credentials["discogs_user_token"])
        self.discogs_query = 'https://www.discogs.com/search?limit=250&sort=want%2Cdesc&style_exact={}&type=release'

    def get_random_track_by_artist(self, artist_name):
        """
        Returns a random track from a random album of a given artist
        :param artist_name: Artist to search by
        :return: Random track of a given artist
        """
        artist = self.search_engine.search(artist_name, type='artist')[0]
        random_release = Utils.get_random_from_collection(artist.releases)
        random_track = Utils.get_random_from_collection(random_release.tracklist)
        return artist_name + ' ' + random_track.title

    def get_random_track_by_genre(self, genre):
        """
        Returns a random track with the given genre
        :param genre: Genre to search by
        :return: Random track of a given genre
        """
        url = self.discogs_query.format(genre)
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        albums = soup.findAll(attrs={'class': 'card card_large float_fix shortcut_navigable'})
        random_album_id = Utils.get_random_from_collection(albums, 'data-object-id')
        album = self.search_engine.release(random_album_id)

        return album.artists[0].name + ' ' + Utils.get_random_from_collection(album.tracklist).title
