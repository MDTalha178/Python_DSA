"""
In this we focus on private and public modifiers
"""
# Private attribute
"""
private attribute are those attribute which can't access outside the class
and we declare a private attribute with __ 
"""
# Public attribute
"""
public attribute are those attribute which can access outside the class by default all attribute is public
"""


# creating a class
class ExpenseTracker:
    """
    this class is used to track expense
    """
    # declaring a class attribute
    expense_traker_version = 0.1

    # initializing a constructor
    def __init__(self, tracker_category, opening_balance, budget, total_balance):
        """
        this a special method called construction to initialize a value of attribute
        :param tracker_category:
        :param opening_balance:
        :param budget:
        :param total_balance
        :return:
        """
        # instance attribute
        # public attribute
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget

        # private attribute
        self.__total_balance = total_balance

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

    # private method
    def __get_total_balance(self):
        """
        this is private method
        return total balance
        """
        return self.__total_balance


# creating an objects  for a class
for_home_budget = ExpenseTracker('Home budget', 3000, 20000, 30000)
"""
Now if try to access __total_balance attribute it will return an error because __total_balance is a private
attribute we don't have access
"""
print(for_home_budget.__dict__)