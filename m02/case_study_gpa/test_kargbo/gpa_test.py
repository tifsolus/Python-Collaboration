''' 
@Program: gpa_test
@Author: Donald Osgood
@Last Date: 2023-11-05 22:36:19
@Purpose:Donald Osgood
'''
def main():
  print("Welcome to the Student Qualification App")
  print("Enter 'ZZZ' for the last name to quit.")

  students = []
  while True:
    last_name = input("Enter student's last name: ")
    if last_name == 'ZZZ':
      break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    students.append((first_name, last_name, gpa))

  print("\nQualification Results:")
  for student in students:
    first_name, last_name, gpa = student
    if gpa >= 3.5:
      print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
      print(f"{first_name} {last_name} has made the Honor Roll.")


if __name__ == "__main__":
  main()