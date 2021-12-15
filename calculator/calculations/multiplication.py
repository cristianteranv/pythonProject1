"""Multiplication Class"""
from calculator.calculations.calculation import Calculation

class Multiplication(Calculation):
    """subtraction calculation object"""
    def __init__(self, values):
        self.operation = "Multiplication"
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
