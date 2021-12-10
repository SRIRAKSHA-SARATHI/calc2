# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=line-too-long
# pylint: disable=unused-argument,redefined-outer-name
# pylint: disable=invalid-name
"""Testing the Calculator"""
import pytest
from calc.calculations.addition import Addition
from calculator.calculator import Calculation
@pytest.fixture

def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculation.clear_history()

def setup_addition_calculation_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    Calculation.add_calculation(addition)
@pytest.fixture
def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculation.count_history() == 1
@pytest.fixture
def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculation.count_history() == 1
    Calculation.clear_history()
    assert Calculation.count_history() == 0
    assert Calculation.clear_history() is True
@pytest.fixture
def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.get_calculation(0).get_result() == 3
@pytest.fixture
def test_get_calculation_last(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.get_last_calculation().get_result() == 3
@pytest.fixture
def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.get_first_calculation().get_result() == 3
@pytest.fixture
def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculation.count_history() == 1
