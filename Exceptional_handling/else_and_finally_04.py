"""
In this we focus on finally and else in exception
"""
# finally:
"""
finally is a keyword which we define after except block and it will always executed either we will get error or not
"""
# else
"""
else block will excused when we will not get any exception error
"""


# creating a custom exception class
class ZeroModelYear(Exception):
    """
    This class used to handle custom exception
    we need to inherit a base class of exception
    """

    # creating a constructor
    def __init__(self, value, message="Model year should less than current year "):
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


# creating a custom exception class
class CarModelString(Exception):
    """
    This class used to handle custom exception
    we need to inherit a base class of exception
    """

    # creating a constructor
    def __init__(self, value, message="Car Model value can't be a string"):
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
        self.value = None
        self.age = None
        self.make = make
        self.model = model
        self.fuel = fuel
        self.status = None

    def get_value(self):
        """
        In this method we get car age
        :return:
        """
        # try block
        age = 2023 - self.model
        status = None
        # checking exception
        try:
            if type(self.model) == str:
                status = 'Custom'
                raise CarModelString(self.model)
            elif self.model >= 2023:
                status = 'Custom'
                raise ZeroModelYear(self.model)
            else:
                self.age = 2023 - self.model
                self.value = 1000 * (1 / self.age)
                status = 'Success'
        except TypeError:
            self.age = 2023 - int(self.model)
            self.value = 1000 * (1 / self.age)
            status = 'Inbuilt'
        except ZeroModelYear as e:
            print("Error**", e)
        else:
            print("Code run without any exception")
        finally:
            if status == 'Custom':
                print('code has custom exception')
            elif status == 'Inbuilt':
                print('code has inbuilt exception')
            else:
                print("The value without any exception", self.value)


obj = Vehicle('Tesla', 2023, 'Yes')
print(obj.get_value())
