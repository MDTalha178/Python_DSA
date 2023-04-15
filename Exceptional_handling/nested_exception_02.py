"""
In this we focus on nested exception
"""
# Exception:
"""
There some error which we got at the run time so those should be handle other wise code will be crash 
so those error come at run time like logical error these type of error Exception error
"""
# Structure:
"""
so we some try and except
try:
   In a try block we write our code or in which we are expecting an exception
except:
   In a except block we handle exception which we get from try block
"""


class Vehicle:
    """
    creating a constructor
    """

    def __init__(self, make, model, fuel):
        """
        assigning a value
        :param make:
        :param model:
        :param fuel:
        """
        self.make = make
        self.model = model
        self.fuel = fuel

    def get_value(self):
        """
        In this method we get car age
        :return:
        """
        # try block
        try:
            age = 2023 - self.model
            return 1000 * (1 / age)
        except TypeError:
            """
            if user will pass any incorrect data type means string so this handle and codel will not crash
            """
            try:
                """
                Here we suppose we will get an age 0 so it will give so for that we use nested exception
                """
                age = int(2023) - int(self.model)
                return 1000 * (1 / age)
            except ZeroDivisionError:
                """
                if we will get and age 0 so 0 can't divide a 1000 we handle this error
                """
                age = int(2023) - int(self.model)
                return 1000 * 1
            except:
                """
                if still we get any exception rest for all exception we will return this block of code
                """
                return "You have entered Model year incorrect format"