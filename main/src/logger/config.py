import logging
import logging.config
import os


def logger():
    path = os.path.dirname(os.path.realpath(__file__))
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
                'level': int(os.getenv('LOGGER_LEVEL')),
                'formatter': 'simple',
                'filename': path + '/' + os.getenv('LOGGER_FILENAME') + '.log',
                'maxBytes': 50000000,
                'backupCount': 1,
                'encoding': 'utf8'
            },
            'log_console': {
                'class': 'logging.StreamHandler',
                'level': int(os.getenv('LOGGER_LEVEL')),
                'formatter': 'simple'
            }
        },
        'root': {
            'level': int(os.getenv('LOGGER_LEVEL')),
            'handlers': ['log_file', 'log_console']
        }
    }

    logging.config.dictConfig(config_logger)
