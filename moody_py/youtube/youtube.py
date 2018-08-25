import logging
import urllib
import urllib2

from bs4 import BeautifulSoup

from moody_py import utils


class YouTube:
    """
    Enables support for YouTube search
    """

    YOUTUBE_URL = 'https://www.youtube.com'
    YOUTUBE_QUERY = YOUTUBE_URL + '/results?search_query='

    def __init__(self):
        """
        Initializes YouTube search engine
        """

    def search_video(self, search_string, feeling_lucky=True):
        """
        Searches YouTube for a specific video.
        :param search_string: A string to search YouTube by
        :param feeling_lucky: If set to true it will return the first video from the result set
                Otherwise it will return a random video from the result set
        :return: A url representing the searched video, None if the video can't be found
        """
        try:
            query = urllib.quote(search_string)
            url = self.YOUTUBE_QUERY + query
            response = urllib2.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html, "html.parser")
            videos = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
            if feeling_lucky:
                target_url = self.YOUTUBE_URL + videos[0]['href']
            else:
                target_url = self.YOUTUBE_URL + utils.get_random_from_collection(videos, 'href')
            logging.info('YouTube search url: %s', target_url)
            return target_url
        except Exception as e:
            logging.error(e.message)
            return None
