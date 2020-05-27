from main.src.application import app
from main.src.thread.runner import runnerTwitter

@app.route('/')
def hello_world():
    runnerTwitter('français')
    return 'Hello World!'