from dotenv import load_dotenv
load_dotenv()

from main.src.thread.satisfaction import runAnalyze
import logging
from main.src.logger.config import logger
from flask import Flask, request
import json

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
        body = request.json
        res = runAnalyze(body['sentence'], body['request_id'])  # runnerTwitter(body['sentence'], body['request_id'])
        return json.dumps(res)


    @app.route('/generate')
    def generate():
        # generateModel('D:/ESGI/DeepLearning/Sentiment_dataset/betsentiment-EN-tweets-sentiment-teams.csv')
        return 'Ok'

    app.run(host='0.0.0.0', port=2000)
