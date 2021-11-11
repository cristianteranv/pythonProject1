"""Testing Subtraction"""
from calculator.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    nums = (1.0,2.0)
    subtraction = Subtraction(nums)
    #Act
    #Assert
    assert subtraction.get_result() == -3
