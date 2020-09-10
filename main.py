# Author: Ismail Al Abdali ija5135@psu.edu

def getGradePoint(grade):
  if (grade == "A"):
    return 4.0
  elif (grade == "A-"):
    return 3.67
  elif (grade == "B+"):
    return 3.33
  elif (grade == "B"):
    return 3.0
  elif (grade == "B-"):
    return 2.67
  elif (grade == "C+"):
    return 2.33
  elif (grade == "C"):
    return 2.0
  elif (grade == "D"):
    return 1.0
  else :
    return 0.0
    
def run():
  course1 = input("Enter your course 1 letter grade: ")
  credit1 = float(input("Enter your course 1 credit: "))
  gradepoint1 = getGradePoint(course1)
  print(F"Grade point for course 1 is: {gradepoint1}")
  
  course2 = input("Enter your course 2 letter grade: ")
  credit2 = float(input("Enter your course 2 credit: "))
  gradepoint2 = getGradePoint(course2)
  print(F"Grade point for course 2 is: {gradepoint2}")
  
  course3 = input("Enter your course 3 letter grade: ")
  credit3 = float(input("Enter your course 3 credit: "))
  gradepoint3 = getGradePoint(course3)
  print(F"Grade point for course 3 is: {gradepoint3}")
  
  GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)
  print(F"Your GPA is: {GPA}")

if __name__ == "__main__":
  run()
  