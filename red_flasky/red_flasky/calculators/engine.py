class engine(object):
    """description of class"""
    def __init__(self):
        self.todolist = ['TODO-LIST']

    def addTask(self, task):
        self.todolist.append(task)

class budget(object):

    def __init__(self):
        self.income = 0
        self.expenses ={'weed': 10.00}

    def addExpense(self, item, cost):
        try:
            cost = float(cost)
            self.expenses[item] = cost
        except:
            pass

    def totalExpense(self):
        return sum(self.expenses.values())

from unittest import TestCase, TextTestRunner, TestLoader

class TestsBudget(TestCase):

    def test_totalExpense(self):
        sample_budget = budget()
        self.assertEqual(sample_budget.totalExpense(), 10)
        sample_budget.addExpense('orange', 2.00)
        sample_budget.addExpense('corn'  , 1.00)
        self.assertEqual(sample_budget.totalExpense(), 13)

suite = TestLoader().loadTestsFromTestCase(TestsBudget)
TextTestRunner().run(suite)


