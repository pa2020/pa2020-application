import logging
import threading
from main.src.logger.config import logger
from .satisfaction import *
import requests

log = logging.getLogger(__name__)
logger()


def printHello():
    threading.Timer(2.0, printHello).start()
    print("Hello")


def runnerTwitter(word, request_id):
    log.info("Twitter inspection started")
    thread = threading.Thread(target=runner, kwargs={'word': word, 'reqId': request_id})
    thread.start()

