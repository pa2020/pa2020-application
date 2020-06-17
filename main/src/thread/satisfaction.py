import logging
import os
from main.src.api.request import Request
import main.src.learning.model as learn
from main.src.logger.config import logger
from main.src.utils.tweet import clearTweets
from datetime import date

log = logging.getLogger(__name__)
logger()


def runAnalyze(word, reqId):
    req = Request()
    log.info('Requesting last tweets with : "' + word + '"')
    res = req.tweets(word)
    cleaned = clearTweets(res)
    log.info('Predicting sentiment of tweets')
    feels = learn.analyze(cleaned)
    stats = learn.statistics(feels)
    stats['word'] = word
    stats['request_id'] = reqId
    log.info('Prediction done. Sending values to the API')
    # req.post('/api/v1/analyze/requests', stats)
    req.put('/api/v1/requests/'+str(reqId), {"update_time": str(date.today()), "state": "DONE"}, {'Authorization': 'Bearer '+os.getenv('API_TOKEN')})
    return stats


def runGenerate(path):
    log.info('Generating model from')

    log.info("Generation done")


