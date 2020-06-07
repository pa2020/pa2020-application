from dotenv import load_dotenv
import logging
from main.src.logger.config import logger
from flask import Flask

load_dotenv()
app = Flask(__name__)
import main.src.api.routes
log = logging.getLogger(__name__)
logger()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000)
