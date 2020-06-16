from dotenv import load_dotenv
load_dotenv()
import logging
from main.src.logger.config import logger
from flask import Flask, request
from main.src.api.request import Request
from main.src.thread.runner import runnerTwitter
from main.src.learning.generation import generateModel
app = Flask(__name__)
log = logging.getLogger(__name__)
logger()

if __name__ == '__main__':
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/analyze', methods=['POST'])
    def analyze():
        if request.data == b'':
            print(request.form)
            return 'form data received. must be JSON row data'
        else:
            print(request.json)
            body = request.json
            req = Request()
            # req.put('/api/v1/request/' + body['request_id'], {"update_time": date.today(), "state": "RUNNING"})
            runnerTwitter(body['sentence'], body['request_id'])
            return 'json data received'


    @app.route('/generate')
    def generate():
        # generateModel('D:/ESGI/DeepLearning/Sentiment_dataset/betsentiment-EN-tweets-sentiment-teams.csv')
        return 'Ok'

    app.run(host='0.0.0.0', port=2000)
