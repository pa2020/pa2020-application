import requests
import tweepy
from main.src.api.config import *


def authenticate():
    auth = tweepy.OAuthHandler(TWITTER_CONFIG.get('client_key'), TWITTER_CONFIG.get('client_secret'))
    auth.set_access_token(TWITTER_CONFIG.get('access_token'), TWITTER_CONFIG.get('access_token_secret'))
    return tweepy.API(auth)


class Request:

    def __init__(self):
        self.api_twitter = authenticate()

    def get(self, route, query='', headers=''):
        request = API_CONFIG.get('url') + route
        res = requests.get(request, params=query, headers=headers)
        return res

    def tweets(self, word, count=100, language='fr'):
        new_tweets = self.api_twitter.search(q=word, count=count, tweet_mode='extended')
        lang = [y for y in new_tweets if y.metadata['iso_language_code'] == language]
        texts = [x.full_text for x in lang]
        return texts
