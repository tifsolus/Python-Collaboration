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
    while True:
        try:
            last_name_input = input(
                'Please enter students last name, enter "ZZZ" to end GPA tool. :'
            )
            if not last_name_input.isalpha():
                print("Please enter letters only, try again")
            elif last_name_input.upper() == "ZZZ":
                break
            else:
                first_name_input = input("Please enter students first name. :")
                grade_input = input("Please enter students gpa. :")
                grade_value = string_to_float(grade_input)
                award_value = get_award(grade_value)
                show_award(first_name_input, last_name_input, award_value)
        except Exception as exception:
            print("Try again invalid entry: " + exception.__str__())
            break


if __name__ == "__main__":
    main()
