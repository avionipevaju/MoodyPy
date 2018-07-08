import twitter
import json


class Moody:
    """
    Enables moody_py Twitter functionality by using python-twitter wrapper for Twitter API.
    """

    def __init__(self):
        with open('credentials.json') as json_file:
            data = json.load(json_file)
        self.api = twitter.Api(consumer_key=data["consumer_key"],
                               consumer_secret=data["consumer_secret"],
                               access_token_key=data["access_token_key"],
                               access_token_secret=data["access_token_secret"])

    def verify_credentials(self):
        try:
            self.api.VerifyCredentials()
            print('Successfully verified')
        except twitter.error.TwitterError:
            print('Invalid credentials')

    def tweet(self, content, media=None):
        try:
            status = self.api.PostUpdate(content, media=media)
            print (status)
        except twitter.TwitterError as e:
            print('Error posting twit: ' + e.message)


