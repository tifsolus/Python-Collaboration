''' 
@Program: vehicle
@Author: Donald Osgood
@Last Date: 2023-11-12 18:26:43
@Purpose:A vehicle super class
'''
from my_types import Vehicle_Type, Door_Type, Roof_Type   

class Vehicle(object):
    """docstring"""

    def __init__(self, type:Vehicle_Type=Vehicle_Type.Car):
        """Constructor"""
        self.type = type


    
    