# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-argument,redefined-outer-name
# pylint: disable=invalid-name
from calc.calcul import Calculation


class Addition(Calculation):
    """The addition class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""

    def get_result(self):
        return sum(v for v in self.values)
