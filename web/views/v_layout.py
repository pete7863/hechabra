import sys
sys.path.insert(0, '/var/www/hechabra')

from flask import render_template

from database.mysql import client
from web import app


@app.route('/')
def home():
    return render_template('home.html', name='Home')

@app.route('/create/word')
def create_word():
    return render_template('create_word.html', name='Create Word')

@app.route('/create/definition')
def create_definition():
    return render_template('create_definition.html', name='Create Definition')

@app.route('/vote')
def vote():
    return render_template('vote.html', name='Vote')

@app.route('/stats')
def stats():
    return render_template('stats.html', name='Stats')