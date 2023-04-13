"""
In this we will focus on abstraction
"""
# Abstraction:
"""
is defined as a process of handling complexity by hiding unnecessary information from the user. 
This is one of the core concepts of object-oriented programming (OOP) languages. 
create a skeleton class which doesn't have any body or function.child have responsibility to  provide body or function 
to parent class means abstract class 
"""

# importing an abc clss
from abc import ABC, abstractmethod


# Creating abstract class
class AbstractClass(ABC):
    """
    This class is used for abstraction
    """

    @abstractmethod
    def get_value(self):
        """
        This is abstract method child class will provide a body
        """
        pass


class ChildClass(AbstractClass):
    """
    This is child class providing body to abstract class
    """
    pass

    def get_value(self):
        return "Providing a body to abstract method"


obj = ChildClass()
print(obj.get_value())


class AbstractClass2(ABC):
    """
    This class is used for abstraction
    """

    def __init__(self, path, file_name):
        """
        initiating a constructor
        """
        self.file_name = file_name
        self.path = path

    @abstractmethod
    def get_path(self):
        """
        This is abstract method child class will provide a body
        """
        pass

    @abstractmethod
    def get_file_name(self):
        """
        This is abstract method return the file name
        """
        pass


class TextReader(AbstractClass2):
    """
    this class is used to provide a property of abstract class
    """

    def get_file_name(self):
        """
        this is used to provide a property to abstract method
        """
        return self.file_name

    def get_path(self):
        """
        this is used to provide a property to abstract method
        """
        return self.path


obj = TextReader('desktop/downloads/', 'sql.txt')
print(obj.path)
print(obj.file_name)
