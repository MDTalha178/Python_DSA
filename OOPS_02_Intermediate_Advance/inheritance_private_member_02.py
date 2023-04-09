"""
In this focus on Inheritance with private member of class
"""
# Inheritance
"""
Inheritance:its property to inherit or achieve a functionality of parent class in a child class
"""

# creating a child class
"""
child class means car class inherit a parent class means Vehicle class
"""


class Vehicle:
    """
    creating a constructor  for this class
    """

    def __init__(self, make, model, fuel, engine_details):
        """
        assign a value of attribute
        :param make:
        :param model:
        :param fuel:
        """
        self.make = make
        self.model = model
        self.fuel = fuel
        # private attribute
        self.__engine_details = engine_details

    def __get_engine_details(self):
        employee_pin = int(input('Enter your Pin'))
        if employee_pin == 70812:
            return self._Car__engine_details
        return "You are not authorized"


# creating a child class
"""
child class means car class inherit a parent class means Vechile class
"""


class Car(Vehicle):
    """
    creating a constructor for this class
    """

    def __init__(self, make, model, fuel, engine_details, air_condition, sunroof):
        """
        In this we assign value for this class and also for parent class
        :param make:
        :param model:
        :param fuel:
        :param air_condition:
        :param sunroof:
        """
        # assigning a value of parent class attribute
        Vehicle.make = make
        Vehicle.model = model
        Vehicle.fuel = fuel
        Vehicle.__engine_details = engine_details

        # assigning a value of child class attribute
        self.air_condition = air_condition
        self.sunroof = sunroof

    def get_parent_attribute(self):
        """
        access a parent attribute
        :return: none
        """
        print(Vehicle.make, " ", Vehicle.model, Vehicle.fuel, Vehicle.__engine_details)

    def get_private_details(self):
        return self._Vehicle__get_engine_details()


# creating an objects  for a class
car_obj = Car(2019, 'Honda', 'Petrol', '12000', 'Yes', 'Panoramic sunroof')
# we can access private attribute of parent is method is knows as name Mangling
print(car_obj.get_private_details())
