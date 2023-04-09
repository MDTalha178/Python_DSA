"""
In this we focus on super on function
"""
# Super Method:
"""
Super function is function which called parent class constructor and it returns the temporary objects of
the class we denote super function : super()
super(child_Class_name, self).__init__(attribute_name)
"""
"""
In this we focus on inheritance
"""
# Inheritance
"""
Inheritance:its property to inherit or achieve a functionality of parent class in a child class
"""


# creating a class it will be a parent class

class Vehicle:
    """
    creating a constructor  for this class
    """

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


# creating a child class
"""
child class means car class inherit a parent class means Vechile class
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


# creating an objects  for a class
car_obj = Car(2019, 'Honda', 'Petrol', 'Yes', 'Panoramic sunroof')
# Accessing an instance method
print(car_obj.__dict__)

# accessing a parent class attribute
print(car_obj.make)
