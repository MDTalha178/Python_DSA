"""
In this file we create class for Expense Tracker and focus on class method
"""
# class method
"""
class  method(): It will directly point to the class instead of instance 
Note:
we don't  need to pass self keyword in parameter we need to pass cls
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

    @classmethod
    def get_attribute(cls, data_entry: str):
        """
        in this class we get data from user in string and we assign a value of attribute
        :param data_entry
        return objects
        """
        tracker_category, opening_balance, budget = data_entry.split(' ')
        # here we create objects for class
        return ExpenseTracker(
            tracker_category.capitalize(),
            opening_balance,
            int(budget)
        )


# creating an objects  for a class
class_objects = ExpenseTracker.get_attribute('Home 12, 7')
# Accessing an instance
print(class_objects.__dict__)
print(class_objects.get_total_year_estimate())
