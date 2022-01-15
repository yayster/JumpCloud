#!/usr/bin/env python3
import os
import os.path
from pathlib import Path
from flask import request
from flask import Flask, jsonify
from flask import make_response

download_url = 'https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt'
content_path = '/tmp/content.txt'

app = Flask(__name__)

@app.route('/')
def index():
    return "jumpcloud Cloud Operations Engineer Exercise"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'404 error': 'Not found'}), 404)

@app.route('/manage_file', methods=['POST'])
def manage_file():
    if not request.json or not 'action' in request.json:
        abort(400)
    message = 'unknown action'
    if request.json['action'] == 'download':
        message = 'downloading content'
        command = 'wget -q -O ' + content_path + ' ' + download_url
        os.system(command)
    if request.json['action'] == 'read':
        message = 'No content found.  Try downloading it'
        if os.path.exists( content_path ):
            message = Path( content_path ).read_text()
            return(message)
    return jsonify({'message': message}), 200

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
