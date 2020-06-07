import logging
from main.src.api.request import Request
import main.src.learning.model as learn
from main.src.logger.config import logger
from main.src.utils.tweet import clearTweets

log = logging.getLogger(__name__)
logger()


def runner(word, reqId):
    log.info('Requesting last tweets with : "' + word + '"')
    req = Request()
    res = req.tweets(word)
    cleaned = clearTweets(res)

    log.info('Predicting sentiment of tweets')
    feels = learn.analyze(cleaned)
    stats = learn.statistics(feels)
    stats['word'] = word

    log.info('Send values to the API')
    # req.post('/api/v1/analyze/request', stats)
    # req.post('/api/v1/request', {"state": "DONE"})
    log.info("Twitter inspection done")


