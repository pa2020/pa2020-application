import csv
import logging

from bs4 import BeautifulSoup
import re
import itertools
import demoji
from .dicts import *
from ..logger.config import logger

log = logging.getLogger(__name__)
logger()


def clearTweets(tweets):
    log.info('Clearing tweets')
    return [clearTweet(tweet) for tweet in tweets]


def clearTweet(tweet):
    tweet = BeautifulSoup(tweet, features="html.parser").get_text()  # Remove HTML content (&amp, %20...)
    tweet = tweet.replace('\x92', "'")  # Special case not handled previously.
    tweet = tweet.replace("’", "'")
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)", ' ', tweet).split())  # Remove hashtags/account
    tweet = ' '.join(re.sub(r'http\S+', ' ', tweet).split())  # Remove web url
    tweet = demoji.replace(tweet)  # Remove emoji (😁)
    tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))  # Fix misspelled word (noooooot -> noot)
    tweet = tweet.lower()  # Lower case to unify the data
    tweet = ' '.join([CONTRACTIONS[word] if word in CONTRACTIONS else word for word in tweet.split()])  # Contraction (We have not -> We haven't)
    tweet = ' '.join([SMILEY[word] if word in SMILEY else word for word in tweet.split()])  # Replace smiley by his intent
    tweet = ' '.join(re.sub(r'[.,!?:;-=]', ' ', tweet).split())  # Remove punctuation (not used in cbow model)
    tweet = strip_accents(tweet)  # Strip accents
    return tweet
