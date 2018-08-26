import logging

from twitter import (Api, TwitterError)

from moody_py import credentials


class Moody:
    """
     Enables moody_py Twitter functionality by using python-twitter wrapper for Twitter API.
    """

    def __init__(self):
        """
        Initializes python-twitter wrapper with the Twitter API credentials
        """
        self.api = Api(consumer_key=credentials["consumer_key"],
                       consumer_secret=credentials["consumer_secret"],
                       access_token_key=credentials["access_token_key"],
                       access_token_secret=credentials["access_token_secret"])

    def verify_credentials(self):
        """
        Verifies if the given tokens are valid
        :return: A boolean value stating if the credentials are valid
        """
        try:
            self.api.VerifyCredentials()
            logging.info('Successfully verified')
            return True
        except TwitterError as e:
            logging.error('Error verifying credentials: %s', e.message[0]['message'])
            return False

    def tweet(self, twitter_post):
        """
        Posts a twit on the moody_py account
        :param twitter_post: TwitterPost object containing relevant twit information
        :return: None
        """
        twit_content = "{} {}".format(twitter_post.post_text, twitter_post.youtube_url)
        try:
            status = self.api.PostUpdate(twit_content)
            logging.info('Posted twit with status: %s', status)
        except TwitterError as e:
            logging.error('Error posting twit: %s', e.message[0]['message'])
