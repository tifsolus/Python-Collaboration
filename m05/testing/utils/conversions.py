""" 
@Program: utilities
@Author: Donald Osgood
@Last Date: 2023-07-02 21:56:38
@Purpose:Donald Osgood
"""

import math
from typing import Any

def truncate_to_decimal(number, decimals=2) -> float:
    """
    Returns a value truncated to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0**decimals
    return math.trunc(number * factor) / factor

def format_number_as_currency(value):
    """Format a number as a currency"""
    currency_format = f"${value}"
    return currency_format

def bankers_rounding(number, precision=2):
    """Return bankers rounding"""
    return round(number, precision)

def string_to_float(value, precision=0):
    """Convert a string to float with or without precisioning"""
    # remove commas
    try:
        if value != "":   
            float_value = float(value)
            if precision > 0:
                return bankers_rounding(value, precision)
            return float_value
    except ValueError as exception:
        return exception

def value_to_int(value: Any) -> int:
    """Convert value to int."""
    try:
        return int(float(value))
    except Exception as error:
        print("Please enter a valid number")
        raise error

def to_currency(value):
    """_summary_

    Args:
        value (float,string): value to be formated as currency

    Returns:
        string: string in currency format
    """
    return f'${value:,.2f}'

def string_to_list(value):
    """convert a string seperated by ; to a list

    Args:
        value (string): a string array seperated by; each value in item seperated by ,

    Returns:
        list: returns a string list
    """
    return value.split(";")
