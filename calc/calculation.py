"""This is our calculation base class / Abstract Class"""
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-argument,redefined-outer-name
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods
class Calculation:

    #contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self,value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b
    # Class Factory Method <- bound to the class and not the instance of the class
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)
