from main.src.api.request import Request
from main.src.application import app
from flask import request
from main.src.thread.runner import runnerTwitter
from main.src.learning.generation import generateModel

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
        # runnerTwitter('français')
        # runnerTwitter(request.json['sentence'], request.json['request_id'])
        req = Request()
        req.post('/api/v1/request', {"state": "RUNNING"})
        return 'json data received'


@app.route('/generate')
def generate():
    generateModel('D:/ESGI/DeepLearning/Sentiment_dataset/betsentiment-EN-tweets-sentiment-teams.csv')
    return 'Ok'

