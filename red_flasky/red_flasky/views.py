"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from red_flasky import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    input = request.form.get("publication") * 2
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        result=input
    )

