from dotenv import load_dotenv
import logging
from main.src.logger.config import logger
from flask import Flask

load_dotenv()
app = Flask(__name__)
import main.src.api.routes
log = logging.getLogger(__name__)
logger()
from main.src.learning.analyze import train
train()


if __name__ == '__main__':
    app.run()
