''' 
@Program: automobile
@Author: Donald Osgood
@Last Date: 2023-11-12 20:19:08
@Purpose:Automobile class for setting automobile information
'''
from vehicle import Vehicle, Vehicle_Type, Door_Type, Roof_Type

class Automobile(Vehicle):
    """docstring"""
    """
    Attributes:    
    year
    make
    model
    doors (2 or 4)
    roof (solid or sun roof)    
    """

    def __init__(self,type:Vehicle_Type=Vehicle_Type.Car,year=1976,make="NA",model="NA",num_doors:Door_Type=Door_Type.Two,roof_type:Roof_Type=Roof_Type.Solid):
        """Constructor"""
        super().__init__(type)
        self.year=year
        self.make=make
        self.model=model
        self.num_doors = num_doors
        self.roof_type = roof_type
    
    if __name__ == "__main__": 
        print ("Executed when invoked directly")