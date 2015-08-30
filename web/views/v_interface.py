import sys
sys.path.insert(0, '/var/www/hechabra')

from flask import render_template, jsonify

from lookup import interface
from web import app

@app.route('/get/definition')
def get_definition():
    return jsonify(interface.get_definition_random())
