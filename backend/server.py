#from flask import Flask, render_template, request
import pandas as pd
import requests as rq

from flask import Flask, abort, current_app, request, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def gpt():

    json_data = json.dumps(0)
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5001, debug = True)