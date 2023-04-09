"""
In this file we create class for Expense Tracker and focus on static method
"""
# static method
"""
static method(): static is not doing anything at instance level or it will not effect any value of instance
Structure: for declaring static method we need to add a @staticmethod decorator 
Note:
we don't need to pass self keyword in parameter 
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

    # declaring a static method
    @staticmethod
    def get_total_year_estimate(amount):
        """
        this static method will return 1 year of estimate of budget
        :param amount
        return one year of budget
        """
        return 12 * amount


# creating an objects  for a class
for_home_budget = ExpenseTracker('Home budget', 3000, 20000)
# Accessing a static method
print(for_home_budget.get_total_year_estimate(3000), 'static method')
