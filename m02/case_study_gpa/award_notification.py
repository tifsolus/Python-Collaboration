""" 
@Program: award_notification
@Author: Donald Osgood
@Last Date: 2023-11-05 19:25:22
@Purpose:Show award notification
"""


def show_award(first_name, last_name, award):
    """Check wich award a student is entitled to based on GPA:"""
    try:
        if (first_name != "") and (last_name != ""):
            name_to_print = f"{first_name}, {last_name}"
            prefix_award = "has made the" if award else "has no awards"            
            notification = f"{name_to_print} {prefix_award} {award}"
            print(notification)
        else:
            print("Incomplete parameters provided, please try again")
    except ValueError as exception:
        print(exception)
