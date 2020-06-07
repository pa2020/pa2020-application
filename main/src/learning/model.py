import logging
import fasttext
from main.src.logger.config import logger

log = logging.getLogger(__name__)
logger()
model = fasttext.load_model('D:/ESGI/DeepLearning/Sentiment_dataset/betsentiment-EN-tweets-sentiment-teams.model')


def analyze(data):
    d = []
    for sentence in data:
        d.append(model.predict(sentence, k=3))
        print('sentence "' + sentence + '" ->', d[-1])
    return d

def statistics(analyzed):
    positive = 0.0
    negative = 0.0
    neutral = 0.0
    for row in analyzed:
        for label in range(0, 3):
            if row[0][label] == '__label__POSITIVE':
                positive += row[1][label]
            elif row[0][label] == '__label__NEGATIVE':
                negative += row[1][label]
            elif row[0][label] == '__label__NEUTRAL':
                neutral += row[1][label]
    total = len(analyzed)
    res = {
        'positive': (positive / total) * 100,
        'negative': (negative / total) * 100,
        'neutral': (neutral / total) * 100,
        'total': total
    }
    log.info('POSITIF :' + str(res['positive']) + '%')
    log.info('NEGATIF :' + str(res['negative']) + '%')
    log.info('NEUTRE :' + str(res['neutral']) + '%')
    return res
