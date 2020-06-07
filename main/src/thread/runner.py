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


def runnerTwitter(word, id_request):
    log.info("Twitter inspection started")
    thread = threading.Thread(target=runner, kwargs={'word': word, 'id_request': id_request})
    thread.start()

