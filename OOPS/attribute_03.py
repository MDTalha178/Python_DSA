"""
In this file we create class for Expense Tracker and focus on attribute
"""
# creating a class for Expense Tracker
"""
Creating a class expense tracker class and declare attribute for a class
Attribute is a set of variable which holding a important information while creating a class
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
        self.tracker_category = tracker_category
        self.opening_balance = opening_balance
        self.budget = budget


# creating an objects  for a class
for_home_budget = ExpenseTracker('Home budget', 3000, 20000)
# Access of instance Attribute
print(for_home_budget.tracker_category, 'for home')


# creating an objects  for a class
for_shopping_budget = ExpenseTracker("Shopping", 1700, 3500)
print(for_shopping_budget.tracker_category, 'for shopping')

# Access all attribute of a class for objects
"""
If we want to access of all attribute of a class for specific objects the we
__dict__ method which return all attribute of class with associated value
"""
# here accessing  all attribute for home budget objects
print(for_home_budget.__dict__, 'for home budget objects')

# here accessing  all attribute for shopping budget objects
print(for_shopping_budget.__dict__, 'for shopping budget objects')

# if you want to access specific attribute value
"""
if you want to access specific attribute value for that we use
getattr() method:this method will return a value of attribute which we passed in a parameter
Structure:
   getattr(object, 'attribute_name')
   Note: attribute_name should be in a string
Note:
   if attribute is not present is will return a error
"""
# here we are using getattr() for home budget objects
print(getattr(for_home_budget, 'opening_balance'), 'for home opening balance')

# here we are using getattr() for home budget objects
print(getattr(for_shopping_budget, 'opening_balance'), 'for shopping opening balance')

# if you want to check this attribute is present in a class or not
"""
if want to check this attribute is present in a class or not the we use
hasattr() method: this method is used to check this attribute is present in a class or not
and it will return a boolean value if present return True, else return False

Structure:
   hasattr(object, 'attribute_name')
   Note: attribute_name should be in a string
"""
# here we are using hasattr() for home budget objects
print(hasattr(for_home_budget, 'opening_balance'), 'for home opening balance')

# here we are using hasattr() for home budget objects
print(hasattr(for_shopping_budget, 'opening_balance'), 'for shopping opening balance')
