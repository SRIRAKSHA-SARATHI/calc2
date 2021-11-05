"""This is the addition calculation that is being inherits the value A and value B from the calculation class"""

from calc.calculation import Calculation

class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def getResult(self):
        return self.value_a + self.value_b