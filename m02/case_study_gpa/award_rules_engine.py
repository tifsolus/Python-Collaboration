""" 
@Program: rules_engine
@Author: Donald Osgood
@Last Date: 2023-11-04 21:15:07
@Purpose: Engine to check if student is entitled to an award
"""
from utils.conversions import string_to_float


def get_award(value):
    """Check wich award a student is entitled to based on GPA:"""
    try:
        if value != "":
            float_value = string_to_float(value)
            if float_value < 3.25:
                return ""
            elif float_value >= 3.5 and float_value <= 4.0:
                return "Dean's List"
            elif float_value >= 3.25:
                return "Honor Roll"
    except ValueError as exception:
        return exception
