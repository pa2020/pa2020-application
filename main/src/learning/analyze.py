import fasttext
import csv
from bs4 import BeautifulSoup
import re
import itertools
import demoji
from .dicts import *


def clearTweet(tweet):
    # Remove HTML content (&amp, %20...)
    tweet = BeautifulSoup(tweet, features="html.parser").get_text()

    # Special case not handled previously.
    tweet = tweet.replace('\x92', "'")
    tweet = tweet.replace("’", "'")

    # Remove hashtags/account
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)", " ", tweet).split())

    # Remove web url
    tweet = ' '.join(re.sub("(\w+:\/\/\S+)", " ", tweet).split())

    # Remove emoji (😁)
    tweet = demoji.replace(tweet)

    # Fix misspelled word (noooooot -> noot)
    tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))

    # Lower case
    tweet = tweet.lower()

    # Contraction (We have not all the same -> We haven't all the same)
    tweet = ' '.join([CONTRACTIONS[word] if word in CONTRACTIONS else word for word in tweet.split()])

    # Replace smiley ( :-) -> "smile")
    tweet = ' '.join([SMILEY[word] if word in SMILEY else word for word in tweet.split()])

    # Remove punctuation (not used in cbow model)
    tweet = ' '.join(re.sub("[\.\,\!\?\:\;\-\=]", " ", tweet).split())

    # Strip accents
    tweet = strip_accents(tweet)
    return tweet


def readData():
    with open('D:/ESGI/PA2020/application/tiny.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            print('row :', row['tweet_text'])
            print('cleared :', clearTweet(row['tweet_text']))
            print('\n____________________________________________________\n')


def readDataFile():
    with open('D:/ESGI/PA2020/application/tiny.csv', newline='') as f:
        file = f.read()
        for i in file.split(','):
            print("line :", i)


def trainModel():
    # Continuous Bag of Words Model :
    model = fasttext.train_unsupervised('D:/ESGI/PA2020/application/tiny.csv', model='cbow')
    print(model.words)


def train():
    readData()
    # clearTweet()