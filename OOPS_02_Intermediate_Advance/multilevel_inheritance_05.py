"""
In this we focus on multilevel Inheritance
"""
# Multilevel Inheritance
"""
Multilevel Inheritance:Suppose we have a class A and Class B and class B inherit a class A and now we have one
more class class C which inherit Class C this know as multilevel inheritance
"""


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


class ElectricVehicle(Car):
    """
    This class is used to give all details of electric Vehicle
    """

    # defining a constructor
    def __init__(self, make, model, fuel, air_condition, sunroof, charging_time, distance):
        """
        In this we assign value for this class and also for parent class
        :param make:
        :param model:
        :param fuel:
        :param air_condition:
        :param sunroof:
        :param charging_time:
        :param distance:
        """
        # calling parent class constructor
        super(ElectricVehicle, self).__init__(make, model, fuel, air_condition, sunroof)

        self.charge_time = charging_time
        self.distance = distance

    def get_all_details(self):
        """
        get all details of car
        :return: car details
        """
        print("Car year {}".format(self.make))
        print("Car model {}".format(self.model))
        print("Car Type {}".format(self.fuel))
        print("Its air condition {}".format(self.air_condition))
        print("Sunroof type {}".format(self.sunroof))
        print('Charging Time {}'.format(self.charge_time))
        print("Total distance once it full charge {}".format(self.distance))


electric_obj = ElectricVehicle(
    2015, 'Honda', 'Electric', 'Yes', 'Panoramic Sunroof', '1hour:30min', '600km'
)
print(electric_obj.get_all_details())
