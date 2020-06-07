import logging
import fasttext
from main.src.logger.config import logger

log = logging.getLogger(__name__)
logger()


def testModel(model, file):
    log.info('Testing the model')
    result = model.test(file)
    log.info('Accuracy: ' + str(result[1]))


def trainModel(file, out=''):
    if out == '':
        out = file[:file.rindex('_')] + '.model'
    log.info('Training start')
    try:
        hyper_params = {"lr": 0.01,
                        "epoch": 50,
                        "wordNgrams": 2,
                        "dim": 20}

        model = fasttext.train_supervised(file, **hyper_params)
        log.info('Model trained with the hyperparameter \n {}'.format(hyper_params))

        log.info('Checking performance')
        testModel(model, file)

        log.info('Reducing size and memory usage by quantizing the model')
        model.quantize(input=file, retrain=True)
        model.save_model(out)
        log.info('Model saved to ' + out)

    except Exception as e:
        log.error('Exception during training: ' + str(e))
