"""This is the addition calculation that is being inherits the value A and value B from the calculation class"""
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long

from calc.calculation import Calculation

class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def getResult(self):
        return self.value_a + self.value_b
