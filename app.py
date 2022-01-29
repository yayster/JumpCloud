#!/usr/bin/env python3
import os
import os.path
import requests
import datetime, json_logging, logging, sys
from pathlib import Path
from flask import request
from flask import Flask, jsonify
from flask import make_response

download_url = \
    'https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt'
content_path = '/tmp/content.txt'

app = Flask(__name__)
json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("test-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

@app.route('/')
def index():
    logger.info("test log statement")
    logger.info("test log statement with extra props", extra={'props': {"extra_property": 'extra_value'}})
    correlation_id = json_logging.get_correlation_id()
    return "JumpCloud Cloud Operations Engineer Exercise"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'404 error': 'Not found'}), 404)

@app.route('/manage_file', methods=['POST'])
def manage_file():
    if not request.json or not 'action' in request.json:
        message = 'unexpected input'
        return jsonify({'message': message}), 200
    message = 'unknown action'
    if request.json['action'] == 'download':
        message = 'downloading content'
        r = requests.get(download_url)
        with open( content_path, 'wb') as f:
            f.write(r.content)
    if request.json['action'] == 'read':
        message = 'No content found.  Try downloading it'
        if os.path.exists( content_path ):
            message = Path( content_path ).read_text()
            return(message)
    return jsonify({'message': message}), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
