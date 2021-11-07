
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-argument,redefined-outer-name
# pylint: disable=invalid-name
from calc.calculation import Calculation

class Addition(Calculation):

    def getResult(self):
        return self.value_a + self.value_b
