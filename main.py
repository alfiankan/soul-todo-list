from threading import Thread
from flask import Flask
import time
import threading

app = Flask(__name__)


mutex = threading.Lock()

todos = ['eat', 'sleep', 'learn']


@app.route('/add')
def create():
    
    return str(mutex.locked())

@app.route('/all')
def index():
    
    with mutex:
        time.sleep(20)
        todos.append('long run')

    return todos

app.run(host='0.0.0.0', port=5000, threaded=True)
