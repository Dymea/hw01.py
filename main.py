# Author: Dymea Schippers dxs5940@psu.edu

# User input for course 1
grade1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")
credit1 = int(credit1)

# Calculating grade point for course letter grade 1
if  grade1 == 'A':
  grade1 = float(4.0)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == 'A-':
  grade1 = float(3.67)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == 'B+':
  grade1 = float(3.33)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == "B":
  grade1 = float(3.0)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == "B-":
  grade1 = float(2.67)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == 'C+':
  grade1 = float(2.33)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == 'C':
  grade1 = float(2.0)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == 'D':
  grade1 = float(1.0)
  print(f"Grade point for course 1 is: {grade1} ")
if grade1 == 'F':
  grade1 = float(0.0)
  print(f"Grade point for course 1 is: {grade1} ")

# User input for course 2
grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")
credit2 = int(credit2)

# Calculating grade point for course letter grade 2
if grade2 == 'A':
  grade2 = float(4.0)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == 'A-':
  grade2 = float(3.67)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == 'B+':
  grade2 = float(3.33)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == "B":
  grade2 = float(3.0)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == "B-":
  grade2 = float(2.67)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == 'C+':
  grade2 = float(2.33)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == 'C':
  grade2 = float(2.0)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == 'D':
  grade2 = float(1.0)
  print(f"Grade point for course 2 is: {grade2} ")
if grade2 == 'F':
  grade2 = float(0.0)
  print(f"Grade point for course 2 is: {grade2} ")

# User input for course 3
grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")
credit3 = int(credit3)

# Calculating grade point for course letter grade 3
if grade3 == 'A':
  grade3 = float(4.0)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == 'A-':
  grade3 = float(3.67)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == 'B+':
  grade3 = float(3.33)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == "B":
  grade3 = float(3.0)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == "B-":
  grade3 = float(2.67)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == 'C+':
  grade3 = float(2.33)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == 'C':
  grade3 = float(2.0)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == 'D':
  grade3 = float(1.0)
  print(f"Grade point for course 3 is: {grade3} ")
if grade3 == 'F':
  grade3 = float(0.0)
  print(f"Grade point for course 3 is: {grade3} ")
  grade1 = float(grade1)
  grade2 = float(grade2)

# Calculating GPA
GPA = float(grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3)

print(f"Your GPA is: {GPA}")