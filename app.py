import socket
import os

from flask import Flask
from flask import render_template, request


app = Flask(__name__)

DELAY_TIMER = os.environ.get('APP_START_DELAY') or 0
COLOR = os.environ.get('COLOR') or "#1649a0"
DAUGHTER_NAME = os.environ.get('DAUGHTER') or 'Sejal'
AGE = os.environ.get('AGE') or 7


@app.route('/')
def main():
    return render_template('hello.html', name=socket.gethostname(), color=COLOR, daughter_name=DAUGHTER_NAME, age=AGE)


if __name__ == '__main__':
    print("Application Ready !!")
    app.run(host="0.0.0.0", port=8080)
