# Author: Dymea Schippers dxs5940@psu.edu

def getGradePoint(coursegrade):
  if coursegrade == "A":
    return 4.0
  elif coursegrade == "A-":
    return 3.67
  elif coursegrade == "B+":
    return 3.33
  elif coursegrade == "B":
    return 3.0
  elif coursegrade == "B-":
    return 2.67
  elif coursegrade == "C+":
    return 2.33
  elif coursegrade == "C":
    return 2.0
  elif coursegrade == "D":
    return 1.0
  else:
    return 0.0

def run():
  coursegrade1 = input("Enter your course 1 letter grade: ")
  course1credit = float(input("Enter your course 1 credit: "))
  gradepoint1 = getGradePoint(coursegrade1)
  print(f"Grade point for course 1 is: {getGradePoint(coursegrade1)}")
  coursegrade2 = input("Enter your course 2 letter grade: ")
  course2credit = float(input("Enter your course 2 credit: "))
  gradepoint2 = getGradePoint(coursegrade2)
  print(f"Grade point for course 2 is: {getGradePoint(coursegrade2)}")
  coursegrade3 = input("Enter your course 3 letter grade: ")
  course3credit = float(input("Enter your course 3 credit: "))
  gradepoint3 = getGradePoint(coursegrade3)
  print(f"Grade point for course 3 is: {getGradePoint(coursegrade3)}")

  GPA = (gradepoint1 * course1credit + gradepoint2 * course2credit + gradepoint3 *course3credit) / (course1credit + course2credit + course3credit)

  print("Your GPA is", GPA)

if __name__ == "__main__":
  run()

