import logging
from main.src.api.request import Request
import main.src.learning.model as learn
from main.src.logger.config import logger
from main.src.utils.tweet import clearTweets
from datetime import date

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
    stats['request_id'] = reqId

    log.info('Send values to the API')
    # req.post('/api/v1/analyze/requests', stats)
    # req.put('/api/v1/requests/'+reqId, {"update_time": date.today(), "state": "DONE"})
    log.info("Twitter inspection done")


