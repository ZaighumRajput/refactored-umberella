"""
Routes and views for the flask application.
"""

from datetime     import datetime
from flask        import render_template, request
from red_flasky   import app
from .calculators import engine


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title   ='Home Page',
        year    =datetime.now().year,
        player1 = "Bunty",
        player2 = "Za"
    )

