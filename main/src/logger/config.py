import logging
import logging.config
import logs
import os
from config import CONFIG
LOGGER_CONFIG = CONFIG.get('logger')


def logger():
    path = os.path.dirname(logs.__file__)
    config_logger = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '%(asctime)s | %(levelname)s | %(module)s | %(funcName)s | %(message)s'
            }
        },
        'handlers': {
            'log_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': LOGGER_CONFIG.get('level'),
                'formatter': 'simple',
                'filename': path + '/' + LOGGER_CONFIG.get('filename') + '.log',
                'maxBytes': 50000000,
                'backupCount': 1,
                'encoding': 'utf8'
            },
            'log_console': {
                'class': 'logging.StreamHandler',
                'level': LOGGER_CONFIG.get('level'),
                'formatter': 'simple'
            }
        },
        'root': {
            'level': LOGGER_CONFIG.get('level'),
            'handlers': ['log_file', 'log_console']
        }
    }

    logging.config.dictConfig(config_logger)
