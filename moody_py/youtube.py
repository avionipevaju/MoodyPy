import urllib
import urllib2
from bs4 import BeautifulSoup
from utils import Utils


class YouTube:
    """
    Enables support for YouTube search
    """
    def __init__(self):
        """
        Initializes YouTube search engine
        """
        self.youtube_url = 'https://www.youtube.com'
        self.youtube_query = 'https://www.youtube.com/results?search_query='

    def search_video(self, search_string, feeling_lucky=True):
        """
        Searches YouTube for a specific video.
        :param search_string: A string to search YouTube by
        :param feeling_lucky: If set to true it will return the first video from the result set
                Otherwise it will return a random video from the result set
        :return: A url representing the searched video
        """
        query = urllib.quote(search_string)
        url = self.youtube_query + query
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        videos = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
        if feeling_lucky:
            return self.youtube_url + videos[0]['href']
        else:
            return self.youtube_url + Utils.get_random_from_collection(videos, 'href')

