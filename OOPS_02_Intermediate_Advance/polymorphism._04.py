"""
In this we focus on Polymorphism
"""
# Polymorphism
"""
The word polymorphism means many form, means the same function name(but with different signature)
"""
class Vehicle:
    """
    creating a constructor  for this class
    """

    # base price
    base_price = 12000000
    # current_year
    current_year = 2023

    def __init__(self, make, model, fuel):
        """
        assign a value of attribute
        :param make:
        :param model:
        :param fuel:
        """
        self.make = make
        self.model = model
        self.fuel = fuel

    def get_current_price(self):
        """
        we will calculate a current price of this car
        :return: current price
        """
        car_age = Vehicle.current_year - self.make
        print('from parent class')
        return Vehicle.base_price // car_age


# creating a child class
"""
child class means car class inherit a parent class means Vechile class
Note:
Number of parameter which we passed in method should be same
"""


class Car(Vehicle):
    """
    creating a constructor for this class
    """

    def __init__(self, make, model, fuel, air_condition, sunroof):
        """
        In this we assign value for this class and also for parent class
        :param make:
        :param model:
        :param fuel:
        :param air_condition:
        :param sunroof:
        """
        # for assigning a value of parent class with the help of super function
        super(Car, self).__init__(make, model, fuel)

        # assigning a value of child class attribute
        self.air_condition = air_condition
        self.sunroof = sunroof

    # # overriding a method
    def get_current_price(self):
        """
        This method will return current price of car
        and this will override of method which already present in parent class
        :return:
        """
        age = Vehicle.current_year - self.make
        print('from child class')
        return Vehicle.base_price // age


# creating an objects  for a class
car_obj = Car(2019, 'Honda', 'Petrol', 'Yes', 'Panoramic sunroof')
# Accessing an instance method
print(car_obj.__dict__)

# accessing a parent class attribute
print(car_obj.make)

print(car_obj.get_current_price())