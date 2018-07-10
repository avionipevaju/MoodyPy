import twitter
import logging
from moody_py import credentials


class Moody:
    """
     Enables moody_py Twitter functionality by using python-twitter wrapper for Twitter API.
    """
    def __init__(self):
        """
        Initializes python-twitter wrapper with the Twitter API credentials
        """
        self.api = twitter.Api(consumer_key=credentials["consumer_key"],
                               consumer_secret=credentials["consumer_secret"],
                               access_token_key=credentials["access_token_key"],
                               access_token_secret=credentials["access_token_secret"])

    def verify_credentials(self):
        """
        Verifies if the given tokens are valid
        :return: None
        """
        try:
            self.api.VerifyCredentials()
            logging.info('Successfully verified')
        except twitter.TwitterError as e:
            logging.error('Error verifying credentials: %s', e.message[0]['message'])

    def tweet(self, content):
        """
        Posts a twit on the moody_py account
        :param content: Content of the twit to post
        :return: None
        """
        try:
            status = self.api.PostUpdate(content)
            logging.info('Posted twit with status: %s', status)
        except twitter.TwitterError as e:
            logging.error('Error posting twit: %s', e.message[0]['message'])
