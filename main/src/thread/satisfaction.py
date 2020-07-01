import logging
import os
from datetime import datetime

import main.src.learning.model as learn
from main.src.api.request import Request
from main.src.logger.config import logger
from main.src.utils.tweet import clearTweets
import main.src.utils.responseFormat as Format

log = logging.getLogger(__name__)
logger()


def runAnalyze(word, reqId):
    now = str(datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))  # 2020-06-29T08:29:46.965000000
    req = Request()

    # Check Blacklisted words
    blacklist = req.get('/api/v1/blacklist/filter', query=f'word={word}').status_code
    if blacklist == 200:
        log.info(f'"{word}" is Blacklisted')
        req.put(f'/api/v1/requests/{str(reqId)}', {"update_time": now, "state": "DONE"})
        ret = Format.ratio(0)
        ret['word'] = word
        ret['request_id'] = reqId
        return ret

    log.info(f'Requesting last tweets with : "{word}"')
    res = req.tweets(word)
    cleaned = clearTweets(res)

    log.info('Predicting sentiment of tweets')
    feels = learn.analyze(cleaned)
    stats_ratio = learn.statistics(feels)

    # Value to return
    ret = stats_ratio
    ret['word'] = word
    ret['request_id'] = reqId
    # Value to send in Stats
    stats_table = Format.stats(stats_ratio['total'],
                               stats_ratio['positive'],
                               stats_ratio['negative'],
                               stats_ratio['neutral'], now)
    # Value to send in analyze
    stats_ratio['requests'] = {'request_id': reqId}
    stats_ratio['unanalyzed'] = 0

    log.info('Prediction done. Sending values to the API')
    word_id = req.post('/api/v1/word/send', {"word": word.lower()})
    stats_table['words'] = {'id': word_id.json()['id']}
    req.post('/api/v1/stats/', stats_table)
    req.post('/api/v1/analyzes/', stats_ratio)
    req.put(f'/api/v1/requests/{str(reqId)}', {"update_time": now, "state": "DONE"})
    return ret
