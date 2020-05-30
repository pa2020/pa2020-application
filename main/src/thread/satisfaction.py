import threading
from time import sleep

from main.src.api.request import Request


def runner(word):
    # request on twitter
    req = Request()
    res = req.tweets(word)

    # update mysql -> RUNNING #
    # req.post(
    #     '/request/sate',
    #     body={
    #         'state': 'RUNNING'
    #     })

    # exec machine learning
    # update mysql -> datas
    # update mysql -> DONE

