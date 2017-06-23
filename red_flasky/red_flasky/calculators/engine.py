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
        
    def addIncome(self, income):
        try:
            self.income = float(income)
        except:
            self.income = 0

    def totalExpense(self):
        return sum(self.expenses.values())

    def remainingBudget(self):
        return self.income - self.totalExpense()

class IncomeStatment(object):
    '''
        Todo:
        Dynamically create all line items
        Dynamically create all the dependencies; for example, Revenue = [CostsOfGoodsSold - CostProfit]

    '''

    #these should be passed during initialization 
    revenueItems        = ['CostsOfGoodsSold', 'GrossProfit']
                           
    operatingExpenses   = { #Major line item : Sub line item
                           'Operating_Profit': ['SGA', 'RD', 'Depreciation'], 
                           'Other'           : ['Interest Expense', 'Gain(Loss)Sale Assets']
                          }

    def __init__(self):
        for lineItems in self.revenueItems:
            setattr(self, lineItems, 0.0)

        for lineItem, subLineItems in self.operatingExpenses.items():

            for item in subLineItems:
                setattr(self, item, 0.0)

            #should be updated whenever sublineItem is
            def createMajorLineItemSum(cls, subLineItems):
                '''Returns the sum of sublineItems'''
                total = sum([getattr(cls, m) for m in subLineItems])
                setattr(self, lineItem, total) 

            createMajorLineItemSum(self, subLineItems)

    def updateMajorLineItemSum(self, majorLineItem):
        total = 0.0
        for subLineItems in getattr(self, majorLineItem):
            total = sum([getattr(self, m) for m in subLineItems])
        setattr(self, majorLineItem, total)


class BalanceSheet(object):

    assetItems      = []
    liabilityItemrs = []
    equityItems     = []

    pass            

from unittest import TestCase, TextTestRunner, TestLoader

class TestsIncomeStatement(TestCase):
    
    def test_attributes_created(self):
        companyIncome = IncomeStatment()
        for lineItem in companyIncome.revenueItems:
            self.assertTrue(hasattr(companyIncome,lineItem))

        for lineItem, subLineItem in companyIncome.operatingExpenses.items():
            self.assertTrue(hasattr(companyIncome,lineItem))
            for item in subLineItem:
                self.assertTrue(hasattr(companyIncome, item))
                
    #def test_MajorLineItemSum(self):
    #    companyIncome = IncomeStatment()
    #    companyIncome.SGA = -95.0 
    #    companyIncome.RD  = -100.0
    #    companyIncome.updateMajorLineItemSum('operatingExpenses')

    #    self.assertEqual(companyIncome.Operating_Profit, -195.0)




suite = TestLoader().loadTestsFromTestCase(TestsIncomeStatement)
TextTestRunner().run(suite)

class TestsBudget(TestCase):

    def test_totalExpense(self):
        sample_budget = budget()
        self.assertEqual(sample_budget.totalExpense(), 10)
        sample_budget.addExpense('orange', 2.00)
        sample_budget.addExpense('corn'  , 1.00)
        self.assertEqual(sample_budget.totalExpense(), 13)

suite = TestLoader().loadTestsFromTestCase(TestsBudget)
TextTestRunner().run(suite)


