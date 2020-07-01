import os
import requests
import tweepy


def authenticate():
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_CLIENT_KEY'), os.getenv('TWITTER_CLIENT_SECRET'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    return tweepy.API(auth)


class Request:

    def __init__(self):
        self.api_twitter = authenticate()
        self.token = requests.post(os.getenv('API_URL') + '/api/v1/auth/signin', json=
                                   {
                                       "username": os.getenv('API_USERNAME'),
                                       "password":  os.getenv('API_PASSWORD')
                                   }).json()['token']
        self.auth = {'Authorization': 'Bearer ' + self.token}

    def tweets(self, word, count=1000, language='en'):
        new_tweets = self.api_twitter.search(q=word, count=count, tweet_mode='extended')
        lang = [y for y in new_tweets if y.metadata['iso_language_code'] == language]
        texts = [x.full_text for x in lang]
        return texts

    def get(self, route, address=os.getenv('API_URL'), query='', auth=False):
        request = address + route
        res = requests.get(request, params=query, headers=self.auth if auth else '')
        return res

    def put(self, route, body='', auth=False):
        request = os.getenv('API_URL') + route
        res = requests.put(request, json=body, headers=self.auth if auth else '')
        return res

    def post(self, route, body='', auth=False):
        request = os.getenv('API_URL') + route
        res = requests.post(request, json=body, headers=self.auth if auth else '')
        return res
