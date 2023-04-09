"""
In this file we create class for Expense Tracker and focus on instance method
"""
# static method
"""
instance  method(): instance method it will work on instance level it will effect value of instance attribute 
Note:
we need to pass self keyword in parameter 
"""


# creating a class
class ExpenseTracker:
    """
    this class is used to track expense
    """
    # declaring a class attribute
    expense_traker_version = 0.1

    # initializing a constructor
    def __init__(self, tracker_category, opening_balance, budget):
        """
        this a special method called construction to initialize a value of attribute
        :param tracker_category:
        :param opening_balance:
        :param budget:
        :return:
        """
        # instance attribute
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

    # declaring an instance method
    def get_total_year_estimate(self):
        """
        this instance method will return 1 year of estimate of budget
        :param amount
        return one year of budget
        """
        return 12 * self.budget


# creating an objects  for a class
for_home_budget = ExpenseTracker('Home budget', 3000, 20000)
# Accessing a instance method
print(for_home_budget.get_total_year_estimate(), 'instance method')
