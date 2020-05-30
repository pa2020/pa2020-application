from main.src.application import app
from main.src.learning.analyze import train
from main.src.thread.runner import runnerTwitter


@app.route('/')
def hello_world():
    train()
    return 'Hello World!'


@app.route('/analyze')
def analyze():
    runnerTwitter('français')
    return 'Ok'
