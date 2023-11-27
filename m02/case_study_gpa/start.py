""" 
@Program: Program entry point
@Author: Donald Osgood
@Last Date: 2023-11-04 20:22:55
@Purpose:Notify if a user should receive and award based on GPA 
"""
from award_rules_engine import get_award
from award_notification import show_award
from utils.conversions import string_to_float


def main():
    """Main entry"""
    # keep track if cancelled if cancelled exit the loop
    cancelled = False
    while not cancelled:
        try:
            # prompt user for last name
            last_name_input = input(
                'Please enter students last name, enter "ZZZ" to end GPA tool. :'
            )
            # check if last name valid
            if not last_name_input.isalpha():
                print("Please enter letters only, try again")
            # check if cancel key of ZZZ enter if so cancel
            elif last_name_input.upper() == "ZZZ":
                cancelled = True
            # continue to first name and GPA
            else:
                # get first name
                first_name_input = input("Please enter students first name. :")
                # get GPA
                grade_input = input("Please enter students gpa. :")
                # convert GPRA to float
                grade_value = string_to_float(grade_input)
                # check which award entitled to
                award_value = get_award(grade_value)
                # show the award details
                show_award(first_name_input, last_name_input, award_value)
        except Exception as exception:
            print("Try again invalid entry: " + exception.__str__())

if __name__ == "__main__":
    """ run main
    """    
    main()
