''' 
@Program: my_types
@Author: Donald Osgood
@Last Date: 2023-11-12 21:00:06
@Purpose: Class for types
'''
from enum import Enum
class Vehicle_Type(Enum):    
    Car = "car"
    Truck = "truck"
    Plane = "plane"
    Boat = "boat"
    Broomstick = "broomstick"

class Roof_Type(Enum):   
    Sunroof = "sunroof"
    Solid = "solid"

class Door_Type(Enum):   
    Two = 2
    Four = 4      