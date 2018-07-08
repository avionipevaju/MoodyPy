import twitter
import json
import logging


class Moody:
    """
    Enables moody_py Twitter functionality by using python-twitter wrapper for Twitter API.
    """

    def __init__(self):
        try:
            with open('credentials.json') as json_file:
                data = json.load(json_file)
            self.api = twitter.Api(consumer_key=data["consumer_key"],
                                   consumer_secret=data["consumer_secret"],
                                   access_token_key=data["access_token_key"],
                                   access_token_secret=data["access_token_secret"])
        except IOError as e:
            logging.error('Couldn\'t load credentials file', e.message)

    def verify_credentials(self):
        try:
            self.api.VerifyCredentials()
            logging.info('Successfully verified')
        except twitter.TwitterError as e:
            logging.error(e.message[0]['message'])

    def tweet(self, content, media=None):
        try:
            status = self.api.PostUpdate(content, media=media)
            logging.info('Posted twit with status: %s', status)
        except twitter.TwitterError as e:
            logging.error('Error posting twit: ' + e.message[0]['message'])


