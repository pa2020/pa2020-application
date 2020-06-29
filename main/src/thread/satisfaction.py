import logging
import os
from datetime import datetime

import main.src.learning.model as learn
from main.src.api.request import Request
from main.src.logger.config import logger
from main.src.utils.tweet import clearTweets

log = logging.getLogger(__name__)
logger()


def runAnalyze(word, reqId):
    now = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))  # 2020-06-29T08:29:46.965000000
    req = Request()
    log.info('Requesting last tweets with : "' + word + '"')
    res = req.tweets(word)
    cleaned = clearTweets(res)
    log.info('Predicting sentiment of tweets')
    feels = learn.analyze(cleaned)
    stats_sentence, stats_ratio = learn.statistics(feels)
    print(now)
    ret = stats_ratio
    ret['word'] = word
    ret['request_id'] = reqId
    stats_table = {
        'analyze_quantity': stats_ratio['total'],
        'average_feeling': stats_ratio['positive'] - stats_ratio['negative'],
        'positive_comment': stats_ratio['positive'],
        'negative_comment': stats_ratio['negative'],
        'neutral_comment': stats_ratio['neutral'],
        'created_time': now
    }
    stats_ratio['requests'] = {'request_id': reqId}
    stats_ratio['unanalyzed'] = 0
    log.info('Prediction done. Sending values to the API')

    word_id = req.post('/api/v1/word/send', {"word": word.lower()})
    stats_table['words'] = {'id': word_id.json()['id']}
    req.post('/api/v1/stats/', stats_table)

    req.post('/api/v1/analyzes/', stats_ratio)
    req.put('/api/v1/requests/'+str(reqId), {"update_time": now, "state": "DONE"})
    return ret


def runGenerate(path):
    log.info('Generating model from')

    log.info("Generation done")


