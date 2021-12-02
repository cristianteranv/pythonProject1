"""Testing Addition"""
from calculator.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    nums = (1.0,2.0)
    addition = Addition(nums)
    assert addition.get_result() == 3.0
