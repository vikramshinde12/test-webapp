import socket
import os

from flask import Flask
from flask import render_template, request


app = Flask(__name__)

DELAY_TIMER = os.environ.get('APP_START_DELAY') or 0


@app.route('/')
def main():
    return render_template('hello.html', name=socket.gethostname(), color='#16a085')


if __name__ == '__main__':
    print("Application Ready !!")
    app.run(host="0.0.0.0", port=8080)
