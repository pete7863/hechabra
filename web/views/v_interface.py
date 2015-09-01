import sys
sys.path.insert(0, '/var/www/hechabra')

import json

from flask import render_template, jsonify, request

from lookup import interface
from web import app

@app.route('/get/definition')
def get_definition():
    return jsonify(interface.get_definition_random())

@app.route('/submit/definition', methods=['POST'])
def submit_definition():
    dataDict = json.loads(request.data)
    interface.add_definition(dataDict)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
