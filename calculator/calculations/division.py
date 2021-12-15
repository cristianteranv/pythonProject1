"""Addition Class"""
from calculator.calculations.calculation import Calculation

class Division(Calculation):
    """ calculation addition class"""
    def __init__(self, values):
        self.operation = "Division"
        self.values = Calculation.convert_args_to_tuple_of_float(values)

    def get_result(self):
        """get the addition results"""
        values = self.values
        if len(values) != 2:
            raise Exception("Division can only take two arguments.")
        if values[1] == 0:
            raise ZeroDivisionError
        return values[0] // values[1]
