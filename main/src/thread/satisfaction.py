import threading
from time import sleep

from main.src.api.request import Request
from main.src.db.request import connect


def runner(word):
    print(threading.currentThread().getName())
    sleep(2)
    db = connect()
    # request on twitter
    req = Request()
    res = req.tweets(word)
    # update mysql -> RUNNING
    # exec machine learning
    # update mysql -> datas
    # update mysql -> DONE

