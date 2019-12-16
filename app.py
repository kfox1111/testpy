from flask import Flask, Response
import os
import json

app = Flask(__name__)

@app.route('/')
def get_root():
    js = json.dumps({'hello':'test'})

    resp = Response(js, status=200, mimetype='application/json')

    return resp

if __name__ == '__main__':
    app.run()

