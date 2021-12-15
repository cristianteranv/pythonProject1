"""Addition Class"""
from calculator.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculation addition class"""
    # pylint: disable=super-init-not-called
    def __init__(self, values):
        self.operation = "Addition"
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values
