""" 
@Program: The main entry
@Author: Donald Osgood
@Last Date: 2023-11-12 19:03:51
@Purpose:Allow user to enter vehicle information
"""

from automobile import Automobile, Vehicle_Type, Roof_Type, Door_Type


def main():
    while True:
        try:
            # get the vehicle year
            vehicle_type = input(
                "Please enter vehicle type(Car,Truck,Boat, etc), enter x to exit:"
            )
            if vehicle_type == "x":
                return False
            
            vehicle_type_value = getattr(Vehicle_Type, vehicle_type.title())
            if  vehicle_type.title() not in [Vehicle_Type.Truck.value.title(),Vehicle_Type.Car.value.title()]:
                print("Car and Truck is the only option availale at this time. Please try again")
                return False
           

            # get the vehicle year
            vehicle_year = input("Please enter vehicle year, enter x to exit:")
            if vehicle_year == "x":
                return False
            
            # get the vehicle make
            vehicle_make = input("Please enter vehicle make, enter x to exit:")
            if vehicle_make == "x":
                return False
            
            # get the vehicle model 
            vehicle_model = input("Please enter vehicle model, enter x to exit:")
            if vehicle_model == "x":
                return False
            
            # get the vehicle # of doors
            vehicle_doors = input("Please enter # doors(Two, Four), enter x to exit:")
            if vehicle_doors == "x":
                return False
            vehicle_door_value = getattr(Door_Type, vehicle_doors.title())
            # get the vehicle # of doors
            vehicle_roof = input("Please enter roof type(Sunroof, Solid), enter x to exit:")
            if vehicle_roof == "x":
                return False
            vehicle_roof_value = getattr(Roof_Type, vehicle_roof.title())
            # init automobile object
            my_automobile = Automobile(vehicle_type_value, vehicle_year, vehicle_make, vehicle_model,vehicle_door_value,vehicle_roof_value)
            text = f"""
            Results:
            Vehicle type: {my_automobile.type.value.title()}
            Year: {my_automobile.year}
            Make: {my_automobile.make.title()}
            Model: {my_automobile.model.title()}
            Number of doors: {my_automobile.num_doors.value}
            Type of roof:{my_automobile.roof_type.value.title()}
            """
            print(text)
        except:
            print("An exception occurred, try enter correct option")
            return False


if __name__ == "__main__":
    main()
