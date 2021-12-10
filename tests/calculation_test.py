# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-argument,redefined-outer-name
# pylint: disable=invalid-name
import pytest
from calc.calcul import Calculation

@pytest.fixture
def test_calculation_create():
    calc_obj = Calculation.create((1, 2, 3))
    assert isinstance(calc_obj, Calculation)


def test_calculation_get_result():
    calc_obj = Calculation.create((1, 2, 3))
    with pytest.raises(NotImplementedError):
        calc_obj.get_result()
