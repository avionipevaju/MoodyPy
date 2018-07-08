import urllib
import urllib2
import random
from bs4 import BeautifulSoup


class YouTube:
    """
    Searches YouTube for a specific video
    """
    def __init__(self):
        self.youtube_url = 'https://www.youtube.com'
        self.youtube_query = 'https://www.youtube.com/results?search_query='

    def search_video(self, search_string):
        query = urllib.quote(search_string)
        url = self.youtube_query + query
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        videos = soup.findAll(attrs={'class': 'yt-uix-tile-link'})
        index = random.randint(0, len(videos)-1)
        return self.youtube_url + videos[index]['href']

