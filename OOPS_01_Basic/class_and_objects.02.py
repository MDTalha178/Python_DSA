"""
In this file basically we create a class, or we can say just create body or structure of a class
"""
# So here we create class
"""
So the class which we are creating name is ExpenseTracker
"""


class ExpenseTracker:
    """
    This is used to Track e expense
    """
    # creating constructor:
    """
    Constructor is a specialise method which used initialize value of data member of a class
    """

    def __init__(self, data, description, transaction_type, amount):
        """
        This method is used assign a value to the class attribute and in this method we four parameter
        :param self: self is instance of a class or self is holding a address of current objects its same as this keyword
        :param data:its holding some data
        :param description: some description
        :param transaction_type :which type transaction we are doing
        :param amount: Amount of a transaction
        Note:
            we can say this __init__() is constructor
        """
        # we initialize  value
        self.data = data
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount


# creating an objects  for a class
obj1 = ExpenseTracker('Talha', 'Amount from Friends', 'Cashback', 1000)
# Access of instance Attribute
"""
This will give me the value of data for obj1
"""
print(obj1.data, 'data for obj1')
# creating another objects  for a class
obj2 = ExpenseTracker('Aman', 'Salary Credited!', 'Salary', 30000)
# Access of class Attribute
"""
This will give value of transaction_type for obj2
"""
print(obj2.transaction_type)

"""
Here we have when we access a value for obj1 and obj2 for both we are getting different values but used
same blueprint means same class
"""
