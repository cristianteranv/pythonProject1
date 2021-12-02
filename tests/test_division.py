"""Testing Addition"""
import unittest
from calculator.calculations.division import Division

class TestDivision(unittest.TestCase):
    """ Testing division """

    def test_calculation_division(self):
        """testing that our calculator has a static method for addition"""
        nums = (2.0,1.0)
        div = Division(nums)
        self.assertEqual(div.get_result(), 2.0)

    def test_division_by_zero(self):
        """Testing that division by zero raises an error"""
        nums = (2.0, 0)
        div = Division(nums)
        self.assertRaises(ZeroDivisionError, div.get_result)

    def test_more_than_two_args(self):
        """Testing that more than two arguments raises an error"""
        nums = (1.0,2.0,3.0)
        div = Division(nums)
        with self.assertRaises(Exception) as context:
            div.get_result()
        self.assertEqual(str(context.exception), 'Division can only take two arguments.')

    def test_one_arg(self):
        """Testing that less than two arguments raises an error"""
        nums = (1.0, )
        div = Division(nums)
        with self.assertRaises(Exception) as context:
            div.get_result()
        self.assertEqual(str(context.exception), 'Division can only take two arguments.')
