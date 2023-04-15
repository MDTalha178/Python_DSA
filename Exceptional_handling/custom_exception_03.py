"""
In this we focus on how to create custom exception class
"""


# creating a custom exception class
class NegativeCarValue(Exception):
    """
    This class used to handle custom exception
    we need to inherit a base class of exception
    """

    # creating a constructor
    def __init__(self, value, message="Car value can't be negative"):
        """
        assigning a value
        :param value:
        :param message:
        """
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        getting a value
        :return:
        """
        return f'{self.message} --> {self.value}'


# creating class
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
        age = 2023 - self.model

        # checking exception
        if age < 0:
            raise NegativeCarValue(age)
        else:
            return 1000 * (1 / age)
