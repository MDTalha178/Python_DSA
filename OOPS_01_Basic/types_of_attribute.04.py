"""
In this we focus on class attribute and instance attribute
"""
# class attribute:
"""
class attribute are those attribute are shared it the value of class attribute will be same for instance 
of a class 
"""
# instance attribute:
"""
instance attribute are those which is shared but the value will be different for all other or different attribute
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


# creating an objects  for a class
for_home_budget = ExpenseTracker('Home budget', 3000, 20000)
# Access of instance Attribute
print(for_home_budget.tracker_category, 'for home')

# creating an objects  for a class
for_shopping_budget = ExpenseTracker("Shopping", 1700, 3500)
print(for_shopping_budget.tracker_category, 'for shopping')

# so here we are accessing an attribute of class
"""
in this we pass a class attribute and it will return false
"""
print(hasattr('for_home_budget', 'expense_traker_version'))

# Access all attribute of a class for objects
"""
here we are accessing all attribute of class for specific objects but it will not include class attribute
"""
# here accessing  all attribute for home budget objects
print(for_home_budget.__dict__, 'for home budget objects')

# we can access a class attribute through instance
print(for_home_budget.expense_traker_version)

# manipulating a value of class attribute
"""
if we will change a of class attribute for objects home_budget after we accessing a value of class attribute for
shopping budget object for this objects value will not change it will remain same
"""
for_home_budget.expense_traker_version = 0.2
print(for_home_budget.expense_traker_version)

# now accessing  a value
print(for_shopping_budget.expense_traker_version)
