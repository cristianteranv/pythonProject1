"""Subtraction Class"""
import pprint

from calculator.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def __init__(self, values):
        self.operation = "Subtraction"
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    def get_result(self):
        """get the subtraction results"""
        difference_of_values = 0.0
        for index, value in enumerate(self.values):
            print("diff = ", difference_of_values, " at index: ", index)
            if index == 0:
                difference_of_values += value
            else:
                difference_of_values -= value
            print("diff after: ", difference_of_values)
            print("value", value)
        return difference_of_values
