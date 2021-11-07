
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-argument,redefined-outer-name
# pylint: disable=invalid-name
from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Multiplication(Calculation):

    def getResult(self):
        #you need to use self to reference the data contained in the instance of the object.  This is encapsulation
        return self.value_a * self.value_b
