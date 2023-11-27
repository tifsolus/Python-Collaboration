""" 
@Program: rules_engine
@Author: Donald Osgood
@Last Date: 2023-11-04 21:15:07
@Purpose: Engine to check if student is entitled to an award
"""
from utils.conversions import string_to_float


def get_award(value):
    """ get award from rules engine

    Args:
        value ([float]): [gpa value]

    Returns:
        [award]: [string]
    """
    try:
        # honor roll min gpa value
        HONORGPA = 3.25
        # deans list min gpa value
        DEANGPA = 3.50
        # max gpa value
        MAXGPA = 4.0
        if value != "":
            # convert string to float
            float_value = string_to_float(value)
            # if value provided is less than minimum award or higher than max retrun null
            if (float_value < HONORGPA) or (float_value > MAXGPA):
                return ""
            # check for deans list
            elif float_value >= DEANGPA:
                return "Dean's List"
            # check for honor roll
            elif float_value >= HONORGPA:
                return "Honor Roll"
    except ValueError as exception:
        return exception
