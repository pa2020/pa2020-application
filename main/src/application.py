import logging
from main.src.logger.config import logger
from flask import Flask
app = Flask(__name__)
import main.src.api.routes
log = logging.getLogger(__name__)
logger()

if __name__ == '__main__':
    app.run()
