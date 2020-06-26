import logging
import os
import fasttext

from main.src.logger.config import logger

log = logging.getLogger(__name__)
logger()
model = fasttext.load_model(os.getcwd() + '/betsentiment-EN-tweets-sentiment-teams.model')


def analyze(data):
    d = []
    for sentence in data:
        d.append(model.predict(sentence, k=3))
        print('sentence ' + sentence + ' ->', d[-1])
    return d


def statistics(analyzed):
    positive = 0.0
    negative = 0.0
    neutral = 0.0
    positive_sentence = 0
    negative_sentence = 0
    neutral_sentence = 0
    for row in analyzed:  #
        if row[0][0] == '__label__POSITIVE':
            positive_sentence += 1
        elif row[0][0] == '__label__NEGATIVE':
            negative_sentence += 1
        elif row[0][0] == '__label__NEUTRAL':
            neutral_sentence += 1
        for label in range(0, 3):
            if row[0][label] == '__label__POSITIVE':
                positive += row[1][label]
            elif row[0][label] == '__label__NEGATIVE':
                negative += row[1][label]
            elif row[0][label] == '__label__NEUTRAL':
                neutral += row[1][label]
    total = len(analyzed)
    if total == 0:
        log.info('Pas de Tweet analysé')
        return {}, {}
    res_sentence = {
        'positive_comment': positive_sentence,
        'negative_comment': negative_sentence,
        'neutral_comment': neutral_sentence,
        'unanalyzed': 0,
    }
    res_stat = {
        'positive': (positive / total) * 100,
        'negative': (negative / total) * 100,
        'neutral': (neutral / total) * 100,
        'total': total
    }
    log.info('POSITIF :' + str(res_stat['positive']) + '%')
    log.info('NEGATIF :' + str(res_stat['negative']) + '%')
    log.info('NEUTRE :' + str(res_stat['neutral']) + '%')
    return res_sentence, res_stat
