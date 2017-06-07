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
        self.expenses[item] = cost

