"""
Routes and views for the flask application.
"""

from datetime     import datetime
from flask        import render_template, request
from red_flasky   import app
from .calculators import engine

todoList = engine.engine()
budget   = engine.budget()

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page."""
    budget.addExpense(request.form.get("item"), request.form.get("cost"))
    budget.addIncome(request.form.get("income"))

    return render_template(
        'index.html',
        title        = 'Home Page',
        year         = datetime.now().year,
        expenses     = budget.expenses,
        totalExpense = budget.totalExpense(),
        income       = budget.income,
        remaining    = budget.remainingBudget()
        
    )

