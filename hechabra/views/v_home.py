import sys
sys.path.insert(0, '/var/www/hechabra')

from hechabra import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html', name='Home')