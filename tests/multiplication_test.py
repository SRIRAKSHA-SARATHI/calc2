# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-argument,redefined-outer-name
# pylint: disable=invalid-name
from calc.calculations.multiplication import Multiplication


def test_multiplication_create():
    calc_obj = Multiplication.create((1, 2))
    assert isinstance(calc_obj, Multiplication)


def test_multiplication_get_result():
    calc_obj = Multiplication.create((3, 4))
    assert calc_obj.get_result() == 12
