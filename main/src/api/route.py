from flask import request
import json
from main.src import app
from main.src.thread.satisfaction import runAnalyze


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
