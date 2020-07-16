import json
import os
import requests
from requests_oauthlib import OAuth1
import tweepy
from plurk_api import PlurkOAuthApi, PlurkApi


def authenticate():
    auth = tweepy.OAuthHandler(os.getenv('TWITTER_CLIENT_KEY'), os.getenv('TWITTER_CLIENT_SECRET'))
    auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
    return tweepy.API(auth)


class Request:

    def __init__(self, auth=True):
        self.api_twitter = authenticate()
        if auth:
            self.token = requests.post(os.getenv('API_URL') + '/api/v1/auth/signin', json=
                                       {
                                           "username": os.getenv('API_USERNAME'),
                                           "password":  os.getenv('API_PASSWORD')
                                       }).json()['token']
            self.auth = {'Authorization': 'Bearer ' + self.token}
        else:
            self.auth = ''

    def tweets(self, word, count=1000, language='en'):
        new_tweets = self.api_twitter.search(q=word, count=count, tweet_mode='extended')
        lang = [y for y in new_tweets if y.metadata['iso_language_code'] == language]
        texts = [x.full_text for x in lang]
        return texts

    def tumblr(self, word, count=1000):
        oauth = OAuth1(os.getenv('TUMBLR_KEY'), os.getenv('TUMBLR_SECRET'))
        payload = {'tag': word, 'limit': count}
        res = requests.get('https://api.tumblr.com/v2/tagged', params=payload, auth=oauth)
        content = json.loads(res.content)
        dif = []
        for post in content["response"]:
            if post["type"] == 'text':
                dif.append(post)
        print(dif)

    def plurk(self, word, count=1000):
        api_auth = PlurkOAuthApi(os.getenv('PLURK_APP_KEY'), os.getenv('PLURK_APP_SECRET'))
        request_token = api_auth.request_token()
        authorization_url = api_auth.authorization_url(request_token)
        access_token = api_auth.access_token(request_token, "613016")

        api = PlurkApi(os.getenv('PLURK_APP_KEY'), os.getenv('PLURK_APP_SECRET'), access_token["oauth_token"], access_token["oauth_token_secret"])
        # print(req.callAPI('/APP/PlurkSearch/search', options={'query': word, 'offset': 30}))
        print(api.request("/APP/Profile/getPublicProfile", {"user_id": 12345}))

    def get(self, route, address=os.getenv('API_URL'), query=''):
        request = address + route
        res = requests.get(request, params=query, headers=self.auth)
        return res

    def put(self, route, body=''):
        request = os.getenv('API_URL') + route
        res = requests.put(request, json=body, headers=self.auth)
        return res

    def post(self, route, body=''):
        request = os.getenv('API_URL') + route
        res = requests.post(request, json=body, headers=self.auth)
        return res
