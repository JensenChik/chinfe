from flask import Flask, send_file
import os.path

app = Flask(__name__)


@app.route('/')
def root():
    return send_file('index.html')


@app.route('/<path:path>')
def static_proxy(path):
    return send_file(path)


if __name__ == '__main__':
    app.run()
